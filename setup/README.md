# setup

Universal Claude Code hygiene — rules that apply on any machine, any project. The drop-in file
is [`CLAUDE.md`](CLAUDE.md).

## What's in scope

Each section names what it's protecting against. If you want to change a rule, know that first.

- **Session durability** — `/rename` early; task lists for multi-step work; conclusions to a
  file, not just the chat. Survives context compaction.
- **Bash discipline** — no shell state persists between calls; chain commands; verify the
  environment took. The most common silent-failure source in agentic sessions.
- **Long-running work** — background past a couple of minutes, log to a file, record the job
  handle. A submitted job is not a finished job.
- **Tool hygiene** — dedicated tools over Bash; parallel calls when independent; plan mode
  before non-trivial changes; read before you edit.
- **Data safety** — never modify raw data in place; destructive operations need an explicit
  yes; credentials and unpublished data stay off the wire.
- **Provenance** — record the exact command, pin versions and seeds, note what you skipped. A
  result you can't regenerate is an anecdote.
- **Claims, citations, and reporting** — don't cite what you haven't read; mark unverified
  claims as unverified; "it ran" is not "it worked."
- **Discovery over validation** — surface the unexpected, don't confirm the expected.
- **Cowork state** — read the tracker in, update it out, leave what's blocked and on whom.

## What's not here

Cluster-specific rules (quotas, sbatch templates, module versions) live in that cluster's
boilerplate — see [`sapelo2-boilerplate`](https://github.com/ChenHsieh/sapelo2-boilerplate) for
a worked HPC example. Project-specific rules (data paths, tool versions, domain conventions)
live in each project's own root `CLAUDE.md`.

## Install

Globally, for every project:

```bash
mkdir -p ~/.claude
curl -L https://raw.githubusercontent.com/ChenHsieh/agentic-research-toolkit/main/setup/CLAUDE.md -o ~/.claude/CLAUDE.md
```

Per-project (layered on top of the global file; project rules win on conflict):

```bash
curl -L https://raw.githubusercontent.com/ChenHsieh/agentic-research-toolkit/main/setup/CLAUDE.md -o ./CLAUDE.md
```

Or symlink a clone so updates flow through:

```bash
git clone https://github.com/ChenHsieh/agentic-research-toolkit.git ~/agentic-research-toolkit
ln -s ~/agentic-research-toolkit/setup/CLAUDE.md ~/.claude/CLAUDE.md
```

## Extending

Keep this as the *base* and layer additions below — don't duplicate these rules in a project
file. Claude Code merges `~/.claude/CLAUDE.md` with the project `CLAUDE.md`, so the universal
rules apply automatically.
