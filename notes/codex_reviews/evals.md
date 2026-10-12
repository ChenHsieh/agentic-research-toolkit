The site’s central safety argument is strong. Its tool comparison is not yet evidence for it.

## Five important problems

1. **It calls a feasibility diary a comparison.**  
   Passage: “*gave each one task from my own work… One task per tool, on a cheap model, so it shows whether they are usable*.”

   Each row changes tool, task, setup burden, agent scaffold, and sometimes mode. One result cannot estimate either usability or tool quality. “Usable” includes installability, task success, cost, latency, and review burden.

   Replace with: “This is a small feasibility diary, not a ranking. Each tool got one task that fit it. The rows show what happened on my cluster with this model and these versions.”

2. **The conclusion outruns the adjudication.**  
   Element: “*The retrieval and the code were mostly right. The sentence that explained the result is where every error was.*”

   That is a valuable pattern, but the trial did not apply one prewritten rubric to all outputs. “Every sentence cited,” “61 of 61 checks pass,” and “sensible ranked plan” are not comparable correctness measures. Some checks are tool-written, and several outputs have no independent gold answer.

   Add a small methods box: “Before each run I wrote what counts as setup success, artifact success, and a supported biological claim. A separate script or source check, written before the run and not shown to the agent, judged each.”

3. **The Jev Router figure is an anecdote presented like a cost result.**  
   Passage: “*On two prompts it was 23 times cheaper… and about a third more expensive.*”

   Two prompts, one draw each, and two different selected models say almost nothing about expected cost, quality, or routing reliability. “Both answers correct” needs a stated rubric, not author judgment.

   Replace caption with: “Two examples, not a router evaluation. They show that routing can save money on an easy request and cost more on another. I have not measured its average cost, answer quality, or stability.”

4. **The map has unmeasured axes and treats predictions as observations.**  
   Element: “*Who drives, and can you check it*,” including “Would produce a notebook you can rerun” for CellVoyager, which did not run.

   “Drives” mixes permission, planning, and execution. “Checkability” mixes reproducibility, time to audit, and whether a domain expert can judge the claim. The placements are useful teaching shorthand, not evidence.

   Add: “This is a sketch, not a measurement. ‘Checkable’ means the particular output has a prewritten, affordable check. A rerunnable notebook can still be hard to validate.”

5. **The benchmark summary compresses unlike findings.**  
   Passage: “*The consistent finding: agents run code well and choose methods and interpret biology poorly.*” Also: “*GPT-4o and Claude 3.5 Sonnet: 17% correct.*”

   BixBench measured integrated open-ended bioinformatics trajectories, not a clean code-versus-method decomposition. Its reported scores were Claude 3.5 Sonnet 17% and GPT-4o 9%, not 17% for both. It also used ten trajectories per analysis, which is the right instinct missing from the local trial. [BixBench PDF](https://storage.googleapis.com/bixbench-results/BixBench.pdf)

   Replace with: “On particular 2024–25 agent setups, end-to-end bioinformatics remained hard. BixBench reported 17% for Claude 3.5 Sonnet and 9% for GPT-4o on its open-answer setting. That does not tell us which step failed in my task.”

## Claims I would qualify

- “METR saw the same… so a check the working session can edit is a check it can make pass.” METR observed reward hacking in specially constructed, automatically scored software/R&D tasks, often when the scorer was visible. It supports keeping important evaluation outside the agent’s write access; it does not show every editable research check will be gamed. [METR’s report](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

- The GPT-5 “2 hours 17 minutes” point is correctly described as not wall-clock autonomy, but should not support biological overnight-run reliability. It is a fitted 50% success point on mostly self-contained software, ML, and cybersecurity tasks, with low-context human baselines. [METR methodology](https://metr.org/time-horizons/)

- “A different model is more independent” is not established. Different providers may share training data, benchmarks, tools, and plausible mistakes. Independence should mean measured disagreement on seeded errors, not a model-brand change.

ScienceAgentBench is the better methodological model here: task-level evaluation, expert validation, multiple attempts, execution results, cost, and rubrics rather than an end-to-end impression. [ScienceAgentBench](https://arxiv.org/abs/2410.05080)

## Missing

A grad student needs a compact evaluation protocol: frozen versions and prompts; a task population; predeclared pass criteria; hidden or separately authored checks; repeated runs; a no-agent or plain-model baseline; cost, latency, and human review time; error severity; and raw traces. Report counts and uncertainty, not ranks.

## Keep

Do not soften the concrete failures: Codex’s wrong claimed output, PaperQA2’s citation overreach, Biomni’s annotation-bias inference, and the retained CellVoyager failure. The planted-bug Aider test and the rule that a check must fail once are the site’s best evidence and best teaching. The explicit “Two prompts is not a test” is excellent.

## One-day measurement

Make twelve tiny, frozen plant-genomics task cards: six loud faults (bad import, wrong column, crash) and six quiet ones (empty control, shuffled labels, wrong grouping unit, self-comparison, hidden threshold, swapped metadata). Run one fixed agent setup twice per card with a time and dollar cap. Give it a hidden, separately written verifier it cannot edit. Record whether it fixes the fault, falsely declares success, and produces a valid check.

Report the two fractions with raw logs: loud-fault recovery versus quiet-fault detection. If the gap is large, the thesis gains real support. If quiet faults are caught too, the site learns exactly where its warning is too broad.