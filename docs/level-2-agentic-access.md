# Level 2: Giving a tool file access

**Setup needed: some.** This level is about a different kind of tool, and, just as
importantly, about deciding when it is actually worth the trouble. For a single day's notes,
it usually is not. Read the rubric before you install anything.

## What "agentic" means, in plain language

The chat you used at Level 1 can only see what you paste into it. It has no eyes on your
computer.

An **agentic** tool is different: it can read and search your files, and it can run things
(open a spreadsheet, count rows, cross-reference two tables) instead of only chatting. You
point it at a folder, and it can look around inside that folder the way you would, but much
faster. Examples of these tools include Claude Code and Codex. The word "agent" just means
"it can take actions on your behalf," not only talk.

This is more powerful and, for exactly that reason, worth being more careful with. The safety
rule still holds and gets a small addition:

> **The assistant drafts and proposes; you approve.** A well-set-up agentic tool shows you the
> change it wants to make and waits for your yes before making it. Your raw data and your
> real notebook stay the source of truth. Nothing is overwritten without you looking at it.

If a tool ever edits your files silently, that is a setup problem, not a normal mode. Level 3
templates exist partly to enforce "propose, then wait."

## When it earns its keep, and when it does not

The honest answer is that most bench recording does **not** need an agentic tool. Here is the
rubric.

**Reach for an agentic tool when:**

- You have **large or structured data you would need to search or cross-reference**: a
  spreadsheet with thousands of rows, or many files scattered across a folder, where the
  question is "find every sample where X" or "check that this table agrees with that one."
- You are **doing the same lookup repeatedly** and want it done consistently across a whole
  dataset, not one row at a time.
- You are **folding many pieces together**: pulling results from twelve experiments into one
  curated summary, and you need the assistant to actually open all twelve.

**Stay with plain chat (Level 1) when:**

- It is **a single day's bench notes, one experiment, or drafting one paragraph.** Pasting the
  text into a chat is faster than any setup, and the setup buys you nothing here.
- The information **fits comfortably in what you can paste.** If you can copy it into the chat
  box, you probably do not need file access.
- You are **still deciding what you even want.** Explore in chat first. Add tooling once the
  task is repetitive and defined.

**A wet-lab-specific note.** Recording results at the bench, the act of writing down what you
just observed, rarely needs agentic access. There is nothing to search yet; there is just
today's observation, and Level 1 handles that beautifully. Agentic tools become useful
**later**, when those results get folded into a shared or curated analysis: a running master
table of every line you have phenotyped, a spreadsheet that has grown past what you can hold
in your head, a folder of many experiments that has to stay internally consistent. That is
the dry-lab, curation side of the work, and it is where file access starts paying for itself.

See the [rubric page](rubric.md) for a compact decision table you can glance at.

## What using it actually looks like

You do not write code. You talk to it in plain English, the same as Level 1, except now it
can look at your files. A session feels like:

- **You:** "Look at `samples_master.csv` and tell me which lines are missing a treatment
  label."
- **It:** reads the file, and answers with the specific rows, quoting them back to you.
- **You:** "Add a note to my log about the three that are missing."
- **It:** shows you the exact text it wants to add, and waits.
- **You:** read it, and say yes or fix it.

The two habits that keep this safe:

1. **Ask it to quote the file back to you.** "Show me the actual rows" beats "how many are
   there," because it forces the answer to come from your data, not from the assistant's guess. If it
   cannot show you the row, do not trust the number.
2. **Keep approval on.** You want a tool that proposes a change and waits, not one that
   edits and tells you afterward. The Level 3 [`CLAUDE.md` template](templates/CLAUDE.md)
   sets this up as a house rule.

## The extra failure mode at this level

Everything from Level 1 still applies: the assistant can misread and can invent. Two things get
sharper once it can touch files:

- **A wrong claim can now be about your real data**, not just a pasted note. "All 40 samples
  have a treatment label" is easy to say and wrong if it only actually opened 30 of them.
  Insisting it quote the rows is your defense.
- **A confident summary can hide a partial read.** If some files did not open (a common thing
  with cloud-synced folders, see [Level 3](level-3-starter-kit.md)), a tidy answer built from
  half the data is worse than no answer. Ask "did every file open?" when a number matters.

None of this means "do not use it." It means: use it where it earns its keep, keep approval
on, and make it show its work.

## Ready for more structure?

If you have decided an agentic tool is worth it for a project, Level 3 gives you the small
set of templates that make it reliable: house rules the assistant follows every session, a one-page
brief so a fresh session gets oriented fast, and a decision log so choices do not get lost.

---

Previous: **[Level 1: Chat only](level-1-chat-only.md)**  |  Next: **[Level 3: The fuller pattern](level-3-starter-kit.md)**
