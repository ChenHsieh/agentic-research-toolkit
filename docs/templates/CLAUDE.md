# CLAUDE.md (house rules template)

> This is a template. Replace everything in [brackets] with your project's details, delete the
> guidance in blockquotes, and keep the rules that fit your work. It contains no real data.
>
> Put this file at the top of your project folder. An assistant will read it at the start
> of a session and follow it. You can read and edit every line yourself; that is the point.

## What this project is

[One short paragraph: what the project is, who runs it, whether it is wet-lab records,
dry-lab analysis, or both. Name the folder this file lives in.]

Example: "Phenotyping records and analysis for [trait] in [organism / line set]. Mostly
bench records now; a curated analysis table is starting to grow. Run by [your name]."

## The rules that keep the assistant honest

1. **Quote before you claim.** Before stating any number, ID, date, or category (a count, a
   measurement, which group a sample is in), open the source file, find the exact row, and
   show it to me. Only then state the claim. Words like "looks like," "probably," and
   "should be" are red flags: either the file says it or it does not.
2. **Do not invent anything.** If a value is missing from the source, say it is missing. Never
   fill a gap with a plausible guess or a standard default.
3. **Anchor to stable IDs, not to labels.** Refer to samples, lines, and genes by their
   permanent ID (for example [SAMPLE_ID / gene_id / accession]), not by a nickname like
   "Line 12" or "the good one," which can drift. When in doubt, write the ID next to the label.
4. **Do not silently edit important files.** These are load-bearing: this `CLAUDE.md`, any
   `README`, and the canonical files listed below. Propose the change, explain why, and wait
   for my yes before editing them. You may write freely to scratch and draft files.
5. **Report [group A] and [group B] separately.** [Delete if not relevant. For hybrid or
   paired data, name the groups that must never be silently summed or averaged together.]
6. **Log decisions.** When we decide something worth remembering, write a short dated entry in
   `docs/log/YYYYMMDD_topic.md` (see the decision-log template). Use the real full file paths,
   not shortened ones.

## Canonical files (the real, trusted ones)

> List the files that everything else must agree with. If a number is not in one of these,
> the assistant should ask before reporting it. Delete this note once filled in.

| File | What it holds | Notes |
|---|---|---|
| `[samples_master_v3.csv]` | [the authoritative sample list] | canonical; do not edit without approval |
| `[data_master_v2.csv]` | [the authoritative measurements] | canonical |
| `docs/log/` | dated decision logs | append-only, one file per decision |

Anything not listed here is provisional. Old copies, drafts, and scratch versions are not
canonical even if they look finished.

## How to handle data files

- **Raw source data** (instrument output, original spreadsheets): read-only. Never edit or
  overwrite. If you need a working copy, copy it to a scratch folder and note where it came
  from.
- **Curated files** (the canonical list above): change them only by making a new dated version
  (for example `_v4` or `_20260314`), never by editing in place, and only with my approval.
- **Drafts and derived outputs** (figures, scratch tables): treat as rebuildable; date-stamp
  exploratory ones.

## How to report back to me

- Lead with the answer in one or two sentences, then the number that supports it, then any
  caveat. Do not narrate your process.
- Use a table when there are more than about three items.
- If a number changed from a previous value, flag it explicitly rather than letting it pass
  silently.
- If you are unsure or a file will not open, stop and say so with the exact file path. Do not
  substitute a similar file or an older version to keep going. A number from the wrong file is
  worse than no number.

## Session start

At the start of a session: read this file, then read `AGENT_BRIEF.md`, then read the newest
one or two files in `docs/log/`. Treat the canonical files above as the source of truth. If a
question is about a number that is not in a canonical file, ask before answering.

> Optional: if your project uses a "current state" summary that you overwrite as things
> change, name it here and tell the assistant to trust the newest decision log over it if the log is
> more recent. That staleness check keeps this file from quietly going out of date.
