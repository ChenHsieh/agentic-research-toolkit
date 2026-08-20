# Agentic Research Toolkit

Reusable scaffolding for doing real scientific research with Claude Code — portable skills and universal session hygiene, independent of cluster or domain.

### 📖 [Read the guide →](https://chenhsieh.github.io/agentic-research-toolkit/)

New to agentic tools? That site is a gentle, no-jargon on-ramp for wet-lab scientists: a three-stage ramp from pasting a bench note into a plain chat, up to running a documented project. No coding or git assumed.

## Why this exists

The gap between "Claude can do science" and "Claude actually does my science" is the platform around the prompt, not the prompt. Scientific work runs for hours, touches real data, fails in informative ways, and has to be reproducible.

**Every skill here is written for discovery, not validation.** The job of an agentic research run is to surface what you didn't expect — anomalies, counter-evidence, overlooked candidates. A skill that only says "yes, your hypothesis holds" is a failure mode, not an output.

## What's in here

| Path | What |
| --- | --- |
| [`docs/`](docs/) | The beginner on-ramp, served as a [site](https://chenhsieh.github.io/agentic-research-toolkit/). Long-form write-ups live alongside as Markdown. |
| [`skills/`](skills/) | Portable `SKILL.md` workflows — named, tool-scoped procedures for Claude Code or as a plain checklist. |
| [`setup/`](setup/) | Universal `CLAUDE.md`: session durability, bash discipline, data safety, provenance, citation integrity. Drop into `~/.claude/` or a project root. |

## Skills

Four compose in order, and each is designed to output something you did not want to hear:

| Skill | Purpose |
| --- | --- |
| [`design-confound-audit`](skills/design-confound-audit/) | Which questions can this design answer? Run before choosing a test. |
| [`statistic-null`](skills/statistic-null/) | Give a derived statistic its own null before believing it. |
| [`result-autopsy`](skills/result-autopsy/) | Execute the checks most likely to kill your own finding. |
| [`second-opinion-concordance`](skills/second-opinion-concordance/) | Independent second method; the disagreements are the product. |

Plus:

| Skill | Purpose |
| --- | --- |
| [`accession-paper-crosswalk`](skills/accession-paper-crosswalk/) | Link an SRA/BioProject accession to its paper and back; the gaps are the finding. |
| [`tikz-figures`](skills/tikz-figures/) | Template-first TikZ/pgfplots figures that match the manuscript's fonts. |
| [`ml-genomics-best-practices`](skills/ml-genomics-best-practices/) | Checklist-driven workflow for defensible ML in genomics. |
| [`scientific-schematics`](skills/scientific-schematics/) | Workflow diagrams as interactive HTML with SVG export. |
| [`trait-gene-miner`](skills/trait-gene-miner/) | Mine validated trait–gene associations into an interactive dashboard. |
| [`ecosystem-mapper`](skills/ecosystem-mapper/) | Map research fields and funding landscapes as network graphs. ⚠ Port incomplete — a design document, not a runnable procedure. |

Six are original to this repo; four are adapted from upstream community / Anthropic examples, `SKILL.md` only. See [`skills/README.md`](skills/README.md) for attribution and porting caveats.

## Companion repo

[`sapelo2-boilerplate`](https://github.com/ChenHsieh/sapelo2-boilerplate) — a worked HPC case built on this repo's `setup/CLAUDE.md`.

## Honest limits

- Skills written against a specific tool version or data schema will rot. Re-verify anything load-bearing.
- Agents summarizing literature sometimes cite papers that don't support the claim. Spot-check before it leaves the chat window.
- Long sessions lose intermediate reasoning to compaction. Task lists and tracker docs are the backup; conversation is not durable.
- Discovery-oriented skills still filter through what the agent knows. Genuinely novel findings need a human to notice the output is strange.

Not a tutorial, not a benchmark, not a framework. Markdown files and shell snippets you copy, fork, and modify.

## License

Code [MIT](LICENSE); content [CC BY 4.0](LICENSE-CONTENT). Fork, adapt, attribute.

By [Chen Hsieh](https://github.com/ChenHsieh) — bioinformatics PhD candidate. Issues and pull requests welcome.
