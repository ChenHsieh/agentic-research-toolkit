import sys; sys.path.insert(0,'tools')
from page import page, COPY
from html import escape as e
def pre(t): return f'<pre><code>{e(t.strip())}</code></pre>\n'

ex='<h1>Examples</h1>\n<p>Files and prompts I reuse. Copy them and change the details. Each one exists because something went wrong without it.</p>\n'
ex+='<h2>A rules file</h2>\n<p>Saved as <code>CLAUDE.md</code> in the project folder (Codex reads <code>AGENTS.md</code>). Read by the agent at the start of every session. Start with five lines; add one after each mistake.</p>\n'+pre('''
# Project: [name]

## Where things are
- Raw data: [path]. Read-only. Never modify or delete.
- Outputs: [path]
- Status: STATUS.md. Read it first.

## How to run things
- Heavy work goes in batch jobs, not on the login node.
- Load software with: [exact commands, exact versions]
- A job is done when the scheduler reports it finished AND the output file is checked.

## Never
- Report a number without the file it came from.
- Commit in a checkout another session is using.

## Mistakes that already happened (newest first)
- [date] A control returned no values and was reported as a pass. A control with no values is BLOCKED.
''')
ex+='<h2>A brief</h2>\n<p>Written before a long task, in a file. When the conversation gets summarized, this is still there.</p>\n'+pre('''
# Brief: [task]

Goal: [one sentence: what question this answers]
Inputs: [paths, with versions or commit]
Done means: [the files that must exist, and what they must contain]
Known traps: [what went wrong last time]
Not in scope: [what not to touch]
What a pure artifact would look like: [write this before seeing the result]
''')
ex+='<h2>A status file</h2>\n<p>Updated after each real step. A new session starts by reading it.</p>\n'+pre('''
# STATUS (updated [date])

Done
- [step]: [output path], commit [hash after push]
Open
- [step]: blocked on [what / whom]
Results and where they live
- [number]: [file], [how computed]
Corrections
- [date] [what changed, and why]
''')
ex+='<h2>Prompts I reuse</h2>\n'
for t,p in [("Catch up","Brief me on [project]. Read STATUS.md and the last ten commits. What is done, what is open, what is blocked and on whom?"),
("Before an analysis","Before running anything, write in the brief what the result would look like if it were an artifact of how the data was built. Then run it."),
("Try to break it","Here is the result. List the three explanations most likely to make it an artifact. Run the checks. Report which it survives, with the file for each check. A check with no values is BLOCKED, not passed."),
("After a talk","After my talk people asked: [questions]. For each: can we answer it with data we already have? If yes, do it. If not, say what it would take."),
("Clean-room reproduction","In a new empty folder, rebuild [results] from the Methods text and the raw inputs only. Do not read existing intermediate files. When the text is missing something you need, stop and mark that number BLOCKED. Do not guess. End with a table: number, expected, observed, PASS / FAIL / BLOCKED."),
("Literature","Read [group]'s recent papers on [topic]. What methods do they treat as standard? Which apply to my data, and what would each cost? Quote the paper for every claim, with page or section. Mark anything you could not open."),
("Update for my advisor","Summarize what changed this week. Results first, one line each, with the figure and file. Flag anything that reverses what I reported before."),
("Make the check fail once","Before we trust this check, show it failing. Run it on an input built to be wrong (empty file, shuffled labels, a known-bad case) and show me that it reports a failure. If it passes, the check is broken."),
("Fresh-eyes review","Another session worked on this today. Read its commits and output files, not its summary. What did it actually do? What is unsupported, unfinished, or wrong?")]:
    ex+=f'<h3>{t}</h3>\n'+pre(p)
ex+='<h2>Figure rules</h2>\n<p>Kept in one file the agent reads before any plot.</p>\n'+pre('''
- One figure per file. Compose panels later.
- Every plot states n. A stats table is written from the same data frame that was plotted.
- Bounded values: box plus points. Counts: bars from zero.
- Log axis only when values span 2+ orders of magnitude, and never for bars. Say "log10" in the axis title.
- Colours come from one palette file. Each group keeps its colour across the project. Colourblind-safe.
- Thresholds are justified, cited, or shown as a range.
- Do not average across groups a reader would consider distinct.
- No titles. Context goes in the filename and caption.
- Open the saved image and check it before calling it done.
''')
ex+='<h2>Working in Word</h2>\n<p>Many advisors review in Word. An agent with a document tool can make its edits as tracked changes under a named author, put questions in as Word comments, and turn a returned file\'s comments into a table of requests and proposed responses. Work on a copy, and open the result in Word before sending it.</p>\n'
page('examples.html','Examples: using an agent for research',ex,'Rules file, brief, status file, prompts and figure rules I reuse.',COPY)

cases=[
("A comparison against a control came back. The agent's summary: \"No significant difference from control. Check passed.\" The control table has 0 rows.","BLOCKED","Nothing compared with nothing is not a difference. The control never ran. This one happened to me; now an empty control fails loudly."),
("A cluster job exited with code 0. The output file exists. It has a header and no data rows.","BLOCKED","Exit code 0 means the program stopped without an error, not that it produced anything. A step is done when the output is checked."),
("Across 48 attention heads in 6 layers, a score correlates with an effect: rho = +0.45, p = 0.001. Computed within each layer, the same correlation is rho = -0.11, p = 0.47.","FAIL","The heads are grouped. The pooled correlation came from differences between layers, not between heads. The claim about heads does not hold."),
("Rebuilding a chapter from its Methods text, the agent's count matches the paper exactly. Its log notes that the Methods did not state a software setting, so it picked the one that matched.","BLOCKED","A guess that matches hides the gap. The Methods are incomplete. In my case, the default setting changed 732 of 13,663 genes."),
("A website build passes every check: inputs pinned, checksums match. The source repository's corrections log changed yesterday.","BLOCKED","Pinned inputs prove the site matches what it was built from, not that the source still stands. My site served a withdrawn gene set for four days with every check green."),
("An intervention shows no effect. In that arm, 2% of the positions that could change actually changed.","BLOCKED","An arm that barely moved cannot show an effect. The null is a fact about the sampler, not about the system."),
("Two classification methods are run on the same reads. They agree on 99.5% or more of reads at family level. Most genus-level disagreement is between two genera in the same family. The report says: family-level results are robust; a few named genera depend on the method.","PASS","The claim matches the evidence and states its limit. The disagreements are reported, not averaged away."),
]
pr='<h1>Practice</h1>\n<p>Seven cases. Each happened in my work, lightly simplified. For each, decide whether the result is done (PASS), wrong (FAIL), or cannot be judged yet (BLOCKED). Then see what happened.</p>\n'
for i,(q,a,why) in enumerate(cases,1):
    pr+=f'''<div class="case" data-a="{a}" style="margin:2.2em 0;padding-top:.2em">
<p><b>{i}.</b> {e(q)}</p>
<p class="opts">{''.join(f'<button class="ans" style="font:15px Georgia,serif;margin-right:.5em;padding:3px 10px;background:none;border:1px solid #999;cursor:pointer">{o}</button>' for o in ("PASS","FAIL","BLOCKED"))}</p>
<p class="why" hidden><span class="verdict"></span> {e(why)}</p>
</div>
'''
pr+='<p class="small">Most of these are BLOCKED. That matches my experience: the common failure is not a wrong number, it is a number that was never really measured.</p>'
js='''<script>
document.querySelectorAll('.case').forEach(function(c){c.querySelectorAll('.ans').forEach(function(b){b.onclick=function(){
var ok=b.textContent===c.dataset.a;var w=c.querySelector('.why');w.hidden=false;
w.querySelector('.verdict').innerHTML=(ok?'Yes, ':'No, ')+'<b>'+c.dataset.a+'</b>.';
c.querySelectorAll('.ans').forEach(function(x){x.style.borderColor=x.textContent===c.dataset.a?'#a33':'#ccc';x.style.color=x.textContent===c.dataset.a?'#a33':'#999'})}})});
</script>'''
page('practice.html','Practice: is this result done?',pr,'Seven real cases: decide PASS, FAIL or BLOCKED.',js)

se='''<h1>A 20-minute session</h1>
<p>If you want to try this on your own project, I am happy to spend 20 minutes with you on a video call. Friends and labmates first.</p>
<h2>What we do</h2>
<p><b>5 minutes.</b> Your project, and one task you would like help with.</p>
<p><b>10 minutes.</b> On your screen, in a folder you know well: start a session, ask it to explain the folder, check its answer against what you know, and write the first five lines of your rules file.</p>
<p><b>5 minutes.</b> What went wrong, what to try this week, and which <a href="examples.html">examples</a> to copy.</p>
<h2>What to bring</h2>
<p>Claude Code installed and logged in (your lab or personal account). A folder you understand: an analysis, a pipeline, or a set of notes. One real task.</p>
<p>No data that cannot leave your institution. We look at code and file names, not protected data.</p>
<h2>How to ask</h2>
<p>Message me on Slack, or open an issue on the <a href="https://github.com/ChenHsieh/agentic-research-toolkit/issues">repository</a> with a sentence about your project.</p>
<h2>Before the call</h2>
<p>Read the <a href="index.html">essay</a> (10 minutes) and try the <a href="practice.html">practice cases</a> (5 minutes).</p>
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
rd+=it("rewrites.bio","https://rewrites.bio/","Seqera, 2026","Twelve principles for rewriting bioinformatics tools with AI: credit the original authors, match outputs exactly, say how AI was used, validate each small step against the original.")
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
