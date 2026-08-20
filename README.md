# Agentic Research Toolkit

Reusable scaffolding for doing real scientific research with Claude Code — portable skills and universal session hygiene, independent of cluster or domain.

## Why this exists

Scientific work runs for hours on shared infrastructure, touches real data, fails in informative ways, and has to be reproducible. The gap between "Claude can do science" and "Claude actually does my science" is the platform around the prompt, not the prompt.

This repo collects the portable, cluster- and domain-agnostic pieces of that platform: **skills** that encode repeatable research procedures, and a universal **setup** (`CLAUDE.md`) covering session durability, bash discipline, tool hygiene, and the cowork pattern with a human collaborator. Cluster- and project-specific configs live in their own boilerplate repos.

**A principle, since this is instruction for science:** every skill here is written for **discovery, not validation**. The goal of an agentic research run is to surface things you didn't expect — anomalies, counter-evidence, overlooked candidates, alternative explanations — not to confirm what you already believe. A skill that only says "yes, your hypothesis holds" is a failure mode, not an output.

> **New to agentic tools?** Most of this repo assumes you already work with Claude Code or similar. If you don't yet, start with the gentle on-ramp in [`docs/`](docs/): it takes a wet-lab scientist from pasting a bench note into a plain chat, up to running a documented project, with no coding or git assumed.

## What's in here

| Path | What |
| --- | --- |
| [`docs/`](docs/) | **An on-ramp to agentic research** — a gentle, no-jargon guide for wet-lab scientists new to these tools, served as an interactive [GitHub Pages site](https://chenhsieh.github.io/agentic-research-toolkit/). Swipe a short archetype test to find your setup, then level up through a three-stage ramp (chat-only → agentic file access → starter-kit templates), with a landscape tool-chain chooser, glossary, copy-pasteable templates, and a [resources](docs/resources.md) page. Long-form write-ups live alongside as Markdown. Start here if you have never used an agentic tool. |
| [`skills/`](skills/) | Portable `SKILL.md` workflows — named, tool-scoped procedures you can load into Claude Code or follow by hand. |
| [`setup/`](setup/) | Universal `CLAUDE.md` — session durability (`/rename`, task lists, memory), bash discipline, tool hygiene, discovery-not-validation, cowork state. Drop it into `~/.claude/` or a project root. |

## Companion repos

- [`sapelo2-boilerplate`](https://github.com/ChenHsieh/sapelo2-boilerplate) — applied HPC case: a fully worked Claude Code setup for UGA's GACRC Sapelo2 cluster (`CLAUDE.md` ruleset, permission allowlist, colorized statusline) alongside a collection of per-tool sbatch scripts and snakemake pipelines. Uses the universal `setup/CLAUDE.md` from this repo as its base.

## Featured skills

Four of the ten included skills are **adapted from upstream community / Anthropic example skills**; the other six are original to this repo. For the adapted four, only `SKILL.md` was ported — companion `references/`, `scripts/`, and `example/` directories from the originals are not included. See [`skills/README.md`](skills/README.md#attribution) for the attribution and porting caveats, and note that `ecosystem-mapper`'s port is **incomplete enough that it is a design document rather than a runnable procedure**.

| Skill | Purpose |
| --- | --- |
| [`ecosystem-mapper`](skills/ecosystem-mapper/) | Map research fields, funding landscapes, and innovation ecosystems as interactive network graphs from public data. |
| [`trait-gene-miner`](skills/trait-gene-miner/) | Mine experimentally validated trait–gene associations from ontology databases and literature into an interactive dashboard. |
| [`ml-genomics-best-practices`](skills/ml-genomics-best-practices/) | Checklist-driven workflow for reproducible, defensible ML in genomics. |
| [`scientific-schematics`](skills/scientific-schematics/) | Publication-quality scientific workflow diagrams as interactive HTML with one-click SVG export for Figma. |
| [`tikz-figures`](skills/tikz-figures/) | Template-first TikZ/pgfplots figures that match the manuscript's fonts and regenerate from a data file. |
| [`design-confound-audit`](skills/design-confound-audit/) | Which questions can this design actually answer? Run before choosing a test. |
| [`statistic-null`](skills/statistic-null/) | Give a derived statistic its own null before believing it. |
| [`result-autopsy`](skills/result-autopsy/) | Execute the checks most likely to kill your own finding, before someone else does. |
| [`second-opinion-concordance`](skills/second-opinion-concordance/) | Validate a call set with an independent method; the disagreements are the product. |
| [`accession-paper-crosswalk`](skills/accession-paper-crosswalk/) | Link an SRA/BioProject accession to its paper and back; the gaps are the finding. |

## Honest limits

- Memories and references drift; skills written against a specific tool version or data schema will rot. Re-verify anything load-bearing.
- Agents summarizing literature sometimes cite papers that don't support the claim. Spot-check citations before they leave the chat window.
- Long sessions lose intermediate reasoning when context is compacted. Task lists and tracker docs are the backup; conversation alone is not durable.
- Even discovery-oriented skills filter through what the agent already knows. Genuinely novel findings need a human to notice that the output is strange.
- Choosing which procedure to run, and deciding what "valid output" looks like, is still the scientist's job.

## What this is NOT

Not a Claude Code tutorial; not a benchmark; not a framework. Markdown files, configs, and shell snippets you copy, fork, and modify.

## License & author

Code under [MIT](LICENSE); content under [CC BY 4.0](LICENSE-CONTENT). Fork, adapt, attribute.

Chen Hsieh — bioinformatics PhD candidate, University of Georgia, graduating Summer 2026. <chen.hsieh.uga@gmail.com>
