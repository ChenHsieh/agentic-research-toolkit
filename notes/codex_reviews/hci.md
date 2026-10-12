Verdict: this is unusually concrete and likely to change some behaviour. Its main weakness is that it teaches “be skeptical” more reliably than it teaches when and how a student can verify an agent’s particular claim.

## Five changes with the highest payoff

1. **The check table is memorable but too detached from the reader’s work.**  
   Element: “Guess first: which of these checks will never say no?”  
   It teaches recognition after the fact. Add a compulsory transfer step below it:

   > Before you run your own task, write one result that would make you stop, and the command or file that would show it. Do this before you read the agent’s summary.

   Making an initial judgment before revealing AI advice is a useful cognitive-forcing pattern, not just a slogan.

2. **Several failure cards still ask the reader to trust the agent’s report.**  
   Element: “Ask the agent for the row count of every control.”  
   That preserves the weak interaction: agent says it checked, student believes it. Replace with:

   > Make the script save `n_control` in the results table. Open that table yourself. If it is 0, write BLOCKED and do not read the comparison.

   This shifts verification from conversational assurance to inspectable evidence.

3. **The “Before I trust this check” prompt lets one agent create both the test and the evidence for it.**  
   Element: “on an input built to have the error … [and] an input with a planted answer.”  
   That is better than no testing, but shared assumptions can make the planted case and test agree while both are wrong. Add:

   > For one important check, make the bad case by hand or from a second, simpler implementation. Write down what differs before the agent sees it.

   Keep the current prompt, but label its result “evidence this check catches this planted error,” not “trust earned.”

4. **The tools page risks a misleading heuristic: code/retrieval good, interpretation bad.**  
   Element: “The retrieval and the code were mostly right. The sentence that explained the result is where every error was.”  
   One selected task per tool, mostly chosen because it could be checked, cannot establish that split. Replace with:

   > In these seven small, checkable trials, the errors I found were often in the sentence after a correct-looking output. That is a reason to check both the table and the claim, not a ranking of what agents are good at.

   Add columns for “how I checked it,” “what I did not check,” and “one task is not a rate.”

5. **The walkthrough has a strong failure exercise, but shows the AI answer before forming an independent view.**  
   Element: “Ask the agent what each file … does, and find one thing in its answer that is wrong.”  
   Start with two minutes alone:

   > Before asking, write what you think the files do, one place you are unsure, and one output that would worry you. Then compare that with the agent’s answer and trace one claim to a file.

   End with a one-week follow-up: one real task, predicted failure, actual result. Twenty minutes can start a habit; it cannot demonstrate transfer.

## Claims I would qualify

- “A check you have never seen say no is a description, not a test.” Too absolute. A failed control is evidence that a check detects that failure, not proof that it detects the important failures. Say “an unexercised check has not yet earned evidence that it can detect its intended error.” Verification matters because explanations rarely help unless they let a person actually verify the answer. [Fok et al., 2024](https://onlinelibrary.wiley.com/doi/full/10.1002/aaai.12182)

- “Do not watch it.” Too categorical. Passive monitoring is a poor safety mechanism, but scheduled review and meaningful wake-up conditions can be appropriate. Say “Do not substitute watching the transcript for a planned check.”

- “A different model is more independent.” Not necessarily. Different models can share training data, prompts, tools, and the first model’s framing. Independence comes from a different source of evidence, method, or blinded reviewer, not a brand name.

- “The consistent finding: agents run code well and choose methods and interpret biology poorly.” The cited benchmarks do not support a universal ordering across tasks, users, tools, and models. Your local evidence supports a narrower claim: plausible outputs and citations still carried overclaims.

The HCI target is **appropriate reliance**, not maximum suspicion: accept correct advice and reject incorrect advice case by case. [Schemmer et al.](https://arxiv.org/abs/2204.06916) Explanations can increase acceptance regardless of correctness. [Bansal et al.](https://idl.uw.edu/papers/ai-explanations-team-performance) Initial commitments and other forcing functions can reduce overreliance, but cost effort and do not eliminate it. [Buçinca et al.](https://arxiv.org/abs/2102.09692)

## Missing

Students need a small risk rule: which tasks may be checked by rerunning code, which require domain judgment, and which need a labmate or advisor. They also need an interpretation checklist: claim, source row/passage, alternative explanation, and what result would change the claim. The site already has the evidence for this in its Biomni and PaperQA examples; bring it into the main essay.

## Keep

Do not soften the failure cards, the distinction between files and chat, the explicit limits on the tools trial, or the quiet design. The interactive table, planted failures, and walkthrough’s requirement to see a real check say no are the site’s best teaching devices.

## One-day experiment

Run eight short, realistic research tasks with 6–10 labmates. For each, provide an agent answer; half contain a seeded, checkable error. Randomize whether they see the answer first or must first write their own expectation and verification plan. Record acceptance of correct answers, rejection of wrong ones, evidence opened, time, and confidence. The central claim wins only if the revised workflow improves both accepting correct work and catching wrong work, not merely skepticism.