# Aider: tests for a real figure helper (2026-10-11)

Use case: hand a mechanical, testable step to a cheap model. Plan written by Claude (PLAN.md),
done by Aider + OpenRouter (deepseek-v4-pro), checked by running the test.

- Input: copy of ms1-dup/ms1-figures/ms1fig/logaxis.py (not edited).
- Aider wrote test_logaxis.py from PLAN.md in one call: 3.5k tokens sent, 2.1k received, $0.0016.
- Tests pass on the real module.
- Made the tests fail on purpose (4 planted bugs: "k"->"K", +1e-9 in log10p, zero check moved,
  boundary 1000 moved to >1000). All 4 caught.
- A quiet failure on the way: the first mutation run reused Python's cached bytecode (.pyc),
  because each mutated copy had the same size and the same mtime second as the last. The restore
  check then "failed" on unmodified code. Fix: PYTHONDONTWRITEBYTECODE=1 and delete __pycache__.
  Without the restore check this would have been invisible.
Command: MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /home/ch29576/envs/figs/bin/python test_logaxis.py
