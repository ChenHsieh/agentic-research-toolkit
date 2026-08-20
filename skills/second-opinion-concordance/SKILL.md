---
name: second-opinion-concordance
description: >
  Re-derive a set of calls with a methodologically independent second method and mine the
  disagreements, which are the actual product. Covers choosing a method that fails differently
  from the first (not a parameter variant of it), running both over the same entities, building
  a concordance table, and classifying each discordance class as a false positive of method A
  versus a blind spot of method B. Use before trusting a call set you will build on, when a
  reviewer asks for validation, or when two tools disagree and you need to decide which to
  believe. Trigger on "validate these calls", "second method", "cross-check with", "these two
  tools disagree", "confirm this gene set / peak set / variant set", "how do I know these are
  real".
allowed-tools: Read Write Edit Bash Glob Grep
---

# Second-opinion concordance

**The concordant rows are the boring output.** If two methods agree everywhere, you learned
that they share assumptions. The disagreements are where the information is, and this
procedure is built to produce and classify them rather than to compute an agreement
percentage and stop.

> **A high concordance rate is not validation.** Two methods that share a database, an aligner,
> a reference, or a statistical assumption will agree with each other while being wrong
> together. Independence is a property you have to argue for, not a number you report.

## When to use this

Before a call set becomes a foundation — a gene list you will do enrichment on, variants you
will follow up, peaks you will annotate, classifications you will model. When a reviewer asks
for orthogonal validation. When two tools already disagree and you need a principled way to
decide.

Do not use it to break a tie by majority vote among three similar tools. That measures
popularity of an assumption, not truth.

## Step 1 — choose a method that fails differently

This is the entire ballgame, and it is where the procedure is usually botched.

**Not independent:** the same tool with different parameters; a wrapper around the same core
algorithm; a second database that was populated by importing the first; a different model
trained on the same corpus; re-running with a different seed.

**Independent:** a different *kind* of evidence or a different *failure mode*. Sequence
similarity versus synteny. Statistical enrichment versus direct assay. Model prediction versus
curated annotation. Automated call versus manual inspection. A method whose systematic errors
have a different cause than the first one's.

Write down, before running: **how does method A fail, how does method B fail, and are those
the same failure?** If you cannot answer, you have not chosen a second method yet. Also check
for hidden shared ancestry — two tools that both depend on the same reference build or the
same upstream annotation are less independent than their documentation suggests.

## Step 2 — run both over the identical entity set

Both methods must be applied to the same units, with the same inclusion criteria, and the
outputs mapped to a shared identifier space. Most apparent discordance in practice is an
identifier-mapping artifact, not a biological or statistical one.

Before interpreting anything: reconcile the identifier spaces, report how many entities failed
to map in each direction, and confirm the entity counts are what you expect. Entities present
in one method's universe but absent from the other's are **not** discordant — they are
out of scope, and mixing the two categories corrupts every number downstream.

## Step 3 — build the concordance table and classify the cells

| | B calls positive | B calls negative |
|---|---|---|
| **A calls positive** | Concordant positive — the boring, reassuring cell | **Discordance class I** |
| **A calls negative** | **Discordance class II** | Concordant negative |

Then do the work that makes this a skill rather than a cross-tab. For each discordance class,
decide what it means *given the known failure modes from Step 1*:

- **Class I (A only).** Candidate false positive of A — or a real signal B is blind to by
  construction. Which one depends on B's failure mode. If B systematically misses a category
  and these calls are in that category, this is B's blind spot, not A's error.
- **Class II (B only).** Symmetric reasoning. This class is frequently the most interesting:
  entities the *original* method missed, surfaced by the second. Do not discard it as noise
  because it was not in your starting list — that is the whole reason you ran a second method.

Assign every discordant entity to a class with a stated reason. "Unresolved" is a legitimate
class; "ignored" is not.

## Step 4 — follow up the discordant set, not the concordant one

The concordant calls need no further work. Spend the effort on the disagreements:

- Take a sample of each discordance class and adjudicate by hand or by a third kind of
  evidence. Report how many you checked and what fraction resolved in each direction.
- Look for structure in the discordant set: are the disagreements concentrated in a category,
  a size range, a region, a class of input? Structured discordance names a systematic
  limitation of one method. Unstructured discordance is closer to noise.
- **Class II entities that survive adjudication are a finding in their own right** — they are
  things the primary method missed, and they often deserve their own follow-up.

## Step 5 — report both methods and the disagreement

Never report the intersection alone as though it were the answer. The intersection is a
high-precision, low-recall set, and presenting it as "the validated calls" silently discards
Class II and overstates confidence.

Report: both call sets with their sizes, the concordance table with counts, the classification
of each discordance class with reasoning, the adjudication sample and its outcome, and which
downstream conclusions change depending on which set you use. If a conclusion holds only under
one method's calls, say that explicitly.

## What this does not cover

| Not covered | Where it belongs |
|---|---|
| Auditing a single result for artifacts | `result-autopsy` |
| Whether the design permits the comparison at all | `design-confound-audit` |
| Whether a derived statistic beats its own null | `statistic-null` |
| Choosing among many models by performance | Model selection; this is about call agreement |
| Benchmarking against a gold standard | Different procedure — that has ground truth, this does not |

## Honest limits

- Independence is argued, not proven. Two methods can share an assumption neither documents.
- When both methods are wrong in the same direction, concordance is maximally reassuring and
  maximally misleading. Nothing in this procedure detects that.
- Adjudicating discordance by hand reintroduces the analyst's own bias; sample before you
  look, and record the sampling rule.
