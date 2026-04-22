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
| [`ecosystem-mapper`](ecosystem-mapper/) | Map research fields, funding landscapes, and innovation ecosystems as interactive HTML network graphs from public data. | Adapted (SKILL.md only) |
| [`trait-gene-miner`](trait-gene-miner/) | Mine experimentally validated trait–gene associations from ontology databases and literature; outputs an interactive HTML dashboard. | Adapted (SKILL.md only) |
| [`ml-genomics-best-practices`](ml-genomics-best-practices/) | Checklist-driven workflow for reproducible, defensible ML in genomics: anti-circularity, class balance, LR baselines, bootstrap CIs, permutation tests. | Adapted (SKILL.md only) |
| [`scientific-schematics`](scientific-schematics/) | Build publication-quality scientific workflow diagrams as self-contained interactive HTML with one-click SVG export for Figma. | Adapted (SKILL.md only) |

## Attribution

The four skills currently in this index are **adapted from upstream community / Anthropic example skills**, not authored from scratch in this repo. The originals carry their own design choices (sprint structure, anti-hallucination controls, dashboard schemas, etc.); modifications here are mostly bias toward discovery-not-validation framing and bioinformatics-specific defaults. Where the original author is known, it should be credited inside the individual skill's `SKILL.md` header — pull requests adding proper attribution are welcome.

**Caveat:** only `SKILL.md` was ported for each. The original skills may reference companion files (`references/*.md`, `scripts/`, `example/`) that are **not included here**. The skill will still run, but Claude will not be able to load those side files; either reconstruct them, point the skill at substitutes, or treat the missing reads as no-ops.

## Using a skill

- **In Claude Code:** copy the skill directory into the project's `.claude/skills/` or your user-level `~/.claude/skills/` and invoke by name.
- **By hand:** open `SKILL.md` and follow the steps as a checklist.

## Porting

Skills assume Claude Code at a recent stable version, a working conda/pixi/virtualenv for the tools declared in frontmatter, and network access to any public databases named. Swap the bioinformatics-specific references when adapting to another domain.
