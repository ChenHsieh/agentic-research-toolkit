1. Design flaws

- “Quiet” often means “no exception,” not genuinely hard to notice. `empty_control` visibly changes controls to `ctrl`; `wrong_unit` explicitly adds `plant` and says three libraries per plant; `stale_cache` creates a conspicuous `cache/` branch and deliberately old timestamp; `other_filter`, `by_position`, and `flipped_sign` directly contradict README steps. The supplied rules almost name these faults one-for-one.
- Loud faults are mostly trivial local repairs (misspelled import/path, syntax, column name), whereas quiet faults require semantic auditing or experimental-design knowledge. Thus fault type is confounded with repair difficulty, added artifacts, library count (`wrong_unit` has 36 libraries), and seed-specific signal strength.
- The agent has unrestricted Bash in a temporary copy, while `truth/`, `score.py`, and the experiment source remain elsewhere in the accessible workspace; `run_one.sh` does not isolate them.
- `score.py` measures final fields, not recovery or detection. A numerically correct answer with `status: "problem"` is still `"right"`; a `"flagged"` result need not identify the planted fault; `"none"` combines timeout, malformed JSON, and no answer. It also permits ±2/10% count error but requires an exact top gene, and never checks the claimed fix, notes, or final code.
- One fixed Sonnet configuration, two runs per card, six unique fault instances per class, and only three clean cards provide weak independent replication and no estimate of false alarms under comparable clean difficulty.

2. What it supports

A result could support a narrow descriptive claim: this particular agent/configuration more often produced score-correct outputs after these six crash-inducing cards than it produced the predeclared quiet-fault outcome on these six highly signposted semantic cards. It cannot establish a general property of coding agents, real silent-analysis bugs, or a causal advantage of “loudness” independent of task difficulty; nor can it cleanly distinguish detection, repair, lucky answers, and refusal.

3. Three valuable cheap fixes

1. Isolate each run so truth, generator, scorer, and sibling experiment files are physically inaccessible; log commands to audit leakage.
2. Build matched loud/quiet variants from the same underlying task/seed, remove literal README/code giveaways, and pretest detectability with blinded reviewers; add more seeds and randomized condition/order.
3. Pre-register separate metrics: detected (specific evidence in notes), repaired (final code/output passes), correct answer, false alarm, timeout, and malformed answer. Score these separately and inspect code diffs.

4. Honest two-sentence report

“On this small, synthetic suite, one Sonnet-based coding-agent setup more often reached a correct scored answer after deliberately crashing scripts than it flagged or repaired deliberately silent deviations from an analysis plan. Because the silent cases were semantic, visibly signposted, and not difficulty-matched to the crash cases, this is preliminary evidence about these cards—not evidence that agents generally cannot detect quiet faults.”