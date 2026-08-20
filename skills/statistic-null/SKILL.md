---
name: statistic-null
description: >
  Give a derived summary statistic its own null distribution before believing anything it
  says. For any scalar computed from data - concentration, peakiness, enrichment ratio,
  importance mass, divergence, specificity, clustering score - construct a null that preserves
  everything except the claimed structure, then check whether the observed value is actually
  extreme under it. Includes the arithmetic-artifact check for ratio statistics whose numerator
  takes an extremum. Use before a derived number becomes a claim, and especially for a metric
  that is conventional in a field but has never been given a null. Trigger on "is this score
  high", "enrichment ratio", "concentration / peakiness / specificity score", "this metric
  shows", "how do I know this number is meaningful".
allowed-tools: Read Write Edit Bash Glob Grep
---

# A null for the statistic itself

Model performance routinely gets a null — permutation tests, shuffled labels, random
baselines. The *summary statistic* computed on top of the results usually does not. It gets
computed, compared across conditions, and reported, with no one having established what value
it takes when nothing interesting is happening.

> **A statistic without a null has no scale.** "Peakiness was 3.2, higher in condition A than
> condition B" is uninterpretable until you know what peakiness is under structureless data.
> If the null also produces 3.2, the metric was measuring its own arithmetic.

This is a different object from a model null. `ml-genomics-best-practices` and similar
checklists cover permutation tests and bootstrap CIs **for a classifier's performance**. This
skill is about the derived scalar you compute *from* results — where the failure mode is that
the number is a property of the formula and the data shape, not of the phenomenon.

## When to use this

Any time a derived scalar is about to carry a claim. Highest priority when:

- The metric is conventional in your field and you inherited it without a null.
- The metric is a **ratio, and the numerator or denominator takes a max, min, or other
  extremum** — these have strong built-in behavior (see Step 2).
- You are comparing the statistic across conditions with different sizes, sparsities, or
  numbers of categories. Most concentration metrics are sensitive to all three.
- The number came out looking clean.

## Step 1 — write down what "nothing interesting" means

The null must preserve everything about the data except the structure you are claiming.
Getting this wrong in either direction is the main way the procedure fails.

- **Too permissive:** shuffle everything, destroy structure you were not claiming, and the
  observed value looks extreme for reasons that have nothing to do with your hypothesis.
- **Too conservative:** preserve so much that the claimed structure survives into the null,
  and nothing is ever significant.

Write one sentence: *"Under the null, the data still has ___, but not ___."* Then choose the
randomization that implements exactly that. Common choices, from weakest to strongest:

| Null | Preserves | Destroys |
|---|---|---|
| Uniform / parametric draw | Range only | Everything else |
| Shuffle values within units | Marginal distribution per unit | Association across units |
| Shuffle labels across units | All data structure | Label–data association |
| Degree- or margin-preserving rewiring | Marginal totals, sparsity | Specific pairings |
| Block / stratified shuffle | Structure within known blocks | Across-block association |

The last two are usually what you want for anything network-, matrix-, or count-shaped, and
they are the ones people skip because they are more work.

## Step 2 — check for the arithmetic artifact first

Before running anything, check whether the statistic has a built-in floor or ceiling from its
own formula. This is a five-minute check that has retired entire metrics.

**The extremum-in-a-ratio trap.** If the numerator is a max or min over a set of alternatives
and the denominator is a mean or sum over the same set, the statistic is partly measuring the
*number of alternatives*, not the concentration among them. The maximum of n draws grows with
n even from an identical distribution. A "specificity" or "peakiness" score built this way
will rank a condition with more categories as more peaked, purely arithmetically.

Test it directly: compute the statistic on structureless data at each of the sizes,
sparsities, and category counts present in your real comparison. If the null value moves with
those, **the statistic is not comparable across your conditions** and no amount of
significance testing fixes it — you need a different statistic or a per-condition null.

## Step 3 — generate the null and place the observation

Generate enough replicates that the resolution supports the claim you want to make. Report the
observed value, the null distribution's center and spread, and where the observation sits —
not just a p-value.

Two practical rules:

- **Use the add-one estimator:** `p = (count of null >= observed + 1) / (n + 1)`. A permutation
  test cannot produce p = 0; the naive fraction prints `0.000` when nothing beat the
  observation, which is an artifact of finite replicates. The floor is `1/(n+1)`, so if you
  need to claim a smaller p, generate more replicates.
- **Compute a null per condition**, not one pooled null, whenever conditions differ in size or
  sparsity. A shared null silently imports Step 2's artifact.

## Step 4 — report the whole grid, including the cells that failed

If you computed the statistic across a grid of conditions, report the null comparison for
**every cell**, not the ones that passed. The most valuable outcome of this procedure is the
one where a metric that has been reported for years fails against its own null across the
board — and that outcome is only visible if the failing cells are in the table.

When a statistic fails its null, the honest consequence is not a caveat sentence. It is that
every claim resting on that statistic is withdrawn, in every document that carries it, with a
dated note saying why. Grep for the metric's name across the project.

## What this does not cover

| Not covered | Where it belongs |
|---|---|
| Null / baseline for a *model's* predictive performance | `ml-genomics-best-practices` and standard permutation testing |
| Whether the design permits the comparison at all | `design-confound-audit` |
| Auditing a finished result for artifacts broadly | `result-autopsy` |
| Multiple-testing correction across many statistics | Standard FDR/FWER procedures; this establishes one statistic's scale |
| Whether the statistic measures the construct you care about | Construct validity — a null cannot tell you the metric is the right metric |

## Honest limits

- A statistic can pass its null and still be the wrong statistic for the question. This
  establishes scale, not relevance.
- The null encodes your belief about what "no structure" means. Two defensible nulls can give
  different answers, and reporting only the one you ran is a forking path.
- Preserving-everything-but-one nulls get expensive fast on large data; the honest fallback is
  a smaller replicate count with the resolution floor stated, not a cheaper null left
  undescribed.
