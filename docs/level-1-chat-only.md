# Level 1: Chat only

**Setup needed: none.** A free chat account (Claude or ChatGPT) and copy-paste. This is the
primary on-ramp, and for a lot of people it is the only level they will ever need. Nothing
here is "agentic" yet: a plain chat assistant cannot touch your files, which is exactly why
it is the safe place to start.

The goal here is small and concrete: take the shorthand you scribble at the bench and turn
it into a clean, consistent notebook entry, without the assistant ever touching a single file
of yours.

## The workflow in one picture

1. You write a bench note the way you always do: fast, abbreviated, for yourself.
2. You paste it into a chat with a short instruction (template below).
3. The assistant gives you back a cleaned-up entry, plus a list of anything it thinks is missing.
4. **You read it against what you actually did**, fix anything wrong, and paste the final
   version into your real notebook.

Step 4 is not optional. It is the point. The assistant drafts; you are the record of truth.

## What to ask it to do

Three jobs, and it can do all three at once:

- **Clean up shorthand into full sentences.** "6 pots ln12, withheld water d0" becomes
  "Six pots of Line 12 were set up. Water was withheld starting on day 0."
- **Flag missing fields.** Date, line or genotype ID, treatment, controls, sample size,
  measurement units, instrument settings. The assistant will tell you what a reader (or future you)
  would need but cannot find in your note.
- **Reformat into a consistent template**, so every entry in your notebook has the same
  shape and is searchable later.

## A worked example

Here is a made-up bench note in the kind of shorthand people actually use:

```
3/14 drought assay setup. 6 pots line12 + 6 WT control. withheld water d0.
scored leaf wilt 0-5 at d3. line12 ~2, WT ~4. forgot pot volume. RH felt low today
```

Pasted into a chat with the prompt template below, you get back something like this.

**Cleaned entry:**

> **Date:** 2026-03-14
> **Experiment:** Drought assay, setup and day-3 scoring
> **Plant material:** Line 12 (n = 6 pots) and wild-type control (n = 6 pots)
> **Treatment:** Water withheld starting day 0
> **Measurement:** Leaf wilt scored on a 0 to 5 scale at day 3
> **Result:** Line 12 mean wilt score approximately 2; wild-type approximately 4
> **Notes:** Relative humidity noted as subjectively low; not measured

**What the assistant flagged as missing or unclear:**

> - **Pot volume / soil amount** is noted as forgotten. Record it if you can still recover it,
>   since it affects how fast pots dry.
> - **"Approximately 2" and "approximately 4"** are averages by eye. Were these means of the
>   six pots, or a general impression? Consider recording the six individual scores.
> - **Relative humidity** is described as "felt low." If you have a reading, add the number
>   and units (percent). If not, mark it as not measured.
> - **Scoring rubric:** what does 0 mean and what does 5 mean? A one-line key makes the score
>   reproducible for someone else.
> - **Time of day** of scoring is not recorded, which can matter for wilt.

Notice what happened: the assistant did not invent the pot volume. It flagged the gap and left it
to you. That is the behavior you want, and the prompt below is written to encourage it.

## The copy-pasteable prompt template

Copy this whole block. Paste it into the chat, then paste your bench note where it says so.

```
You are helping me turn a rough bench note into a clean lab-notebook entry.

Do three things:
1. Rewrite my shorthand into clear, full sentences, using a consistent structured format
   with these fields: Date, Experiment, Plant material / sample, Treatment, Measurement,
   Result, Notes. Leave a field blank and mark it "[not recorded]" if my note does not
   contain it.
2. List separately, under a heading "Missing or unclear," any field a reader would need but
   cannot find, and any place where my note is ambiguous.
3. Do not invent, guess, or fill in any value I did not write. If a number, unit, date, or
   ID is missing, say it is missing. Do not assume standard values.

Keep my original meaning. Do not add interpretation or conclusions I did not state.

Here is my bench note:
---
[PASTE YOUR NOTE HERE]
---
```

You can keep this template in a sticky note, a text file, or the top of your notebook. The
part that does the heavy lifting is point 3: it tells the assistant to leave gaps as gaps instead
of papering over them.

## The failure mode, stated plainly

The assistant is a fast, tireless copy editor with one dangerous habit: when something is missing
or unclear, it will sometimes fill the gap with a plausible-sounding detail that is simply
not true. It can misread "d0" as a date, swap two numbers, or turn "felt low" into a
specific humidity reading. It does this confidently, in the same clean prose as everything
it got right, so a wrong detail does not look wrong.

This is why the human stays in the loop:

- **Read every field of the draft against your actual observation** before it goes into the
  notebook. Do not skim.
- **Treat any number, unit, ID, or date as suspect** until you have confirmed the assistant copied
  it from your note rather than inventing it.
- **The assistant drafts. You are the record of truth.** If the draft and your memory disagree,
  your memory (and your raw data) win, every time.

Used this way, the worst case is that you catch a bad draft and rewrite one line. The assistant
never had the power to change your notebook on its own, because at Level 1 it cannot touch
your files at all.

## When Level 1 is all you need

If your job is "make today's messy notes readable and consistent," you are done. You do not
need any tool, any install, or any of the later levels. Most day-to-day bench recording
lives happily right here.

Move on to Level 2 only when you find yourself pasting the same background into the chat
over and over, or wishing the assistant could look across many files or a big spreadsheet instead
of the one note in front of you.

---

Previous: **[Home](index.md)**  |  Next: **[Level 2: Giving a tool file access](level-2-agentic-access.md)**
