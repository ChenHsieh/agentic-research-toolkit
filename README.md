# Using an agent for research

**Site: https://chenhsieh.github.io/agentic-research-toolkit/**

How I use Claude Code for research on a university cluster, what failed, and what I changed. Written for friends and labmates who asked.

The short version: in my long sessions, the errors left behind were the ones that look like success. When I tested that on 15 small fresh tasks (90 runs, in `experiments/loud_quiet/`), the agent caught the quiet faults too; the one it missed was a choice nobody had written down. So: write the plan before the run, make every check fail once, and turn the rules that matter into code that something actually runs.

## On the site

- [Essay](https://chenhsieh.github.io/agentic-research-toolkit/): setup, tasks, failures with dates and numbers, long sessions, models, how to start.
- [Prompts & files](https://chenhsieh.github.io/agentic-research-toolkit/examples.html): a five-line rules file, a brief, a status file, and the prompts I reuse.

- [Tools](https://chenhsieh.github.io/agentic-research-toolkit/tools.html): seven research-agent tools set up on a cluster, one task each, every output checked. Notes and scripts in `notes/tools_on_sapelo2/`.
- [Reading](https://chenhsieh.github.io/agentic-research-toolkit/reading.html): papers, tools and guides, with links checked.
- [Walkthrough](https://chenhsieh.github.io/agentic-research-toolkit/session.html): 20 minutes with me on your own project.

## Install the skills

In Claude Code:

```
/plugin marketplace add ChenHsieh/agentic-research-toolkit
/plugin install result-checks@agentic-research-toolkit
```

That adds six skills: five procedures for testing a result (design confounds, a null for a derived statistic, result autopsy, a second method, accession-to-paper crosswalk) and the agent playbook. They cost about 1,100 tokens per session until one is used. The other skills in `skills/` are adapted from other people's work or unfinished, and are not in the plugin.

## In the repository

- `setup/AGENT_PLAYBOOK.md`: rules my agents read at the start of a task and again before reporting, with the incident in brackets where there was one.
- `setup/CLAUDE.md`: a longer general rules file. For one project, the five-line version on the Prompts & files page is enough.
- `skills/`: procedures for testing a result (design confounds, nulls for derived statistics, result autopsy, a second method). Attribution in `skills/README.md`.
- `docs/`: the site, plain HTML. `index.html` is edited by hand; `examples.html`, `reading.html` and `session.html` are written by `tools/build_pages.py` (edit the script, then run `python3 tools/build_pages.py` from the repository root).

Code MIT. Text and figures CC BY 4.0.
