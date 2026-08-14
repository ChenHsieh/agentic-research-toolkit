# AGENT_BRIEF (front-door template)

> This is a template. Replace everything in [brackets], delete the blockquote guidance, and
> keep it to one page. It contains no real data.
>
> This is the single entry point. Anyone, human or assistant, who is new to the project reads this
> file top to bottom first, then reads the two or three files it points at, then starts. The
> goal is to get oriented fast without exploring the whole folder blindly.

## The situation, in a few sentences

[Three to six plain sentences. What is this project, what stage is it at, what is the current
task, and what is the one thing a newcomer most needs to know. Write it the way you would
brief a new labmate on their first morning.]

Example: "This project tracks [trait] measurements for [line set]. Bench recording is ongoing;
we are now folding results into a curated master table. The current task is [X]. The thing
people get wrong first is [Y]."

## Read these next, in this order

1. `CLAUDE.md` in this folder. The house rules. Non-negotiable.
2. `[the file that holds current state, e.g. docs/log/ newest entry, or a STATE.md]`. Where
   the project stands right now.
3. `[the file that lists locked numbers or canonical values, if you have one]`. If your work
   contradicts a value here, assume you are wrong until you can prove otherwise, and if you do
   prove it, update this file and say so clearly.

Only read further into the folder once you know which part your task touches.

## Canonical sources (the real, trusted files)

| File | What it is | Rule |
|---|---|---|
| `[samples_master_v3.csv]` | [authoritative sample list] | canonical; quote rows before claiming |
| `[data_master_v2.csv]` | [authoritative measurements] | canonical |
| `[STATE.md or newest docs/log entry]` | where we left off | trust the newest one |

## Where "current state" lives

[Name the one place that always reflects the latest state of the project: a `STATE.md`, a
"current state" section in `CLAUDE.md`, or simply the newest file in `docs/log/`. Say how to
find the newest log: sort `docs/log/` by filename, not by date-modified, because cloud sync
scrambles modified times.]

## The four to six rules that cost the most time when broken

> These are the mistakes that have actually burned you (or that you can see coming). Keep the
> list short and specific. Examples below; replace with your own.

- **Do not invent numbers, IDs, dates, or units.** If it is missing, say so.
- **Refer to samples by their stable ID, not a nickname.** [SAMPLE_ID], not "the good line."
- **Report [group A] and [group B] separately.** Never silently combine them.
- **Use the canonical file for a number, not an old copy.** If unsure which file is canonical,
  ask.
- **[A project-specific rule that has bitten you, e.g. a naming quirk, a unit convention, a
  file that looks current but is not.]**

## Optional: if a shared folder is involved

[Delete this section if it does not apply. If part of your project is a folder that someone
else reads (a PI, a collaborator, a shared drive), state the rule plainly: that folder is
read-only for the assistant. Deliverables go to a staging folder first, you review them, and you copy
them over yourself. This keeps anything unreviewed out of the shared space.]

## How to report back

Lead with the answer in one or two sentences, then the supporting number, then the caveat.
Tables over paragraphs when there are more than three items. Do not narrate the process. If
asked for a count, give the count first and the method second.

## Your first message back to me

State which task you picked, which files you read, what you are about to do, and anything that
blocks you. Then start.
