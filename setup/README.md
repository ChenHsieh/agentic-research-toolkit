# setup

Universal Claude Code hygiene — the rules and practices that apply on any machine, any project. The drop-in file is [`CLAUDE.md`](CLAUDE.md).

## What's in scope

Each rule in `CLAUDE.md` names its own *why* in one line. If you want to change a rule, know what it's protecting against first. The full list:

- **Session durability** — `/rename` early; task lists for multi-step work; memory discipline. Keeps work findable across sessions and survivable across context compaction.
- **Bash discipline** — no shell state persists between Bash tool calls; chain commands. The single most common silent-failure source in agentic sessions.
- **Tool hygiene** — dedicated tools over Bash; parallel calls when independent; plan mode before non-trivial changes. Produces faster, more reviewable work than free-form shell.
- **Discovery over validation** — skills and explorations exist to surface the unexpected, not to confirm what you already believe. An agent that only produces "yes, your hypothesis holds" is broken.
- **Cowork state** — if there's a shared tracker doc, read it in and update it out. That's the durable handoff.

## What's not here

- **Cluster-specific rules** (filesystem quotas, sbatch templates, module versions, QOS tables) — those live in the boilerplate for that cluster. For a worked HPC example: [`sapelo2-boilerplate/claude-code/`](https://github.com/ChenHsieh/sapelo2-boilerplate/tree/main/claude-code).
- **Project-specific rules** (data paths, tool versions, domain conventions) — those live in each project's own `CLAUDE.md` at the project root.

## Install

Globally (applies to every project Claude Code sees):

```bash
mkdir -p ~/.claude
curl -L https://raw.githubusercontent.com/ChenHsieh/agentic-research-toolkit/main/setup/CLAUDE.md -o ~/.claude/CLAUDE.md
```

Per-project (layered on top of `~/.claude/CLAUDE.md`, project rules win on conflict):

```bash
curl -L https://raw.githubusercontent.com/ChenHsieh/agentic-research-toolkit/main/setup/CLAUDE.md -o ./CLAUDE.md
```

Or clone the toolkit and symlink so updates flow through:

```bash
git clone https://github.com/ChenHsieh/agentic-research-toolkit.git ~/agentic-research-toolkit
ln -s ~/agentic-research-toolkit/setup/CLAUDE.md ~/.claude/CLAUDE.md
```

## Extending

If you are writing a cluster or project-specific `CLAUDE.md`, keep this file as the *base* and layer your additions below — don't duplicate the rules here in your project file. Claude Code merges `~/.claude/CLAUDE.md` with the project `CLAUDE.md`, so the universal rules apply automatically.
