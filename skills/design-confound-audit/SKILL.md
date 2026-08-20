---
name: design-confound-audit
description: >
  Determine which questions a dataset's design can actually answer, before any model is fit.
  Cross-tabulates the factor of interest against every nuisance factor to find perfect
  confounding (a factor fully nested inside another cannot be separated from it by any
  statistical method), cells below an inferential floor, and unbalanced strata - then returns
  a per-question verdict of answerable / answerable-with-blocking / not answerable. Use at the
  start of an analysis, when inheriting someone else's dataset, when a reviewer asks whether
  an effect is confounded, or when choosing a statistical test. Trigger on "what test should
  I use", "is this confounded", "can I compare these groups", "batch effect", "inherited this
  dataset", "before I run the stats".
allowed-tools: Read Write Edit Bash Glob Grep
---

# Design confound audit

**Run this before choosing a test, not after a reviewer asks.** The question is not "which
model fits this data" but "which comparisons does this design permit at all." Those are
different questions, and the second one has answers no amount of modeling can change.

> **A factor perfectly nested inside another cannot be separated from it.** If every treated
> sample came from one cage, one batch, one run, or one site, then treatment and that factor
> are the same variable wearing two names. You cannot adjust for it, covary it out, or fit
> your way around it. This is a limit of the design, not a modeling choice.

## When to use this

At the start of an analysis, especially on a dataset you did not design. On inheriting a
project. Before committing to a statistical plan. When results look surprisingly clean.

Skip it for a designed experiment you ran yourself with known randomization — though even
then, check what the *realized* design looks like after dropouts and failed samples, which is
often not the design you planned.

## Step 1 — get the metadata table, not the measurements

You need one row per experimental unit and one column per factor: the factor of interest, and
every nuisance factor that could plausibly track it. Nuisance factors people forget:

- **Processing:** batch, run, plate, lane, kit lot, reagent lot, extraction day.
- **Environment:** cage, tank, shelf, room, field plot, site, greenhouse bench position.
- **Time:** collection date, processing order, season, operator shift.
- **Personnel:** who collected, who prepared, who scored. Scorer is a factor.
- **Provenance:** source colony, supplier, litter, family, clone, passage number.
- **Instrument:** machine, flow cell, microscope, column.

If a factor was not recorded, that is itself a finding — record it as *unrecorded*, not as
absent. An unrecorded batch effect is not a missing batch effect.

## Step 2 — cross-tabulate the factor of interest against each nuisance factor

For each nuisance factor, build the contingency table against the factor of interest and
classify it:

| Pattern | What it means | Consequence |
|---|---|---|
| **Perfect nesting** — each level of interest appears in exactly one nuisance level | The two are the same variable | **Not answerable.** No test separates them. |
| **Partial confounding** — heavily unbalanced but overlapping | Separable in principle, with reduced power | Answerable with blocking; report the imbalance |
| **Crossed and balanced** | Independent | Answerable; include the nuisance factor as a block |
| **Singleton cells** — a combination with n = 1 | No within-cell variance | That cell supports no inferential test |

Report the actual counts. "Balanced" claimed without a table is not a finding.

## Step 3 — apply an inferential floor

Set a minimum cell size *before* looking at the outcome, and state it. Below that floor, the
honest verdict is "descriptive only," not "a p-value with a caveat." A comparison resting on
n = 1 per arm has no within-arm variance to estimate, and no test on it means anything
regardless of what a package will happily print.

Where a study has several arms — a clean arm and a compromised one — evaluate each arm
separately. It is common for one arm to support inference and another not to, and reporting a
pooled result hides that.

## Step 4 — the confound can hide an effect, not only create one

Most confound discussions assume the confound manufactures a false positive. The reverse is at
least as common and much less often checked: **a nuisance factor that varies with the
comparison can absorb a real effect and hide it.** Splitting a comparison by a nuisance
factor, or drawing controls separately within each arm, can partition away the very contrast
you are testing.

Check both directions. For each nuisance factor, ask: if I pool across it instead of
stratifying, does an effect appear? If I stratify instead of pooling, does one vanish? A
factor that changes the answer in either direction is load-bearing and belongs in the report.

## Step 5 — return a per-question verdict

The deliverable is a table, one row per question the user believes they are asking:

| Question | Verdict | Limiting factor | What would fix it |
|---|---|---|---|
| Does treatment affect the outcome? | Not answerable | Treatment perfectly nested in batch | Re-run with treatments split across batches |
| Does treatment affect the outcome, cohoused subset? | Answerable | — | — |
| Does the effect differ by genotype? | Descriptive only | n = 1 in two genotype × treatment cells | More units in those cells |

Deliver this **before** running any model. Its purpose is to stop work on questions the data
cannot answer, and to redirect that effort toward the ones it can.

## Also check: circularity in the variable list

While you have the metadata open, list any variable that is derived from, or computed using,
the outcome. These cannot be predictors of it. Write the forbidden list down explicitly and
assert it at runtime in the analysis code — a comment does not survive a refactor. Derived
labels are the usual culprit: a label computed from a variable that is also a feature builds
the answer into the input.

## What this does not cover

| Not covered | Where it belongs |
|---|---|
| Auditing a result you have already produced | `result-autopsy` |
| Whether a summary statistic is meaningful | `statistic-null` |
| Choosing a specific test once the design is cleared | A statistics reference; this stops at answerable / not |
| Power analysis for a study not yet run | Prospective design tools; this audits a realized dataset |
| Causal identification from observational data | Causal inference proper — nesting is necessary, not sufficient |

## Honest limits

- The audit only sees factors that were recorded. The dangerous confound is usually the
  unrecorded one, and this procedure can only tell you it is unrecorded.
- "Answerable" here means the design does not preclude the comparison. It is not a promise
  that the measurement is valid or the effect is real.
- Perfect nesting is sometimes unavoidable and the study still worth reporting. The point is
  to say so plainly, not to abandon the data.
