# Using an agent for research

**Site: https://chenhsieh.github.io/agentic-research-toolkit/**

How I use Claude Code for research on a university cluster, what failed, and what I changed. Written for friends and labmates who asked.


The one lesson: rules written in a file get skipped at the moment they apply. The important ones should be code that stops the work.


## On the site

- [Essay](https://chenhsieh.github.io/agentic-research-toolkit/): setup, tasks, failures with dates and numbers, long sessions, models, how to start.
- [Examples](https://chenhsieh.github.io/agentic-research-toolkit/examples.html): a rules file, a brief, a status file, prompts, figure rules.
- [Practice](https://chenhsieh.github.io/agentic-research-toolkit/practice.html): seven real cases. Is the result done, wrong, or not yet measurable?
- [Reading](https://chenhsieh.github.io/agentic-research-toolkit/reading.html): papers, tools and guides, with links checked.
- [Session](https://chenhsieh.github.io/agentic-research-toolkit/session.html): 20 minutes with me on your own project.

## In the repository

- `setup/CLAUDE.md`: the rules file I start projects from.
- `skills/`: procedures for testing a result (design confounds, nulls for derived statistics, result autopsy, a second method). Attribution in `skills/README.md`.
- `docs/`: the site. Plain HTML, no build step.
- `tools/build_pages.py`: writes Examples, Practice and Session.

Code MIT. Text and figures CC BY 4.0.
