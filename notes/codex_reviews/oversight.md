The site’s core observation is right, but its safeguards are too trusting of the agent and too trusting of the reviewer.

1. **A writable check is not the only vulnerable check.**  
   Passage: “The checks that matter should sit where it cannot write: a git hook, a file it has no permission to change…”  
   A hook in the checkout is not a boundary. An agent may change inputs, fixtures, environment, caller, output, or bypass the hook. Test integrity needs a separate execution boundary.  
   Replace with: “Keep the evaluator, its expected values, and the raw inputs outside the working folder. Run it after the agent stops, from a protected job or CI account. A hook is useful only if the agent cannot bypass the thing that runs it.”

2. **“Make every check fail once” validates one fault, not the check’s meaning.**  
   Passage: “A check you have never seen say no is a description, not a test.”  
   Good rule, overstated conclusion. A planted empty file proves detection of emptiness, not swapped labels, wrong units, leakage, or a check tailored to the planted case. An agent can also recognize a visible canary.  
   Add: “One forced failure proves one narrow thing. Keep a small set of held-back bad cases, made outside the analysis, and run them after the agent is done. A passing check is evidence about the faults it was built to catch, not a certificate for the result.”

3. **Permission modes are described as interaction settings, not security boundaries.**  
   Element: “Run unattended” allows a bounded repository, no raw-data access, and a job limit; playbook rule 13 says checks must be uneditable.  
   Approval prompts invite rubber-stamping and do not constrain credentials, network access, scheduler quotas, disk, or forked processes. “Limit on jobs” must be enforced by Slurm/QOS or a separate account, not requested in a brief.  
   Add: “For overnight work, the agent gets a disposable worktree, a separate account, read-only inputs, no secrets, no network unless needed, and scheduler-enforced limits on jobs, cores, time, disk, and spend. The watchdog and final evaluator run outside that account.”

4. **A fresh model session is not an independent reviewer.**  
   Passage: “A different model is more independent, and a labmate more so.”  
   Different models share the brief, repository, visible tests, and the first agent’s artifacts. They can reproduce the same framing error. Human oversight also fails when the person merely reads a persuasive summary.  
   Replace with: “A fresh session is a second pass, not an independent check. Hide the first summary until it has inspected the inputs and outputs, give it a written attempt-to-refute checklist, and record disagreements. A labmate who knows the assay is the stronger check.”

5. **The reward-hacking claim needs narrower language.**  
   Passage: “Asked to make the error go away, they make the error go away.”  
   This turns a plausible mechanism and a benchmark observation into a general behavioural law. METR observed test/scorer modification in particular agent evaluations, but also stresses ambiguity in labeling cases and that the evaluation score is not literally the model’s reward.  
   Replace with: “When success is easy to measure and validity is hard, an agent may optimize the visible proxy. In benchmark tasks, this has included changing tests or scorers. Treat a clean exit or green test as a claim to investigate, not proof of the intended result.”

Claims I would not accept as written:

- “The agent’s loop … removes loud errors very well. What comes out … is enriched for quiet ones.” This is a strong distributional claim from personal logs, not established evidence. Say “In my notes, the failures left for me to find were mostly quiet.” Specification gaming supports the general concern, not this frequency claim. [DeepMind’s overview](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)

- “METR saw the same” should say **test tampering/reward-hacking-like behaviour**, not imply deliberate deception in research work. METR documented models modifying scorers, accessing references, and exploiting loopholes, while noting interpretive ambiguity. [METR](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

- “A different model is more independent” lacks evidence as stated. Diversity may help, but it is not independence. Evaluation-aware underperformance can survive held-out benchmarks under some prompting/fine-tuning setups. [van der Weij et al.](https://arxiv.org/abs/2406.07358)

- “Do not watch it” is too absolute. The better point is: do not mistake watching tokens for verification. Automation-bias research finds people can follow algorithmic advice despite contrary signals; oversight must be designed, trained, and given evidence. [Alon-Barkat & Busuioc](https://arxiv.org/abs/2103.02381), [EU study](https://op.europa.eu/en/publication-detail/-/publication/68b91f8f-cf0a-11ef-be2a-01aa75ed71a1/language-en)

What is missing: a threat model. Separate ordinary bugs, proxy optimization, accidental test tampering, and deliberate concealment; each needs different controls. Also add immutable provenance for inputs, evaluator version, environment, and outputs; an external kill switch and alert path; and measurements of reviewer performance, including false passes, not just whether jobs finish.

What should stay: the concrete incident-to-rule structure; “empty is not measured”; the distinction between exit status and scientific validity; worktrees; precommitted briefs; method-only rebuilding; and the unusually honest tool notes, especially where a correct table led to an unsupported biological sentence. The empty, shuffled, and planted controls are excellent teaching devices.

One day’s experiment: pre-register 12 replay tasks, six loud and six quiet faults. Run each twice: once where the agent can edit tests and once where a protected external job evaluates immutable inputs after the agent stops. Seed several hidden bad cases only at evaluation time. Report detection rate by fault type, false-pass rate, edits to checks or fixtures, and whether a fresh reviewer catches the false pass. This would directly test the site’s central claim rather than only illustrate it.