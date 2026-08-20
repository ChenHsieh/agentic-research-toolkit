# CLAUDE.md — universal agentic research hygiene

Rules that apply on any machine, any project. Not cluster-specific, not domain-specific. Drop this at `~/.claude/CLAUDE.md` for global effect or in a project root for per-project effect.

Every rule below names what it is protecting against. If a rule costs more than the failure it prevents, delete it — but delete it knowingly.

---

## Session durability

*Research runs span days and multiple sessions; conversation context does not.*

- **`/rename` early.** Give the session a descriptive name in the first few turns so `claude --resume` can find this work later. Default timestamp names become un-findable after a month.
- **Use task lists for anything spanning more than ~3 non-trivial tool calls.** `TaskCreate` at the start, `TaskUpdate` as work progresses. Task state survives context compaction and explicit resumes; conversation state does not.
- **Write conclusions to a file, not just to the chat.** Anything you would be annoyed to re-derive belongs in a tracker, a decision log, or a commit message before the session ends. Compaction silently discards the reasoning that got you there.
- **Commit durable facts to memory; prune stale ones.** Memory is for "what was true at a point in time" — re-verify before acting on recalled details.

## Bash discipline

*The single most common silent-failure source in agentic sessions: a command that ran in the wrong environment and reported success.*

- **No shell state persists between Bash tool calls.** Each call is a fresh shell — `module load`, `conda activate`, `export`, `cd` all reset. Chain everything needed into one `&&`-joined command.
- Exception: a conda env activated *before* `claude` launched is inherited for the whole session.
- **Check that the environment took, don't assume it.** When a command depends on a specific interpreter or toolchain, confirm which one actually resolved (`which`, `--version`) before trusting the output of a long run.
- **Quote paths and globs.** Research paths carry spaces, brackets, and version numbers; an unquoted glob that matches nothing expands to itself and gets passed along as a literal filename.

## Long-running work

*Scientific jobs run for hours. An agent that blocks on them wastes the session; an agent that forgets them loses the result.*

- **Background anything that outlives a couple of minutes**, then poll it. Do not sit in a foreground call waiting for a job to finish.
- **Capture output to a log file, not only to the terminal.** `> run.log 2>&1` costs nothing and is the only artifact left after a disconnect or a compaction.
- **Record the job handle** — PID, job ID, log path — into the task list or tracker the moment the job starts, so a later session can find a run it did not launch.
- **A submitted job is not a finished job.** Report "submitted, ID 12345" as submitted. Check the exit status and the actual output before calling it done.

## Tool hygiene

*Faster, more reviewable work than free-form shell.*

- **Prefer dedicated tools over Bash.** Use `Read`, `Edit`, `Write`, `Glob`, `Grep` when they fit — they give cleaner UX than `cat`, `grep`, `find` in shell.
- **Parallel tool calls when independent.** Multiple Read/Grep/Bash calls with no data dependency go in one message, not sequentially.
- **Plan mode before non-trivial changes.** A change that touches three or more files deserves a written plan first. Coding without a plan breaks more than it builds.
- **Read before you edit.** Editing a file you have only inferred the contents of is how working analysis code quietly stops matching the paper it produced.

## Data safety

*Raw data is often irreplaceable — a re-run costs weeks of bench time or an exhausted sample.*

- **Never modify raw or source data in place.** Read it, write derived output to a separate directory. If a step must transform inputs, it writes a new file.
- **Destructive operations need explicit confirmation** — `rm -rf`, overwriting an existing result, force-pushing, dropping a table, or truncating a shared file. Say what will be lost and wait for a yes.
- **Look before you overwrite.** If the target's contents contradict how it was described, or you did not create it, surface that instead of proceeding.
- **Keep credentials and unpublished data out of anything that leaves the machine.** API keys, participant identifiers, embargoed results, and manuscript text under peer review do not belong in a commit, a pasted snippet, or a third-party service.

## Provenance

*A result you cannot regenerate is an anecdote.*

- **Record the exact command that produced a result** next to the result — full arguments, input paths, and the directory it ran from.
- **Pin what varies:** tool versions, reference genome or database builds and their download dates, random seeds. "Latest" is not a version.
- **Separate the parameters from the code.** A run configured by an edited-in-place constant cannot be reproduced from the file that remains.
- **Note what you skipped.** Sampling, filtering, a step that failed and was worked around — an undocumented shortcut reads as full coverage to whoever inherits the analysis.

## Claims, citations, and reporting

*The failure mode is confident, well-formatted, and wrong.*

- **Do not cite a source you have not read the relevant passage of.** Summarizing a title or an abstract into a specific claim is how a paper ends up cited for something it does not say. Quote or point to the line.
- **Mark unverified claims as unverified** rather than smoothing them into the prose. A hedge the reader can see beats a confident sentence they have to catch.
- **Report failures with the output.** If tests fail, a job died, or a step was skipped, say so plainly and show what came back — do not narrate around it.
- **Distinguish "it ran" from "it worked."** An exit code of 0 is not a validated result; check that the output is the shape, size, and range you expected.
- **Numbers and units get checked before they get formatted.** Order-of-magnitude and unit slips survive every downstream step, because the plot still looks fine.

## Discovery, not validation

Any skill or open-ended exploration is for surfacing things the user didn't expect — anomalies, counter-evidence, overlooked candidates, alternative explanations. "Yes, your hypothesis holds" is a failure mode. If a prompt can only be answered *confirm* or *deny*, reframe it so it surfaces what's missing from the reasoning.

- **Report the disconfirming result first**, while it can still change the plan. Negative and null results are findings, not setbacks to be buried in a summary's last paragraph.
- **Say when the data cannot answer the question.** Underpowered, confounded, or wrong-assay is a legitimate answer, and a cheaper one than a plausible number.

## Cowork state

If the project has a shared tracker doc (e.g. `docs/cowork/Project_Tracker.md`), read it at session start and update it on the way out. The tracker is the durable handoff between agent sessions and human working time; conversation context is not.

- **Leave the next session a way in:** what is done, what is in flight, what is blocked and on whom. A tracker that only records completed work is a changelog, not a handoff.

---

**Scope of this file.** This file is deliberately domain- and infrastructure-agnostic. Cluster-specific rules (filesystem quotas, sbatch templates, module versions) live in the boilerplate for that cluster — see [`sapelo2-boilerplate/claude-code/`](https://github.com/ChenHsieh/sapelo2-boilerplate/tree/main/claude-code) for one worked example. Project-specific rules (data paths, tool versions, domain conventions) live in that project's own `CLAUDE.md`.
