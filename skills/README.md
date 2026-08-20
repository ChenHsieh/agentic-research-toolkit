# Skills

Portable, named workflows for Claude Code. Each skill is a directory with a `SKILL.md` —
YAML frontmatter (`name`, `description`, `allowed-tools`) and a step-by-step procedure.
Optional `references/` and `example/` alongside it.

Dual-use: readable by Claude Code, or as a plain checklist.

## Criteria for inclusion

1. Repeatable research task, not a one-off.
2. Explicit inputs, outputs, and allowed tools.
3. **Written for discovery, not validation.** A skill's job is to surface anomalies,
   counter-evidence, and overlooked candidates — not to confirm what the user already
   believes. A skill that only reports "yes, your hypothesis holds" is broken.
4. Has a worked run in its own `example/`, or a clear path to one.

If the whole thing fits in three sentences, it is a prompt, not a skill.

## Index

| Skill | Purpose | Status |
| --- | --- | --- |
| [`design-confound-audit`](design-confound-audit/) | Which questions the design can actually answer, before any model is fit. | Original |
| [`statistic-null`](statistic-null/) | Give a derived statistic its own null; includes the arithmetic-artifact check for ratios. | Original |
| [`result-autopsy`](result-autopsy/) | Execute the checks most likely to kill a finding you already produced. | Original |
| [`second-opinion-concordance`](second-opinion-concordance/) | Independent second method; the discordant cells are the deliverable. | Original |
| [`accession-paper-crosswalk`](accession-paper-crosswalk/) | Accession ↔ paper linking, routing around NCBI's near-empty BioProject→PubMed table. | Original (endpoints verified 2026-08) |
| [`tikz-figures`](tikz-figures/) | Template-first TikZ/pgfplots figures that regenerate from a data file. | Original |
| [`ml-genomics-best-practices`](ml-genomics-best-practices/) | Anti-circularity, class balance, LR baselines, bootstrap CIs, permutation tests. | Adapted |
| [`scientific-schematics`](scientific-schematics/) | Workflow diagrams as interactive HTML with one-click SVG export. | Adapted |
| [`trait-gene-miner`](trait-gene-miner/) | Trait–gene associations from ontology databases and literature. | Adapted |
| [`ecosystem-mapper`](ecosystem-mapper/) | Research fields and funding landscapes as network graphs. | ⚠ Adapted, **port incomplete** — see the warning in its `SKILL.md` |

## The discovery four

The first four compose in a rough order:

1. **Before analysis** — `design-confound-audit`: which questions can this data answer?
2. **While computing** — `statistic-null`: does this derived number mean anything?
3. **Before writing up** — `result-autopsy`: what would kill this finding?
4. **Before building on it** — `second-opinion-concordance`: does an independent method agree,
   and what does it see that the first one missed?

Each carries a "what this does not cover" table pointing at the others, so they stay distinct
rather than sprawling into one general-purpose skepticism skill.

## Attribution

The four **Adapted** skills come from upstream community / Anthropic example skills, not
authored here. Modifications are mostly discovery-not-validation framing and bioinformatics
defaults. Where an original author is known, credit belongs in that skill's `SKILL.md` header —
PRs adding proper attribution are welcome.

**Caveat:** only `SKILL.md` was ported for each. Originals may reference companion
`references/`, `scripts/`, or `example/` files **not included here**. For most, treat the
missing reads as no-ops. For `ecosystem-mapper` this is fatal — two of its reads are
load-bearing, and it is a design document rather than a runnable procedure.

## Using a skill

- **In Claude Code:** copy the directory into `.claude/skills/` or `~/.claude/skills/` and
  invoke by name.
- **By hand:** open `SKILL.md` and follow it as a checklist.

Skills assume a recent Claude Code, a working environment for any tools named, and network
access to any public databases referenced. Swap the bioinformatics-specific defaults when
adapting to another domain.
