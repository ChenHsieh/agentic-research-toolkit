# CLAUDE.md — universal agentic research hygiene

Rules that apply on any machine, any project. Not cluster-specific, not domain-specific. Drop this at `~/.claude/CLAUDE.md` for global effect or in a project root for per-project effect.

---

## Session durability

- **`/rename` early.** Give the session a descriptive name in the first few turns so `claude --resume` can find this work later. Default timestamp names become un-findable after a month.
- **Use task lists for anything spanning more than ~3 non-trivial tool calls.** `TaskCreate` at the start, `TaskUpdate` as work progresses. Task state survives context compaction and explicit resumes; conversation state does not.
- **Commit durable facts to memory; prune stale ones.** Memory is for "what was true at a point in time" — re-verify before acting on recalled details.

## Bash discipline

- **No shell state persists between Bash tool calls.** Each call is a fresh shell — `module load`, `conda activate`, `export`, `cd` all reset. Chain everything needed into one `&&`-joined command.
- Exception: a conda env activated *before* `claude` launched is inherited for the whole session.

## Tool hygiene

- **Prefer dedicated tools over Bash.** Use `Read`, `Edit`, `Write`, `Glob`, `Grep` when they fit — they give cleaner UX than `cat`, `grep`, `find` in shell.
- **Parallel tool calls when independent.** Multiple Read/Grep/Bash calls with no data dependency go in one message, not sequentially.
- **Plan mode before non-trivial changes.** A change that touches three or more files deserves a written plan first. Coding without a plan breaks more than it builds.

## Discovery, not validation

Any skill or open-ended exploration is for surfacing things the user didn't expect — anomalies, counter-evidence, overlooked candidates, alternative explanations. "Yes, your hypothesis holds" is a failure mode. If a prompt can only be answered *confirm* or *deny*, reframe it so it surfaces what's missing from the reasoning.

## Cowork state

If the project has a shared tracker doc (e.g. `docs/cowork/Project_Tracker.md`), read it at session start and update it on the way out. The tracker is the durable handoff between agent sessions and human working time; conversation context is not.

---

**Scope of this file.** This file is deliberately domain- and infrastructure-agnostic. Cluster-specific rules (filesystem quotas, sbatch templates, module versions) live in the boilerplate for that cluster — see [`sapelo2-boilerplate/claude-code/`](https://github.com/ChenHsieh/sapelo2-boilerplate/tree/main/claude-code) for one worked example. Project-specific rules (data paths, tool versions, domain conventions) live in that project's own `CLAUDE.md`.
