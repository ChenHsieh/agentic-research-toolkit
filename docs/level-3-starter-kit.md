# Level 3: The fuller pattern (starter kit)

**Setup needed: more, but only once per project.** This level is for when a project has grown
big enough that you want an assistant to stay consistent across many sessions: same rules,
same canonical files, same record of decisions. Everything here is copy-pasteable and
genericized. Fill in the bracketed blanks with your own project's details.

You do **not** need any of this to get value from these tools. Level 1 stands on its own. Come here
when "keep this project's documentation coherent over months" becomes the actual problem.

## The idea

Left to itself, an assistant starts every conversation from nothing. It does not remember
your project, which spreadsheet is the real one, or the decision you made last week. So it
guesses, and guesses drift.

The fix is a few small documents that live in your project folder and give the assistant its memory
back, in a controlled way:

- **House rules** it should follow every session.
- **A one-page brief** that is the single front door to the project.
- **A dated log** of decisions, so "why did we do it this way" has an answer.

These are just text files. You can read and edit every one of them yourself. That is the
point: the assistant's memory is written down where you can see it and correct it.

## The four templates

Each links to a ready-to-copy file. Open it, copy the contents, and fill in the brackets.

### 1. `CLAUDE.md` — house rules

The standing rules an assistant should follow every time it works in this project: which
files are canonical (the real, trusted ones), what it must never edit without asking, how to
report numbers, and where to write things down. Named `CLAUDE.md` by convention for one
common tool, but the content is useful to any assistant. Put it at the top of your project
folder.

**[Open the `CLAUDE.md` template](templates/CLAUDE.md)**

The single most valuable rule in it: **quote before you claim.** Before the assistant states any
number or fact, it has to open the source file and show you the actual row it came from. This
one habit prevents most confident-but-wrong answers.

For a real, lived-in version of this file (denser, and tuned for an active research project),
see the toolkit's own
[`setup/CLAUDE.md`](https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/setup/CLAUDE.md).
The template here is the stripped-down beginner version of that.

### 2. `AGENT_BRIEF.md` — the one-page front door

A single entry point a fresh agentic session reads before doing anything: the situation in a few
sentences, a table of which files are canonical, where the "current state" of the project
lives, and the four to six rules that cost the most time when broken. If someone (human or assistant)
can only read one file, this is it.

**[Open the `AGENT_BRIEF.md` template](templates/AGENT_BRIEF.md)**

### 3. `docs/log/YYYYMMDD_topic.md` — decision log

One short file per meaningful decision or work session, named by date so it sorts correctly.
It records what you did, what you decided, and what to double-check later. Months from now,
this is how you (or a collaborator, or the assistant) reconstruct why the analysis looks the way it
does. The filename pattern matters: `20260314_drought_scoring_rubric.md`, not `notes.md`.

**[Open the decision-log template](templates/decision-log-template.md)**

A decision log outlives any one person's time on the project. When whoever wrote an entry is
about to leave the lab, have them note **who inherits any open question** in that entry, not
just what they concluded. A log that records only conclusions leaves the next person with the
answer but not the thread.

### 4. Chat context pack — for people with chat only

If you do not have an agentic tool (Level 2) and are working purely in a chat window, you
cannot point the assistant at these files. Instead you paste a small summary at the start of each
conversation. Keep it deliberately short, because you have to re-paste it every time and long
context is easy to get wrong.

**[Open the chat context pack template](templates/chat-context-pack.md)**

Because you will use this one constantly, here it is inline as well:

```
Project context (read before answering):
- Project: [one line: what this project is]
- I am: [your role, e.g. wet-lab, recording phenotype data]
- Canonical files (the real, trusted ones): [name them, e.g. samples_master_v3.csv]
- Current state / where we left off: [one or two sentences]
- Rules that matter here:
  1. Do not invent numbers, IDs, dates, or units. If something is missing, say so.
  2. Report [group A] and [group B] separately; do not combine them.
  3. [any other rule that has bitten you before]
When you are unsure, ask instead of guessing.
```

## The cloud-sync trap (OneDrive, Dropbox, Google Drive)

One specific gotcha bites almost everyone who keeps their project in a synced folder, so it
gets its own section.

**Do not find your newest log by sorting the folder by "date modified."** Cloud sync tools
(OneDrive, Dropbox, Google Drive) touch files when they sync, download, or re-check them. So a
file you have not opened in a month can show a "modified" time of this morning, purely because
the sync client looked at it. Sort by modified time and the newest-looking file may be an old
one the sync tool just happened to poke.

**Instead, put the date in the filename and sort by name.** That is the whole reason the
decision-log template uses `YYYYMMDD_topic.md`: `20260314_...` always sorts after
`20260228_...`, no matter what the sync client did to the timestamps. The date is baked into
the name, where nothing can quietly change it.

A related tip for large synced folders: files can show up as "placeholders" that are not
actually downloaded yet. They usually download fine the moment something opens them, it just
takes a few seconds. If a file genuinely will not open, do not let the assistant substitute a similar
file or an older version to keep going. A number built from the wrong file is worse than no
number. Better to stop and sort out the missing file first.

## Putting it together

A typical Level 3 project folder ends up looking like:

```
my_project/
  CLAUDE.md                       <- house rules
  AGENT_BRIEF.md                  <- one-page front door
  samples_master_v3.csv           <- a canonical file
  data_master_v2.csv              <- a canonical file
  docs/
    log/
      20260228_intake_batch1.md   <- decision logs, sorted by name
      20260314_scoring_rubric.md
```

You do not have to build all of this at once. Start with `AGENT_BRIEF.md` (it is the highest
value for the least work), add a `CLAUDE.md` when you notice the assistant repeating a mistake, and
write a log entry whenever you make a decision you would be annoyed to re-derive later.

Once this feels comfortable, the [Resources](resources.md) page points to libraries of
ready-made **skills** (reusable procedures for whole research tasks) and to the fuller skills
that ship with this toolkit. That is the natural next step up from templates.

## A word on trust

None of these templates make the assistant trustworthy on their own. They make it **auditable**:
every claim traces to a file, every decision has a dated record, and nothing canonical changes
without you approving the change. That is the realistic goal. Not an assistant you never have
to check, but one whose work you can always check quickly.

---

Previous: **[Level 2: Giving a tool file access](level-2-agentic-access.md)**  |  Next: **[Rubric](rubric.md)**
