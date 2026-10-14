import sys; sys.path.insert(0,'tools')
from page import page, COPY, COPY2
from html import escape as e
def pre(t): return f'<pre><code>{e(t.strip())}</code></pre>\n'

ex='<h1>Examples</h1>\n<p>Three files and the prompts I actually use. Copy them, then change the details to fit your project.</p>\n'
ex+='<h2 id="a-rules-file">A rules file</h2>\n<p>Save it as <code>CLAUDE.md</code> in your project folder (Codex reads <code>AGENTS.md</code>). The agent reads it at the start of every session. A few lines is enough to begin; add one each time something goes wrong.</p>\n'+pre("""
# [Project name]

Raw data is in [path]. Never modify or delete it.
Write outputs to [path].
Read STATUS.md before starting.
Load software with: [your exact module or conda commands]
A job is finished when its output file has been checked, not when it exits.
Never send an e-mail or message, post, or push to a live site in my name without asking first. "Continue" means more of the same kind of work.

## Things that went wrong before
- [date] A control came back empty and was reported as a pass.
""")
ex+='<h2 id="a-brief">A brief</h2>\n<p>Save it as <code>BRIEF.md</code> before any task longer than an hour, and before every overnight run. It is the morning check written in advance, so the result gets compared with what you asked for and not with the agent\'s summary. Write the "Done when" line first. If you cannot, the task is not ready to hand over.</p>\n'+pre("""
# Brief: [task] ([date])

Goal: [one sentence]
Inputs (read-only): [paths, with versions]
Done when: [file] exists, has [N] rows, values between [low] and [high]
Decided before seeing results: [filters, thresholds, samples to drop]
If the result were an artifact, it would look like: [your guess, written now]
Before the full run: the check says no to [a known-bad file], and one [sample] is run and checked.
May run without asking: [commands]
Ask first: deleting files, more than [N] jobs, anything outside [path]
If a check fails or an input is missing: stop and write BLOCKED in STATUS.md. Do not change the check.
Known traps: [what went wrong last time]
""")
ex+='<h2 id="a-status-file">A status file</h2>\n<p>Save it as <code>STATUS.md</code>. Ask the agent to update it after each real step. When a session ends or gets long, the next one starts from here instead of from memory.</p>\n'+pre("""
# Status ([date])

Goal: [one sentence]
Done when: [which files exist, and what they show]

## Done
- [step]: [output file]

## Open
- [step]: waiting on [what or whom]

## Numbers and where they came from
- [number]: [file], [how it was computed]

## Decisions
- [choice made]: [alternatives tried and dropped], decided [before / after] seeing results
""")
ex+='<h2 id="git">Git and GitHub habits</h2>\n<p>The lines I put in a new project\'s rules file so that the repository stays the record.</p>\n'+pre("""
## Git
- Commit after every real step, with a message that says what changed and why.
- Quote a commit hash only after the push has succeeded.
- Each session works in its own worktree and branch; never in a checkout another session is using.
- Never commit raw data, large outputs or secrets. Commit a pointer instead: path, size, checksum.
- Anything visual goes in docs/ and is published with GitHub Pages; check the live page, not the local file.
""")+'<p>Starting a project:</p>\n'+pre("""
git init my-project && cd my-project
mkdir docs && echo "first rough version" > docs/index.html
git add -A && git commit -m "Start: first rough page"
# create a private repository on github.com, then:
git remote add origin https://github.com/<you>/my-project.git
git push -u origin main
# Settings > Pages > Deploy from a branch > main /docs
""")+'<p>One worktree per agent session:</p>\n'+pre("""
git worktree add ../my-project-fix-figures -b fix-figures
cd ../my-project-fix-figures    # start the agent here
git worktree remove ../my-project-fix-figures   # when done; the branch stays
""")
ex+='<h2 id="skills">Skills</h2>\n<p>The checking procedures I use are packaged as a Claude Code plugin. In Claude Code, run these two lines:</p>\n'+pre('/plugin marketplace add ChenHsieh/agentic-research-toolkit\n/plugin install result-checks@agentic-research-toolkit')+'<p>It adds six skills: check a design for confounds, give a derived statistic a null, try to break a finished result, compare with a second method, trace a data accession to its paper, and the <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/setup/AGENT_PLAYBOOK.md">agent playbook</a>. About 1,100 tokens per session until one is used.</p>\n'
ex+='<h2 id="prompts">Prompts</h2>\n'
for t,p in [("Catch me up","Read STATUS.md and the last ten commits. What is done, what is still open, and what is waiting on someone?"),
("Before I trust this check","Run this check three ways, through the same script the real run uses: on an input built to have the error this check is for (such as shuffled labels), where it should say no; on a copy with only the header line, where it should say no; and on an input with a planted answer, made without the code being checked, where it should say yes. Show me the output each time and the line that calls the check. If it gets any of the three wrong, stop and tell me before changing anything."),
("Try to break this result","What are the three most likely ways this result could be an artifact? Check each one and show me the file for each check."),
("Rebuild from the Methods","In an empty folder, rebuild these results using only the Methods text and the raw data. If the text leaves something out, stop and tell me instead of guessing. Finish with a table of each number: expected, what you got, and whether it matched."),
("Read the papers","Read these papers and tell me which methods they treat as standard. Quote the paper for each claim, with the section. Tell me which papers you could not open."),
("Before an overnight run","It is tomorrow morning. This run produced a result that looks convincing but is wrong. List five ways that could have happened. For each, add the smallest check that would catch it, and run that check on a known-bad input now."),
("Review today's work","Another session worked on this today. Read its commits and output files, not its summary. What was actually done, and what is not supported?")]:
    ex+=f'<div class="prompt"><div class="ph">{t}</div><p>{e(p)}</p></div>\n'
page('examples.html','Examples: using an agent for research',ex,'A rules file, a brief, a status file, and the prompts I use.',COPY2)

se='''<h1>A 20-minute walkthrough</h1>
<p>If you want to try this on your own project, I am happy to spend 20 minutes with you on a video call. Friends and labmates first.</p>
<h2>What we do</h2>
<div class="steps">
<div><span class="min">5 min</span><b>Your project</b><p>What you work on, one task you would like help with, and how you would know that task worked.</p></div>
<div><span class="min">10 min</span><b>On your screen</b><p>You type; I watch. First write down what you think the files do and one output that would worry you. Then ask the agent the same thing, and find one thing in its answer that is wrong. Then try your task with approval on, and give its check an empty or shuffled input to see whether it says no.</p></div>
<div><span class="min">5 min</span><b>Before you go</b><p>Write your five-line rules file, with the mistake you found as its first entry. Then what to try on your own. Last, one thing that helped and one that confused you; I use those to fix this page.</p></div>
</div>
<p>You leave with a rules file for your project, one task you have already tried, and one check you have watched say no. What you will copy: the <a href="examples.html#a-rules-file">rules file</a>, the <a href="examples.html#a-status-file">status file</a>, and the <a href="examples.html#prompts">prompts</a>.</p>
<h2>What to bring</h2>
<p>Claude Code installed and logged in. It needs a paid Claude plan or API access; the free plan does not include it. If installing fails, say so when you ask and we use the 20 minutes for that. A folder you understand: an analysis, a pipeline, or a set of notes. One real task.</p>
<p>Leave out data that cannot leave your institution: whatever the agent reads is sent to the company that runs the model. We look at code and file names, not protected data.</p>
<h2>How to ask</h2>
<p>If we share a Slack workspace, message me there. Otherwise open an issue on the <a href="https://github.com/ChenHsieh/agentic-research-toolkit/issues">repository</a>; issues are public, so keep the project line general. Three lines is enough:</p>
<div class="prompt"><div class="ph">Request</div><p>I work on [project, one line]. I would like to try [one task]. I have Claude Code installed / need help installing it.</p></div>
<p>I reply when I can. No obligation either way, and nothing to prepare beyond the three things above.</p>
<h2>Before the call</h2>
<p>Read the <a href="index.html">essay</a> (about 15 minutes). Note which of the seven failure patterns you think you would have missed. We can start there.</p>
'''
page('session.html','A 20-minute walkthrough',se,'Go through this on your own project with me in 20 minutes. You leave with a rules file for your project and one task already tried.',COPY2)
print('ok')

LAND='''<script src="https://cdn.jsdelivr.net/npm/d3@7"></script><script src="graph.js"></script><script>
drawDiagrams({land:{height:380,collide:true,axis:['you drive','it drives'],legend:[['you','coding agents'],['file','research assistants'],['agent','autonomous research systems'],['bad','idea-to-paper']],nodes:[
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
TRIED_LIST='<dl class="tried">\n<dt>Codex CLI <span class="small">read-only review of a figure helper I use</span></dt>\n<dd>Found four edge cases nobody had tested, such as values below 1e-10 printed as "0". One of its concrete claims was wrong when I ran the input: it said a value printed as "1e+09"; it printed "1000M". <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/codex.md">Notes</a></dd>\n<dt>Aider <span class="small">write tests from a plan, $0.0016</span></dt>\n<dd>Wrote working tests in one call. I then broke the code four ways on purpose and the tests caught all four. On the way, Python reused a stale compiled copy of the file and made a correct file look broken, a quiet failure of its own. <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/aider.md">Notes</a></dd>\n<dt>Paper2Agent <span class="small">my two manuscripts as tools Claude Code can query</span></dt>\n<dd>Its own checks still pass (61 of 61). It answers "how many genes, from which file, at which commit", and warns when an old number is still in circulation. Setup takes an afternoon per paper.</dd>\n<dt>PaperQA2 <span class="small">a question over 20 open-access papers on young genes</span></dt>\n<dd>Answered in three paragraphs with a citation on every sentence. Checking the citations found one overreach: "at most a third come from divergence" became "the majority are de novo", which the paper does not say. Its agent mode crashed on a version mismatch; the plain mode works. <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/paperqa.md">Notes</a></dd>\n<dt>Biomni <span class="small">look up and compare five tandem-duplicated Arabidopsis genes</span></dt>\n<dd>Wrote and ran its own database code; the table matched UniProt. Then it concluded one gene had "functionally diversified" because it had more GO terms, which mostly means it was studied more. Its install left out three packages. <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/biomni.md">Notes</a></dd>\n<dt>Virtual Lab <span class="small">four role-played experts plan how to show young genes are real, $0.01</span></dt>\n<dd>A sensible ranked plan in six minutes, close to what my chapter actually did. It also listed the two parent species of my hybrid as outgroups, which they are not, and used stock thresholds with no reason given. This tested the meeting only. <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/vlab.md">Notes</a></dd>\n<dt>zotero-skills <span class="small">let an agent search and edit a Zotero library</span></dt>\n<dd>I have no Zotero library on the cluster, so this was a read-only trial on a public group. Search worked and a write was correctly refused. Its status check reports "connected" whenever a key is set, without making a request; with a made-up key it said connected and the next call failed. The write paths, which are most of what it is for, are untested. <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/zotero-skills.md">Notes</a></dd>\n<dt>CellVoyager <span class="small">reanalyse a public single-cell dataset</span></dt>\n<dd>Did not run. Five attempts failed before any analysis: a stale package picked up from my home directory, then two parts of its code that need the same model named two different ways when everything goes through one gateway key. It expects OpenAI and Anthropic keys of its own. <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/cellvoyager.md">Notes</a></dd>\n<dt>Not run</dt>\n<dd>Gemini CLI (needs a Google login or key), Robin and Kosmos (need the paid Edison platform), AI co-scientist (not generally available), AI Scientist (machine-learning experiments on GPUs, not genomics). <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/not_run.md">Why</a></dd>\n</dl>'
def it(name,url,who,what):
    return f'<p><a href="{url}">{name}</a> <span class="small">({who})</span>. {what}</p>\n'
rd='''<h1>Reading</h1>
<p>Papers, tools and guides on agents for research, checked on 6 October 2026. Every link was opened at its source. Numbers are quoted from the source.</p>
<figure><div class="g" data-g="land"></div><figcaption>Left: you drive, the tool assists. Right: the system plans and runs the research itself. Placement is my reading of each paper. Hover for a summary; click to open the paper.</figcaption></figure>
<p>I ran the open-source ones on our cluster and checked every output: see <a href="tools.html">Tools tried</a>.</p>
<h2>Start here</h2>
'''
rd+=it("Building effective agents","https://www.anthropic.com/engineering/building-effective-agents","Anthropic, 2024","Start with one model call; add agent steps only when the simpler version measurably falls short.")
rd+=it("Best practices for Claude Code","https://code.claude.com/docs/en/best-practices","Anthropic docs","Give the agent a check it can run. Keep the rules file short. Use hooks for anything that must always happen.")
rd+=it("Designing agentic loops","https://simonwillison.net/2025/Sep/30/designing-agentic-loops/","Simon Willison, 2025","Run unattended agents only in a sandbox, with limited credentials, on problems with clear success criteria. His definition: \"An LLM agent runs tools in a loop to achieve a goal.\"")
rd+=it("rewrites.bio","https://rewrites.bio/","Seqera","Twelve principles for rewriting bioinformatics tools with AI: credit the original authors, match outputs exactly, say how AI was used, validate each small step against the original.")
rd+=it("AI for Auto-Research: Roadmap and User Guide","https://arxiv.org/abs/2605.18661","Kong et al., 2026","A map of AI use across the research cycle. Conclusion: more automation can hide failure modes rather than remove them.")
rd+='<h2>What the benchmarks say</h2>\n<p>On the agent setups these papers tested, end-to-end analysis stayed hard, and several point at choosing methods and interpreting results as the weak steps. They do not tell you which step will fail in your task.</p>\n'
rd+=it("BixBench","https://arxiv.org/abs/2503.00096","FutureHouse, 2025","About 300 open-answer bioinformatics questions, with repeated runs per analysis. The two models tested (GPT-4o and Claude 3.5 Sonnet) reached at most 17% on open answers.")
rd+=it("FlowBench","https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1","Kurjan and Cribbs, 2026","23 models. Choosing a toolchain from the biological goal alone: 44 to 57%. Agents often \"fix\" a failing run so it exits cleanly while the data stay invalid.")
rd+=it("BiomniBench","https://www.biorxiv.org/content/10.64898/2026.05.12.724604v1","Qu et al., 2026","Scores the agent's whole working trail against expert rubrics. The harness around the model moved scores more than a model generation did.")
rd+=it("ScienceAgentBench","https://arxiv.org/abs/2410.05080","Chen et al., 2024","102 tasks from 44 papers. Best agent solved 32.4%.")
rd+=it("LAB-Bench","https://arxiv.org/abs/2407.10362","Laurent et al., 2024","Over 2,400 questions on practical biology tasks: literature, databases, figures, sequences, protocols.")
rd+='<h2>Critiques</h2>\n'
rd+=it("I told ChatGPT to continue, and it went too far","https://www.nature.com/articles/d41586-026-02714-y","Ying Zhao, Nature career column, 2026","A researcher with her e-mail connected typed \"please continue\"; the chatbot e-mailed other researchers in her name and reported it afterwards. Her lesson: \"capability is not permission.\" Part of the article is behind a login.")
rd+=it("Hidden pitfalls of AI scientist systems","https://arxiv.org/abs/2509.08713","Luo, Kasirzadeh, Shah, 2025","Data leakage, metric misuse and post-hoc selection are often invisible in the final paper. Recommends requiring trace logs and code.")
rd+=it("Evaluating Sakana's AI Scientist","https://arxiv.org/abs/2502.14297","Beel, Kan, Baumgart, 2025","42% of experiments failed on coding errors; established ideas labelled as novel.")
rd+=it("AI scientists fail without strong implementation capability","https://arxiv.org/abs/2506.01372","Zhu et al., 2025","The bottleneck is running the checks, not generating ideas.")
rd+=it("The verification gap","https://arxiv.org/abs/2608.05179","Ding et al., 2026","Survey of 24 systems. Most release code; few release what is needed to check their claims.")
rd+=it("Phantom references","https://arxiv.org/abs/2607.00738","Russinovich et al., 2026","About one in twenty NeurIPS and USENIX Security papers has at least two likely fabricated references.")
rd+=it("Fabricated citations at NeurIPS 2025","https://gptzero.me/news/neurips/","GPTZero, 2026","100+ fabricated citations in 53 accepted papers.")
rd+='<h2>What it does to the person using it</h2>\n<p>The essay cites Bainbridge (1983) and Parasuraman and Riley (1997). These carry the same question into generative AI.</p>\n'
rd+=it("Ironies of generative AI","https://arxiv.org/abs/2402.11364","Simkute et al., 2024","Bainbridge's ironies applied to generative AI: \"a shift in users' roles from production to evaluation\", and \"a tendency for automation to make easy tasks easier and hard tasks harder\".")
rd+=it("How AI impacts skill formation","https://arxiv.org/abs/2601.20245","Shen and Tamkin, Anthropic, 2026","Randomized: 52 people learning a new Python library. With AI they scored 17% lower on a quiz of concepts, code reading and debugging, and were not significantly faster. The high scorers asked for explanations, alone or alongside generated code.")
rd+=it("The widening gap","https://arxiv.org/abs/2405.17739","Prather et al., ICER 2024","21 novice programmers observed while coding with AI tools. Those who already knew what code they meant to write went faster and ignored bad suggestions. Those who struggled overestimated how well they did and \"finished with an illusion of competence\". Students in an intro course, not researchers with agents.")
rd+=it("Endoscopist deskilling risk after exposure to AI in colonoscopy","https://doi.org/10.1016/S2468-1253(25)00133-5","Budzyń et al., Lancet Gastroenterology and Hepatology 2025","Observational, four centres in Poland. In colonoscopies done without AI, the adenoma detection rate fell from 28.4% to 22.4% in the three months after AI arrived. Other changes over those months could contribute.")
rd+=it("Artificial intelligence and illusions of understanding in scientific research","https://doi.org/10.1038/s41586-024-07146-0","Messeri and Crockett, Nature 2024","AI tools can leave scientists believing they understand more than they do: \"a phase of scientific enquiry in which we produce more but understand less\".")
rd+=it("We are changing our developer productivity experiment design","https://metr.org/blog/2026-02-24-uplift-update/","METR, 2026","The follow-up to the 2025 trial in the essay. With 57 developers and 800+ tasks the data gave \"an unreliable signal\", partly because developers who did not want to work without AI stayed out of the study. METR reads the new estimate as a lower bound on the speedup.")
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
rd+=it("ai-research-skills","https://github.com/WenyuChiou/ai-research-skills","Wenyu Chiou","Seventeen installable skills from literature search to manuscript, tied to Zotero, Obsidian and NotebookLM, with a dated verification record per skill and a written list of where automation must stop. Its author says it was tested by one person, in water resources. I have not run it.")
rd+=it("design-taste","https://github.com/madebymustafa/design-taste","Mustafa, 2026","Plain-text skills that stop an agent from producing the default AI look (purple gradients, centered hero, three cards, emoji icons), plus a pre-flight checklist to run before calling a page done. No service or account needed.")
rd+=it("AGENTS.md","https://agents.md/","Linux Foundation","One instructions file many agents read.")
rd+=it("Agent Skills","https://agentskills.io/","open standard","A folder with a SKILL.md; loaded only when a task matches.")
rd+='<p class="small">Not included: several 2026 preprints seen in search but not read. Affiliations for some arXiv entries are from the author groups, not the abstract pages. Full notes: <a href="https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/lit_round_2026-10.md">notes/lit_round_2026-10.md</a>.</p>\n'
page('reading.html','Reading: agents for research',rd,'Papers, tools, benchmarks and critiques on agents for research, checked October 2026.',LAND)

# ---- Tools tried page
N='https://github.com/ChenHsieh/agentic-research-toolkit/blob/main/notes/tools_on_sapelo2/'
tl='''<h1>Tools tried</h1>
<p>In October 2026 I set up the open-source research agents from the <a href="reading.html">Reading</a> list on our university cluster and gave each one task, mostly from my own work, then checked every output by hand. This page is the picture version. It is a small feasibility diary, not a ranking: each tool got one task that suited it, once, on one cheap model. A failure can belong to the tool, the model, the gateway or my task.</p>

<h2 id="plug">One key, many tools</h2>
<figure><div class="g" data-g="gateway"></div><figcaption>Most of these tools do not need their own account. They can all talk to one gateway (OpenRouter), which passes each request to whichever model you name. One key with a spending cap covered five tools; the whole day cost $0.49.</figcaption></figure>

<h2 id="score">What each one did</h2>
<table class="score">
<tr><th>Tool</th><th>Task</th><th>Setup</th><th>The work</th><th>The interpretation</th></tr>
<tr><td>Aider</td><td>Write tests from a plan</td><td class="ok">ready</td><td class="ok">tests caught 4 of 4 planted bugs</td><td class="na">none made</td></tr>
<tr><td>Codex CLI</td><td>Review a figure helper</td><td class="ok">ready</td><td class="ok">found untested edge cases</td><td class="bad">one stated output was wrong</td></tr>
<tr><td>Paper2Agent</td><td>Query my two manuscripts</td><td class="mid">an afternoon per paper</td><td class="ok">61 of 61 checks pass</td><td class="na">answers only from tables</td></tr>
<tr><td>PaperQA2</td><td>Question over 20 papers</td><td class="mid">agent mode crashed</td><td class="ok">every sentence cited</td><td class="bad">"at most a third" became "the majority"</td></tr>
<tr><td>Biomni</td><td>Compare 5 tandem genes</td><td class="mid">3 packages missing</td><td class="ok">table matched UniProt</td><td class="bad">"more GO terms" read as "diversified"</td></tr>
<tr><td>Virtual Lab</td><td>Plan how to test young genes</td><td class="ok">clean</td><td class="ok">sensible ranked plan</td><td class="bad">parent species called outgroups</td></tr>
<tr><td>zotero-skills</td><td>Read a public Zotero library</td><td class="ok">one minute</td><td class="ok">122 of its tests pass; read worked, write refused without a key</td><td class="bad">its status check says "connected" without connecting</td></tr>
<tr><td>CellVoyager</td><td>Reanalyse a public dataset</td><td class="bad">5 failed starts</td><td class="na">never ran</td><td class="na">never ran</td></tr>
</table>
<p>Read the last column. In these eight small trials, the errors I found were mostly in the sentence after a correct-looking output. That is a reason to check both the table and the claim. It is not a measurement of what agents are good at: one task is not a rate, and I chose tasks I could check.</p>
<p class="small">What each row did not test. PaperQA2: only its manual local-papers path, not its literature-search agent. Biomni: without its data lake, so as a code-writing database assistant, not its curated tools. Virtual Lab: the meeting, not the design-and-validation workflow in its paper. Paper2Agent: its checks confirm it reproduces my tables, not that a new question is answered correctly. CellVoyager: a setup failure through one gateway key, not a verdict on its analyses.</p>

<h2 id="map">Who drives, and can you check it</h2>
<figure><div class="g" data-g="map2"></div><figcaption>Left to right: how much the tool decides on its own. Bottom to top: how easy its output is to check (rerun the code, look up the passage, or take its word). This is a sketch, not a measurement, and the placement is my reading. "Easy to check" means there is an affordable check for that kind of output; a notebook you can rerun can still be hard to judge. The corner to be careful in is the bottom right.</figcaption></figure>

<h2 id="jev">A router that picks the model for you</h2>
<figure><div class="g" data-g="jev"></div><figcaption>Jev Router (on OpenRouter) chooses a model per request. Each cost is shown against my fixed model (DeepSeek V4 Pro) on the same prompt. Two examples, not an evaluation: they show routing can save money on an easy request and cost more on a harder one. I have not measured its average cost, answer quality or stability.</figcaption></figure>

<h2 id="fail">Why one tool never ran</h2>
<figure><div class="g" data-g="cvfail"></div><figcaption>CellVoyager sends the model name down two code paths. Through a gateway, each path needs the name written differently, so one of them always fails. It expects its own OpenAI and Anthropic keys.</figcaption></figure>

<h2 id="notes">Notes for each tool</h2>
'''+TRIED_LIST
TOOLS_JS='''<script src="https://cdn.jsdelivr.net/npm/d3@7"></script><script src="graph.js"></script><script>
drawDiagrams({
gateway:{height:330,narrow:{height:520,pos:{a:[.25,.05],p:[.75,.05],b:[.25,.15],v:[.75,.15],c:[.5,.25],or:[.5,.45],jr:[.5,.62],m1:[.2,.82],m2:[.5,.82],m3:[.8,.82],m4:[.5,.95]}},
 groups:[{id:'gt',label:'tools on the cluster',members:['a','p','b','v','c']},{id:'gm',label:'models, billed per use',members:['m1','m2','m3','m4']}],
 nodes:[
 {id:'a',label:'Aider',kind:'you',x:.1,y:.14,info:'Works directly: model named openrouter/<model>.'},
 {id:'p',label:'PaperQA2',kind:'file',x:.1,y:.31,info:'Works directly through LiteLLM, same naming.'},
 {id:'b',label:'Biomni',kind:'file',x:.1,y:.48,info:'Works with its "Custom" source pointed at the gateway address.'},
 {id:'v',label:'Virtual Lab',kind:'agent',x:.1,y:.65,info:'Works by pointing its OpenAI settings at the gateway. Its price table only knows OpenAI models, so I added the price by hand.'},
 {id:'c',label:'CellVoyager',kind:'bad',x:.1,y:.84,info:'Reached the gateway but never ran: see the last diagram.'},
 {id:'or',label:'OpenRouter: one key, $200 cap',kind:'you',x:.47,y:.42,info:'<b>Gateway</b><br>One account, one key, a spending limit. It forwards each request to the model named in it and bills per use.'},
 {id:'jr',label:'Jev Router',kind:'muted',x:.47,y:.78,info:'Optional: a "model" that is really a router choosing a model per request.'},
 {id:'m1',label:'DeepSeek V4 Pro',kind:'agent',x:.86,y:.16,info:'The cheap model I used for every run: $0.21 in, $0.42 out per million tokens.'},
 {id:'m2',label:'Claude',kind:'agent',x:.86,y:.36,info:'Available through the same key at its own price.'},
 {id:'m3',label:'GPT',kind:'agent',x:.86,y:.56,info:'Same.'},
 {id:'m4',label:'Gemini',kind:'agent',x:.86,y:.76,info:'Same.'}],
 links:[{s:'gt',t:'or'},{s:'or',t:'gm'},{s:'or',t:'jr',dash:1},{s:'jr',t:'gm',dash:1,label:'picks one'}]},
map2:{height:430,axis:['you drive','it drives'],yaxis:['hard to check: take its word','easy to check: rerun it'],collide:true,
 legend:[['you','coding agents'],['file','research assistants'],['agent','autonomous research systems'],['bad','idea-to-paper']],
 nodes:[
 {id:'cc',label:'Claude Code',kind:'you',x:.17,y:.13,info:'Output is code and files you can rerun.'},
 {id:'cx',label:'Codex CLI',kind:'you',x:.36,y:.11,info:'Same. Its review claims are testable by running the input.'},
 {id:'ai',label:'Aider',kind:'you',x:.15,y:.26,info:'Every change is a git commit; pair it with a test.'},
 {id:'p2',label:'Paper2Agent',kind:'file',x:.34,y:.24,info:'Every number comes with a file, a commit and a hash.'},
 {id:'bm',label:'Biomni',kind:'file',x:.42,y:.42,info:'The table and code can be rerun; the paragraph explaining them cannot.'},
 {id:'pq',label:'PaperQA2',kind:'file',x:.32,y:.5,info:'Each sentence points to a passage you can look up.'},
 {id:'cv',label:'CellVoyager',kind:'agent',x:.58,y:.38,info:'Placed from its paper: it writes a notebook. It did not run here, so this position is a guess.'},
 {id:'ks',label:'Kosmos',kind:'agent',x:.82,y:.52,info:'Long reports with traceable claims; 79.4% of statements judged accurate in its paper. Not run here.'},
 {id:'rb',label:'Robin',kind:'agent',x:.62,y:.62,info:'Hypotheses with literature behind them; humans run the experiments. Not run here.'},
 {id:'vl',label:'Virtual Lab',kind:'agent',x:.5,y:.78,info:'A written plan from role-played experts. Nothing to rerun; you need to know the field to catch errors.'},
 {id:'co',label:'AI co-scientist',kind:'agent',x:.74,y:.7,info:'Ranked hypotheses. Not public.'},
 {id:'as',label:'AI Scientist',kind:'bad',x:.88,y:.82,info:'A finished paper. Independent test: 42% of experiments failed on coding errors. Not run here.'}],links:[]},
jev:{height:250,narrow:{height:420,pos:{e:[.5,.05],h:[.5,.17],j:[.5,.36],s:[.27,.56],g:[.73,.56],c1:[.27,.8],c2:[.73,.92]}},
 nodes:[
 {id:'e',label:'"rename this variable"',kind:'you',x:.14,y:.25,info:'A trivial request: most of what an agent sends looks like this.'},
 {id:'h',label:'"is this inference valid?"',kind:'you',x:.14,y:.75,info:'A request that needs reasoning.'},
 {id:'j',label:'Jev Router',kind:'muted',x:.45,y:.5,info:'Decides per request which model answers.'},
 {id:'s',label:'small model',kind:'agent',x:.7,y:.25,info:'It picked gpt-6-luna.'},
 {id:'g',label:'mid model',kind:'agent',x:.7,y:.75,info:'It picked gemini-3.8-flash.'},
 {id:'c1',label:'$0.000007 vs $0.000166',kind:'ok',x:.86,y:.08,info:'23 times cheaper than DeepSeek V4 Pro on the same prompt. Both answers correct.'},
 {id:'c2',label:'$0.00226 vs $0.00167',kind:'bad',x:.86,y:.93,info:'About a third more expensive than DeepSeek V4 Pro on the same prompt. Both answers correct.'}],
 links:[{s:'e',t:'j'},{s:'h',t:'j'},{s:'j',t:'s'},{s:'j',t:'g'},{s:'s',t:'c1'},{s:'g',t:'c2'}]},
cvfail:{height:260,narrow:{height:420,pos:{n1:[.5,.06],p1:[.5,.2],o1:[.5,.34],x1:[.5,.47],n2:[.5,.6],p2:[.5,.73],o2:[.5,.86],x2:[.5,.97]}},
 groups:[{id:'g1',label:'name written for the gateway',members:['n1','p1','o1','x1']},{id:'g2',label:'name written plainly',members:['n2','p2','o2','x2']}],
 nodes:[
 {id:'n1',label:'openrouter/deepseek/...',kind:'file',x:.14,y:.22,info:'The form LiteLLM wants for a gateway.'},
 {id:'p1',label:'OpenAI client',kind:'agent',x:.42,y:.22,info:'One code path sends the name unchanged.'},
 {id:'o1',label:'OpenRouter',kind:'you',x:.64,y:.22,info:'Does not know a model with that prefix.'},
 {id:'x1',label:'not a valid model ID',kind:'bad',x:.87,y:.22,info:'Attempts 3 and 4.'},
 {id:'n2',label:'deepseek/...',kind:'file',x:.14,y:.74,info:'The form the gateway itself wants.'},
 {id:'p2',label:'LiteLLM',kind:'agent',x:.42,y:.74,info:'The other code path reads "deepseek/" as "call DeepSeek directly".'},
 {id:'o2',label:'DeepSeek directly',kind:'muted',x:.64,y:.74,info:'Skips the gateway; I have no key there.'},
 {id:'x2',label:'authentication fails',kind:'bad',x:.87,y:.74,info:'Attempt 5.'}],
 links:[{s:'n1',t:'p1'},{s:'p1',t:'o1'},{s:'o1',t:'x1'},{s:'n2',t:'p2'},{s:'p2',t:'o2'},{s:'o2',t:'x2'}]}
});
</script>'''

page('tools.html','Tools tried: research agents on a university cluster',tl,'Eight research-agent tools set up on a cluster, one task each, every output checked.',TOOLS_JS)

# ---- keep the installable playbook skill in step with setup/AGENT_PLAYBOOK.md
_pb=open('setup/AGENT_PLAYBOOK.md').read()
open('skills/agent-playbook/SKILL.md','w').write("""---
name: agent-playbook
description: Rules for an agent doing research work. Use at the start of any analysis, job submission, reproduction or delegation, and again before reporting a result, or when unsure whether a result is done, wrong, or not yet measured.
---
Follow the rules below. This file is generated from setup/AGENT_PLAYBOOK.md; edit that file, not this one.

"""+_pb)
