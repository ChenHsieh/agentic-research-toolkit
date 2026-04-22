---
name: ml-genomics-best-practices
description: >
  A checklist-driven workflow for running reproducible, defensible ML experiments in genomics.
  Enforces anti-circularity, class balance audit, LR baselines, bootstrap CIs, permutation tests,
  proper feature leakage prevention, and standardized reporting. Invoke whenever building a
  classification or regression model that predicts expression-derived, phenotype-derived, or
  any biologically-derived labels from genomic features. Critical for: fate prediction, ASE
  classification, expression divergence regression, gene property prediction.
allowed-tools: Read Write Edit Bash
---

# ML Genomics Best Practices Skill

## 0. Overview Philosophy

Every ML analysis in genomics must answer three questions before reporting a number:
1. **Is there circularity?** Features must not encode the target, even indirectly.
2. **Is the evaluation honest?** Train/test properly separated, baseline compared, uncertainty quantified.
3. **Is the interpretation causal-safe?** AUC measures "information content in features", not "causation". Never overstate.

---

## 1. Pre-Analysis Checklist (run before writing any model code)

### 1A. Define target and features explicitly

```
TARGET: [exact column name and biological meaning]
FEATURES: [list all candidate feature groups -- structural, sequence, embedding, etc.]
UNIT: [what is one row? gene pair, gene, array, sample?]
N: [total n, positive class n, negative class n]
```

Write this down as a comment at the top of the notebook.

### 1B. Circularity check

Circularity occurs when features are derived from or correlated with the target by construction.

Common traps in genomics:

| Target | Dangerous features to EXCLUDE |
|--------|-------------------------------|
| Expression fate (PCC binary) | PCC itself, tau values, log2FC, TPM, tissue counts |
| ASE binary (FC>=2) | mean_abs_log2fc, max_abs_log2fc, pcc, fc_cat, any expression measure |
| Methylation level | Methylation-adjacent features computed from expression |
| Tissue specificity | Expression breadth, tau index, max TPM |
| Expression divergence | Any expression-based distance or similarity |

**Rule**: if a feature requires the expression data to compute, it cannot be used to predict an expression-derived label.

**Action**: After listing features, create two lists:
```python
GENOMIC_FEATURES = [...]  # OK -- derived from genome only (Ks, gene structure, TE, sequence)
EXPRESSION_FEATURES = [...]  # FORBIDDEN for expression-derived targets
```

Use `assert` statements to verify no forbidden features appear in model input:
```python
forbidden = set(EXPRESSION_FEATURES)
used = set(feature_cols)
assert len(forbidden & used) == 0, f"CIRCULARITY: {forbidden & used}"
```

---

## 2. Class Balance Audit

### 2A. Compute and report balance for every binary task

```python
def balance_report(y, label='dataset'):
    n = len(y)
    n_pos = y.sum()
    n_neg = n - n_pos
    ratio = max(n_pos, n_neg) / max(min(n_pos, n_neg), 1)
    severity = 'OK' if ratio < 1.5 else 'MODERATE' if ratio < 3 else 'SEVERE'
    print(f'{label}: n={n}, pos={n_pos}({n_pos/n:.1%}), neg={n_neg}({n_neg/n:.1%}), ratio={ratio:.2f} [{severity}]')
    return ratio

ratio = balance_report(y, label='TD fate binary')
```

Severity thresholds:
- ratio < 1.5: OK -- proceed without correction
- ratio 1.5-3.0: MODERATE -- use stratified CV; report balanced_accuracy alongside AUC
- ratio > 3.0: SEVERE -- use majority-class undersampling with 10 seeds AND report both imbalanced and balanced AUC

### 2B. Balanced subsampling (for severe imbalance)

```python
def balanced_subsample(X, y, seed):
    rng = np.random.RandomState(seed)
    n_min = min((y==0).sum(), (y==1).sum())
    i0 = rng.choice(np.where(y==0)[0], n_min, replace=False) if (y==0).sum() > n_min else np.where(y==0)[0]
    i1 = rng.choice(np.where(y==1)[0], n_min, replace=False) if (y==1).sum() > n_min else np.where(y==1)[0]
    idx = np.sort(np.concatenate([i0, i1]))
    return X[idx], y[idx]

# Run 10 seeds and report mean +/- SD
aucs_bal = [cv_auc(*balanced_subsample(X, y, s), seed=s) for s in range(10)]
print(f'Balanced AUC: {np.mean(aucs_bal):.3f} +/- {np.std(aucs_bal):.3f}')
```

**Note**: ROC AUC is theoretically class-imbalance invariant, but MLP (sklearn) and models without built-in class weighting are affected in practice. CatBoost/XGBoost with stratified CV are more robust.

---

## 3. Model Hierarchy

Always build models from simple to complex. Report each level. Never report only the best model.

```
Level 0: Null baseline (predict majority class always)
Level 1: Logistic Regression (LR) -- the mandatory baseline for ANY classification
Level 2: Tree model (CatBoost/XGBoost/RF) with structural/genomic features
Level 3: + Sequence features (k-mer composition, motifs, methylation proxies)
Level 4: + Embedding distances (cosine/euclidean from pretrained model)
Level 5: MLP on full embedding vectors (separate from CatBoost L4)
```

**Rule**: You must always report LR as a baseline. CB_minus_LR (delta AUC) is as important as the absolute AUC.

```python
def lr_baseline_auc(X, y, seed=42, n_fold=3):
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import StratifiedKFold
    sc = StandardScaler()
    skf = StratifiedKFold(n_fold, shuffle=True, random_state=seed)
    aucs = []
    for tr, te in skf.split(X, y):
        clf = LogisticRegression(C=1.0, max_iter=500, random_state=seed)
        clf.fit(sc.fit_transform(X[tr]), y[tr])
        aucs.append(roc_auc_score(y[te], clf.predict_proba(sc.transform(X[te]))[:,1]))
    return np.mean(aucs)
```

---

## 4. Embedding Handling

Embeddings (DNABERT-2, ESM, etc.) require special treatment.

### 4A. Do NOT reduce embeddings to 2 scalars for tree models

Using only cosine + euclidean distance from a 768-dim embedding throws away most of the information. The two scalars are:
- Fast and interpretable (good for CatBoost feature matrix)
- But weak signal: they rank last in SHAP importance when competing with hand-crafted features

### 4B. For embedding-specific analysis, use MLP not tree

```
MLP(hidden_layer_sizes=(256, 64)) on [e1 - e2] (embedding difference vector)
  -- captures nonlinear combinations of all 768 dims
  -- requires balanced classes or class_weight handling
  -- use as a SEPARATE probe, not mixed with CatBoost features
```

### 4C. For combining embeddings with hand-crafted features

Option 1: PCA-reduce embedding to 20-50 dims, append to feature matrix, run CatBoost.
Option 2: Stacking -- generate OOF predictions from (a) CatBoost on HC features and (b) Ridge on full embeddings; combine with meta-learner.
Option 3 (honest): Accept that embeddings add minimal signal if strong HC features exist.

### 4D. Reporting embedding results

Always report:
- MLP on full embedding (standalone probe, measures maximum extractable signal)
- LR on PCA-100 of embedding (linear extractable signal)
- CatBoost with 2-scalar distances (practical feature matrix contribution)
- The 3 numbers tell very different stories -- report all 3.

---

## 5. Cross-Validation Setup

```python
# ALWAYS use stratified k-fold
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

# For gene pair data: if pairs share genes, use group-aware CV
# Prevent data leakage: if gene A appears in pair (A,B) in train, it should not
# appear in (A,C) in test. Use GroupKFold on gene_id_1 or array_id.

# Haplotype CV (additional validation for phased assemblies)
# Train on HAP1, test on HAP2 -- tests generalizability across haplotypes
# If symmetric (H1->H2 AUC ≈ H2->H1 AUC), the model is not haplotype-biased
```

**Important for tandem array data**: use array-level blocking in CV. Genes in the same array must all be in the same fold to prevent leakage between array members.

---

## 6. Statistical Rigor

### 6A. Bootstrap confidence intervals (mandatory for key AUCs)

```python
def bootstrap_auc_ci(y_true, y_pred_proba, n_bootstrap=1000, alpha=0.05, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    boot_aucs = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        if len(np.unique(y_true[idx])) < 2:
            continue
        boot_aucs.append(roc_auc_score(y_true[idx], y_pred_proba[idx]))
    boot_aucs = np.array(boot_aucs)
    return np.percentile(boot_aucs, [100*alpha/2, 100*(1-alpha/2)])

ci_lo, ci_hi = bootstrap_auc_ci(y_true_oof, oof_proba)
print(f'AUC = {roc_auc_score(y_true_oof, oof_proba):.3f} [{ci_lo:.3f}, {ci_hi:.3f}]')
```

### 6B. Permutation test (mandatory for headline claims)

```python
def permutation_test_auc(X, y, model_fn, n_permutations=100, observed_auc=None, seed=42):
    """model_fn: callable that takes X, y and returns AUC (via CV)"""
    rng = np.random.RandomState(seed)
    null_aucs = []
    for i in range(n_permutations):
        y_perm = rng.permutation(y)
        null_aucs.append(model_fn(X, y_perm))
    null_aucs = np.array(null_aucs)
    p_value = (null_aucs >= observed_auc).mean()
    print(f'Observed AUC={observed_auc:.4f}, Null median={np.median(null_aucs):.4f}, p={p_value:.3f}')
    return p_value, null_aucs
```

### 6C. Multiple seeds for small datasets

If n < 5000, model variance is high. Run 5-10 seeds and report mean +/- SD:
```python
aucs = [cv_auc(X, y, seed=s) for s in range(10)]
print(f'AUC = {np.mean(aucs):.4f} +/- {np.std(aucs):.4f}')
```

---

## 7. Interpretation Rules

### 7A. Framing language

Use: "features contain information about X" or "X is predictable from Y at AUC=Z"
Avoid: "Y causes X" or "Y drives X" (unless you have perturbation evidence)

Correct: "Structural features predict TD expression fate with AUC=0.748, showing that gene structure captures information about expression divergence."
Wrong: "Gene structure drives expression divergence."

### 7B. Generalizability triangle

Always test across three axes before claiming generalizability:
- Across folds (stratified CV): standard
- Across haplotypes (HAP1->HAP2 and vice versa): haplotype CV
- Across duplication types (TD->sWGD transfer): cross-type transfer

If a finding holds on only one axis, say so explicitly.

### 7C. SHAP interpretation caveats

- SHAP measures feature contribution to model prediction, not to biology
- Correlated features will split SHAP importance between them (sum is still correct)
- For embeddings: SHAP on cosine/euclidean is not interpretable in biological terms -- use it only to show rank relative to HC features
- Report both mean |SHAP| (overall importance) and dependence plots (direction)

---

## 8. Cross-Type Transfer Template

```python
# Test whether model trained on one duplication type generalizes to another
results = []
for train_type in ['TD', 'sWGD', 'aWGD', 'syntelog']:
    for test_type in ['TD', 'sWGD', 'aWGD', 'syntelog']:
        if train_type == test_type: continue
        df_tr = df[df['dup_type'] == train_type]
        df_te = df[df['dup_type'] == test_type]
        # use L3 or L4 features -- make sure test type has all feature columns
        X_tr = prep_X(df_tr, FEAT_COLS)
        X_te = prep_X(df_te, FEAT_COLS)
        y_tr = df_tr['fate_binary'].values
        y_te = df_te['fate_binary'].values
        if min(y_te.sum(), (y_te==0).sum()) < 10: continue
        clf.fit(X_tr, y_tr)
        auc = roc_auc_score(y_te, clf.predict_proba(X_te)[:,1])
        results.append({'train': train_type, 'test': test_type, 'auc': auc})

# Interpret: AUC >> 0.5 = information transfers; AUC ~ 0.5 = type-specific
```

---

## 9. Reporting Template

Every ML analysis section in a manuscript should contain, in order:

1. **n and class balance** for each dataset used
2. **LR baseline AUC** (CB_minus_LR = value)
3. **Primary model AUC** with 95% CI from bootstrap
4. **Permutation p-value** (confirms AUC is above chance)
5. **Top 3 features by SHAP** (with interpretation)
6. **Cross-validation scheme used** (stratified k-fold, group-k-fold, haplotype CV)
7. **Generalizability note** (which axes were tested, what held/failed)

Minimum table columns for any comparison table:
```
Model | n_pairs | class_balance | AUC | CI_95 | LR_baseline | delta_LR | perm_p | top3_features
```

---

## 10. Quick Sanity Checks Before Reporting

```python
# 1. Check for NaN leakage
assert not np.isnan(X_train).any(), "NaN in training features"

# 2. Check for identical rows between train and test (exact duplicate leakage)
train_hashes = set(map(tuple, X_train.tolist()))
test_hashes = set(map(tuple, X_test.tolist()))
overlap = len(train_hashes & test_hashes)
if overlap > 0: print(f"WARNING: {overlap} identical rows in train and test")

# 3. Sanity check: LR AUC should be <= tree AUC (if not, check features)
assert lr_auc <= cb_auc + 0.02, f"LR ({lr_auc:.3f}) outperforms CatBoost ({cb_auc:.3f}) -- suspect feature issue"

# 4. Verify haplotype CV is symmetric (within +/- 0.02)
h1_to_h2_auc = ...
h2_to_h1_auc = ...
assert abs(h1_to_h2_auc - h2_to_h1_auc) < 0.05, f"Haplotype CV asymmetric: {h1_to_h2_auc:.3f} vs {h2_to_h1_auc:.3f}"

# 5. AUC from balanced subsample should be within 0.02 of imbalanced AUC
# (larger delta = suspect that imbalance is masking real performance)
```

---

## 11. Common Pitfalls Reference

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Circularity | AUC > 0.95 | Remove expression-derived features |
| Feature leakage across array members | AUC drops ~0.05 in group CV | Use array-level GroupKFold |
| Imbalanced class (ratio > 3) | F1 misleadingly low, model predicts majority only | Balanced subsample + report both |
| Embedding reduced to 2 scalars | SHAP ranks distances last | Run separate MLP probe on full 768-dim |
| AUC reported without baseline | Cannot assess information gain | Always compare to LR and to permutation null |
| Cross-type transfer not tested | Over-claiming generalizability | Always test H1->H2 and type A->B |
| PCA applied to embedding before all data | Test set leaks into PCA | Fit PCA on train, transform test separately |
| F1 reported on imbalanced test set | Misleadingly low for minority class | Use balanced_accuracy or per-class F1 |
| Overfitting via hyperparameter search on test set | AUC inflated by ~0.02-0.05 | Tune on inner CV, evaluate on separate outer fold |
