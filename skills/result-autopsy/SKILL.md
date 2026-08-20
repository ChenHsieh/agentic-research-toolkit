---
name: result-autopsy
description: >
  Adversarially audit a result you have already produced, before a reviewer or a collaborator
  does it for you. Given a finding, a results file, or a claim in a draft, this executes the
  checks most likely to kill it - shared variables on both sides of a comparison, censoring
  that points the same way as the effect, caps and budgets that manufacture the trend, and
  nulls that do not exclude the artifact - and reports what survived at what strength. Use
  when a result is about to be written up, cited, presented, or built on; when a number looks
  better than expected; or when someone asks "how confident are you in this." Trigger on
  "sanity check this result", "is this real", "before I write this up", "audit my analysis",
  "why is this effect so clean".
allowed-tools: Read Write Edit Bash Glob Grep
---

# Result autopsy

**The job is to break your own result.** Not to review it, not to describe its limitations in
a paragraph — to run the specific checks that would falsify it and report what happened.

A finding that survives an honest autopsy is worth more than one that was never tested. A
finding that dies here dies cheaply, months before it would have died in review.

> **Execute the checks. Do not list them.** A section that says "we considered the possibility
> of circularity" and shows no test is not an audit; it is an alibi. If a check cannot be run,
> say so and say why — that is a different and honest outcome.

## When to use this

Use it when a result is about to become load-bearing: written into a draft, shown in a talk,
used to choose the next experiment, or cited by someone else. Use it when a number came out
cleaner than the design should permit.

Do not use it as a first look at fresh data — you cannot autopsy something that has not been
computed yet, and running it too early turns into generic skepticism. Do not use it to review
someone else's work without their agreement; the register here is deliberately harsh, and it
is only appropriate pointed at your own claims.

## Step 0 — write the claim down as a falsifiable sentence

Before touching data, get the claim into one sentence with the effect, the direction, the
comparison, and the population. "Model A is more robust" is not auditable. "Model A's accuracy
degrades less than Model B's under the same perturbation budget, across the held-out set" is.

Write down separately: **what would have to be true for this to be an artifact.** That list
drives everything below. If you cannot name a single way the result could be spurious, you do
not understand it well enough to audit it yet.

## Step 1 — run the structural checks

These are ordered by how often they are the actual cause. Run each one, record the outcome.

**1. Shared variables across the comparison.** Does any quantity appear on both sides — as a
regressor and inside the regressand, as a filter and as an outcome, in the features and in the
label? A ratio whose numerator and denominator share a term will trend on its own. Derived
targets are the common trap: a label computed from a variable that is also a feature builds
the answer into the input. Check the actual column provenance, not the variable names.

**2. Censoring and truncation that point the same way as the effect.** Are values clipped,
capped, floored, or dropped at a boundary — and does the fraction affected differ between the
groups being compared? An effect that lives entirely in the censored region is a property of
the boundary. Report the censoring rate per group, not overall.

**3. Caps, budgets, and stopping rules.** Any procedure with a maximum — iterations, edits,
retries, sequence length, time limit — can produce a trend purely by running out. If the
groups hit the cap at different rates, the trend is the cap. Rerun with the cap raised on a
subsample; if the effect shrinks, you have your answer.

**4. Selection into the analysis set.** How did rows get in? Filters applied after seeing
outcomes, "successful runs only", quality thresholds correlated with the effect, and
convenience sampling all select for the result. Compare the excluded rows to the included ones
on the outcome variable.

**5. Does the null exclude the artifact?** A p-value is only as good as what its null permits.
A permutation that shuffles labels but preserves the structure causing the artifact will
happily report significance. State what the null holds fixed and confirm the suspected
artifact is *not* among the things it preserves.

**6. Multiplicity and the garden of forking paths.** How many variants — models, thresholds,
subsets, preprocessing choices — were tried before this one? Count them honestly, including
the ones abandoned early. Report the count next to the p-value even when you do not formally
correct.

**7. Does it hold under a harder split?** If the units share structure — homology, family,
batch, subject, site, time — a random split leaks. Re-split so related units cannot straddle
the boundary and rerun. Ranking inversions under a harder split are common and informative.

## Step 2 — record the verdict at the right resolution

The output is not "holds" or "fails." It is a table with one row per check:

| Check | Ran? | Finding | Effect on the claim |
|---|---|---|---|
| Shared variables | Yes | Outcome shares a term with predictor X | Effect size falls when recomputed without it |
| Censoring | Yes | Censoring rate differs sharply between arms | Restricting to uncensored removes the trend |
| Harder split | No | No grouping metadata available | Unresolved — flag before citing |

(Illustrative rows. Fill in your own measured values; do not carry these forward.)

Three outcomes are legitimate and each must be reported plainly:

- **Survived.** The claim stands. State what it survived, because that is now its warrant.
- **Survived weaker.** Very common and the most valuable result of an autopsy. The conclusion
  holds but the evidence is not what you thought — the effect is smaller, the p-value orders of
  magnitude larger, the scope narrower. **Downgrade the claim in every artifact that carries
  it,** not just the one you audited.
- **Did not survive.** Say so directly and identify every downstream result that inherited it.
  A retraction note at the top of the affected file, dated, beats a quiet deletion.

**Record the concerns that turned out to be unfounded, too.** An autopsy that only reports
problems is performing doubt rather than testing it, and the reader cannot tell how hard you
looked. "Suspected the embedding pipeline had collapsed; tested it; the geometry was
unusual but the pipeline was fine" is a real finding.

## Step 3 — propagate

A finding that changed here has children. Grep the project for the number, the figure, and the
claim's phrasing. Update or flag each occurrence, and date the change. The failure mode is an
audited result that stays corrected in one file and uncorrected in the abstract.

## What this does not cover

| Not covered | Where it belongs |
|---|---|
| Whether the statistic itself is meaningful before any comparison | A null for the statistic — see `statistic-null` |
| Whether the study design can answer the question at all | A design-confound audit, run before analysis |
| Confirming a result with an independent method | `second-opinion-concordance` |
| Code correctness and unit-level bugs | Tests and code review; this assumes the code does what it says |
| Reviewing another person's manuscript | Out of scope by design — see "When to use this" |

## Honest limits

- An autopsy tests the failure modes you can name. Novel artifacts survive it.
- Running the same check twice with different framings mostly produces the same answer twice;
  breadth across check types beats depth within one.
- The skill's output is only as good as the claim written in Step 0. A vague claim yields a
  vague verdict, which reads as reassurance.
