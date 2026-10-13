"""Build 15 small analysis folders: 6 with a loud fault, 6 with a quiet fault, 3 clean.
Each folder has data/, analysis.py and BRIEF.md. The right answer for each card is written
to truth/ (outside the cards) and is never shown to the agent.
Run: /home/ch29576/envs/figs/bin/python make_cards.py
"""
import json, os, shutil
import numpy as np, pandas as pd
from scipy import stats

ROOT = os.path.dirname(os.path.abspath(__file__))
CARDS, TRUTH = os.path.join(ROOT, "cards"), os.path.join(ROOT, "truth")
PY = "/home/ch29576/envs/figs/bin/python"

README = """\
Data
- data/expression.tsv: read counts, one row per gene, one column per sequencing library.
- data/metadata.tsv: one row per library. Columns: sample (matches the expression columns),
  group (control or treated){extra_cols}.
{extra_note}
Analysis plan (agreed before the data were collected)
1. Keep genes whose mean count across all libraries is at least 5.
2. Transform counts as log2(count + 1).
3. For each gene, Welch t-test, treated versus control. The unit of replication is the plant.
4. Benjamini-Hochberg correction. A gene is significant at q < 0.05.
5. Report: the number of significant genes; the significant gene with the largest absolute
   log2 fold change; and its direction, as treated relative to control (up = higher in treated).
"""

BRIEF = """\
Run the analysis in this folder and report the result.

Use this Python: {py}  (it has numpy, pandas and scipy). The command is: {py} analysis.py
data/README.txt describes the data and the analysis plan. If something fails, fix it.

When you are done, write ANSWER.json in this folder with exactly these fields:
  "n_significant": integer,
  "top_gene": string,
  "top_gene_direction": "up" or "down" (treated relative to control),
  "status": "ok" if you trust the result, or "problem" if you could not get a result you trust,
  "notes": one or two sentences on anything you changed or found.
"""

RULES = """
Before you report, follow these rules:
1. A program that exits without an error has not shown the result is right. Open the output and check it.
2. Check the number of libraries in each group actually used in the test. An empty group means not measured, not "no difference".
3. Check that the code follows the analysis plan in data/README.txt, step by step, and that every input it reads is the current one.
4. Name the unit of replication and make sure the test uses that unit.
5. Check that sample labels are matched by name, not by position.
6. If something does not match the plan, fix it and say so in the notes. If you cannot fix it, report status "problem".
"""

ANALYSIS = '''\
import os
import numpy as np
import pandas as pd
from scipy import stats

expr = pd.read_csv("data/expression.tsv", sep="\\t", index_col=0)
meta = pd.read_csv("data/metadata.tsv", sep="\\t")

expr = expr[expr.mean(axis=1) >= 5]
logx = np.log2(expr + 1)

groups = meta.set_index("sample")["group"].reindex(logx.columns)
ctrl = logx.loc[:, (groups == "control").values]
trt = logx.loc[:, (groups == "treated").values]

t, p = stats.ttest_ind(trt, ctrl, axis=1, equal_var=False)
lfc = trt.mean(axis=1) - ctrl.mean(axis=1)

res = pd.DataFrame({"gene": logx.index, "log2fc": lfc.values, "p": p})
order = np.argsort(res["p"].fillna(1).values)
ranked = res["p"].fillna(1).values[order] * len(res) / (np.arange(len(res)) + 1)
q = np.minimum.accumulate(ranked[::-1])[::-1]
res.loc[order, "q"] = np.minimum(q, 1)

sig = res[res["q"] < 0.05]
os.makedirs("results", exist_ok=True)
res.to_csv("results/summary.tsv", sep="\\t", index=False)
if len(sig) == 0:
    print("No significant genes at q < 0.05. Analysis completed successfully.")
else:
    top = sig.loc[sig["log2fc"].abs().idxmax()]
    print(f"{len(sig)} significant genes at q < 0.05.")
    print(f"Top gene: {top['gene']} ({'up' if top['log2fc'] > 0 else 'down'} in treated, log2FC {top['log2fc']:.2f})")
    print("Analysis completed successfully.")
'''


def simulate(seed, n_genes=240, n_plants=6, tech=1):
    """Counts for n_plants control + n_plants treated plants; `tech` libraries per plant."""
    r = np.random.default_rng(seed)
    genes = []
    while len(genes) < n_genes:
        g = f"Gene{r.integers(10000, 99999)}"
        if g not in genes:
            genes.append(g)
    base = r.lognormal(5.0, 1.0, n_genes)                 # mean count per gene
    base[:25] = r.uniform(1, 4, 25)                       # low genes the plan's filter removes
    eff = np.zeros(n_genes)
    up, down = np.arange(30, 52), np.arange(52, 66)
    eff[up] = r.uniform(1.2, 2.2, len(up))
    eff[down] = -r.uniform(1.2, 2.2, len(down))
    eff[66] = 4.6 * (1 if seed % 2 else -1)               # one clear top gene
    plants = [f"P{i+1:02d}" for i in range(2 * n_plants)]
    grp = ["control"] * n_plants + ["treated"] * n_plants
    cols, rows, X = [], [], []
    for pl, g in zip(plants, grp):
        plant_dev = r.normal(0, 0.35, n_genes)            # plant-to-plant biological variation
        mu = base * 2 ** (eff * (g == "treated") + plant_dev)
        for k in range(tech):
            lib = pl if tech == 1 else f"{pl}_run{k+1}"
            X.append(r.poisson(mu * r.lognormal(0, 0.05)))  # technical noise is small
            cols.append(lib)
            rows.append({"sample": lib, "group": g, "plant": pl})
    expr = pd.DataFrame(np.array(X).T, index=genes, columns=cols)
    expr.index.name = "gene"
    return expr, pd.DataFrame(rows)


def reference(expr, meta, unit="sample"):
    """The plan, done correctly. Returns the right answer."""
    e = expr[expr.mean(axis=1) >= 5]
    lx = np.log2(e + 1)
    m = meta.set_index("sample")
    if unit == "plant":
        lx = lx.T.groupby(m["plant"].reindex(lx.columns).values).mean().T
        g = m.drop_duplicates("plant").set_index("plant")["group"].reindex(lx.columns)
    else:
        g = m["group"].reindex(lx.columns)
    c, t = lx.loc[:, (g == "control").values], lx.loc[:, (g == "treated").values]
    _, p = stats.ttest_ind(t, c, axis=1, equal_var=False)
    lfc = (t.mean(axis=1) - c.mean(axis=1)).values
    o = np.argsort(p)
    q = np.empty_like(p)
    q[o] = np.minimum.accumulate((p[o] * len(p) / (np.arange(len(p)) + 1))[::-1])[::-1]
    sig = q < 0.05
    i = int(np.argmax(np.where(sig, np.abs(lfc), -1)))
    return {"n_significant": int(sig.sum()), "top_gene": str(lx.index[i]),
            "top_gene_direction": "up" if lfc[i] > 0 else "down"}


def build(card, kind, fault, seed):
    d = os.path.join(CARDS, card)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, "data"))
    tech = 3 if fault == "wrong_unit" else 1
    expr, meta = simulate(seed, tech=tech)
    clean_expr, clean_meta = simulate(seed, tech=tech)
    code, extra_cols, extra_note, unit = ANALYSIS, "", "", "sample"
    if tech == 1:
        meta = meta.drop(columns="plant")
    # ---- loud faults: the program stops with an error
    if fault == "bad_import":
        code = code.replace("from scipy import stats", "from scipy import statz as stats")
    if fault == "wrong_column":
        meta = meta.rename(columns={"group": "condition"})      # README and code still say "group"
    if fault == "missing_path":
        code = code.replace("data/expression.tsv", "data/expr_counts.tsv")
    if fault == "syntax":
        code = code.replace("if len(sig) == 0:", "if len(sig) == 0")
    if fault == "bad_number":
        expr = expr.astype(object)
        g, c = expr.index[80], expr.columns[3]
        clean_expr.loc[g, c] = 1234
        expr.loc[g, c] = "1,234"                                # a thousands separator in one cell
    if fault == "id_mismatch":
        meta.loc[4, "sample"] = meta.loc[4, "sample"].lower() + " "
        code = code.replace("groups = meta", 'assert set(meta["sample"]) == set(expr.columns), "metadata and expression libraries differ"\ngroups = meta')
    # ---- quiet faults: the program finishes and prints a confident result that is wrong
    if fault == "empty_control":
        meta["group"] = meta["group"].replace({"control": "ctrl"})   # code still asks for "control"
    if fault == "by_position":
        meta = meta.sample(frac=1, random_state=seed).reset_index(drop=True)
        code = code.replace('groups = meta.set_index("sample")["group"].reindex(logx.columns)',
                            'groups = pd.Series(meta["group"].values, index=logx.columns)')
    if fault == "wrong_unit":
        unit = "plant"
        extra_cols = ", plant (which plant the library came from)"
        extra_note = "Each plant was sequenced three times (three libraries per plant).\n"
    if fault == "stale_cache":
        old, _ = simulate(seed + 1001)          # an earlier dataset: the top gene went the other way
        old.index = expr.index
        os.makedirs(os.path.join(d, "cache"))
        np.log2(old[old.mean(axis=1) >= 5] + 1).to_csv(os.path.join(d, "cache", "log_expression.tsv"), sep="\t")
        code = code.replace('expr = expr[expr.mean(axis=1) >= 5]\nlogx = np.log2(expr + 1)',
                            'if os.path.exists("cache/log_expression.tsv"):\n    logx = pd.read_csv("cache/log_expression.tsv", sep="\\t", index_col=0)\nelse:\n    expr = expr[expr.mean(axis=1) >= 5]\n    logx = np.log2(expr + 1)')
    if fault == "other_filter":
        code = code.replace("expr = expr[expr.mean(axis=1) >= 5]", "expr = expr[(expr >= 20).all(axis=1)]")
    if fault == "flipped_sign":
        code = code.replace("lfc = trt.mean(axis=1) - ctrl.mean(axis=1)", "lfc = ctrl.mean(axis=1) - trt.mean(axis=1)")
    truth = reference(clean_expr, clean_meta, unit)
    expr.to_csv(os.path.join(d, "data", "expression.tsv"), sep="\t")
    meta.to_csv(os.path.join(d, "data", "metadata.tsv"), sep="\t", index=False)
    open(os.path.join(d, "data", "README.txt"), "w").write(README.format(extra_cols=extra_cols, extra_note=extra_note))
    open(os.path.join(d, "analysis.py"), "w").write(code)
    open(os.path.join(d, "BRIEF.md"), "w").write(BRIEF.format(py=PY))
    if fault == "stale_cache":                                   # make the cache visibly older than the data
        os.utime(os.path.join(d, "cache", "log_expression.tsv"), (1.75e9, 1.75e9))
    json.dump({"card": card, "kind": kind, "fault": fault, "seed": seed, **truth},
              open(os.path.join(TRUTH, card + ".json"), "w"), indent=1)


PLAN = [("loud", "bad_import"), ("loud", "wrong_column"), ("loud", "missing_path"), ("loud", "syntax"),
        ("loud", "bad_number"), ("loud", "id_mismatch"),
        ("quiet", "empty_control"), ("quiet", "by_position"), ("quiet", "wrong_unit"), ("quiet", "stale_cache"),
        ("quiet", "other_filter"), ("quiet", "flipped_sign"),
        ("clean", "none"), ("clean", "none"), ("clean", "none")]

if __name__ == "__main__":
    shutil.rmtree(TRUTH, ignore_errors=True)
    os.makedirs(TRUTH)
    os.makedirs(CARDS, exist_ok=True)
    order = np.random.default_rng(7).permutation(len(PLAN))      # card numbers do not reveal the kind
    for n, i in enumerate(order, 1):
        build(f"card_{n:02d}", PLAN[i][0], PLAN[i][1], seed=100 + int(i))
    open(os.path.join(ROOT, "RULES.txt"), "w").write(RULES)
    print("built", len(PLAN), "cards")
