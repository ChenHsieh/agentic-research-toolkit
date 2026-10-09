# Work modes for coding agents used in research

Source round completed 2026-10-09. “Time horizon” below is a task-difficulty measurement, not a promise that an agent can be left unattended for that many wall-clock hours. Every numbered citation is a page opened during this review; URLs are direct source URLs.

## 1. Supervision modes

1. **Anthropic, current CLI reference** — [URL](https://code.claude.com/docs/en/cli-usage). Claude Code exposes `default`/manual, `acceptEdits`, `plan`, `auto`, `dontAsk`, and `bypassPermissions`; `--dangerously-skip-permissions` is equivalent to bypass and skips prompts. The documentation labels this dangerous and also permits an external permission-prompt tool for non-interactive runs. [Opened: 2026-10-09]

2. **OpenAI, 8 May 2026, “Running Codex safely at OpenAI”** — [URL](https://openai.com/index/running-codex-safely/). Codex combines a technical sandbox (write paths and network) with approval policy; user approval can be once or for the session. OpenAI says its auto-review can approve low-risk requests but higher-risk actions stop for review. [Opened: 2026-10-09]

4. **OpenAI, 13 May 2026, “Building a safe, effective sandbox to enable Codex on Windows”** — [URL](https://openai.com/index/building-codex-windows-sandbox/). It contrasts approving nearly every command with Full Access, which runs commands without approval or restrictions. The stated trade-off is less friction versus less oversight. [Opened: 2026-10-09]

5. **OpenAI, 2026, Codex system-card material** — [URL](https://deploymentsafety.openai.com/gpt-5-1-codex-max/preparing-for-high-cyber-capability). Local and cloud Codex are sandboxed by default: workspace-only writes and no network by default. Cloud networking can be enabled per project with allow/deny lists; the source says this increases prompt-injection, credential-leakage, and licensing risks. [Opened: 2026-10-09]

6. **OpenAI, current, Self-hosted sandboxes** — [URL](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted). An agent harness can command an executor in a laptop, container, or remote sandbox; OpenAI advises isolating environments by user/workload because agents sharing one environment can reach the same files and credentials. It specifies a restricted environment key rather than placing the application API key in the sandbox. [Opened: 2026-10-09]

7. **Cursor, current, Background Agents** — [URL](https://docs.cursor.com/background-agent). Cursor describes asynchronous remote agents that edit and run code on an isolated Ubuntu machine, clone a GitHub repository to a separate branch, and permit follow-up or takeover. It explicitly warns that background agents auto-run terminal commands and have internet access, creating prompt-injection/exfiltration risk. [Opened: 2026-10-09]

8. **Cursor, current, Run Modes** — [URL](https://prod.cursor.com/docs/agent/security/run-modes). Local Cursor agents have read, command, and network controls; network can be `sandbox.json` only, allowlist plus defaults, or all access. Cloud Agents are separate: the documentation says they run on a dedicated machine and never ask the user to approve an action. [Opened: 2026-10-09]

9. **GitHub, current, Copilot cloud-agent firewall** — [URL](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall). Copilot cloud agent has a firewall, enabled by default, and organization/repository allowlists. GitHub says limiting egress manages the risk that unexpected behavior or malicious instructions leak code; disabling the firewall permits any host and raises that risk. [Opened: 2026-10-09]

10. **OpenHands, current, Agent Canvas overview** — [URL](https://github.com/OpenHands/docs/blob/main/openhands/usage/agent-canvas/overview.mdx). OpenHands can run against a local machine, Docker, VM, Modal, or its managed cloud. The docs say to use Docker rather than the direct npm backend for a sandboxed local setup. [Opened: 2026-10-09]

11. **OpenHands, current, custom sandbox guide** — [URL](https://github.com/OpenHands/docs/blob/main/openhands/usage/advanced/custom-sandbox-guide.mdx). In V1, the sandbox container is the agent server and can be a custom image. This is a deployment mechanism, not a claim that the agent is harmless; users control the image and its available tools. [Opened: 2026-10-09]

## 2. Unattended duration and reliability

12. **METR, 2025, “Measuring AI Ability to Complete Long Tasks”** — [URL](https://arxiv.org/abs/2503.14499). On METR’s suite, Claude 3.7 Sonnet’s 50%-task-completion horizon was **about 50 minutes**; the fitted frontier trend doubled about every **7 months** since 2019. This is performance on the suite, not a general unattended-run SLA. [Opened: 2026-10-09]

13. **METR, 8 May 2026, Time Horizons FAQ** — [URL](https://metr.org/time-horizons/). METR’s current GPT-5 agent example is **about 2 hours 17 minutes** at 50% horizon. For tasks whose expert-human times are 90 minutes–3 hours, it reports roughly one-third always succeeds, one-third always fails, and one-third is variable; it says directly that horizon is not the wall-clock duration an agent can act autonomously. [Opened: 2026-10-09]

15. **Anthropic, 19 Dec 2024, “Building effective agents”** — [URL](https://www.anthropic.com/engineering/building-effective-agents). Anthropic says autonomous loops create higher costs and potential compounding errors; its recommendation is extensive testing in sandboxed environments plus guardrails. It presents SWE-bench code resolution as an example agent task, not as evidence of general reliability. [Opened: 2026-10-09]

16. **Cursor, current, “What are background agents?”** — [URL](https://prod.cursor.com/help/ai-features/background-agents). Cursor says cloud agents plan, edit, run commands, and test over “minutes or hours,” so a laptop may be closed; artifacts such as logs, screenshots and videos support later review. This is a product description, with no published success/failure rate. [Opened: 2026-10-09]

17. **Anthropic, Jan 2026, “How AI is transforming work at Anthropic”** — [URL](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic). Across **200,000** internal Claude Code transcripts from February and August 2025, Anthropic estimates independent action sequences rose from about **10** to **20** actions before human input. That is observed internal use, not a controlled reliability rate or an overnight-duration result. [Opened: 2026-10-09]

## 3. Productivity and attention

18. **Becker, Rush, Barnes & Rein / METR, July 2025, RCT** — [URL](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf). In **246** real tasks by **16** experienced open-source developers using early-2025 tools, AI access increased completion time **19%**; participants forecast a **24%** reduction beforehand. They worked in mature projects with an average **5 years** prior experience, so this does not estimate effects for novices, greenfield work, or later tools. [Opened: 2026-10-09]

19. **METR, 24 Feb 2026, productivity-study update** — [URL](https://metr.org/blog/2026-02-24-uplift-update/). METR characterizes the prior result as a **20% slowdown** and says it began a larger, latest-tools study in August 2025. It is an experiment-design update, not a new outcome estimate. [Opened: 2026-10-09]

20. **Anthropic, Jan 2026, internal-work report** — [URL](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic). The report says an internal adoption was associated with **67%** more merged PRs per engineer per day, and **27%** of Claude-assisted work was work that otherwise would not have been done. These are company observational/self-report measures, not randomized causal estimates. [Opened: 2026-10-09]

## 4. Conditions for good or bad unattended runs

23. **Simon Willison, 30 Sep 2025, “Designing agentic loops”** — [URL](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/). Willison’s central recommendation is to design the tools and loop, rather than treating the model as an unbounded replacement for process. Coding agents improve when they can run the code, observe errors, inspect implementation, and iterate. [Opened: 2026-10-09]

24. **Anthropic, 19 Dec 2024, “Building effective agents”** — [URL](https://www.anthropic.com/engineering/building-effective-agents). Clear, well-documented tools and feedback loops matter because agents plan, act, observe and adapt. Anthropic recommends designing tool arguments to make errors harder, and testing tool use with many example inputs. [Opened: 2026-10-09]

25. **OpenAI, 8 May 2026, “Running Codex safely at OpenAI”** — [URL](https://openai.com/index/running-codex-safely/). OpenAI’s stated operational pattern is bounded environments for routine work, review for higher-risk actions, network policies, and logs/telemetry. It says it does not give Codex open-ended outbound access. [Opened: 2026-10-09]

26. **OpenAI, 2026, Codex cloud security material** — [URL](https://deploymentsafety.openai.com/gpt-5-1-codex-max/preparing-for-high-cyber-capability). Default no-network and workspace-only writes reduce prompt injection and exfiltration exposure. When expanding network access, the source tells users to restrict to trusted domains and safe HTTP methods and review results carefully. [Opened: 2026-10-09]

27. **GitHub, current, Copilot firewall** — [URL](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall). Egress control is a concrete response to prompt injection that tries to send repository contents away. The recommended package-registry allowlist is convenient, but broader than a project-specific allowlist. [Opened: 2026-10-09]

28. **Anthropic, 9 Jan 2026, “Demystifying evals for AI agents”** — [URL](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Multi-turn agents modify state and adapt, making evaluation difficult; Anthropic recommends task-specific evaluations that capture the full transcript/tool calls and use production-like environments. This supports independent verifiers and checkpointable artifacts rather than trusting a final claim. [Opened: 2026-10-09]

29. **Anthropic, 9 Apr 2026, “Trustworthy agents in practice”** — [URL](https://www.anthropic.com/research/trustworthy-agents). Anthropic identifies less oversight, misread intent, and prompt injection as risks that rise with autonomy. It describes layers including model training, production monitoring and red teaming, rather than a single prompt-level defense. [Opened: 2026-10-09]

## 5. Scientists, HPC, and analysis pipelines

30. **NCAR, current, “Using Agentic Coding Assistants”** — [URL](https://ncar-hpc-docs.readthedocs.io/en/latest/best-practices-for-supercomputer-users/agentic-ai/). NCAR says agents can submit jobs under the researcher’s account/allocation and recommends approval before commands on shared systems. It specifically warns about a runaway `qsub` loop, recursive deletion, and allocation-consuming jobs; it says not to run the agent itself in automatic mode through `qcmd`. [Opened: 2026-10-09]

31. **Aalto Scientific Computing, current, “AI Agents on HPC”** — [URL](https://scicomp.aalto.fi/triton/usage/ai-agents/). Aalto notes agents may run on a login node and send accessible code/data to a remote provider. Its practical policy is to request confirmation for job submission/cancellation and deletion, and to provide documentation search tools so agents need not guess site policy. [Opened: 2026-10-09]

32. **Stanford Sherlock, current, “AI coding agents”** — [URL](https://www.sherlock.stanford.edu/docs/software/ai/coding-agents/). CLI agents work over SSH and can inspect logs/outputs and run on compute nodes; the same proximity means most hosted-model tools send prompts/code externally. This is relevant to unpublished data and to separating controller, data, and credentials. [Opened: 2026-10-09]

33. **ASCEND authors, 2026, scientific-HPC case report** — [URL](https://arxiv.org/abs/2609.32868). A preprint reports four recorded cases using a policy-checked local tool layer: a fault-recovery loop, a weather evaluation matching curves within **2.1%** and **2.4%**, and a solver reduced from about **12 hours** to **2 hours**. These are case studies, not comparative failure-rate evidence. [Opened: 2026-10-09]

34. **HPC modernization authors, 2026, “Structuring agentic AI for HPC code modernization”** — [URL](https://arxiv.org/abs/2606.08710). The authors report that unstructured LLM use was inadequate, while manually supplied examples, continuous buildability, and limited session scope were effective in their work. It supports short, verifiable stages over an unbounded overnight refactor. [Opened: 2026-10-09]

## Synthesis: 8 practical rules

1. Start new projects in read/plan mode; require an explicit plan and acceptance tests before granting edit/command autonomy. [1, 24]
2. Treat “auto accept” and bypass/Full Access as distinct risk decisions, not as a convenience toggle; use them only inside a bounded disposable environment. [1, 4, 15]
3. For unattended work, provide an independent verifier: tests, numerical tolerances, a build, or an artifact review—not just the agent’s completion statement. [16, 24, 28, 34]
4. Make checkpoint commits, branches, logs and output artifacts mandatory; this preserves review and rollback when a long loop goes wrong. [7, 16, 21]
5. Scope credentials, filesystem paths and network egress to the task. Do not co-locate unrelated secrets merely because the run is sandboxed. [5, 6, 9, 26]
6. Budget unattended time and money, and stop for a human when tests repeatedly fail or the plan changes. Autonomous loops can compound errors and cost. [15, 17, 28]
7. Do not translate benchmark horizon into an overnight reliability guarantee: METR’s 50% point is task difficulty and mixes reliable successes, reliable failures and variable tasks. [12, 13]
8. On shared HPC, never put the controller in unrestricted automatic mode; approve scheduler/deletion actions and encode allocation, queue and data rules in the tools/instructions. [30, 31, 32]

## Not verified

- I did not find an opened primary Devin documentation page that states comparable permission modes, background-session controls, or a recommended use boundary; Devin is therefore not characterized above.
- I did not find an opened primary source with a general, independently measured “multi-hour/overnight coding-agent failure rate.” Product pages describe runs lasting minutes/hours, but do not supply that rate.
- I did not find an opened, credible primary report establishing a general rate of agents modifying tests to game them or deleting research data. The risk is operationally plausible, but it should not be represented here as measured evidence.
- Anthropic’s best-practices and team-use pages were located, but their redirects could not be opened by the verification tool. They are not cited in the numbered source list.
