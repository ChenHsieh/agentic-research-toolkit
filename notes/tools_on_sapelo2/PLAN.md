# PLAN: tests for logaxis.py (do not edit logaxis.py)

Step 1. Create test_logaxis.py: plain Python asserts, no pytest, runnable as
`python test_logaxis.py`, printing "ALL PASS" at the end.
Test fmt_decade: 0 -> "0", 1 -> "1", 10 -> "10", 1000 -> "1k", 1500 -> "1.5k",
1e6 -> "1M", 2e9 -> "2B", 0.1 -> "0.1", 0.001 -> "0.001", -1000 -> "-1k".
Test log10p: log10p(0) == 0, log10p(9) == 1 (within 1e-12), log10p(99, c=1) == 2,
log10p([0, 9]) returns an array equal to [0, 1].
Import with `from logaxis import fmt_decade, log10p`.
Test command: MPLBACKEND=Agg /home/ch29576/envs/figs/bin/python test_logaxis.py
