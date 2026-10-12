## Five important problems

1. **“one task per tool, on a cheap model, so it shows whether they are usable”**

   This is an installation diary, not a usable comparison. Tool, model, task, corpus, and adapter all change together. The table invites ranking anyway.

   Replace with: “This is a record of seven setups on one cluster. A failure can belong to the tool, the model, the gateway, or my task. It does not rank the tools.”

2. **PaperQA2: “agent mode crashed; the plain mode works.”**

   The plain `Docs.add`/`query` path is supported, but it bypasses the agent workflow that searches, gathers evidence, and traverses citations. Your result is a fair test of local cited RAG over a hand-built corpus, not of PaperQA2 as reported in its paper. A fair trial would pin the release, use its agent path and normal dense retrieval, then compare citation entailment and recall against the same fixed paper set. [PaperQA2 documentation](https://github.com/shanmarken/paper-qa2)

   Replace with: “I tested PaperQA2’s manual local-corpus path. Its agent path did not start in this environment, so this is not a test of its literature-search workflow.”

3. **Biomni: “No 11 GB data lake” and a UniProt lookup written from scratch.**

   Skipping the data lake is an advertised option for limited tests, so this is not misuse. But it mostly tests whether a model can write UniProt REST code, not Biomni’s distinctive claim: retrieval and execution across its curated biomedical action space. [Biomni’s README](https://github.com/danhively/biomni) explicitly frames the data lake as optional for specific tools.

   Replace with: “This tested Biomni as a code-writing database assistant without its data lake. It did not test its curated analysis tools. A fairer next task is one of those tools on a public genomics dataset, with the same task also given to a bare coding agent.”

4. **Virtual Lab: “a sensible ranked plan in six minutes, close to what my chapter actually did.”**

   This is a useful meeting simulation, but it is only the deliberation part of the published Virtual Lab. The reported nanobody result included human feedback, a computational design pipeline, and wet-lab validation, not a one-off four-role discussion. [The paper](https://doi.org/10.1038/s41586-025-09442-9) supports the 92 designs and two improved binders, but not treating a meeting transcript as an equivalent trial.

   Replace with: “I tested the meeting part of Virtual Lab. It was useful for making a checklist. It did not test the design-and-validation workflow in the paper.”

5. **CellVoyager: “Did not run” beside tools that produced results.**

   This is a gateway compatibility failure, not evidence about CellVoyager’s science. Its documented workflow expects an `.h5ad` file, a paper/background summary, API keys, and recommends interactive pauses and notebook editing. [CellVoyager’s README](https://github.com/zou-group/CellVoyager) A fair trial would use its COVID example or a CellBench case, supplied background, supported keys, and a predeclared biological check.

   Replace with: “I could not test CellVoyager through my one-key setup. This is a setup result, not a verdict on its analyses.”

## Claims I would qualify

- **“61 of 61 checks pass” for Paper2Agent** does not establish that answers about new data are right. Its tests are meant to reproduce tutorial/reference outputs, then exclude repeatedly failing tools. That is valuable, but it is regression testing, not external scientific validation. [Paper2Agent](https://github.com/jmiao24/Paper2Agent)

- **“abSENSE-style tests … are the standard answer”** is too strong. abSENSE is a good null model for homology-detection failure, but requires detectable homologs in at least three species and its own assumptions. Gene-age inference also needs assembly and annotation checks, synteny, orthology, loss, and repeat-aware searches. [abSENSE](https://github.com/PrincetonUniversity/abSENSE), [phylostratigraphy caveats](https://academic.oup.com/bioinformatics/article/35/19/3617/5380767)

- **“AI co-scientist … not public”** is stale or imprecise. Access is limited, but Google now has an interest form for its Hypothesis Generation interface. Say “not generally available” instead. [Google help](https://support.google.com/hypothesis-generation/answer/17106281)

- **Kosmos: “79.4% … accurate.”** Keep the number, but name it as a report-statement audit, not discovery accuracy or independent replication. The paper itself reports seven cross-domain discoveries and that aggregate statement figure. [Kosmos](https://arxiv.org/abs/2511.02824)

- **AI Scientist: “42% … failed on coding errors.”** Accurate for the independent evaluation of the original ML-only release, but it should not become a general rate for “AI scientist” systems. [Independent evaluation](https://arxiv.org/abs/2502.14297), [original scope](https://arxiv.org/abs/2408.06292)

## Missing

A plant-genomics reader needs a short page on what counts as evidence for a young protein-coding gene: gene model integrity, assembly and haplotype context, repeat/TE origin, expression, translation, homology and microsynteny, and population-genetic evidence. None is universally required or sufficient. Thresholds need calibration on positive and negative loci, not stock cutoffs. Also add a warning that more GO terms are compatible with annotation and publication bias; they are not evidence of functional diversification.

## Keep

Do not touch the central distinction between loud and quiet errors, the insistence that empty controls are blocked, or the planted positive and negative checks. The concrete incidents, modest scope statements, status-file practice, and “fresh review” are unusually good. The PaperQA2, Biomni, and Virtual Lab notes do the most important thing correctly: separate correct retrieval from unsupported interpretation. Robin is also described fairly as lab-in-the-loop rather than wet-lab autonomous. [Robin](https://arxiv.org/abs/2505.13400)

## One day’s experiment

Make 12 small, blinded analysis fixtures from your own completed work: four loud failures, four quiet failures that exit cleanly, and four clean controls. Quiet failures should include an empty control, shuffled labels, a wrong grouping unit, and a stale input. Run the same agent brief twice: normal workflow, then your gated workflow with uneditable checks. Measure sensitivity and false-positive rate by failure type, plus time to detection. That would directly test the site’s thesis instead of illustrating it.