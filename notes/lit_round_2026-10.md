# AI agents for scientific research: literature and landscape round (October 2026)

Compiled 2026-10-06. Every entry was opened at its primary source on that date
(arXiv abstract page, bioRxiv record through the bioRxiv API, PubMed record, or
official project or docs page). Where a journal page was paywalled, the PubMed
record was used instead; this is noted. Limitations are given only where the source
itself, or a named critique, states them. Numbers are quoted from the source, not
recomputed.

## (a) Autonomous "AI scientist" systems

1. **The AI Scientist (v1)**: Lu, Lu, Lange, Foerster, Clune, Ha, arXiv Aug 2024 (Sakana AI with UBC, Vector Institute and Oxford per the Nature announcement); journal version in *Nature*, March 2026.
   - Approach: an LLM pipeline generates ideas, writes and runs experiment code, makes figures, writes a full paper, and scores it with an automated reviewer, at under $15 per paper. Limited to machine learning topics.
   - Limits: Sakana's own Nature announcement says it "occasionally produces naive or underdeveloped ideas", struggles with methodological rigour and complex code, produces inaccurate citations and duplicated figures, and is limited to computational experiments. See also entry 31 (Beel et al.).
   - Verified: https://arxiv.org/abs/2408.06292 ; https://sakana.ai/ai-scientist-nature/ (gives the Nature DOI 10.1038/s41586-026-10265-5; the Nature page itself was not opened because of the paywall redirect)

2. **The AI Scientist-v2**: Yamada, Lange, Lu, Hu et al. (Sakana AI), arXiv April 2025.
   - Approach: uses a progressive agentic tree search over experiments, with a vision-language model reviewing the figures. One generated paper passed peer review at an ICLR 2025 workshop.
   - Limits: the authors call it workshop-level, not main-conference level. Sakana withdrew the accepted paper before publication.
   - Verified: https://arxiv.org/abs/2504.08066

3. **AI co-scientist**: Gottweis, Weng, Daryin, Tu et al. (Google), arXiv Feb 2025, revised June 2026 (title now "Accelerating scientific discovery with Co-Scientist").
   - Approach: a multi-agent system built on Gemini. Agents generate, critique, rank (in a tournament) and refine hypotheses, running tasks asynchronously. Validated on drug repurposing, target discovery and antimicrobial-resistance mechanisms.
   - Limits: validated in three biomedical areas only, and output quality depends on the quality of the existing literature given to it.
   - Verified: https://arxiv.org/abs/2502.18864

4. **Robin**: Ghareeb, Chang, Mitchener et al. (FutureHouse), arXiv May 2025.
   - Approach: a multi-agent system combining literature-search agents and a data-analysis agent to run the cycle of hypothesis, experiment proposal and result interpretation. The wet-lab work is done by humans. It proposed ripasudil (a ROCK inhibitor) as a candidate for dry age-related macular degeneration.
   - Limits: the authors describe it as semi-autonomous.
   - Verified: https://arxiv.org/abs/2505.13400

5. **Kosmos**: Mitchener, Yiu, Chang et al. (FutureHouse), arXiv Nov 2025.
   - Approach: a structured "world model" coordinates a data-analysis agent and a literature-search agent over long runs. A run is reported as about 42,000 lines of code executed and 1,500 papers read, ending in a report with traceable claims.
   - Limits: independent scientists judged 79.4% of report statements accurate, so about one statement in five was not.
   - Verified: https://arxiv.org/abs/2511.02824

6. **Agent Laboratory**: Schmidgall, Su, Wang et al., arXiv Jan 2025.
   - Approach: takes a human research idea and runs three stages (literature review, experiments, report writing), with optional human feedback at each stage. Reports an 84% cost reduction compared with earlier autonomous methods.
   - Limits: the authors report that quality improved markedly with human feedback, so the system is not fully autonomous in practice.
   - Verified: https://arxiv.org/abs/2501.04227

7. **Coscientist**: Boiko, MacKnight, Kline, Gomes (Carnegie Mellon, Emerald Cloud Lab), *Nature* 624:570-578, Dec 2023.
   - Approach: a GPT-4 agent with web and documentation search, code execution and lab-automation tools. It planned and ran experiments on robotic hardware, including optimising palladium-catalysed cross-coupling reactions.
   - Verified via the PubMed record (PMID 38123806; the Nature page redirected to a login): https://doi.org/10.1038/s41586-023-06792-0

8. **The Virtual Lab**: Swanson, Wu, Bulaong, Pak, Zou (Stanford, Chan Zuckerberg Biohub), bioRxiv Nov 2024; *Nature* 646:716-723, 2025.
   - Approach: an LLM "principal investigator" agent runs team meetings and one-on-one meetings with LLM specialist agents (chemist, computer scientist, critic), with a human giving high-level feedback. It built a nanobody design pipeline from ESM, AlphaFold-Multimer and Rosetta. Of the 92 nanobodies designed, two bound the JN.1 or KP.3 SARS-CoV-2 variants better while keeping binding to the original spike protein.
   - Verified via the PubMed record (PMID 40730228) and bioRxiv 10.1101/2024.11.11.623004: https://doi.org/10.1038/s41586-025-09442-9

9. **CellVoyager**: Alber, Chen, Sun, Isakova, Wilk, Zou (Stanford), bioRxiv June 2025; published in *Nature Methods* in 2026 (DOI 10.1038/s41592-026-03029-6, per the bioRxiv record).
   - Approach: an LLM agent that takes a single-cell RNA-seq dataset plus a record of the analyses already done, then proposes and runs new analyses in a Jupyter notebook. Evaluated on CellBench (50 studies, 483 analyses) and on three reanalysis case studies; the original authors rated 80% of its hypotheses "scientifically interesting".
   - Verified: https://www.biorxiv.org/content/10.1101/2025.06.03.657517v1 (the Nature Methods page was not opened because of the paywall redirect)

10. **BioDiscoveryAgent**: Roohani, Lee, Huang, Vora, Steinhart et al., arXiv May 2024, revised March 2025.
    - Approach: an LLM agent designs rounds of genetic perturbation (CRISPR screen) experiments using biological reasoning, literature search and tools, without training a model. Reports a 21% improvement over Bayesian-optimisation baselines in finding hit genes.
    - Limits: one evaluation dataset is unpublished (chosen to avoid training-data contamination), and the gene-combination results are exploratory.
    - Verified: https://arxiv.org/abs/2405.17631

## (b) Assistants and tools for a researcher in the loop

11. **PaperQA2**: Skarlinski, Cox, Laurent, Braza et al. (FutureHouse), arXiv Sept 2024.
    - Approach: a retrieval agent for scientific literature that searches papers, gathers evidence and writes cited answers. Matched or exceeded subject experts on retrieval and summarisation, and 70% of the contradictions it flagged in papers were validated.
    - Limits: the paper is framed around LLM hallucination, which is still a risk.
    - Verified: https://arxiv.org/abs/2409.13740

12. **FutureHouse Platform**: FutureHouse, launched 1 May 2025.
    - Approach: web interface and API for four agents. Crow answers literature questions, Falcon writes deep literature reviews (with database access, e.g. Open Targets), Owl answers "has anyone done X?", and Phoenix plans chemistry tasks (built on ChemCrow and labelled experimental).
    - Verified: https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents

13. **Biomni**: Huang, Zhang, Wang et al.; Leskovec senior author (Stanford, with Regev, Snyder and others), bioRxiv June 2025.
    - Approach: a general-purpose biomedical agent. An "action discovery" agent mined tools, databases and protocols from publications in 25 biomedical domains to build its working environment. The agent then plans with retrieval and works by executing code. Web app at biomni.stanford.edu.
    - Limits: no journal version was found (the bioRxiv record shows "published_doi: NA"). Its own group's later benchmark (entry 29) reports weak method selection and biological interpretation.
    - Verified: https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1

14. **Paper2Agent**: Miao, Davis, Zhang, Pritchard, Zou (Stanford), arXiv Sept 2025.
    - Approach: turns a paper and its code repository into an MCP server (Model Context Protocol, a standard way to expose tools to agents). It generates and runs tests to check the tools, so a chat agent can run the paper's methods on new inputs.
    - Verified: https://arxiv.org/abs/2509.06917

15. **CellAgent**: Xiao, Liu, Zheng et al., arXiv July 2024.
    - Approach: LLM agents in planner, executor and evaluator roles, coordinated hierarchically, automate single-cell RNA-seq analysis tasks and evaluate and refine their own outputs.
    - Verified: https://arxiv.org/abs/2407.09811

16. **ChemCrow**: M. Bran, Cox, Schilter, Baldassari, White, Schwaller (EPFL, Rochester, FutureHouse, IBM), *Nature Machine Intelligence* 6:525-535, 2024.
    - Approach: GPT-4 combined with 18 expert-designed chemistry tools. It planned syntheses of an insect repellent and three organocatalysts, and guided discovery of a new chromophore.
    - Verified via the PubMed record (PMID 38799228): https://doi.org/10.1038/s42256-024-00832-8

17. **Claude Code**: Anthropic.
    - Approach: an agentic coding tool that reads a codebase, edits files and runs commands. It runs in the terminal, VS Code, JetBrains, a desktop app and the web.
    - Configuration: reads `CLAUDE.md` (and `AGENTS.md`) instruction files, skills (`SKILL.md`), hooks, subagents and MCP servers.
    - Verified: https://code.claude.com/docs/en/overview

18. **OpenAI Codex CLI**: OpenAI, Apache-2.0.
    - Approach: "Lightweight coding agent that runs in your terminal". Listed by agents.md as an AGENTS.md reader and by agentskills.io as a skills client.
    - Verified: https://github.com/openai/codex

19. **Gemini CLI**: Google, Apache-2.0.
    - Approach: open-source terminal agent with Google Search grounding, file and shell tools, and MCP support. Its context file is `GEMINI.md`. The README states a free tier of 60 requests per minute and 1,000 per day.
    - Verified: https://github.com/google-gemini/gemini-cli

20. **Cursor**: Anysphere.
    - Approach: an AI code editor plus coding agents (local and cloud, parallel) that also run from a CLI, Slack and GitHub. Supports models from several providers. Listed as a skills client.
    - Verified: https://cursor.com/ (an ownership statement on the page was not independently checked and is not repeated here)

21. **Aider**: open source (aider.chat).
    - Approach: terminal pair-programming tool. It builds a map of the repository for context and commits every change to git with a descriptive message, so changes can be reviewed and reverted. Works with most LLM providers and with local models.
    - Verified: https://aider.chat/

22. **Jupyter AI**: Project Jupyter (incubating under the JupyterLab organisation).
    - Approach: JupyterLab extension that connects external agents (Claude, Codex, Copilot, Gemini) to notebooks through the Agent Client Protocol. A built-in Jupyter MCP server lets the agent edit files and run commands after the user approves.
    - Verified: https://github.com/jupyterlab/jupyter-ai

23. **Claude for Life Sciences**: Anthropic, announced 20 Oct 2025.
    - Approach: a bundle of connectors (Benchling, BioRender, PubMed, Wiley Scholar Gateway, Synapse.org, 10x Genomics) and Agent Skills (for example `single-cell-rna-qc`) for Claude. The post cites a Protocol QA score of 0.83 against a human baseline of 0.79 for Claude Sonnet 4.5.
    - Verified: https://www.anthropic.com/news/claude-for-life-sciences

24. **AGENTS.md**: originated jointly by OpenAI Codex, Amp, Google Jules, Cursor and Factory; now stewarded by the Agentic AI Foundation under the Linux Foundation.
    - Approach: one plain Markdown file of project instructions that many coding agents read. The site claims more than 60,000 open-source projects use it; readers include Codex, Copilot, Jules, Gemini CLI, Aider, goose, Zed and VS Code. Claude Code reads it alongside `CLAUDE.md`.
    - Verified: https://agents.md/ ; https://code.claude.com/docs/en/overview

25. **Agent Skills (`SKILL.md`)**: originated by Anthropic, released as an open standard.
    - Approach: a skill is a folder holding a `SKILL.md` file (name, description, instructions) plus optional scripts and reference files. Agents read only the name and description at startup and load the full text when a task matches ("progressive disclosure"). The site lists dozens of clients, including Claude Code, Codex, Gemini CLI, Cursor, Copilot / VS Code, OpenHands and goose.
    - Verified: https://agentskills.io/

## (c) Benchmarks and critiques

26. **LAB-Bench**: Laurent, Janizek, Ruzo et al. (FutureHouse), arXiv July 2024.
    - Approach: more than 2,400 multiple-choice questions on practical biology research tasks: literature search, database lookup, reading figures and tables, sequence manipulation, and protocols.
    - Verified: https://arxiv.org/abs/2407.10362

27. **BixBench**: Mitchener, Laurent, Andonian, Tenmann et al. (FutureHouse), arXiv Feb 2025 (v3 Oct 2025).
    - Approach: more than 50 real bioinformatics analysis scenarios with about 300 open-answer questions, run in a notebook-based agent environment.
    - Finding: GPT-4o and Claude 3.5 Sonnet reached 17% accuracy on open answers and did no better than random on multiple choice.
    - Verified: https://arxiv.org/abs/2503.00096

28. **ScienceAgentBench**: Chen, Chen, Ning, Zhang, Wang et al., arXiv Oct 2024.
    - Approach: 102 tasks from 44 peer-reviewed papers in four disciplines (including bioinformatics), each checked by experts and scored on the Python program the agent produces.
    - Finding: the best agent solved 32.4% of tasks (34.3% with expert hints). o1-preview reached 42.2% at more than 10 times the cost.
    - Verified: https://arxiv.org/abs/2410.05080

29. **BiomniBench**: Qu, Lu, Tu et al.; Leskovec and Huang senior authors (Phylo, Stanford), bioRxiv May 2026.
    - Approach: scores the agent's whole working trail (trajectory) against expert rubrics instead of only its final answer. The first release has 100 data-analysis tasks, each based on a published paper and co-developed with an original author or a domain expert.
    - Findings: the agent harness moved scores more than one model generation did. Agents cite real sources reliably but fall short on method selection, biological interpretation and reasoning.
    - Verified: https://www.biorxiv.org/content/10.64898/2026.05.12.724604v1

30. **FlowBench / FlowAgent**: Kurjan, Cribbs (Entelo Bio), bioRxiv June 2026.
    - Approach: splits agentic bioinformatics into four separately scored parts: planning, fault recovery, biological interpretation and output fidelity. Tested 23 models on one modular harness.
    - Findings:
      - Choosing a toolchain from the biological goal alone passed 44-57% across all models.
      - Recovering from faults is unsolved: agents often "fix" a run so it exits cleanly while the data stay invalid.
      - Reasoning-tier models were among the worst at recognising faults that cannot be recovered.
    - Verified: https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1

31. **Evaluating Sakana's AI Scientist**: Beel, Kan, Baumgart, arXiv Feb 2025 (revised Oct 2025).
    - Approach: an independent hands-on evaluation of AI Scientist v1.
    - Findings:
      - It labelled established ideas as novel.
      - 42% of its experiments failed because of coding errors.
      - Its manuscripts had a median of 5 citations and contained placeholder text and missing figures.
    - Verified: https://arxiv.org/abs/2502.14297

32. **The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems**: Luo, Kasirzadeh, Shah, arXiv Sept 2025.
    - Approach: controlled tests of AI scientist systems for four failure types: unsuitable benchmark choice, data leakage, metric misuse and post-hoc selection bias.
    - Finding: these failures are often invisible in the final paper. The authors recommend that venues require trace logs and code.
    - Verified: https://arxiv.org/abs/2509.08713

33. **AI Scientists Fail Without Strong Implementation Capability**: Zhu, Xie, Weng, Wu et al., arXiv June 2025.
    - Approach: a position paper that assesses 28 papers produced by five AI scientist systems.
    - Argument: the bottleneck is running the verification steps needed to check a result, not generating ideas.
    - Verified: https://arxiv.org/abs/2506.01372

34. **Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap**: Ding, Nannapaneni, Liu, Zhang, arXiv June 2026.
    - Approach: a survey of 24 systems.
    - Findings: 83% of the runnable systems release code, but artifacts that allow reproduction or checking of claims are rare. Only 38% report any method for checking novelty.
    - Verified: https://arxiv.org/abs/2608.05179

35. **Fabricated citations in NeurIPS 2025 accepted papers**:
    - **GPTZero** (21 Jan 2026): checked 4,841 accepted papers and confirmed 100+ hallucinated citations across 53 papers, all of which had passed peer review.
    - **Ansari, "Compound Deception in Elite Peer Review"** (arXiv Feb 2026): sorts those 100 citations into a five-category taxonomy. Total fabrication was 66%, often combined with semantic hallucination (63%).
    - Verified: https://gptzero.me/news/neurips/ ; https://arxiv.org/abs/2602.05930

36. **Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences**: Russinovich, Siva Kumar, Salem, arXiv July 2026.
    - Approach: built RefChecker, an open citation-verification pipeline.
    - Finding: about one in twenty NeurIPS and USENIX Security papers contains at least two likely hallucinated references.
    - Verified: https://arxiv.org/abs/2607.00738

## (d) Practical reading

37. **Building effective agents**: Erik S. (as credited on the page) and Barry Zhang (Anthropic), 19 Dec 2024.
    - Distinguishes workflows (fixed code paths) from agents (the model directs its own process). Advice: start with a single LLM call and add agentic complexity only when simpler versions measurably fall short; keep planning steps visible; put real effort into tool descriptions (the agent-computer interface).
    - Verified: https://www.anthropic.com/engineering/building-effective-agents

38. **Best practices for Claude Code**: Anthropic docs (the old engineering-blog URL now redirects here).
    - Central constraint: the context window fills and performance degrades as it does.
    - Advice:
      - Give the agent a check it can run (tests, a script, a screenshot).
      - Explore, then plan, then code.
      - Keep `CLAUDE.md` short and prune it; put occasional knowledge in skills; use hooks for anything that must always happen.
      - Use subagents for investigation and for adversarial review in a fresh context; `/clear` between unrelated tasks.
    - Verified: https://code.claude.com/docs/en/best-practices

39. **Simon Willison on agents**: two blog posts, Sept 2025.
    - "I think 'agent' may finally have a widely enough agreed upon definition to be useful jargon now" (18 Sept) proposes: "An LLM agent runs tools in a loop to achieve a goal."
    - "Designing agentic loops" (30 Sept) advises running agents unattended only inside a sandbox (containers, Codespaces), giving scoped, budget-limited credentials, exposing CLI tools by documenting them, and picking problems with clear success criteria.
    - Verified: https://simonwillison.net/2025/Sep/18/agents/ ; https://simonwillison.net/2025/Sep/30/designing-agentic-loops/

40. **AI for Auto-Research: Roadmap & User Guide**: Kong, Sun, Chow et al., arXiv May 2026 (revised July 2026).
    - Approach: maps AI use across the research lifecycle, with a taxonomy, benchmark and tool inventory, and a playbook for practitioners.
    - Conclusion: "greater automation can obscure rather than eliminate failure modes", so human-guided collaboration is the more reliable mode.
    - Verified: https://arxiv.org/abs/2605.18661

## Not verified or not included

- The Coscientist, ChemCrow, Virtual Lab, CellVoyager (Nature Methods) and AI Scientist (Nature 2026) journal pages redirect to a Nature login. Bibliographic details come from PubMed records (Coscientist, ChemCrow, Virtual Lab), the bioRxiv "published DOI" field (CellVoyager) and Sakana's own announcement (AI Scientist Nature). The abstracts on the journal pages themselves were not read.
- Biomni: no peer-reviewed version found as of this round.
- Seen in search results but not opened, so excluded: PromptBio-Bench, BioDesignBench, HeurekaBench, the "Evaluating Agentic Bioinformatics through Function, Evidence, and Validation" preprint, InternAgent-1.5, EvoScientist, and the "Agentic Economies" and "SCP" preprints. Candidates for the next round.
- No separate guide written specifically for biologists using coding agents was found and verified in this round.
- Organisation labels for PaperQA2, Robin, Kosmos, LAB-Bench, BixBench (FutureHouse), Paper2Agent (Stanford) and AI co-scientist (Google) come from general knowledge of the author groups. The arXiv abstract pages that were opened do not show affiliations. Titles, authors, dates and findings were checked; these labels were not.
