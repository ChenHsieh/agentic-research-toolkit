# Loud versus quiet faults: a small test of the essay's claim

Claim under test: a coding agent recovers from faults that crash far more often than it detects
faults that finish cleanly with a wrong answer.

Result: not supported on these cards. 90 runs, 89 right.

| folders | plan in the folder | plan plus six rules | plan deleted |
|---|---|---|---|
| 6 loud faults x 2 runs | 12/12 | 12/12 | 12/12 |
| 6 quiet faults x 2 runs | 12/12 | 12/12 | 11/12 |
| 3 clean x 2 runs | 6/6 | 6/6 | 6/6 |

The one miss: with the plan deleted, the card whose filter differed from the plan had no record of
the intended filter; one run kept the wrong filter and reported status "ok".

Setup
- Cards: `make_cards.py` builds 15 folders of simulated counts (240 genes, 6 control and 6 treated
  plants) with `analysis.py`, `data/README.txt` and `BRIEF.md`. `validate_cards.py` confirms each
  card behaves as designed before any agent sees it (loud cards crash, quiet cards exit 0 with a
  wrong answer, clean cards are right, and the scorer rejects a wrong answer).
- Agent: Claude Code headless, model Sonnet 5.5, run from a temp folder with
  `--setting-sources project` so none of my rules, memory or skills were loaded (`run_one.sh`).
- Conditions: `plain` (brief only), `rules` (brief plus `RULES.txt`), `noplan` (the analysis plan
  removed from the README). Two runs per card per condition.
- Scoring: `score.py` against `truth/`, which the agent is never told about. Right = number of
  significant genes within max(2, 10%), top gene and direction exact. `results.tsv` has every run
  with the agent's own notes. Total cost $7.78.

What it can and cannot support
- It supports: on small fresh tasks, this agent audited the analysis it was asked to run and caught
  faults that contradicted the data, the code or a written plan.
- It does not test: long sessions, code the agent wrote itself, tasks with no written plan and
  nobody asking for a result to be trusted, other models, real data.
- Design weaknesses (from `notes/codex_reviews/experiment_design.md`, written by Codex without seeing the
  results): the quiet faults are signposted by the README; loud and quiet are not matched for
  difficulty; the answer files were outside the run folder but not physically walled off (no run
  record mentions them); the score checks the final answer, not whether the notes name the fault
  (I read the notes for the quiet cards by hand: each names the planted fault).

Rerun: `python make_cards.py && python validate_cards.py`, then `./run_one.sh card_01 plain 1`,
then `python summarize.py`.
