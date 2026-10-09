import sys; sys.path.insert(0,'tools')
from page import page, COPY, COPY2
from html import escape as e
def pre(t): return f'<pre><code>{e(t.strip())}</code></pre>\n'

ex='<h1>Examples</h1>\n<p>Two files and six prompts I actually use. Copy them, then change the details to fit your project.</p>\n'
ex+='<h2>A rules file</h2>\n<p>Save it as <code>CLAUDE.md</code> in your project folder (Codex reads <code>AGENTS.md</code>). The agent reads it at the start of every session. Five lines is enough to begin; add one each time something goes wrong.</p>\n'+pre("""
# [Project name]

Raw data is in [path]. Never modify or delete it.
Write outputs to [path].
Read STATUS.md before starting.
Load software with: [your exact module or conda commands]
A job is finished when its output file has been checked, not when it exits.

## Things that went wrong before
- [date] A control came back empty and was reported as a pass.
""")
ex+='<h2>A status file</h2>\n<p>Save it as <code>STATUS.md</code>. Ask the agent to update it after each real step. When a session ends or gets long, the next one starts from here instead of from memory.</p>\n'+pre("""
# Status ([date])

Goal: [one sentence]
Done when: [which files exist, and what they show]

## Done
- [step]: [output file]

## Open
- [step]: waiting on [what or whom]

## Numbers and where they came from
- [number]: [file], [how it was computed]
""")
ex+='<h2>Prompts</h2>\n'
for t,p in [("Catch me up","Read STATUS.md and the last ten commits. What is done, what is still open, and what is waiting on someone?"),
("Before I trust this check","Run this check on an input that should fail, such as an empty file or shuffled labels, and show me that it fails."),
("Try to break this result","What are the three most likely ways this result could be an artifact? Check each one and show me the file for each check."),
("Rebuild from the Methods","In an empty folder, rebuild these results using only the Methods text and the raw data. If the text leaves something out, stop and tell me instead of guessing. Finish with a table of each number: expected, what you got, and whether it matched."),
("Read the papers","Read these papers and tell me which methods they treat as standard. Quote the paper for each claim, with the section. Tell me which papers you could not open."),
("Review today's work","Another session worked on this today. Read its commits and output files, not its summary. What was actually done, and what is not supported?")]:
    ex+=f'<div class="prompt"><div class="ph">{t}</div><p>{e(p)}</p></div>\n'
page('examples.html','Examples: using an agent for research',ex,'A rules file, a status file, and six prompts I use.',COPY2)

se='''<h1>A 20-minute session</h1>
<p>If you want to try this on your own project, I am happy to spend 20 minutes with you on a video call. Friends and labmates first.</p>
<h2>What we do</h2>
<div class="steps">
<div><span class="min">5 min</span><b>Your project</b><p>What you work on, and one task you would like help with.</p></div>
<div><span class="min">10 min</span><b>On your screen</b><p>Start a session in a folder you know. Ask it to explain the folder. Check its answer against what you know. Write your first five-line rules file.</p></div>
<div><span class="min">5 min</span><b>Next week</b><p>What went wrong, what to try on your own, which examples to copy.</p></div>
</div>
<p>You leave with a working setup, a rules file for your project, and one task you have already tried.</p>
<h2>What to bring</h2>
<p>Claude Code installed and logged in (your lab or personal account). A folder you understand: an analysis, a pipeline, or a set of notes. One real task.</p>
<p>No data that cannot leave your institution. We look at code and file names, not protected data.</p>
<h2>How to ask</h2>
<p>Message me on Slack, or open an issue on the <a href="https://github.com/ChenHsieh/agentic-research-toolkit/issues">repository</a> with a sentence about your project.</p>
<h2>Before the call</h2>
<p>Read the <a href="index.html">essay</a> (10 minutes). Note which of the seven failure patterns you think you would have missed. We can start there.</p>
'''
page('session.html','A 20-minute session',se,'Go through this on your own project with me in 20 minutes.')
print('ok')

LAND='''<script src="https://cdn.jsdelivr.net/npm/d3@7"></script><script src="graph.js"></script><script>
drawDiagrams({land:{height:380,axis:['you drive','it drives'],legend:[['you','coding agents'],['file','research assistants'],['agent','autonomous research systems'],['bad','idea-to-paper']],nodes:[
{id:'cc',label:'Claude Code',kind:'you',x:.08,y:.2,info:'Terminal agent. You approve commands and set the rules.',url:'https://code.claude.com/docs/en/overview'},
{id:'cx',label:'Codex CLI',kind:'you',x:.1,y:.42,info:'Terminal agent from OpenAI. Reads AGENTS.md.',url:'https://github.com/openai/codex'},
{id:'gm',label:'Gemini CLI',kind:'you',x:.08,y:.64,info:'Open-source terminal agent with a free tier.',url:'https://github.com/google-gemini/gemini-cli'},
{id:'ai',label:'Aider',kind:'you',x:.12,y:.8,info:'Commits every change to git; works with local models.',url:'https://aider.chat/'},
{id:'pq',label:'PaperQA2',kind:'file',x:.33,y:.25,info:'Literature agent that answers with citations.',url:'https://arxiv.org/abs/2409.13740'},
{id:'bm',label:'Biomni',kind:'file',x:.35,y:.55,info:'General biomedical agent; tools mined from 25 domains. Its own benchmark finds weak method choice.',url:'https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1'},
{id:'p2',label:'Paper2Agent',kind:'file',x:.32,y:.78,info:'Turns a paper plus its code into callable tools, with tests.',url:'https://arxiv.org/abs/2509.06917'},
{id:'cv',label:'CellVoyager',kind:'agent',x:.55,y:.2,info:'Proposes and runs new analyses on published single-cell data.',url:'https://www.biorxiv.org/content/10.1101/2025.06.03.657517v1'},
{id:'vl',label:'Virtual Lab',kind:'agent',x:.56,y:.48,info:'LLM PI plus specialist agents plus a human. 92 nanobodies designed; 2 improved.',url:'https://doi.org/10.1038/s41586-025-09442-9'},
{id:'rb',label:'Robin',kind:'agent',x:.58,y:.74,info:'Literature and analysis agents; humans run the wet lab.',url:'https://arxiv.org/abs/2505.13400'},
{id:'co',label:'AI co-scientist',kind:'agent',x:.78,y:.3,info:'Agents generate and rank hypotheses in a tournament.',url:'https://arxiv.org/abs/2502.18864'},
{id:'ks',label:'Kosmos',kind:'agent',x:.8,y:.6,info:'Long autonomous runs. 79.4% of report statements judged accurate.',url:'https://arxiv.org/abs/2511.02824'},
{id:'as',label:'AI Scientist',kind:'bad',x:.9,y:.78,info:'Idea to paper with automated review, machine learning only. Independent test: 42% of experiments failed on coding errors.',url:'https://arxiv.org/abs/2408.06292'}],links:[]}});
</script>'''
def it(name,url,who,what):
    return f'<p><a href="{url}">{name}</a> <span class="small">({who})</span>. {what}</p>\n'
rd='''<h1>Reading</h1>
<p>Papers, tools and guides on agents for research, checked on 6 October 2026. Every link was opened at its source. Numbers are quoted from the source.</p>
<figure><div class="g" data-g="land"></div><figcaption>Left: you drive, the tool assists. Right: the system plans and runs the research itself. Placement is my reading of each paper. Hover for a summary; click to open the paper.</figcaption></figure>
<h2>Start here</h2>
'''
rd+=it("Building effective agents","https://www.anthropic.com/engineering/building-effective-agents","Anthropic, 2024","Start with one model call; add agent steps only when the simpler version measurably falls short.")
rd+=it("Best practices for Claude Code","https://code.claude.com/docs/en/best-practices","Anthropic docs","Give the agent a check it can run. Keep the rules file short. Use hooks for anything that must always happen.")
rd+=it("Designing agentic loops","https://simonwillison.net/2025/Sep/30/designing-agentic-loops/","Simon Willison, 2025","Run unattended agents only in a sandbox, with limited credentials, on problems with clear success criteria. His definition: \"An LLM agent runs tools in a loop to achieve a goal.\"")
rd+=it("rewrites.bio","https://rewrites.bio/","Seqera","Twelve principles for rewriting bioinformatics tools with AI: credit the original authors, match outputs exactly, say how AI was used, validate each small step against the original.")
rd+=it("AI for Auto-Research: Roadmap and User Guide","https://arxiv.org/abs/2605.18661","Kong et al., 2026","A map of AI use across the research cycle. Conclusion: more automation can hide failure modes rather than remove them.")
rd+='<h2>What the benchmarks say</h2>\n<p>The consistent finding: agents run code well and choose methods and interpret biology poorly.</p>\n'
rd+=it("BixBench","https://arxiv.org/abs/2503.00096","FutureHouse, 2025","About 300 open-answer bioinformatics questions. GPT-4o and Claude 3.5 Sonnet: 17% correct.")
rd+=it("FlowBench","https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1","Kurjan and Cribbs, 2026","23 models. Choosing a toolchain from the biological goal alone: 44 to 57%. Agents often \"fix\" a failing run so it exits cleanly while the data stay invalid.")
rd+=it("BiomniBench","https://www.biorxiv.org/content/10.64898/2026.05.12.724604v1","Qu et al., 2026","Scores the agent's whole working trail against expert rubrics. The harness around the model moved scores more than a model generation did.")
rd+=it("ScienceAgentBench","https://arxiv.org/abs/2410.05080","Chen et al., 2024","102 tasks from 44 papers. Best agent solved 32.4%.")
rd+=it("LAB-Bench","https://arxiv.org/abs/2407.10362","Laurent et al., 2024","Over 2,400 questions on practical biology tasks: literature, databases, figures, sequences, protocols.")
rd+='<h2>Critiques</h2>\n'
rd+=it("Hidden pitfalls of AI scientist systems","https://arxiv.org/abs/2509.08713","Luo, Kasirzadeh, Shah, 2025","Data leakage, metric misuse and post-hoc selection are often invisible in the final paper. Recommends requiring trace logs and code.")
rd+=it("Evaluating Sakana's AI Scientist","https://arxiv.org/abs/2502.14297","Beel, Kan, Baumgart, 2025","42% of experiments failed on coding errors; established ideas labelled as novel.")
rd+=it("AI scientists fail without strong implementation capability","https://arxiv.org/abs/2506.01372","Zhu et al., 2025","The bottleneck is running the checks, not generating ideas.")
rd+=it("The verification gap","https://arxiv.org/abs/2608.05179","Ding et al., 2026","Survey of 24 systems. Most release code; few release what is needed to check their claims.")
rd+=it("Phantom references","https://arxiv.org/abs/2607.00738","Russinovich et al., 2026","About one in twenty NeurIPS and USENIX Security papers has at least two likely fabricated references.")
rd+=it("Fabricated citations at NeurIPS 2025","https://gptzero.me/news/neurips/","GPTZero, 2026","100+ fabricated citations in 53 accepted papers.")
rd+='<h2>Systems that run research themselves</h2>\n'
rd+=it("The AI Scientist","https://arxiv.org/abs/2408.06292","Sakana AI, 2024; Nature 2026","Idea, code, experiments, paper, automated review. Machine learning only. Sakana lists inaccurate citations and duplicated figures among its limits. <a href=\"https://arxiv.org/abs/2504.08066\">v2</a> uses tree search; one paper passed a workshop review.")
rd+=it("AI co-scientist","https://arxiv.org/abs/2502.18864","Google, 2025","Agents generate, critique and rank hypotheses in a tournament. Tested on drug repurposing and resistance mechanisms.")
rd+=it("Kosmos","https://arxiv.org/abs/2511.02824","Mitchener et al., 2025","Long runs over data and literature. Scientists judged 79.4% of report statements accurate.")
rd+=it("Robin","https://arxiv.org/abs/2505.13400","Ghareeb et al., 2025","Literature and analysis agents; humans do the wet lab. Proposed a drug candidate for dry macular degeneration.")
rd+=it("The Virtual Lab","https://doi.org/10.1038/s41586-025-09442-9","Swanson et al., Nature 2025","An LLM \"PI\" runs meetings with specialist agents and a human. Designed 92 nanobodies; two improved binding to new SARS-CoV-2 variants.")
rd+=it("Coscientist","https://doi.org/10.1038/s41586-023-06792-0","Boiko et al., Nature 2023","Planned and ran chemistry on robotic hardware.")
rd+=it("Agent Laboratory","https://arxiv.org/abs/2501.04227","Schmidgall et al., 2025","Literature, experiments, report, with optional human feedback. Quality improved markedly with it.")
rd+=it("CellVoyager","https://www.biorxiv.org/content/10.1101/2025.06.03.657517v1","Alber et al., 2025; Nature Methods 2026","Proposes and runs new analyses on published single-cell data in a notebook.")
rd+=it("BioDiscoveryAgent","https://arxiv.org/abs/2405.17631","Roohani et al., 2024","Designs rounds of CRISPR screens by reasoning plus literature, without training a model.")
rd+='<h2>Tools for a researcher in the loop</h2>\n'
rd+=it("Claude Code","https://code.claude.com/docs/en/overview","Anthropic","Terminal, editor, desktop and web. Reads CLAUDE.md and AGENTS.md, skills, hooks.")
rd+=it("Codex CLI","https://github.com/openai/codex","OpenAI","Terminal coding agent. Reads AGENTS.md.")
rd+=it("Gemini CLI","https://github.com/google-gemini/gemini-cli","Google","Open-source terminal agent with search grounding. Reads GEMINI.md. Has a free tier.")
rd+=it("Aider","https://aider.chat/","open source","Commits every change to git so it can be reviewed and reverted. Works with local models.")
rd+=it("Cursor","https://cursor.com/","Anysphere","Code editor with agents.")
rd+=it("Jupyter AI","https://github.com/jupyterlab/jupyter-ai","Project Jupyter","Connects agents to notebooks; edits and commands need approval.")
rd+=it("PaperQA2","https://arxiv.org/abs/2409.13740","FutureHouse, 2024","Literature agent that answers with citations. The <a href=\"https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents\">FutureHouse platform</a> offers it and three related agents.")
rd+=it("Biomni","https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1","Huang et al., 2025","General biomedical agent with tools mined from 25 domains. Preprint.")
rd+=it("Paper2Agent","https://arxiv.org/abs/2509.06917","Miao et al., 2025","Turns a paper and its code into tools an agent can call, with generated tests.")
rd+=it("CellAgent","https://arxiv.org/abs/2407.09811","Xiao et al., 2024","Planner, executor and evaluator agents for single-cell analysis.")
rd+=it("ChemCrow","https://doi.org/10.1038/s42256-024-00832-8","Bran et al., 2024","GPT-4 with 18 chemistry tools.")
rd+=it("Claude for Life Sciences","https://www.anthropic.com/news/claude-for-life-sciences","Anthropic, 2025","Connectors (PubMed, Benchling, 10x Genomics and others) and skills.")
rd+=it("AGENTS.md","https://agents.md/","Linux Foundation","One instructions file many agents read.")
rd+=it("Agent Skills","https://agentskills.io/","open standard","A folder with a SKILL.md; loaded only when a task matches.")
rd+='<p class="small">Not included: several 2026 preprints seen in search but not read. Affiliations for some arXiv entries are from the author groups, not the abstract pages. Full notes: <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/lit_round_2026-10.md">notes/lit_round_2026-10.md</a>.</p>\n'
page('reading.html','Reading: agents for research',rd,'Papers, tools, benchmarks and critiques on agents for research, checked October 2026.',LAND)
