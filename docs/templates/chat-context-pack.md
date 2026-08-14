# Chat context pack template

> For people working in a plain chat window with no file access. Paste this at the start of a
> conversation to give the assistant the project context it cannot see. Keep it short: you re-paste it
> every conversation, and long context is easy to get wrong. Fill in the brackets and delete
> this blockquote.

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

## Tips

- Keep it under about a dozen lines. This is a reminder, not the whole project.
- Update the "current state" line as you go, and save your filled-in version somewhere handy
  so you can paste it again next time.
- The assistant cannot open your files in a plain chat, so any number you want it to use has to be in
  what you paste. If it states a number you did not give it, that number is a guess.
