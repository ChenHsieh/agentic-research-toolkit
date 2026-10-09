# Using an agent for research

**Site: https://chenhsieh.github.io/agentic-research-toolkit/**

How I use Claude Code for research on a university cluster, what failed, and what I changed. Written for friends and labmates who asked.

The short version: an agent fixes the errors that crash and leaves the ones that look like success. Before trusting a check, make it fail once. Rules that matter become code that something actually runs.

## On the site

- [Essay](https://chenhsieh.github.io/agentic-research-toolkit/): setup, tasks, failures with dates and numbers, long sessions, models, how to start.
- [Prompts & files](https://chenhsieh.github.io/agentic-research-toolkit/examples.html): a five-line rules file, a brief, a status file, and the prompts I reuse.

- [Reading](https://chenhsieh.github.io/agentic-research-toolkit/reading.html): papers, tools and guides, with links checked.
- [Walkthrough](https://chenhsieh.github.io/agentic-research-toolkit/session.html): 20 minutes with me on your own project.

## In the repository

- `setup/AGENT_PLAYBOOK.md`: rules my agents read at the start of a task and again before reporting, with the incident in brackets where there was one.
- `setup/CLAUDE.md`: a longer general rules file. For one project, the five-line version on the Prompts & files page is enough.
- `skills/`: procedures for testing a result (design confounds, nulls for derived statistics, result autopsy, a second method). Attribution in `skills/README.md`.
- `docs/`: the site, plain HTML. `index.html` is edited by hand; `examples.html`, `reading.html` and `session.html` are written by `tools/build_pages.py` (edit the script, then run `python3 tools/build_pages.py` from the repository root).

Code MIT. Text and figures CC BY 4.0.
