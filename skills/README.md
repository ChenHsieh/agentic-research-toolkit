# Skills

Portable, named workflows for Claude Code. Each skill is a directory with:

- `SKILL.md` — YAML frontmatter (`name`, `description`, `allowed-tools`) and a step-by-step procedure.
- `references/` — supporting material loaded on demand (optional).
- `example/` — a worked run with public inputs (optional, recommended).

Dual-use: readable by Claude Code or as a plain checklist.

## Criteria for inclusion

1. Repeatable research task, not a one-off.
2. Explicit inputs, outputs, and allowed tools.
3. **Written for discovery, not validation.** A skill's job is to surface anomalies, counter-evidence, and overlooked candidates — not to confirm what the user already believes. A skill that only reports back "yes, your hypothesis holds" is broken.
4. Has a worked run in its own `example/`, or a clear path to one.

If the whole thing fits in three sentences, it is a prompt, not a skill.

## Index

| Skill | Purpose | Status |
| --- | --- | --- |
| [`ecosystem-mapper`](ecosystem-mapper/) | Map research fields, funding landscapes, and innovation ecosystems as interactive HTML network graphs from public data. | ⚠ Adapted, **port incomplete** — depends on 6 unported files and on the Cowork sandbox; see the warning at the top of its `SKILL.md`. Design document, not a runnable procedure. |
| [`trait-gene-miner`](trait-gene-miner/) | Mine experimentally validated trait–gene associations from ontology databases and literature; outputs an interactive HTML dashboard. | Adapted (SKILL.md only) |
| [`ml-genomics-best-practices`](ml-genomics-best-practices/) | Checklist-driven workflow for reproducible, defensible ML in genomics: anti-circularity, class balance, LR baselines, bootstrap CIs, permutation tests. | Adapted (SKILL.md only) |
| [`scientific-schematics`](scientific-schematics/) | Build publication-quality scientific workflow diagrams as self-contained interactive HTML with one-click SVG export for Figma. | Adapted (SKILL.md only) |
| [`tikz-figures`](tikz-figures/) | Template-first TikZ/pgfplots workflow for manuscript figures that share the body text's fonts and regenerate from a data file; front-loads the failure modes that render silently wrong figures. | Original |
| [`result-autopsy`](result-autopsy/) | Adversarially audit a result you already produced: execute the checks most likely to kill it, and report what survived at what strength. | Original |
| [`design-confound-audit`](design-confound-audit/) | Decide which questions a dataset's design can actually answer, before any model is fit. Returns a per-question answerable / not-answerable verdict. | Original |
| [`second-opinion-concordance`](second-opinion-concordance/) | Re-derive a call set with a methodologically independent method and mine the disagreements, which are the product. | Original |
| [`statistic-null`](statistic-null/) | Give a derived summary statistic its own null before believing it; includes the arithmetic-artifact check for ratio statistics. | Original |
| [`accession-paper-crosswalk`](accession-paper-crosswalk/) | Link a BioProject/SRA/GEO accession to its paper and back, routing around NCBI's near-empty BioProject→PubMed link table; treats deposited-but-unpublished data and accession mismatches as the finding. | Original (endpoints verified 2026-08-19) |

## The discovery four

`result-autopsy`, `design-confound-audit`, `second-opinion-concordance`, and `statistic-null`
are designed to be used together and to compose in a rough order:

1. **Before analysis** — `design-confound-audit`: which questions can this data answer?
2. **While computing** — `statistic-null`: does this derived number mean anything?
3. **Before writing up** — `result-autopsy`: what would kill this finding?
4. **Before building on it** — `second-opinion-concordance`: does an independent method agree,
   and what does it see that the first one missed?

Each one's designed output is something the user did not want to hear, which is the point.
Each `SKILL.md` carries a "what this does not cover" table pointing at the others, so they
stay distinct rather than sprawling into one general-purpose skepticism skill.

## Attribution

The first four skills in this index are **adapted from upstream community / Anthropic example skills**, not authored from scratch in this repo. The originals carry their own design choices (sprint structure, anti-hallucination controls, dashboard schemas, etc.); modifications here are mostly bias toward discovery-not-validation framing and bioinformatics-specific defaults. Where the original author is known, it should be credited inside the individual skill's `SKILL.md` header — pull requests adding proper attribution are welcome.

**Caveat:** only `SKILL.md` was ported for each. The original skills may reference companion files (`references/*.md`, `scripts/`, `example/`) that are **not included here**. The skill will still run, but Claude will not be able to load those side files; either reconstruct them, point the skill at substitutes, or treat the missing reads as no-ops.

## Using a skill

- **In Claude Code:** copy the skill directory into the project's `.claude/skills/` or your user-level `~/.claude/skills/` and invoke by name.
- **By hand:** open `SKILL.md` and follow the steps as a checklist.

## Porting

Skills assume Claude Code at a recent stable version, a working conda/pixi/virtualenv for the tools declared in frontmatter, and network access to any public databases named. Swap the bioinformatics-specific references when adapting to another domain.
