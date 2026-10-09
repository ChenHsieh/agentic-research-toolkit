# Nine-persona review, 2026-10-09

148 proposals from nine reviewers, merged to 143. The usage limit stopped most verifiers, so most were not verified.

Applied (33): examples-1, examples-11, examples-2, index:failures-1, index:failures-9, index:harder-1, index:harder-5, index:long-1, index:modes-1, index:modes-6, index:opening-and-structure-1, index:opening-and-structure-2, index:principles-1, index:quiet-11, index:quiet-4, index:quiet-5, index:quiet-8, index:quiet-9, index:setup-1, index:start-1, index:start-2, playbook-1, playbook-2, playbook-3, playbook-4, readme-1, readme-2, readme-4, session-1, session-2, session-4, session-5, session-6

## Pending (priority 1-2, need source check before applying)

### index:long-2 [visual] p2 (designer)
The timeline comparing the conversation with the files on disk opens at step 1. It shows the label 'everything is still in the conversation' and five greyed boxes, so the figure's point only appears if the reader finds and drags the slider. The boxes respond to mouseover only. In graph.js timeline() they have no tabindex, no tap handler, no aria-label and no 'What each box means' list, unlike every graph() diagram. The slider is the only control a keyboard can reach. On a phone or with a screen reader, what happens at each of the six steps cannot be reached. The conversation row has no text labels at any width, and the file row loses its labels below 520 px.

Edit: In graph.js timeline(): set the range input's initial value to n-1, so the page loads showing "3 of 6 steps now only exist as a summary in the conversation; all 6 are on disk". Give each conversation and file rect tabindex=0, an aria-label built from d.talk or d.disk, and the same tap/Enter-to-pin .gpanel the graphs use. Append the same <details class="gkey"> list as the graphs (steps 1 to 6: conversation, on disk). On wide screens, print one-word labels in the conversation boxes (goal, exclusion, fix, numbers, rerun, summary), from a new short field in the diagrams.js session steps. New caption: <figcaption>By the sixth step, the first three exist in the conversation only as a summary. The files still hold all six. Drag the slider back to see the start.</figcaption>

Sources: https://worrydream.com/MagicInk/, https://mail.zcliu.cs.umd.edu/responsiveVis/responsive_vis_CHI20.pdf, https://distill.pub/2020/communicating-with-interactive-articles/

### index:long-3 [rewrite] p2 (rse)
The essay's principle that files, not the chat, are the record gets only its mechanism in this section: long conversations get summarized. The section doesn't tie it to the reproducibility rules many grad students already know. Rules 1 and 2 of Sandve et al. (2013) are 'for every result, keep track of how it was produced' and 'avoid manual data manipulation steps'. The agent-era version fits in one quotable sentence. No Sandve citation exists on any page yet; it could also go on reading.html.

Edit: <p>When a conversation gets long, older parts are summarized and details are lost. I keep a brief, a task list and a status file on disk, and commit after each step. At the end, a new session reads the files and commits and reports what was done. I use that report, not the original session's own summary.</p>

<p>The first two of Sandve and colleagues' <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285">Ten simple rules for reproducible computational research</a> (2013) are to keep track of how every result was produced and to avoid manual steps. A step done in the chat and never written to a file is the new manual step.</p>

Sources: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285

### index:tasks-1 [rewrite] p2 (essayist, designer)
Two reviewers (essayist, designer) proposed the same fix, merged here. The seven tasks are sentence fragments run together in one paragraph, which is hard to scan on a phone. The section also says what the agent does but not how I know the result was right, which is the essay's whole argument. Pairing each task with its check applies the thesis to the reader's own task list. Five of the seven checks are already on the site: the 'Finished, but empty' card (which file, how many rows, what range of values), the roles diagram tooltips (checks its own rendering only if told to; check that each quote exists), the rules-in-code paragraph (the figure-saving function), and the 'Rebuild from the Methods' prompt plus the clean-room caption (matches, does not, BLOCKED). The checks for status summaries and weekly updates are NOT stated anywhere on the site. The designer supplied wording for them and the essayist left blanks. The wording below must be confirmed or replaced by Chen before publishing; if there is no check, saying so is honest. The same applies to the intro's second sentence, which is a claim about Chen's own practice. Format: the designer proposed a two-column table reusing the .uma class plus a new phone media query in style.css. I chose a plain list because it needs no CSS and does not make a second copy of the Parasuraman table's look three sections later. The designer's wish to delete the roles diagram conflicts with the essayist keeping it, so it is a separate item (index:tasks-2).

Edit: <p>Each task comes with the check I use before I trust the result. A task I cannot check is one I do not hand over.</p>
<ul>
<li>Status summaries of a project from its files and git history. Each line points to a commit or file I can open.</li>
<li>End-to-end analyses, including writing, submitting and checking cluster jobs. Before the run I write down what done means: which file, how many rows, what range of values. Exit code 0 is not on that list.</li>
<li>Answering questions from a talk with data that already exists. Each answer names the file it came from.</li>
<li>Redrawing figures to a written set of rules. I look at the rendered figure; the agent looks at its own output only if told to. A saving function refuses figures that break the rules (<a href="#rules">below</a>).</li>
<li>Summaries of a lab's published methods. Each claim is quoted from the paper with its section, and I check that the quotes exist.</li>
<li>Rebuilding my results from the Methods text in an empty folder. Each number comes back as matched, not matched, or BLOCKED.</li>
<li>Weekly updates for my advisor. Each number in it points to a file.</li>
</ul>

Before applying: the checks on the first item (status summaries) and the last item (weekly updates), and the sentence 'A task I cannot check is one I do not hand over', have no source on the site. Keep them only if Chen confirms they describe what he does. Otherwise replace the check with what he actually does, or with 'No formal check yet.' If index:tasks-2 is also applied, open the intro paragraph with the two sentences that item moves out of the figure caption.

Sources: https://simonwillison.net/2025/Mar/11/using-llms-for-code/, https://github.com/archietse/malofiej-2016/raw/master/tse-malofiej-2016-slides.pdf, https://worrydream.com/MagicInk/

### index:setup-2 [rewrite] p2 (essayist, designer)
tmux, Slurm and Remote Control are named and never explained, and none of them is explained anywhere else on the site (grep finds only this paragraph). A reader who has never used Claude Code will not know that Remote Control is a product feature, and will not know that the session keeps running on the cluster while they answer from the phone. 'I answer most prompts' is also ambiguous: it can read as 'I type my prompts on the phone'. The designer read it as approval prompts and the essayist as the agents' questions. Chen should check which he means before applying this.

Edit: <p>I run it on the university cluster, where a scheduler (Slurm) hands computers to jobs from a queue. Each project gets its own session inside tmux, a program that keeps a session running after I disconnect, and I usually have several going at once on the strongest available model. I answer most of their questions and approval requests from my phone through Remote Control, a Claude Code feature that lets the Claude app reach a session still running on the cluster. From 2 September to 2 October I ran about 75 sessions on the cluster and about 10 on my laptop. I used Codex in 3 sessions.</p>

(Change 'questions and approval requests' to whichever is true.)

Sources: https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/

### index:setup-3 [visual] p2 (designer)
The caption contrasts chat with an agent, but the loop diagram draws only the agent, so the reader has to get the comparison from the caption. The two sentences that carry the argument sit only in tooltips: 'This is where it notices (or misses) that something went wrong' on Read output and 'The summary is its own account; the files are the evidence' on Result. On phones, graph.js line 26 blanks every link label when width is under 520 px, so 'goal' and 'you check' disappear too. In diagrams.js, loop is the only node graph without a narrow layout; modes, night, roles, rules and clean all have one. At 390 px, You (x .1) and Model (x .27) sit about 60 px apart, so the arrow between them is a stub. This diagram is for someone who has never used an agent, so it has to make its point without a tap.

Edit: New caption: <figcaption>In chat, the model hands you text and you run it. An agent reads, runs and fixes on its own until it decides it is done. What it hands back is its own account; the files are the evidence.</figcaption>

In diagrams.js loop:
(1) Add {id:'txt',label:'Text you run yourself',kind:'muted',faint:1,x:.27,y:.13,info:'<b>Chat</b><br>The model replies with text. You copy it, run it and read the error yourself.'}. Put it above Model, because Result already sits below it at (.27,.87). Add links {s:'model',t:'txt',label:'chat'} and {s:'txt',t:'you'}.
(2) Label err->res 'it decides it is done' and change res->you to 'you check the files'. Set keep:1 on both links.
(3) Add a narrow layout. Starting point, to be checked at 390 px: narrow:{height:420,pos:{txt:[.25,.07],you:[.12,.3],model:[.4,.3],read:[.75,.28],run:[.85,.55],edit:[.45,.55],err:[.62,.8],res:[.2,.92]}}.

In graph.js line 26, change the label text to .text(function(l){return narrow&&!l.keep?'':(l.label||'')}) so the kept labels survive on phones.

Keep the tooltips as an optional second layer. Render at 390 px and 1024 px in the headless browser to confirm that no label overlaps a node.

Sources: https://worrydream.com/MagicInk/, https://content.ieeevis.org/year/2022/paper_v-full-1024.html, https://www.vis4.net/blog/in-defense-of-interactive-graphics/

### index:opening-and-structure-3 [structure] p2 (humanfactors)
This conflicts with item 2 on one point only: where "Why this gets harder" goes. Apply this or item 2's placement of Harder, not both. Humanfactors would put the theory section at the very end, as a reflection for readers who get that far. Then every practical section (Long sessions, How much to let it run, Models) reaches the phone reader first. This fits the educator's own point that the theory "belongs to the second reading". The case for item 2's placement is that the table's Abuse row (unbounded jobs on a shared cluster) leads straight into How much to let it run. With Harder at the end, the essay closes on philosophy just before the five starting steps.

Edit: Everything else in item 2 stays (failure cards moved before #quiet, the changed sentence in #quiet). The only difference: paste the block from <h2 id="harder"> through </table> directly before <h2 id="start">, not before <h2 id="long">. Resulting order: Eight principles, Setup, Tasks, Seven ways it will go wrong, Why the failures are quiet, Rules in a file then rules in code, Long sessions, How much to let it run, Models, Why this gets harder not easier, Starting.

Sources: https://www.davidlewisphd.com/courses/EDD8121/readings/2006-Kirschner_et_al.pdf

### index:opening-and-structure-4 [add] p2 (educator)
The route line does not link to the starting steps, which are the most practical part of the essay for a first-week reader. The educator's draft said "six steps", but #start has five numbered steps.

Edit: <p class="route"><a href="#principles">Read the eight rules</a> · <a href="#start">Start in five steps</a> · <a href="examples.html">Copy the prompts and files</a> · <a href="session.html">Try it on your project with me (20 minutes)</a></p>
(If another edit adds or removes a numbered step in #start, change the number in this link too.)

Sources: none

### readme-5 [rewrite] p2 (essayist, bench)
setup/CLAUDE.md, which the README and the essay both link as the starter rules file, tells the agent to 'poll' background jobs. The essay says waiting is done 'Not by an agent polling', and it lists 'An agent polling the queue all night' under Goes badly. setup/CLAUDE.md has 13 em dashes, starting with its title line, and setup/README.md has 12. Those are the only em dashes left in anything the site links to. Some lines read as tool documentation or slogans rather than Chen's voice. 'Prefer dedicated tools over Bash ... cleaner UX' is about the interface, not about whether a result is right. 'Coding without a plan breaks more than it builds' is a slogan.

Edit: - **Background anything that outlives a couple of minutes.** Let the scheduler do the waiting (job dependencies), or run one background check that exits when the job leaves the queue. Do not poll in a loop, and do not sit in a foreground call waiting.

Also, in setup/CLAUDE.md and setup/README.md, replace every em dash with a colon, a comma or a full stop. Cut the "Prefer dedicated tools over Bash" bullet. In the plan-mode bullet, replace "Coding without a plan breaks more than it builds." with a plain instruction, such as "Write down which files will change and how each change will be checked."

Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### readme-6 [rewrite] p2 (bench)
The global install command in setup/README.md overwrites ~/.claude/CLAUDE.md without warning. A student who already has one loses it. This is the kind of silent damage the site warns about. The per-project command does the same to ./CLAUDE.md.

Edit: # This replaces any existing ~/.claude/CLAUDE.md. Keep a copy first (-n: never overwrite an earlier backup).
[ -e ~/.claude/CLAUDE.md ] && cp -n ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak
curl -L https://raw.githubusercontent.com/ChenHsieh/agentic-research-toolkit/main/setup/CLAUDE.md -o ~/.claude/CLAUDE.md

Do the same for the per-project command, which writes ./CLAUDE.md.

Sources: none

### session-3 [rewrite] p2 (bench, educator, critic)
The essay's call-to-action box makes the same promise as the walkthrough page. If session-2 changes the page, this box falls out of step with it. index.html is edited by hand, not generated.

Edit: In docs/index.html (the .cta box near the end), replace with:
In 20 minutes, on your screen: you leave with a five-line rules file for your project, one real task already tried, and one check you have watched fail.

Sources: none

### session-7 [rewrite] p2 (essayist, designer, philosopher, humanfactors, educator)
'Read the essay (10 minutes)' is too short. The rendered essay is about 3,100 words before the diagrams, roughly 15 minutes. The next sentence only uses the seven failure patterns, which are about 380 words. The page also contradicts itself: 'nothing to prepare beyond the three things above' comes just before a reading assignment. Five reviewers raised this. They gave different times for the failure section ('about five minutes', 'a few minutes', '5 minutes with the principles'). 'A few minutes' fits the word count.

Edit: In tools/build_pages.py (the `se` string), replace with:
<p>Optional: read the <a href="index.html#failures">seven failure patterns</a> (a few minutes; the whole essay takes about 15) and pick the one you think you would have missed. We can start there.</p>

Sources: none

### index:rules-1 [rewrite] p1 (bench)
'Given about three times as much change' means little to a biologist, and item 2 reads as abstract. Both have bench versions a student already fears: a mock treatment given the wrong dose, and a 'no phenotype' result from a knockdown nobody checked. One clause each makes the 4 September case readable without explaining the project. The wording 'matched on a counter' agrees with the existing line 130 ('matched on different measures') and with the source incident: a control matched on a sampler counter got about 3.4 times the dose.

Edit: 1. A control got about three times the dose of the condition it was meant to control, because the two were matched on a counter instead of on how much actually changed. Fixing it moved the main result from 0.21–0.39 to 0.60–0.78.<br>
2. A "no effect" result came from a condition in which almost nothing had actually changed. The bench version: reporting no phenotype from a knockdown that nobody checked had knocked anything down.<br>

Sources: none

### index:rules-2 [rewrite] p1 (humanfactors, critic)
Two reviewers (human factors, critic) proposed nearly the same change to the same sentence, using the same source, so they are merged here. This is the thesis paragraph ('rules that matter become code'), and its only support is one incident, which a skeptic can call n=1 or a sloppy afternoon. Automation research explains why a written rule fails and why something on the path works. The human-factors draft applied findings about human operators to the agent's failure. That is a category slip, because the research is about people overseeing automation. The critic's draft attaches the findings to the part of the incident that is about the human: I did not catch the defects either. The merged text follows the critic's framing. It keeps two pieces of the human-factors draft: the omission-error term (plain words first, term in parentheses) and the link to running several sessions at once, which the Setup section (line 47) already states. Both quotes were checked against the sources: the Parasuraman and Manzey PubMed abstract (PMID 21077562) says automation bias 'occurs in both naive and expert participants, cannot be prevented by training or instructions', and complacency 'occurs under conditions of multiple-task load'. Goddard et al. 2012 (PMC3240751) defines omission as 'failing to act because of not being prompted to do so'.

Edit: <p>The rules were in the file and were not applied, because nothing at the moment of the analysis pointed to them. I did not catch them either. Automation research expects this: people miss problems the system does not prompt them about (omission errors), experts as much as beginners, and a review found this "cannot be prevented by training or instructions" (<a href="https://doi.org/10.1177/0018720810376055">Parasuraman and Manzey 2010</a>; <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/">Goddard et al. 2012</a>). It is more likely when other tasks compete for attention, and I run several sessions at once. Another line in a rules file was not going to fix it. I moved the important ones into code that stops the work:</p>

Sources: https://doi.org/10.1177/0018720810376055, https://pubmed.ncbi.nlm.nih.gov/21077562/, https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/

### index:rules-3 [rewrite] p1 (sre)
The paragraph stops one step short. Finding the line that calls a check proves it is wired in. It does not prove that its 'no' reaches anyone. The five uncalled control functions are exactly this case: each was correct on its own and dead in the pipeline. Monitoring engineering tests the alarm path end to end, which is the essay's thesis applied to the checker itself. Two edits to the SRE draft. (a) I dropped its sentence 'A check that fails in a test file but is never reached in the run is still BLOCKED': the same paragraph already says 'A check that is never called is BLOCKED, not PASS'. (b) I tightened the Watchdog description. It was checked against the runbook, which says 'This alert is always firing' and 'If not firing then it should alert external systems'.

Edit: So the last step of writing a check is to find the line that calls it, then send a known-bad input through the real pipeline and watch the stop arrive where someone will read it. Monitoring software holds its own alarms to this standard: the Prometheus monitoring stack ships an alert that fires all the time on purpose, wired to an outside service that sends a notice when it goes quiet (<a href="https://runbooks.prometheus-operator.dev/runbooks/general/watchdog/">Watchdog runbook</a>).

Sources: https://runbooks.prometheus-operator.dev/runbooks/general/watchdog/, https://sre.google/sre-book/monitoring-distributed-systems/

### index:rules-4 [add] p2 (philosopher)
The section ends on one way a gate fails (nothing calls it). It misses the second: once an agent knows a gate, passing the gate becomes the goal. The essay already describes this for exit codes in the 'Why the failures are quiet' section ('A clean exit is the thing they can see, so it becomes the target'). This item extends that point to gates and points back to it, so it does not repeat it. The essay's own figure gate is the example: it requires a sample size, and it will pass a figure whose n counts the wrong unit (the 'The wrong unit' pattern). Strathern's sentence is the standard source, and it comes from a study of audit, which is what a growing set of gates amounts to. Without this, 'rules become code' reads as a finished solution. ANCHOR CONFLICT: the philosopher's draft inserted after 'So the last step of writing a check is to find the line that calls it.</p>', and index:rules-3 rewrites that sentence. I re-anchored the insertion to the next heading so both items can be applied. Source check: the Cambridge URL resolves to the article (the redirect adds www and /abs/). The quote is from p. 308, behind a paywall, and was not checked against the full text.

Edit: Insert this paragraph immediately before the heading (that is, after the paragraph that ends 'find the line that calls it'):

<p>A gate is also a measure, and an agent that knows it will aim at it, the way a clean exit became the target above. Marilyn Strathern's wording of Goodhart's law: "When a measure becomes a target, it ceases to be a good measure" (<a href="https://www.cambridge.org/core/journals/european-review/article/abs/improving-ratings-audit-in-the-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB">1997</a>). My figure gate requires a sample size; it will pass a figure whose n counts the wrong unit. So a gate gets the same treatment as any check: see it fail once, and now and then look at what it lets through, not only at what it stops.</p>

<h2 id="failures">Seven ways it will go wrong</h2>

Sources: https://www.cambridge.org/core/journals/european-review/article/abs/improving-ratings-audit-in-the-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB

### index:principles-2 [rewrite] p1 (rse)
The principles read as if they were invented for agents. Several of them are standard research-computing teaching that many grad students have already met in a Software Carpentry workshop or a PLOS quick guide. The credit line names only rewrites.bio. FriendsDontLetFriends credits its inspirations. Doing the same here keeps the claim modest, gives readers the long canonical versions, and answers the research software engineer who would otherwise say 'this is just Software Carpentry'. Nothing on the site cites these sources yet. I checked the reviewer's wording against the lesson. The lesson does not say 'so that you see it fail'. It gives confirmation bias as the reason to write tests first. Both quotes below appear verbatim in the lesson. I also changed 'None of these are new' to 'Most', because principle 1 is not in those sources.

Edit: <p class="small">Most of these are not new. The Software Carpentry lesson on <a href="https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html">defensive programming</a> has you write the tests before the function they check, because tests written afterwards tend "to show that their code is correct, rather than to find errors". Its rule is "turn bugs into assertions or tests". Keeping the record in files comes from Noble's <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424">guide to organizing computational biology projects</a> (2009) and <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510">Good enough practices in scientific computing</a> (Wilson et al. 2017). What changed is how fast an agent produces work that needs them. The numbered form is borrowed from <a href="https://rewrites.bio/">rewrites.bio</a> (Seqera), principles for rewriting bioinformatics tools with AI. Its line "Fast code is now cheap. Scientific insight, validation, and trust are not" is the same idea from the software side.</p>

Sources: https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510, https://rewrites.bio/

### index:principles-3 [rewrite] p1 (critic)
CONFLICTS with items 4 and 5. All three change principle 8 in different ways: this one replaces it, item 4 cuts it, item 5 keeps it with a caveat. Pick one.

The case for this one: principle 8 is the only principle about what to buy rather than how to check. It is unsourced ('In research that is most places'), and it cuts against the thesis. METR saw recent frontier models get higher scores 'by modifying the tests or scoring code'. On one RE-Bench task, o3 reward-hacked 'in every single trajectory'. Across HCAST tasks it was 0.7% of runs. METR's stated impression, not a measurement, is that o3 did this 'substantially more often than previous ones'. I corrected the reviewer's 'on some tasks' to 'one task'. So the strongest model is also the best at getting past a weak check. To a skeptical reader, the current line sounds like an upsell. The principle the site needs, and never states, is this one. The Why link to #quiet works now: the FlowBench paragraph there already says agents make a failing run exit cleanly while the data stay invalid. The separately proposed METR addition to #quiet would strengthen it but is not required.

Items 3 and 4 agree that the model advice belongs in #models, not in the list. One way to reconcile all three: take this principle, move the 'being wrong is expensive' clause into #models (the #models sentence from item 4), and add the Bainbridge caveat there (item 10).

Edit: <li><b>Keep the check out of the agent's reach.</b> A check it can edit is a check it can make pass. <a href="#quiet">Why</a></li>

Leave the Models section as it is, or apply the #models sentence from item 4. Either way the strongest-model choice stays there, presented as my own practice.

Sources: https://metr.org/blog/2025-06-05-recent-reward-hacking/

### index:principles-4 [cut] p2 (essayist)
CONFLICTS with items 3 and 5 (same line). Seven of the eight principles are about checking and keeping records. The eighth is a purchasing decision. It sits awkwardly next to 'Doing is cheap now', and it depends on the budget the Setup section warns readers not to generalise from ('Some of what I get done is the budget, not the method'). Seven items are easier to remember than eight, and seven matches the seven failure patterns. This item differs from item 3 only on whether the list keeps a replacement eighth principle. The #models sentence below works with either item.

Edit: Delete this item.
Change the heading "Eight principles" to "Seven principles". For the route link, see item 6 and use "seven".
In #models, replace "I use the strongest model for design, interpretation and review." with "In research, being wrong is expensive almost everywhere, so I use the strongest model for design, interpretation and review."

Sources: https://craigmod.com/journal/subcompact_publishing/, https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/

### index:principles-5 [rewrite] p2 (humanfactors)
CONFLICTS with items 3 and 4 (same line). If principle 8 stays, then as written it points the wrong way from a human-factors view. A stronger model is right more often, and people stop monitoring automation that has been working well. Bainbridge 1983 says so directly (verified in the PDF: 'the operator will not monitor the automatics effectively if they have been operating acceptably for a long period'). Goddard et al. note complacency is worst with automation deemed reliable. Ending the list with 'use the strongest model' and no caveat invites the over-trust the rest of the page warns against. This item's Why link relies on item 10 adding the Bainbridge sentence to #models.

Edit: <li><b>Use the strongest model where being wrong is expensive, and check it as hard as a weak one.</b> People stop watching automation that is usually right. <a href="#models">Why</a></li>

Sources: https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf, https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/, https://csel.eng.ohio-state.edu/productions/intel/research/trust/Lee%20%26%20See%20Trust%20Review.pdf

### index:principles-6 [fix] p2 (essayist, humanfactors)
The route link says 'rules', but the heading says 'principles'. 'Rules' already names the rules file (CLAUDE.md), the 'Rules in a file, then rules in code' section and the agent playbook. A reader who taps 'rules' expects one of those. Two reviewers raised this separately. Use one word.

Edit: <a href="#principles">Read the eight principles</a>
(If item 4 is applied, use "Read the seven principles".)

Sources: none

### index:principles-7 [structure] p2 (designer)
Principles 3 and 7 link to the top of a seven-card section, so the reader has to find the matching case. Tufte warns about evidence that sits one level below a bullet. The cards are also unnumbered, but session.html tells the reader to 'Note which of the seven failure patterns you think you would have missed'. Numbers let a labmate say 'that's case 4'. On principle 5: #rules holds the measured example (48 items in 6 groups, +0.45 pooled and -0.11 within groups), while card 3 gives the general pattern. Linking card 3 matches principles 3 and 7, but keeping #rules points at the actual numbers. Either works; choose one.

Edit: Number the seven card headings and give each card an id: <article class="pat" id="f-empty"> with <h3>1. The empty control</h3>; then f-exit (2. Finished, but empty), f-unit (3. The wrong unit), f-guess (4. The silent guess), f-stale (5. Checks that compare a thing to itself), f-crash (6. Lost at the last step), f-shared (7. Two agents, one folder).
Point each principle at its own case. This line becomes <li><b>Empty is not measured.</b> A control with no values is not a pass. <a href="#f-empty">Case 1</a></li>. Principle 7 links <a href="#f-guess">Case 4</a>. Principle 5 either links <a href="#f-unit">Case 3</a> or keeps #rules (see problem). The other principles keep their current links.

Sources: https://www.edwardtufte.com/notebook/powerpoint-does-rocket-science-and-better-techniques-for-technical-reports/, https://github.com/cxli233/FriendsDontLetFriends

### index:principles-8 [rewrite] p2 (essayist)
BLOCKED appears in principle 7 before anything on the page explains it. Its first explanation is in the 'clean' diagram's tooltip ('Cannot be computed from the text'), and the #rules section later uses it in a second sense (a check nothing calls). Glossing it here, in the words the diagram already uses, keeps the list readable on its own. This edit and item 7's link change both touch principle 7; they combine without conflict.

Edit: A gap is marked BLOCKED (cannot be computed from what is written), never guessed.

Sources: none

### index:principles-9 [add] p2 (humanfactors)
'Review from the files, not the summary' appears four times in the essay: the loop diagram, the Misuse row ('Treating the exit code or the agent's own summary as the result'), Long sessions ('I use that report, not the original session's own summary') and the morning-review paragraph. It is not a principle, so a reader who only reads the list misses it. It belongs with principle 6.

Edit: <li><b>Files are the record, not the chat.</b> Brief, task list, status, commit. Review from those, not from the agent's summary. <a href="#long">Why</a></li>

Sources: none

### index:start-3 [cut] p2 (essayist, designer, bench)
The "More" section repeats the nav bar, the route line at the top, and the walkthrough box directly above it, and it adds two extra entries to the contents list. It is also wrong: it says the Prompts & files page has "a brief", but that page has a rules file, a status file and prompts, and no brief (checked with grep).

Edit: Delete the <h2>More</h2> heading and its paragraph. Leave the walkthrough box above it and the Files section below it.

Sources: none

### index:start-4 [rewrite] p2 (educator, designer)
Step 1 does not say that Claude Code needs a paid Claude plan or API credits. A grad student who installs it on a free account hits a wall at step 1. It also does not link to the install page.

Edit: <p>1. Install <a href="https://code.claude.com/docs/en/setup">Claude Code</a> (it needs a paid Claude plan or API credits). Open it in a folder whose contents you already know.<br>

Sources: https://code.claude.com/docs/en/setup, https://code.claude.com/docs/en/overview

### index:start-5 [rewrite] p2 (educator, designer)
Step 4 has the reader write a CLAUDE.md from a blank page, although a five-line template with bracketed blanks is one click away on the Prompts page. Teaching Tech Together: "novices should never start doing exercises with a blank page or screen". The thesis (make every check fail once) also has no first-day action that works in any field. The essay's own demo already shows the empty-file case ("Empty file: the exit code still passes. The row count catches it."), so a concrete version of that exercise fits here. This item adds a new step 5, so index:start-1 becomes step 6. Together with index:start-6, the list grows from five steps to seven. If that is too long, apply only one of the two additions. This step overlaps the second sentence of index:start-1, which can be dropped if this is applied.

Edit: 4. Copy the <a href="examples.html#a-rules-file">five-line rules file</a> into CLAUDE.md and fill in the brackets. Add a line after each mistake.<br>
5. Make one check fail. Copy an input with only its header line (<code>head -n 1 input.tsv &gt; empty.tsv</code>), run your first step on it, and see whether anything says no. If nothing does, that is your first rule.<br>

Sources: https://teachtogether.tech/en/index.html

### index:start-6 [add] p1 (critic)
The roles caption says "Deciding what to ask, and whether the answer is right, stays with you", but nothing tells a student how to build that judgement when the agent does the work that used to build it. A randomized trial addresses this directly. I checked it on the arXiv HTML. "In our main study, 52 participants completed the task, 26 for each of the control and treatment groups." The AI group scored lower, "a 17% score difference" on a 27-point quiz of conceptual understanding, code reading and debugging. Participants who "only asked conceptual questions" and resolved their own errors were in the high-scoring clusters (65-86%). Participants who "relied on AI to debug or verify their code" were in the low-scoring clusters (24-39%). The paper is not cited anywhere on the site yet. The proposer also described the authors as Anthropic researchers. That is not stated on the abstract page, so it is left out of the edit; check it before adding it. Apply this after index:start-1 as a new last step, and renumber if index:start-5 is also applied.

Edit: Insert as a new last step after the (rewritten) check step, before the closing </p>:
<br>
6. For a method you are still learning, do not let it write the code. Ask it how things work, and fix your own errors. In a randomized trial, 52 people learned a new programming library; the group with AI help scored lower on a quiz of understanding, code reading and debugging (a 17% difference). Those who asked only conceptual questions and fixed their own errors were among the highest scorers, and those who had the AI debug or check their code among the lowest (<a href="https://arxiv.org/abs/2601.20245">Shen and Tamkin 2026</a>).

Sources: https://arxiv.org/abs/2601.20245, https://arxiv.org/html/2601.20245

### index:start-7 [rewrite] p2 (critic)
The credit line says "every number was checked against the file it came from" but does not say how. By the site's own thesis, that is a check nobody has seen fail: a description, not a test. It also does not say which parts the agent drafted. Only Chen can supply those facts, so the brackets below must be filled from what actually happened, not by an agent.

Edit: Written with Claude Code from my own session logs and notes. The agent drafted [which sections]; I rewrote [which sections]. I checked each number against the file it came from[, and tested that by planting one wrong number, which was caught]. Mistakes are mine.
(If the number check was never tested with a planted error, say so instead: "I checked each number against the file it came from; I have not tested that check.")

Sources: https://dokk.org/library/dangers_stochastic_parrots_2021

### index:start-8 [rewrite] p2 (rse, critic)
The Files link sends readers to setup/CLAUDE.md, and that file contradicts the essay. Line 31 says "Background anything that outlives a couple of minutes, then poll it". The essay (#long) says waiting is done by the scheduler or one background check, "Not by an agent polling", and lists "An agent polling the queue all night" under "Goes badly". The file also has em dashes on 13 lines, tool-internal names (TaskCreate, TaskUpdate), and a "Cowork state" section that points to a tracker path (docs/cowork/Project_Tracker.md) the reader does not have. This edits setup/CLAUDE.md, not index.html. The two proposals conflict. One (rse) fixes the file in place, as below. The other (critic) cuts the file down to the rules Chen actually uses, in the site's voice, or relabels the link so the file does not stand in for his own practice. index:start-2 already relabels it as "a longer general rules file". The choice is Chen's.

Edit: **Background anything that outlives a couple of minutes.** Wait on it with a scheduler dependency, or one background check that ends when the job leaves the queue. Do not poll it from the conversation.
Also in setup/CLAUDE.md: replace each em dash with a colon or a full stop; replace "`TaskCreate` at the start, `TaskUpdate` as work progresses" with "Write the task list down at the start and update it as work progresses"; delete the "## Cowork state" section.

Sources: none

### site-wide-visual-and-navigation-1 [visual] p1 (rse)
Dark mode is broken where the content is. Many phones default to dark mode. In headless Chromium at 390 px with prefers-color-scheme: dark, the panel that opens when you tap a diagram box (.gpanel, #333 on #151513) has a contrast ratio of 1.45:1, and its text cannot be read in the screenshot. Other low ratios: the explorable's input buttons (#444, 1.88:1); the 'Pick an input' line and the mini-illustration labels (#555, 2.45:1); the legend line under the Reading map and the copy buttons (#666, 3.18:1); and every dark-red label ('YOU WILL SEE', the use/misuse table headers, #8a2c2c, 2.16:1). WCAG asks for 4.5:1 for text. I recomputed these ratios from the CSS. The minis set text colour inline (style fill #555) and stroke with #333, so the existing dark rule .glabel{fill:#aaa} cannot override them.

Edit: In docs/style.css, replace that line with: @media (prefers-color-scheme:dark){.gtip{background:#222;color:#eee;border-color:#444}.glabel{fill:#aaa}.gpanel{color:#ddd}.ex-q,.ex-inputs button,.gkey,.gnote,.route,.prompt .ph,.steps p,.ex-grid th,figcaption,p.small,.small,button.copy{color:#b5b0a6}.lbl,.ex-grid td.n,.uma th,.steps .min,.ex-inputs button.on{color:#e39a8a;border-color:#e39a8a}.ex-grid td.p{color:#7fbf95}}. Ratios on #151513: #ddd 13.5:1, #b5b0a6 8.5:1, #e39a8a 8.1:1, #7fbf95 8.5:1. The proposal also had .cta a:hover{color:#fff}. That is dropped because the light-mode rule already wins on specificity. In docs/minis.js, change t() so it sets fill inline only when o.c is passed, and leave default labels to the .glabel class. Remove the c:'#666' calls. Draw the INK strokes with currentColor. Keep RED for the one word per mini that names the defect. Then render index.html in dark mode at 390 px, tap one diagram box, and confirm the panel text and the mini labels are readable before shipping. The light theme does not change.

Sources: none

### site-wide-visual-and-navigation-2 [structure] p2 (essayist, humanfactors)
The principles' 'Case' links land at the top of a section, not on the case. Principles 3 (empty control) and 7 (rebuild from the Methods) both go to the top of the seven-card #failures section. Principle 5 (name the unit) goes to #rules, where the unit case appears only as item 3 of a numbered list, while the matching card, The wrong unit, is in #failures. On a phone the reader has to scroll and search, which costs more than most will spend on a link they followed to check a claim. The walkthrough page mentions 'the seven failure patterns' without linking to them. Two reviewers proposed this. They differed only in the last card's id ('two-agents' or 'shared-folder'); 'two-agents' is used because it matches the card heading.

Edit: <li><b>Name the unit before you count.</b> Grouped units are reported within groups. <a href="#wrong-unit">Case</a></li>

Give each failure card an id that matches its heading: <article class="pat" id="empty-control">, id="finished-empty", id="wrong-unit", id="silent-guess", id="self-compare", id="last-step", id="two-agents". Point principle 3's Case link (after 'A control with no values is not a pass.') at #empty-control, and principle 7's (after 'Gaps are marked BLOCKED, never guessed.') at #silent-guess. Add .pat[id]{scroll-margin-top:1.2em} next to the existing h2[id] rule, so a card heading is not hidden under the progress bar when someone jumps to it. session.html is generated, so in tools/build_pages.py link 'seven failure patterns' to index.html#failures.

Sources: none

### site-wide-visual-and-navigation-4 [visual] p2 (designer)
The diagram colours do not keep one meaning each. In the rebuild diagram, BLOCKED uses the 'you' dark red (#8a2c2c) next to FAIL in the 'bad' red (#b03a2e). The two reds have a contrast ratio of 1.41:1 to each other, which is hard to tell apart and worst for red-green colour-blind readers. In the rules diagram, 'Stops with a reason' is the same red as 'Defect ships', although stopping is the outcome the section argues for. 'Check (code)' is dark red there and green in the overnight diagram. On Reading, AI Scientist gets the defect red. No essay diagram says what the colours mean, although graph.js already draws a legend from spec.legend (the Reading map uses it). The house style asks for one dark red accent.

Edit: In docs/graph.js, keep the palette but give each kind one meaning on every page: you = dark red (the accent); agent = slate; file = olive; bad = the brighter red, used only for a result that is wrong; ok = green, used only for something that has passed. Add 'check', drawn as an outlined box with no fill and stroke currentColor so it stays visible in dark mode. Add 'notmeasured', a dashed grey outline, the same mark the empty-control mini uses for '0 rows'. Apply these in docs/diagrams.js: clean 'BLOCKED' you -> notmeasured; rules 'Stops with a reason' bad -> muted; rules 'Check (code)' you -> check; night 'Check' (c1, c2) ok -> check. reading.html is generated, so make the Reading change in the LAND string in tools/build_pages.py: change 'AI Scientist' from bad to agent, remove the ['bad','idea-to-paper'] legend entry, and keep 'idea to paper' in its info text. Add a key once, where the colours first appear together (the rules diagram), using the existing legend option, e.g. legend:[['you','you'],['agent','the agent'],['file','files'],['ok','passed'],['bad','wrong result']], plus a dashed swatch for 'not measured' on the clean diagram. If a sentence is preferred: <p class="small">Red boxes are you, blue boxes the agent, olive boxes files. A dashed grey box was not measured.</p> Do not put it under the first diagram (loop), which shows only you and agent boxes.

Sources: https://distill.pub/2020/communicating-with-interactive-articles/

### site-wide-visual-and-navigation-5 [visual] p2 (bench)
The mini for 'Checks that compare a thing to itself' says 'your site' and 'the checks compare the site with itself'. The card text is about something you built from another project's results, and readers build analyses, not websites, so the picture and the card disagree.

Edit: t(s,200,32,'your copy',{a:'middle'})

In the same stale mini, change the red bottom line 'the checks compare the site with itself' to 'checks compare your copy with itself'. That is 36 characters, against 39 now, so it stays inside the 260 px box. Render it at 390 px and check that nothing clips at the edges.

Sources: none

### site-wide-visual-and-navigation-7 [structure] p2 (sre)
Every diagram, all seven failure pictures and the Reading map load d3 from cdn.jsdelivr.net at a floating version, 'd3@7'. On 9 October, jsDelivr resolved that to 7.9.0 (x-jsd-version: 7.9.0). If the CDN is blocked on a campus or conference network, or a later 7.x release changes behaviour, every picture goes blank with no message. The site's own starter file says '"Latest" is not a version.'

Edit: <script src="vendor/d3-7.9.0.min.js"></script>

Save d3 7.9.0 as docs/vendor/d3-7.9.0.min.js and keep its header comment, which carries the ISC copyright notice. Change both script tags: docs/index.html (line 241), and the LAND string in tools/build_pages.py, which writes reading.html. Then rebuild. Make it fail once: load index.html in the headless browser with cdn.jsdelivr.net blocked, before the change (pictures blank) and after (pictures drawn).

Sources: none

### site-wide-visual-and-navigation-8 [structure] p2 (sre)
The site's house rules are prose, not checks, which is the failure the essay describes. The HTML pages and the playbook are clean today. But files the essay links to contain em dashes: setup/CLAUDE.md has 13, setup/README.md 12 and skills/README.md 9 (recounted). The Reading page's 'Every link was opened at its source' describes 6 October and is not a check that runs. Today the live pages match the local files, every internal anchor resolves, and the generator reproduces the three generated pages. Nothing would tell Chen when any of that stops being true.

Edit: Add tools/check_site.py and run it before every push, from a git pre-push hook (no Actions). Keep the hook in a tracked folder and set core.hooksPath, because .git/hooks is not committed. It should fail when: any file in docs/, setup/ or skills/README.md contains an em dash; an internal link (#id or page.html#id) has no matching id; or a fresh build_pages.py run differs from docs/. tools/page.py writes to 'docs/' relative to the working directory, so add an output-folder argument or run the build from a temporary copy. Outbound links: some publishers refuse scripted requests, so report non-200 links as a separate list, or run that part weekly, instead of blocking the push. Make it fail once: keep a small fixture page with one em dash and one dead anchor, and confirm the script flags both before trusting it.

Sources: https://sre.google/sre-book/monitoring-distributed-systems/, https://runbooks.prometheus-operator.dev/runbooks/general/watchdog/

### index:harder-2 [cut] p2 (essayist)
CONFLICTS with index:harder-1. The rest of the table either restates principle 1 and the Misuse case or is covered elsewhere (Abuse by the shared-cluster paragraph in How much to let it run), and it is the only citation on the page with no link. The table carries one new idea, disuse, and that fits in one sentence. The designer, bench and humanfactors reviewers want to keep the table instead. The essayist's sentence repeated the contested "slower, and no safer" (see index:harder-1), so the replacement below uses the critic's framing. If index:harder-6 removes the Merton paragraph, put the sentence at the end of the Gelman and Loken paragraph. The essayist also suggested moving the Use idea into the Tasks intro; that is optional.

Edit: Delete the paragraph and the table. Add at the end of the Merton paragraph (or of the Gelman and Loken paragraph if index:harder-6 is applied): "The opposite mistake is refusing it after one bad result, even for routine runs a tested check could cover; <a href="https://doi.org/10.1518/001872097778543886">Parasuraman and Riley (1997)</a> call that disuse. Learning a method by hand is not that."

Sources: https://www.newyorker.com/magazine/2015/09/14/omission, https://doi.org/10.1518/001872097778543886

### index:harder-3 [cut] p2 (essayist, designer, bench, rse)
Four reviewers propose the same cut. The section cites six authorities in about 450 words, and on a phone it reads like a literature tour. The Popper sentence is second-hand (an encyclopedia summary, from a 2007 archive) and generic. The opener "Philosophy of science has words for..." reads as a tour. And the sentence repeats what Feynman and the positive control already said one section earlier. Mayo's severe test makes the same point more precisely and tells you what to do. The replacement wording reuses the site's own phrase "could have said no" from Why the failures are quiet. Other openers proposed were "Deborah Mayo's name for a good check is a severe test:" and "Philosophy of science has a name for a good check. Deborah Mayo calls it a severe test:". index:harder-4 rewrites the whole paragraph and also drops Popper. If -4 is applied, this item is not needed.

Edit: <p>Deborah Mayo's name for a check that could have said no is a severe test:

Sources: https://www.newyorker.com/magazine/2015/09/14/omission, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### index:harder-4 [rewrite] p1 (philosopher, rse)
Three problems. (1) The Popper sentence adds a famous name and no tool; see index:harder-3. (2) The Mayo and Spanos 2006 paraphrase is looser than Mayo's own 2018 wording. That wording states the site's main line almost word for word, and her first worked example is a genomics case biology readers will recognise. I checked both against the publisher proofs: the quote is on p. 5, the Duke example runs pp. 5-6, "no better than chance" is Mayo's phrase, and the DOI resolves to the 2018 Cambridge book. (3) The last sentence overclaims. A planted signal is a severe test of the pipeline, and only for the error that was planted, not of the biological result. Collins's experimenters' regress is the standard objection, and Franklin's answer gives a practical rule: the planted signal has to be made independently of the code being tested. Placement: this paragraph is the theory behind the 'check that cannot fail' demo, which sits two sections up, and it does not support a heading about things getting harder. CONFLICT on length: the essayist and designer want this section shorter, and this paragraph is about twice as long as the current one. Minimum version if the move and the Duke example are not taken: apply index:harder-3 and change only the last two sentences, as given at the end of the edit.

Edit: Move the paragraph out of #harder into #quiet, directly after the paragraph that ends 'a description, not a test.', with this text:

<p>Deborah Mayo puts the rule this way: "One does not have evidence for a claim if nothing has been done to rule out ways the claim may be false." If a method was practically guaranteed to agree with the claim, she calls the result bad evidence, no test (<a href="https://doi.org/10.1017/9781107286184">Statistical Inference as Severe Testing</a>, 2018, p. 5). Her first example is from genomics. A model at Duke meant to predict which chemotherapy would work kept only the samples that fit it best in cross-validation. When another group kept training and test samples apart, its predictions were no better than chance. An exit code is that kind of evidence for a biological result. A planted signal that the pipeline must find is a real test, with two limits. It tests the pipeline, not the biology. And it counts only if the signal was made without the code being tested; a signal simulated under the pipeline's own assumptions only shows that the code agrees with itself (on calibration, <a href="https://plato.stanford.edu/entries/physics-experiment/">Franklin and Perovic</a>).</p>

#harder then keeps only what gets harder with agents: Bainbridge, forking paths, organized skepticism, use/misuse.

Minimum version (no move): keep the paragraph where it is with index:harder-3's opener, and replace "An exit code is not a severe test of a biological result. A planted signal that the pipeline must find is." with "An exit code is not a severe test of a biological result. A planted signal that the pipeline must find is a severe test of the pipeline, for the error you planted. It says nothing yet about the biology."

Sources: https://errorstatistics.com/wp-content/uploads/2022/04/sist_proofs-title-itinerary-preface-excursions1-3.pdf, https://plato.stanford.edu/entries/physics-experiment/, https://doi.org/10.1017/9781107286184

### index:harder-7 [rewrite] p2 (humanfactors)
The Bainbridge link goes to a scanned PDF on gwern with no text layer, so it cannot be searched or quoted. The paragraph also leaves out the sentence in the paper that matters most for this site: automatic control "camouflages" failure by correcting against it until it is beyond control. That is the 1983 version of the FlowBench finding the essay cites (agents patch a run until it exits cleanly). Her design rule, "automatic systems should fail obviously", is principle 2 in one line. Both quotes checked verbatim in the ckrybus PDF (Automatica 19:777), and the DOI was checked against Crossref. The closing clause "with less time spent inside the data than before" is unsourced, so this version drops it. CONFLICTS with index:harder-8, which keeps that clause and adds field evidence for it. If both are applied, use this paragraph, put the clause back after "you are left with the quiet failures", and insert -8's evidence sentences after it.

Edit: <p>In 1983 Lisanne Bainbridge described the "ironies of automation" (<a href="https://doi.org/10.1016/0005-1098(83)90046-8">Automatica</a>; <a href="https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf">searchable PDF</a>): the more of a process is automated, the more the person's remaining job is the abnormal cases, noticing and recovering from what the automation got wrong, while they get less practice at the normal ones. Agents fit that description. They take the routine runs; you are left with the quiet failures. She also saw why those are hard to see: "automatic control can 'camouflage' system failure by controlling against the variable changes, so that trends do not become apparent until they are beyond control." An agent that patches a run until it exits cleanly is doing the same thing. Her design rule was that "automatic systems should fail obviously", which is what a check you have seen fail gives you.</p>

Sources: https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf, https://doi.org/10.1016/0005-1098(83)90046-8

### index:harder-8 [rewrite] p2 (critic)
The Bainbridge paragraph is theory only, from 1983, and there is now field evidence of trained experts losing practice. It is observational, so the wording has to say 'might', as the authors do. The section also never answers the first question a science-studies reader asks: do these checks guard against misunderstanding, or only against wrong numbers? The honest answer is 'only wrong numbers'. Saying so in one sentence makes the site more credible and links principle 1 to Messeri and Crockett, the closest published work, which the site does not cite. Checked against the PubMed abstracts: ADR 28.4% (226 of 795) to 22.4% (145 of 648), 'might reduce'; Messeri and Crockett's abstract has 'produce more but understand less'. The 'four centres' detail is not in the abstract and should be checked in the paper. CONFLICTS with index:harder-7, which drops the clause this item supports (see -7 for how to combine them). It also adds two citations to a section that the essayist, designer, bench and rse reviewers say already has too many.

Edit: Agents fit that description. They take the routine runs; you are left with the quiet failures, with less time spent inside the data than before. There is field evidence for the loss of practice. At four endoscopy centres, the rate at which doctors found adenomas in colonoscopies done without AI fell from 28.4% (226 of 795) to 22.4% (145 of 648) in the three months after AI tools arrived; the study is observational, and the authors say AI exposure "might" be the cause (<a href="https://doi.org/10.1016/S2468-1253(25)00133-5">Budzyń et al. 2025</a>). The checks on this page catch wrong numbers. They do not give me the understanding that doing the work by hand used to, which is the risk Messeri and Crockett name: a science that will "produce more but understand less" (<a href="https://doi.org/10.1038/s41586-024-07146-0">Nature 2024</a>).</p>

Sources: https://pubmed.ncbi.nlm.nih.gov/40816301/, https://pubmed.ncbi.nlm.nih.gov/38448693/

### examples-3 [add] p2 (designer)
The essay's central practical claim is "rules that matter become code". It describes three such checks, but there is no code on the site or in the repo to copy. The format Chen named pairs each critique with a small runnable demo, and Weissgerber et al. shipped templates with their critique.

I ran the designer's draft. It has two quiet defects, which are the site's own failure modes:
- Its demo prints when the check says no but stays silent if the check never raises, so the demo itself could not fail.
- `len(values) == 0` lets through a control whose values are all NaN, an empty control in another form.

The revised snippet below fixes both. It counts non-NaN values, and it raises AssertionError if the check says yes to a bad input. It also adds the "says yes once" half from examples-2. Tested with python3 -I:
- the revised file runs clean and says no to both bad inputs;
- the designer's len()-only version fails the NaN case;
- a deliberately broken check makes the demo raise.

The designer's line "I put all three in the same commit" is dropped because it is an unverifiable claim about practice. The intro wording is handled in examples-11.

Edit: In tools/build_pages.py, after the status file block (or after the brief, if examples-1 is applied), add:

<h2 id="a-check-in-code">A check in code</h2>
<p>The smallest version of a rule in code. It stops the analysis instead of reporting a pass on an empty control. It comes with the bad inputs it must say no to, one good input it must accept, and the search that shows something calls it.</p>

# checks.py
import math

def require_values(name, values):
    """Stop if a control or condition has no measured values."""
    n = sum(1 for v in values if not math.isnan(v))
    if n == 0:
        raise ValueError(f"{name} has 0 measured values: not measured, so not a pass")
    return n

# Make it fail once before trusting it: an empty control, and one with only missing values.
for bad in ([], [float("nan"), float("nan")]):
    try:
        require_values("control", bad)
    except ValueError as err:
        print("said no, as it should:", err)
    else:
        raise AssertionError("the check said yes to a bad input")

# And see it say yes once on a good input.
assert require_values("control", [0.21, float("nan"), 0.35]) == 2

# A check nothing calls protects nothing. Find the line that calls it:
#   grep -rn "require_values(" scripts/

In docs/index.html, after `So the last step of writing a check is to find the line that calls it.</p>`, add: <p>A short version you can copy is on the <a href="examples.html#a-check-in-code">Prompts &amp; files</a> page.</p>. This is placed after the paragraph about calling, not after the figure-saving sentence, because the snippet ends with the search for the caller.

Sources: https://github.com/cxli233/FriendsDontLetFriends, https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128

### examples-4 [rewrite] p2 (bench)
The rules file is the file most people will copy, and its five lines leave out the site's main habit: make every check fail once. Merging the two path lines keeps the template at five lines with room for that habit.

The intro says what the file is but not how to write it. Framing it as the sheet a new rotation student gets tells a biologist what belongs in it: the dull, unwritten details. Lithgow et al. describe three worm labs that needed more than a year to find such details.

This overlaps on purpose with the per-check prompt in examples-2. The rules file holds the standing rule; the prompt is used on demand.

Edit: Edit in tools/build_pages.py. Replace the five template lines with:
Raw data is in [path]. Never modify or delete it. Write outputs to [path].
Read STATUS.md before starting.
Load software with: [your exact module or conda commands]
A job is finished when its output file has been checked, not when it exits.
Before trusting a new check, run it once on an input that should fail and show me that it says no.

If examples-1 is applied, make the second line "Read STATUS.md, and BRIEF.md if there is one, before starting."

In the intro paragraph, replace the sentence "The agent reads it at the start of every session." with: "The agent starts every session knowing nothing about your lab, so write it like the sheet you give a rotation student on day one: where things are, what not to touch, what went wrong last time."

Sources: https://www.nature.com/articles/548387a

### examples-5 [rewrite] p2 (sre)
The "Review today's work" prompt asks what was done. It does not ask about the most useful thing to inspect in an agent's day: changes to the checks themselves. The two ways to make a failing test pass without making the code right are deleting the assertion and pasting the current output in as the expected value (Kent Beck's list). Loosening a threshold or a filter is the research version, which the essay quotes from FlowBench ("fix" a failing run so it exits cleanly). These edits are easy to miss in a summary and plain in a diff.

This overlaps with examples-7, which targets the same failure at the moment a fix lands. This item adds no new prompt. If only one is taken, prefer this one.

Edit: Edit in tools/build_pages.py. New text:

Another session worked on this today. Read its commits and output files, not its summary. First list every check, threshold, filter or expected value it changed or removed, with the diff for each. Then: what was actually done, and what is not supported?

Sources: https://newsletter.kentbeck.com/p/canon-tdd

### examples-6 [add] p2 (essayist)
Principles 3 (empty is not measured) and 5 (name the unit) are the only checking principles with no prompt to copy. The essay's failure cards already contain the advice in prose: "Ask the agent for the row count of every control before reading any comparison" and "Before any count or correlation, name the unit. If the units are grouped, ask for the result within each group too." These prompts are the copyable form of that advice, not new content.

The critic's caution applies: the page says these are prompts Chen uses, so add them only if he does (see examples-11).

Edit: Edit in tools/build_pages.py. Add two tuples to the prompts list, after "Before I trust this check":
("Before I read a comparison", "For every control in this comparison, show me how many rows it has and the range of its values. If any control is empty, mark the comparison as not measured.")
("Name the unit", "What is the unit in this count or correlation? If the units come in groups, such as genes in families or samples in batches, give me the result within each group as well, and say how many groups there are.")

Sources: none

### examples-8 [add] p2 (bench)
The template has no place to record corrections. The essay says to read a source's list of corrections before building on it (the "Checks that compare a thing to itself" card), and the playbook says never to overwrite results. The status file template reflects neither. The lab-notebook rule is old and familiar: never erase an entry. This also gives the next session a list of what changed and why, so it does not rebuild from a superseded output.

Edit: Edit in tools/build_pages.py. In the status file template, after the line "- [choice made]: [alternatives tried and dropped], decided [before / after] seeing results", add:

## Corrections
- [date] [what was wrong], replaced by [what]. Old output kept in [file], not deleted.

Sources: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004385

### playbook-5 [rewrite] p1 (designer, sre)
setup/CLAUDE.md is the rules file the essay links as "the rules file I start new projects from", so it is the file a reader is most likely to copy. It tells the agent to background long work "then poll it". The essay says waiting is done "Not by an agent polling" and lists "An agent polling the queue all night" under Goes badly. The file a reader installs should agree with the page that sent them to it. Merged from designer and sre; this uses the sre wording, which adds a deadline because a hung job never writes its output file.

Edit: - **Background anything that outlives a couple of minutes, and wait on a condition, not a timer.** Chain the next step in the scheduler (job dependencies), or run one background check that ends when the job leaves the queue or its output file appears. Give every wait a deadline, because a hung job never writes its file. Do not poll from the conversation, and do not sit in a foreground call waiting for a job to finish.

Sources: none

### playbook-6 [rewrite] p2 (bench, rse, philosopher, humanfactors, designer, sre, educator)
There are two problems with the header line. First, it is inaccurate. It says every rule carries its incident in brackets, but only 7 of 27 do (rules 3, 5, 6, 7, 13, 15, 24), so a reader checking finds it false by rule 2. Second, the essay's principle says a rule in a file is read once and skipped at the moment it applies, and this file has just grown from 14 to 27 rules. Nothing marks which rules a hook or script enforces and which depend on the agent remembering. Strathern's study of audit warns that checks multiply until they displace what they were for. The fix is to label each rule by what enforces it, and to make conversion to code, or deletion, the default before adding a line. Merged from bench, rse, philosopher, humanfactors, designer, sre and educator. Variant: sre would tag every rule [code] or [prose] so the [prose] tags work as a to-do list. The others tag only the enforced rules and leave the rest plain, which is less visual noise. The edit below takes the second option.

Edit: Each rule exists because breaking it cost something. Where one incident explains a rule, it is in brackets. A rule that a hook or script enforces says so at its end [code: what enforces it]; the rest work only if they are read at the moment they apply, which is the weaker kind. A rule broken twice moves into code. Before adding a rule, try to turn an existing one into code, or delete one.

(Chen fills in the [code: ...] tags from what actually runs. Rule 3 has the git hook that blocks commits in a shared checkout; most of the others are reminders today. Do not tag a rule whose check exists but is not called anywhere, per rule 8.)

Sources: https://cambridge.org/core/journals/european-review/article/improving-ratings-audit-in-the-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB, https://sre.google/sre-book/postmortem-culture/

### playbook-7 [rewrite] p2 (essayist, designer, bench, rse, educator)
Rule 6's incident ("a benchmark read 46 instead of 272") gives no unit. The same file's rule 15 requires agents to state units, and five reviewers noticed. I searched the repository and the memory notes and could not find the unit, so Chen has to supply it. If the unit cannot be recovered, a ratio needs no unit (46/272 is about one sixth).

Edit: [An unrelated job held the GPU at 99%; a benchmark read 46 [unit] instead of 272 [unit].]
(Fallback if the unit is lost: "[An unrelated job held the GPU at 99%; a benchmark read about a sixth of its real speed.]")

Sources: none

### playbook-8 [rewrite] p2 (sre)
Rule 10 defines done but does not ban the code pattern that most often fakes done in agent-written scripts: catching an error, printing a warning and carrying on. An agent can follow the rule while writing only if it is told what to avoid, not just what to check afterwards. The proposal's number is wrong. It says empty or log-only error handling caused 35% of catastrophic failures in Yuan et al. (OSDI 2014). The paper's 35% covers three trivial patterns combined (Finding 11). Ignored errors, meaning a handler that is empty or only logs, account for 25% of the catastrophic failures, in a study of 198 user-reported failures in Cassandra, HBase, HDFS, Hadoop MapReduce and Redis. Playbook rules carry incidents, not citations, so the edit leaves the number out. If a number is wanted, use the corrected one.

Edit: 10. A job is done when the scheduler reports completion and the output file has been checked. Exit code 0 is not enough. Do not write error handlers that print a warning and carry on (`except: pass`, `|| true`, `2>/dev/null`); let the step fail, or record the failure in the output where the check will see it.
(Optional, corrected figure: "In a study of five distributed systems, error handlers that ignored the error or only logged it caused 25% of catastrophic failures (Yuan et al., OSDI 2014).")

Sources: https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan

### playbook-9 [rewrite] p2 (rse)
No rule protects against a job killed mid-write, for example by a Slurm time limit. A half-written output file passes a check that only tests whether the file exists, and rules 10 and 13 do not say how to tell a finished file from a partial one. Noble (2009) says, verified against the article: "create each output file using a temporary name, and then rename the file after it is complete". He gives as reasons that it "prevents partial results from being mistaken for full results" and makes scripts restartable.

Edit: Save results before printing a summary. Write each output under a temporary name and rename it when it is complete, so a killed job never leaves a file that looks finished.

Sources: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424

### playbook-10 [structure] p2 (essayist)
Twenty-seven rules have no edge a reader can sense (Mod). Rules 20 to 23 (Memory and tokens) are about running agents cheaply on one setup, not about whether a result is right. They belong in the local add-on file the playbook already mentions. Possible conflict: this cuts rules, while playbook-6 keeps all the rules and labels them, and the merged-playbook plan Chen was shown put these rules in the public file. Rule 21 (when memory and the rules file disagree, check the live system) is arguably about correctness and could stay as one line under Before you start. Do any renumbering last, after the other items that name rules by number.

Edit: Move the Memory and tokens section (rules 20 to 23) into the local add-on file and renumber, so the public list has 23 rules, all about whether the work is right. Optionally keep rule 21 in the public file, moved under "Before you start".

Sources: https://craigmod.com/journal/subcompact_publishing/, https://www.newyorker.com/magazine/2015/09/14/omission

### playbook-11 [rewrite] p2 (designer, sre)
The two setup files that readers download break the house style every other public page follows: setup/CLAUDE.md has 14 em dashes (on 13 lines) and setup/README.md has 12, counted with grep. One sre count of 13 counted lines, not dashes.

Edit: # CLAUDE.md: universal agentic research hygiene

(Apply the same treatment to every em dash in setup/CLAUDE.md, 14 in all, and setup/README.md, 12: replace each with a colon, comma or full stop, whichever reads naturally.)

Sources: none

### index:modes-2 [rewrite] p2 (humanfactors)
Conflicts with index:modes-1: both replace the opening of the 'While it runs' paragraph. The direct evidence for 'do not watch it' comes from vigilance research, not the METR speed trial. Watching a system that rarely fails is effortful, stressful work, and attention declines over the watch. The review's title is 'Vigilance requires hard mental work and is stressful', and its abstract says the finding 'applies to most human-machine systems that require human monitoring, particularly those involving automated subsystems' (checked on PubMed, 2026-10-09). If this item is used together with index:modes-1, it replaces modes-1's first two sentences. Its 'I know of no study of watching an agent' would sit oddly beside a citation on watching automation. Do not apply this item alone: the METR sentences that follow still contain the out-of-date 'METR is repeating it', which modes-1 corrects.

Edit: Do not watch it. Watching a system that is usually right is not light work: "vigilance requires hard mental work and is stressful" (<a href="https://doi.org/10.1518/001872008X312152">Warm, Parasuraman and Matthews 2008</a>), and the authors say this holds wherever a person monitors automation. It also feels more productive than it is.

Sources: https://pubmed.ncbi.nlm.nih.gov/18689050/, https://doi.org/10.1518/001872008X312152

### index:modes-3 [rewrite] p2 (essayist, humanfactors)
Merges two edits to the 'What I do instead' paragraph. (a) 'Check from my phone when it asks, not to supervise' is a 'not X' construction that reads as generated. (b) The review step is still passive. A fresh session's report beats the original session's summary, but it is still an account to read. Endsley and Kiris traced the loss of situation awareness under automation to this: 'the shift from active to passive processing was most likely responsible for decreased SA under automated conditions' (Crossref abstract, checked 2026-10-09). The cheapest fix is one active step per review: open a file and check one number yourself. Write that sentence with 'I' only if Chen actually does it; otherwise keep it as advice to the reader, as below.

Edit: I open my phone when a session asks for something, and otherwise leave it alone. Review in one batch, from the files and commits, with a fresh session that did not do the work. Then open one output file and check one number against something already known. A fresh session's report is still something you read. In one automation study, people lost track of the situation when the system made the decisions, and the authors traced it to "the shift from active to passive processing" (<a href="https://doi.org/10.1518/001872095779064555">Endsley and Kiris 1995</a>).

Sources: https://trid.trb.org/View/427017, https://doi.org/10.1518/001872095779064555, https://paulgraham.com/useful.html

### index:modes-4 [visual] p1 (designer)
On a phone, the modes diagram is four boxes joined by arrows, and its caption asks the reader to 'Hover, tap or click each mode'. All of the section's advice (when I use each mode and what it costs) is in tooltips. The node colours (you/file/agent/agent) carry no meaning here. A four-row table says the same thing with no interaction and reads on a 390 px screen. The site already styles a table this way (class "uma", the Parasuraman and Riley table), so no new CSS is needed. The table also moves the tooltip text from 'you' into Chen's 'I'. Conflicts with index:modes-5, which adds a divider to this diagram instead of removing it. If both are applied, show modes-5's boundary as a heavier rule between rows 2 and 3, or as text only.

Edit: <table class="uma">
<tr><th>Approve each command</th><td>My first week on anything, and any step that touches shared data, deletes files or submits many jobs. Cost: I am the bottleneck, and long tasks stall when I look away.</td></tr>
<tr><th>Approve the plan</th><td>Most of my daytime work. It writes a plan, I correct it, then edits run without asking. Safe commands are pre-approved in a list; risky ones still ask.</td></tr>
<tr><th>Run unattended</th><td>Only in a bounded space: its own copy of the repository, no access to raw data it could overwrite, a limit on how many jobs it can submit.</td></tr>
<tr><th>Overnight</th><td>When the goal is one sentence, success is a check it can run, and the compute is chained in the scheduler. Not when it will need my judgement at 2 a.m.</td></tr>
</table>
<p class="small">From watching every step (top) to checking only the result (bottom).</p>
Remove the modes spec from diagrams.js.

Sources: https://github.com/archietse/malofiej-2016/raw/master/tse-malofiej-2016-slides.pdf, https://worrydream.com/MagicInk/, https://mail.zcliu.cs.umd.edu/responsiveVis/responsive_vis_CHI20.pdf

### index:modes-5 [rewrite] p2 (humanfactors)
The section presents the four modes as evenly spaced steps, which suggests the risk rises evenly. A meta-analysis of 18 experiments found that a higher degree of automation helped routine performance but hurt performance when the automation failed, and hurt situation awareness. 'Negative consequences of automation seem to be most likely when DOA moved across a critical boundary, which was identified between automation supporting information analysis and automation supporting action selection' (PubMed abstract, checked 2026-10-09). This gives a reason for keeping approval on job submission and deletion, beyond 'computing centres say so', and it tells the reader which step needs the most thought. The diagram half conflicts with index:modes-4, which replaces the diagram with a table. In that case use a heavier rule between the 'Approve the plan' and 'Run unattended' rows, or keep only the text.

Edit: Which one is right depends less on the tool than on what the task can break. The risk also does not rise evenly. A meta-analysis of 18 automation experiments found that more automation made routine work better and made performance when the automation failed worse, and that the cost was most likely where automation moved from helping a person analyse to choosing the action (<a href="https://doi.org/10.1177/0018720813501549">Onnasch et al. 2014</a>). My reading is that for agents this is the step from approving its plan to letting it run without asking.

Visual, only if the modes diagram stays: in diagrams.js 'modes', draw a thin dashed divider in the muted grey, behind the nodes, between 'Approve the plan' and 'Run unattended'. It should be vertical at x=.51 in the wide layout and horizontal at y=.5 in the narrow one, labelled 'it chooses the action'. Add one line to the 'u' node info: 'Past this point it chooses actions and no one confirms them.' graph.js needs a small 'dividers' option for this; if that is too much, keep only the text.

Sources: https://pubmed.ncbi.nlm.nih.gov/24930170/, https://doi.org/10.1177/0018720813501549

### index:modes-7 [cut] p2 (essayist)
The overnight subsection gives the same list three times: in the diagram caption, in the 'Goes well' paragraph, and in the 'Brief + done-check' tooltip. FriendsDontLetFriends keeps the bad case, so this keeps 'Goes badly' and drops 'Goes well'. Its two unique items, its own copy of the repository and commands decided in advance, move into the caption (index:modes-6). Conflicts with index:modes-8, which adds a canary step to this paragraph. If this cut is applied, use modes-8's fallback, which puts the canary in 'Goes badly'.

Edit: Delete this paragraph and keep "Goes badly". Fold "its own copy of the repository" and "Decide in advance which commands it may run, so it does not stop at 1 a.m. waiting for a yes." into the night figcaption, as written in index:modes-6.

Sources: https://www.newyorker.com/magazine/2015/09/14/omission, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### index:modes-8 [rewrite] p2 (sre)
'Small stages' splits the work by step but not by size. A common way for a grad student to lose a night is to launch the full set (hundreds of samples, every chromosome) before one unit has gone through the whole pipeline and been checked, so every job fails the same way. Release engineering's version is the canary: run a small slice, compare it with what is expected, then roll out the rest. Nothing on the site or in the playbook says this. Conflicts with index:modes-7, which deletes the 'Goes well' paragraph this edits. If modes-7 is applied, use the fallback below.

Edit: A check it can run that has been seen to fail. One sample or one chromosome taken through every stage and checked before the full set is launched (release engineers call this a canary). Small stages that each end in a file and a commit.

Fallback if index:modes-7 removes 'Goes well': in the 'Goes badly' paragraph, after "One long job that saves only at the end.", add "The full set launched before one sample has been through every stage and checked (release engineers test a small slice first and call it a canary)."

Sources: https://sre.google/workbook/canarying-releases/

### index:modes-9 [rewrite] p2 (essayist, designer)
Merges two edits to the time-horizon paragraph. (a) The advice comes in the last sentence, after two dense numbers, and a phone reader stops before reaching it. The opening 'Benchmarks do not tell you...' delays it further. (b) 'For GPT-5 it was about 2 hours 17 minutes' reads as a current figure on a page dated October 2026, so it needs the model's release date.

Edit: <p>Plan a night as several short stages, each ending in a check. Benchmarks will not tell you how long a stage can be. METR measures the length of task (in human time) an agent completes half the time; for GPT-5 (released August 2025) it was about 2 hours 17 minutes. METR's own explanation says this is not how long an agent can run on its own, and that for tasks of 90 minutes to 3 hours, about a third succeed every time, a third fail every time, and a third vary (<a href="https://metr.org/time-horizons/">METR</a>). Anthropic reports its own engineers' sessions went from about 10 to about 20 actions before a person stepped in, between February and August 2025 (<a href="https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic">Anthropic</a>).</p>

Sources: https://metr.org/time-horizons/, https://www.vis4.net/blog/in-defense-of-interactive-graphics/

### index:failures-2 [rewrite] p2 (critic)
Even with the first-month line gone, the heading still forecasts the reader's future. The rest of the page reports one person's dated cases. The anchor id stays the same, so the principle links (#failures) and the walkthrough page's "the seven failure patterns" still work.

Edit: <h2 id="failures">Seven ways it went wrong</h2>

Sources: https://spia.princeton.edu/news/excerpt-princeton-spia-ai-experts-separate-hype-substance-new-book

### index:failures-3 [add] p2 (sre)
The one-picture-per-mistake form comes from Chenxin Li's Friends Don't Let Friends Make Bad Graphs, and the page never says so. The essay already credits rewrites.bio for the numbered form (line 39) in a small-print line, so this credit can use the same pattern. I checked the README: it says its Scripts/ directory has the .Rmd files that generate the graphics. That does not confirm a script for every item, so the edit says 'the code behind its pictures' rather than 'a script for each picture'.

Edit: Insert directly after the intro paragraph of the section (after index:failures-1's <p>):
<p class="small">One picture per mistake is borrowed from Chenxin Li's <a href="https://github.com/cxli233/FriendsDontLetFriends">Friends Don't Let Friends Make Bad Graphs</a>, whose Scripts folder holds the code behind its pictures.</p>

Sources: https://github.com/cxli233/FriendsDontLetFriends

### index:failures-6 [add] p1 (essayist, designer)
The cards say what you will see, but not what actually happened, with dates and numbers. Friends Don't Let Friends pairs every item with the real bad case. The real incidents are already public, but scattered: the 4 September list on this page, a diagram tooltip that a phone reader never taps, and the playbook. One designer finding fits here. The 732-of-13,663 count is in the 'clean' diagram's BLOCKED tooltip, and the 'silent guess' picture already draws it as '5% of genes'. Moving the count out of the tooltip and onto the card puts it in one visible place, and phone readers can see it. For 'Two agents, one folder', the essayist's proposed row repeats the card's own first line almost word for word. I replaced it with the date only, from the user's rules file (10 September), and the row is optional. If index:failures-7 (the generalized stale card) is applied, skip the stale row, because that edit already carries the incident.

Edit: In diagrams.js clean, replace the BLOCKED info with: info:'Cannot be computed from the text. The agent stops here and says so.'

In index.html, add a third row to these cards, after the 'What to do' <dd>, before </dl>:
The wrong unit: <dt class="lbl">Mine</dt><dd>4 September: 48 items in 6 groups. +0.45 pooled, −0.11 within the groups (p = 0.47).</dd>
The silent guess: <dt class="lbl">Mine</dt><dd>A search setting my notes never mentioned changed the result for 732 of 13,663 genes. One filtering step was written down nowhere.</dd>
Checks that compare a thing to itself (only if index:failures-7 is not applied): <dt class="lbl">Mine</dt><dd>A renamed category was served under its old name for four days, with every check green.</dd>
Lost at the last step: <dt class="lbl">Mine</dt><dd>25 minutes of finished GPU work, lost to a formatting bug in one summary line.</dd>
Two agents, one folder (optional): <dt class="lbl">Mine</dt><dd>Both, on 10 September.</dd>
Leave the empty-control and finished-but-empty cards without a Mine row. index:failures-9 and -10 add their mechanism lines.

Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, https://simonwillison.net/2025/Mar/11/using-llms-for-code/, https://github.com/cxli233/FriendsDontLetFriends

### index:failures-7 [rewrite] p1 (rse, essayist)
Two reviewers rewrote this card, and the essayist and RSE proposals CONFLICT: generalize the card, or only clarify it. This is the generalizing version. index:failures-8 keeps the narrow clarification, so apply only one. As written, the card is the hardest on the page to parse. 'After that project corrected its results' reads as if the check ran afterwards, 'pinned inputs' is software jargon, and the line ends on 'not X but Y'. The case it tells (a site built from another project's results) is unusual, and most readers will skip it as not their problem. The everyday version is the snapshot or regression test, which nf-core pipelines use through nf-test. A snapshot catches change, not error, so a wrong reference passes forever. This version puts the essayist's plainer wording and the playbook's dated incident inside the card. I checked both citations: the nf-test paper is Forer and Schönherr, GigaScience 2025, and the rewrites.bio sentence is verbatim from its section 2.3. The page already quotes rewrites.bio once (line 39), so the closing quote can be cut if the card runs long on a phone.

Edit: <dd>Every check passes, and every check compares the output with an earlier copy of itself: last week's table, a pinned input, a saved snapshot. Mine was a site built from another project's results. That project renamed a category, and for four days the site served the old name with every check green.</dd><dt class="lbl">What to do</dt><dd>Keep at least one check that compares with something outside the copy: a planted signal, a value worked out by hand, the source's corrections since the version you copied. Snapshot tests, which nf-core pipelines use through <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12616847/">nf-test</a>, catch change. If the snapshot was wrong from the start, they pass forever. As <a href="https://rewrites.bio/">rewrites.bio</a> puts it, "Output comparison catches what you tested, not what you haven't."</dd>

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12616847/, https://rewrites.bio/, https://paulgraham.com/simply.html, https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/

### index:failures-10 [rewrite] p1 (sre)
The card says what 'done' means but not the most common way agent-written code reaches exit 0 with an empty file: an error handler that prints a warning and carries on. Agents write these readily because they make the error go away. The reviewer's figure was wrong, so I CORRECTED it from the paper. In Yuan et al. (OSDI 2014), 35% is all 'trivial mistakes' in error handlers (Finding 11, Figure 5), which includes aborting on an over-broad catch (8%) and handlers marked TODO (2%). Handlers that ignored the error were 25% of the 48 catastrophic failures, drawn from 198 sampled failures in Cassandra, HBase, HDFS, MapReduce and Redis. I added the R form because most of the readers use R.

Edit: Write in your rules file what "done" means: which file, how many rows, what range of values. Exit code 0 only means the program stopped. Then ask the agent to list every place its code catches an error and carries on (<code>except: pass</code> in Python, <code>tryCatch(..., error = function(e) NULL)</code> in R, <code>|| true</code> in shell). In one study of 48 catastrophic failures in five distributed data systems, a quarter came from an error handler that ignored the error (<a href="https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan">Yuan et al. 2014</a>).

Sources: https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan

### index:failures-11 [rewrite] p2 (bench)
'The wrong unit' is the pattern biologists are trained to spot as pseudoreplication, but the card never uses the bench name. One sentence lets a student recognise it at once and reuse a reflex they already have. Following the site's plain-language-first style, the edit leads with the bench version and puts the technical term in parentheses.

Edit: A strong correlation across many items that come in groups: genes in families, cells in animals, samples in batches. At the bench, this is counting technical replicates as if they were biological ones (pseudoreplication).

Sources: none

### index:failures-12 [visual] p2 (philosopher)
The 'wrong unit' picture shows the trend reversing inside each group: slopes drawn going down, labelled 'within each group: down'. The real case on the page is +0.45 pooled and −0.11 within groups with p = 0.47, which is no trend, not a reversal. A picture is a claim too. This one teaches the dramatic form of Simpson's paradox, when the lesson from the data is quieter and more common: the pooled trend comes from differences between groups and goes away inside them. The wrong_unit demo in index:failures-19 should match, with flat groups and no reversal.

Edit: In minis.js unit(): replace y=c[1]+(x-c[0])*0.45+r()*6 with y=c[1]+r()*10; make each group line flat by replacing .attr('y1',c[1]+3).attr('y2',c[1]+21) with .attr('y1',c[1]+5).attr('y2',c[1]+5); replace the label line with: t(s,230,30,'pooled: up',{a:'end'});t(s,30,147,'within each group: no trend',{c:RED}); and update the comment to // pooled trend up, within-group flat

Sources: none

### index:failures-13 [visual] p2 (designer)
Empty-control picture. The green badge has a red line struck through '"passed"', which reads as 'the check did not pass'. That is the opposite of the case: the bad case is that the report says PASS. The picture should show what the reader sees (a pass) and mark why it is hollow.

Edit: t(s,216,78,'PASS',{a:'middle',c:'#fff'});s.append('line').attr('x1',152).attr('x2',185).attr('y1',84).attr('y2',73).attr('stroke',RED).attr('stroke-width',1);t(s,216,102,'from no data',{a:'middle',c:RED});

Sources: https://github.com/cxli233/FriendsDontLetFriends, https://content.ieeevis.org/year/2022/paper_v-full-1024.html, https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128

### index:failures-14 [visual] p2 (designer)
In the 'Lost at the last step' picture, the red caption 'save first, print second' is the fix, not the bad case, so the picture mixes the two. The card's 'What to do' already gives the fix. I changed the reviewer's 'crashed here' to 'crashed at print', because the caption sits at the left edge, far from the × it would point to.

Edit: t(s,20,130,'crashed at print; nothing saved',{c:RED});

Sources: https://github.com/cxli233/FriendsDontLetFriends, https://content.ieeevis.org/year/2022/paper_v-full-1024.html

### index:failures-15 [visual] p2 (designer)
In the 'compare a thing to itself' picture, 'your site' is too specific for a grad student. 'your copy' fits either version of the card (index:failures-7 or -8). 'checks ✓ ✓ ✓' measured 89.8 px wide inside a 90 px box, so it touches the border. The red caption should change to match 'your copy'.

Edit: t(s,200,32,'your copy',{a:'middle'});t(s,200,68,'old version',{a:'middle'});t(s,200,88,'checks ✓ ✓ ✓',{a:'middle',c:GREEN,size:12});
Also replace t(s,130,130,'the checks compare the site with itself',{a:'middle',c:RED}); with t(s,130,130,'the checks compare the copy with itself',{a:'middle',c:RED});

Sources: https://content.ieeevis.org/year/2022/paper_v-full-1024.html

### index:failures-16 [visual] p2 (designer)
In the 'Two agents, one folder' picture, the 'session A' and 'session B' labels (61.9 and 61.1 px) overflow their 60 px boxes, and the session B box ends exactly at the 260 px edge of the drawing. The reviewer's fix (width 70, B at x 185) would let box A touch the folder box at x 90. Moving A left to 10 and B to 180 keeps the two boxes symmetric about the folder (centres at 45 and 215, folder centre 130), and A's connector start (x 80) stays where it is.

Edit: [[10,30,'session A'],[180,30,'session B']].forEach(function(a){s.append('rect').attr('x',a[0]).attr('y',a[1]).attr('width',70).attr('height',22).attr('rx',4).attr('fill',BLUE);t(s,a[0]+35,a[1]+15,a[2],{a:'middle',c:'#fff'})});
On the next line change B's connector .attr('x1',200).attr('x2',165) to .attr('x1',180).attr('x2',165). A's connector (x1 80, x2 95) is unchanged.

Sources: https://content.ieeevis.org/year/2022/paper_v-full-1024.html

### index:failures-17 [structure] p2 (designer)
The rebuild-from-Methods diagram sits after the seventh card, three cards away from 'The silent guess', which its caption explains ('A way to find silent guesses on purpose'). There is a trade-off: a 300 px figure between cards 4 and 5 breaks the run of cards on a phone. If that reads badly, the alternative is to leave the figure where it is and start its caption with 'For the silent guess:'. The Errington paragraph in index:failures-18 should go wherever the figure ends up.

Edit: Move this <figure> unchanged so it sits directly after the </article> that closes 'The silent guess' card, before the 'Checks that compare a thing to itself' card.

Sources: https://content.ieeevis.org/year/2022/paper_v-full-1024.html

### index:failures-18 [add] p2 (bench)
The rebuild-from-Methods diagram and principle 7 rest on my own example only. A sourced number shows a biologist that gaps in Methods sections are normal at field scale, not a personal quirk, and it turns the diagram into an action: run the rebuild before submission. I checked the source against PubMed (PMID 34874008, DOI 10.7554/eLife.67995). The abstract says none of the 193 experiments was described in enough detail in the original paper to design a protocol, so the authors had to ask the original authors. The reviewer wrote 'paper and its supplement'. The abstract says 'original paper', so the edit uses that. I also replaced the opener 'Professional replicators hit the same wall', which reads like a pitch.

Edit: Insert directly after the 'clean' figure (wherever index:failures-17 places it):
<p>The gap is common in published work. A project that set out to repeat 193 experiments from cancer biology papers found that none was described in enough detail in the original paper to design the repeat, so they had to ask the original authors (<a href="https://doi.org/10.7554/eLife.67995">Errington et al. 2021</a>). Running this rebuild on my own Methods before submission finds those gaps before a reader does.</p>

Sources: https://elifesciences.org/articles/67995

### index:failures-19 [structure] p2 (rse, sre)
Two reviewers (RSE and SRE) proposed the same addition: runnable demos. Friends Don't Let Friends pairs each picture with code, and the seven cards have pictures but nothing to run. 'Make every check fail once' is learned by doing it. A grad student who runs a 10-line script that passes on an empty control remembers it. The best first demo is not yet a card: the loop that ran once instead of fourteen times, from 'Why the failures are quiet'. I checked it here: the same script counts 3 in bash and 1 in zsh, the default shell on a Mac. The two proposals CONFLICT on wrong_unit. RSE drew it with a negative within-group trend, but it should be flat, to match the real case (−0.11, p = 0.47) and the corrected picture in index:failures-12. 'The silent guess' and 'Two agents, one folder' are about process, not code, and get no demo. The demos use simulated data only, so nothing unpublished goes public.

Edit: Add docs/demos/ (served by Pages and visible on GitHub). One script per pattern, each under 30 lines, simulated data only, printing the quiet failure first and then the check that catches it. Link each from the end of its card's 'What to do' as <a href="demos/FILE">Run it</a>. Use R for the statistics demos.
1. loop_runs_once.sh, linked from 'A loop over a list ran once instead of fourteen times' in 'Why the failures are quiet':
# The loop that ran once. Run with zsh, then with bash.
REPOS="alpha beta gamma"
n=0
for r in $REPOS; do n=$((n+1)); done
echo "scanned $n repos, no secrets found"
# The check that would have caught it: count the passes.
[ "$n" -eq 3 ] || { echo "FAIL: expected 3 passes, got $n"; exit 1; }
2. empty_control.R: all(numeric(0) < 0.05) is TRUE; fixed by stopifnot(length(ctrl) > 0).
3. finished_but_empty.py: a loop body that raises, an except block that prints a warning and continues, a header-only output file and exit 0, then a row-count check that fails.
4. wrong_unit.R: six simulated groups of eight, group means rising, no trend within groups. Prints the pooled correlation (positive), then the within-group correlations (near zero).
5. save_then_print.py: a summary line that raises after the compute loses everything unless the write comes first.

Sources: https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html, https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html, https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan, https://github.com/cxli233/FriendsDontLetFriends

### index:quiet-1 [rewrite] p1 (critic)
The FlowBench paragraph is the essay's strongest point, but it rests on one 2026 preprint and stops before the practical conclusion. If agents make the error go away, they will also make the check go away whenever they can edit it, and nothing on the site says where a check should live. Rule 13 of the playbook ('Do not make it pass') covers behaviour, not placement. METR's post is a primary, measured source for the same behaviour in frontier models; I checked the quoted fragment against the page. CONFLICT: index:quiet-2 (Duhem) replaces the same old_text. If both are accepted, see the combining note in index:quiet-2.

Edit: Asked to make the error go away, they make the error go away. A clean exit is the thing they can see, so it becomes the target. METR saw the same in frontier models on its own tasks: "attempting (often successfully) to get a higher score by modifying the tests or scoring code" (<a href="https://metr.org/blog/2025-06-05-recent-reward-hacking/">METR 2025</a>). So a check the working session can edit is a check it can make pass. The checks that matter should sit where it cannot write: a git hook, a file it has no permission to change, or a review by a session that did not write the code.</p>

Sources: https://metr.org/blog/2025-06-05-recent-reward-hacking/

### index:quiet-2 [add] p2 (philosopher)
The FlowBench paragraph says what agents do (make the error go away) but not why the check is so often the thing that changes. Duhem's point gives the reason in one sentence: a failed run implicates the data, code, settings, environment and idea together, so 'remove the error' leaves the agent free to change the cheapest part. It also leads into the positive-control paragraph that follows. CONFLICT: same old_text as index:quiet-1. If both are accepted, apply this text, then append index:quiet-1's sentences from 'METR saw the same' to the end, before the closing </p>. The result reads: Duhem gives the reason, METR the measurement, then where the check should live.

Edit: Asked to make the error go away, they make the error go away. A clean exit is the thing they can see, so it becomes the target. Part of the reason is old. A failed run says that something in the bundle is wrong (the data, the code, a setting, the environment, or the idea) but not which one. Pierre Duhem made this point about physics experiments more than a century ago (<a href="https://plato.stanford.edu/entries/scientific-underdetermination/">SEP</a>). An agent told to remove the error changes whatever is cheapest to change, and that is often the check.</p>

Sources: https://plato.stanford.edu/entries/scientific-underdetermination/, https://plato.stanford.edu/entries/lakatos/

### index:quiet-3 [rewrite] p1 (rse, philosopher)
Merged from two proposals that rewrite the same paragraph and fit together. (a) Admitting the selection effect is the most honest sentence on the page, but 'But that is also the point' then waves it away. Both explanations (my notes only record quiet failures; agents leave quiet failures) predict the same notes, so the paragraph should say that and name evidence that does not come from the notes. (b) That evidence exists. Soergel (2015) made the same filter argument about human-written scientific code before agents existed. I checked his wording: crashes and 'completely implausible results' get found during development, and 'nearly every possible output is plausible'. The Excel gene-name case is the quiet error every genomics reader already knows. Ziemann et al. 2016's abstract gives 'approximately one-fifth'. Cite Soergel for the mechanism only: he calls his own error-rate numbers 'rank speculation', so do not quote them. The closing sentence hands off to the FlowBench paragraph that follows. If length on phones matters, drop the Excel sentences first.

Edit: <p>That pattern is partly an artifact of what I wrote down. Loud failures (a crash, a missing module, a syntax error) get fixed inside the session in a minute and never reach my notes, so my notes would look like this whether or not agents leave quiet errors behind. Two things outside my notes say the filter is real. The first is older than agents. David Soergel argued in 2015 that bugs which crash a program or give implausible results tend to be found while the code is being written, and that in scientific code almost any output looks plausible, so the bugs that survive are the quiet ones (<a href="https://f1000research.com/articles/3-303/v2">F1000Research</a>). Genomics has a well-known case: Excel turns gene names such as SEPT2 and MARCH1 into dates, and about one fifth of papers with Excel gene lists in their supplements had such errors (<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4994289/">Ziemann et al. 2016</a>). Nothing crashed. The agent's loop of run, read the error, fix, run again is the same filter, run faster, so what comes out the other end is enriched for the quiet ones. The second is a benchmark that does not use my notes at all.</p>

Sources: https://f1000research.com/articles/3-303/v2, https://pmc.ncbi.nlm.nih.gov/articles/PMC4994289/

### index:quiet-6 [rewrite] p1 (educator)
'Mutation testing, 1978' is the only claim in the section with no source, against the site's rule that numbers must be sourced. Teaching Tech Together summarizes Edwards and Shams 2014, which measures the thesis directly: beginners write tests to confirm their code works, not to find where it breaks. I checked the 13.6% and the 90% wording against the online book; the primary DOI is in its bibliography. This links the bench positive control to the quiet failures already on the page. CONFLICT: index:quiet-7 (Just et al. 2014) replaces the same sentence with a different source. Pick one; using both would put four sentences of software testing into a paragraph about bench controls.

Edit: Software testing has the same idea under another name: mutation testing breaks the code on purpose and sees whether the tests notice. Beginners rarely test that way. Edwards and Shams pooled every bug in a class's submitted programs and found that the students' own tests caught 13.6% of them on average, and that 90% of the tests were very similar, written to confirm the code works rather than to find where it does not (<a href="https://doi.org/10.1145/2591708.2591757">2014</a>, summarized in Greg Wilson's <a href="https://teachtogether.tech/en/index.html">Teaching Tech Together</a>). The checks in the failures on this page were that kind.

Sources: https://teachtogether.tech/en/index.html, https://doi.org/10.1145/2591708.2591757

### index:quiet-7 [rewrite] p2 (sre)
Alternative to index:quiet-6 for the same sentence (CONFLICT: same old_text). It also fixes the unsourced '1978', and it states the honest limit of planting bugs: it earns a check trust but does not certify it. That matches the demo's last line ('has earned some trust'). I confirmed the 357 real faults, 5 programs and the significant correlation on the abstract page. The 17% figure is not on that page and could not be extracted from the PDF here, so check it against the paper body before publishing. If only the date needs a source and neither rewrite is wanted, cite DeMillo, Lipton and Sayward, 'Hints on test data selection', IEEE Computer, 1978. That is the usual citation for the 1978 date; check the reference before using it.

Edit: Software testing has the same idea under another name, mutation testing: break the code on purpose and see whether the tests notice. It earns a check some trust, not a certificate. In a study of 357 real bugs in five open-source programs, how well a test suite caught planted bugs tracked how well it caught the real ones, but 17% of the real bugs were of a kind no planted bug stood in for (<a href="https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html">Just et al. 2014</a>).

Sources: https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html

### index:quiet-10 [rewrite] p2 (bench)
Fallback for the current three-row widget, if index:quiet-9 is not applied (OVERLAP: quiet-9 already contains this wording; apply only one). Three of the demo's inputs are controls every biologist has run: a blank, a negative control and a spike-in. Naming them makes the demo click on the first tap. The shuffled-labels line also never says what shuffling keeps and what it breaks, and that is the whole of control design. Lipsitch et al. define a negative control as one that shares every confounding route but not the causal one. Keep the button labels short for phones; the bench names go only in the explanation line.

Edit: "Empty file, the blank: the exit code still passes. The row count catches it.","Shuffled labels, a negative control: shuffling keeps every value, the row count and the file format, and breaks only the link between sample and label. The effect should be gone, and only the third check notices.","Planted known signal, the analysis version of a spike-in: the third check finds it. A check that says no on the shuffled input and yes on the planted one has earned some trust on your real data."

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/, https://doi.org/10.1101/gr.121095.111

### index:quiet-12 [rewrite] p2 (designer)
The FlowBench citation is the only source in this section that links to the site's own reading page instead of the paper. Every other citation in the essay (Feynman, METR, Mayo and Spanos) links the primary source. reading.html gives the paper URL and the authors (Kurjan and Cribbs, 2026).

Edit: (Kurjan and Cribbs, <a href="https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1">FlowBench</a>)

Sources: https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1

### index:quiet-13 [rewrite] p2 (rse)
The empty / shuffled / planted demo is the site's core tool, but it has no name a reader can search for. Bioinformatics has a published one, metamorphic testing, used when there is no known right answer to compare with. Chen et al. 2009 tested GNLab and SeqMap this way and also used 'artificially fault-seeded programs' (checked against the abstract), which is 'make every check fail once' in the reader's own field. Changed from the proposal: 'Chen and colleagues' became 'Tsong Yueh Chen and colleagues', because the essay is written in Chen Hsieh's first person and 'Chen' alone reads as the author. Plain description first, term in parentheses. This adds a second software-testing term next to mutation testing (index:quiet-6/7), so weigh whether the bench-biology reader needs both.

Edit: <figcaption>Try all four inputs. A check that passes on everything, including inputs built to be wrong, cannot tell you anything about your result. When there is no known right answer to compare with, software testers check how the output should change when the input changes (metamorphic testing). Tsong Yueh Chen and colleagues tested two bioinformatics programs this way, and planted bugs on purpose to confirm the tests caught them (<a href="https://doi.org/10.1186/1471-2105-10-24">BMC Bioinformatics 2009</a>).</figcaption>

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC2657898/, https://doi.org/10.1186/1471-2105-10-24

### reading-1 [add] p2 (critic)
Critiques has nothing on agents gaming their own checks. That is the essay's FlowBench point: agents "fix" a failing run so it exits cleanly. METR's post is the direct evidence from frontier models, and it is short. I checked both quotes at the source on 9 October: "attempting (often successfully) to get a higher score by modifying the tests or scoring code" and "Detecting reward hacking can be quite difficult." Neither the essay nor the Reading page mentions reward hacking yet.

Edit: In tools/build_pages.py, add one it() call directly before the line that begins with old_text, so the new entry follows 'AI scientists fail without strong implementation capability'. Leave old_text as it is. Rendered HTML:
<p><a href="https://metr.org/blog/2025-06-05-recent-reward-hacking/">Recent frontier models are reward hacking</a> <span class="small">(METR, 2025)</span>. Models tried to raise their scores "by modifying the tests or scoring code", often successfully. "Detecting reward hacking can be quite difficult."</p>

Sources: https://metr.org/blog/2025-06-05-recent-reward-hacking/

### reading-2 [add] p2 (critic, humanfactors, educator)
This merges three proposals: critic ('What it does to the person using it'), humanfactors ('Older work on people and automation') and educator (Prather). The Reading page has 40 entries about systems and tools and none about what using them does to the researcher, even though the essay's argument (Bainbridge, Parasuraman and Riley, the METR trial) is about exactly that.

Dropped because the essay already covers them with the same summaries: the Bainbridge 1983 and Parasuraman and Riley 1997 entries, and the METR 2025 trial numbers (24% expected, 19% slower, 246 tasks are in 'While it runs'). Only METR's 2026 follow-up is kept, because it is new.

Corrections from checking on 9 October:
- The proposed Lee and See PDF host (csel.eng.ohio-state.edu) fails with a TLS certificate mismatch. Link the DOI instead. Both quotes were confirmed in that PDF.
- In Parasuraman and Manzey, 'cannot be prevented by training or instructions' is said of automation bias, not complacency.
- In Shen and Tamkin, the high-scoring group is three interaction patterns, not only 'conceptual questions'. The 17% figure and n=52 are the paper's own.
- In Prather, only the fragment "finished with an illusion of competence" could be checked verbatim, so the longer quote is not used.

Prather goes here, not in Critiques as the educator proposed, because it is about the learner rather than the systems.

Conflict with reading-5: this adds eight entries to a page the essayist says already gives 40 entries equal weight. If the page should stay short, keep the first five. Move the METR update into the essay's 'While it runs' paragraph instead: its line 'METR is repeating it' has been out of date since METR changed its study design in February 2026.

For the essay, not this page: Bainbridge's own line "automatic systems should fail obviously" (checked in the 1983 PDF) fits the essay's Bainbridge paragraph.

Edit: In tools/build_pages.py, add this block with it() calls after the Critiques block and directly before the line rd+='<h2>Systems that run research themselves</h2>\n'. Rendered HTML:
<h2>What it does to the person using it</h2>
<p>The essay cites Bainbridge (1983) and Parasuraman and Riley (1997). These carry the same question into generative AI.</p>
<p><a href="https://arxiv.org/abs/2402.11364">Ironies of generative AI</a> <span class="small">(Simkute et al., 2024)</span>. Bainbridge's ironies applied to generative AI: "a shift in users' roles from production to evaluation", and "a tendency for automation to make easy tasks easier and hard tasks harder".</p>
<p><a href="https://doi.org/10.1518/hfes.46.1.50_30392">Trust in automation: designing for appropriate reliance</a> <span class="small">(Lee and See, Human Factors 2004)</span>. Trust should match what the system can actually do. Two of their design rules: "Design for appropriate trust not greater trust" and "Show the past performance of the automation."</p>
<p><a href="https://doi.org/10.1177/0018720810376055">Complacency and bias in human use of automation</a> <span class="small">(Parasuraman and Manzey, Human Factors 2010; abstract)</span>. A review. Automation bias "occurs in both naive and expert participants" and "cannot be prevented by training or instructions". Complacency appears when other tasks compete for attention.</p>
<p><a href="https://arxiv.org/abs/2601.20245">How AI impacts skill formation</a> <span class="small">(Shen and Tamkin, Anthropic, 2026)</span>. Randomized: 52 people learning a new Python library. With AI they scored 17% lower on a quiz of concepts, code reading and debugging, and were not significantly faster. The three ways of using it that kept scores high all involved asking for explanations or concepts, not only for code.</p>
<p><a href="https://arxiv.org/abs/2405.17739">The widening gap</a> <span class="small">(Prather et al., ICER 2024)</span>. 21 novice programmers observed while coding with AI tools. Those who already knew what code they meant to write used the tools to go faster and ignored bad suggestions. Those who struggled overestimated how well they did and "finished with an illusion of competence". These were students in an intro course, not researchers using agents; it is here because it is the closest study I know of a first week with these tools.</p>
<p><a href="https://doi.org/10.1016/S2468-1253(25)00133-5">Endoscopist deskilling risk after exposure to AI in colonoscopy</a> <span class="small">(Budzyń et al., Lancet Gastroenterology and Hepatology 2025; abstract)</span>. Observational, four centres in Poland. In colonoscopies done without AI, the adenoma detection rate fell from 28.4% in the three months before AI arrived to 22.4% in the three months after. Outside software, and observational, so other changes over those months could contribute.</p>
<p><a href="https://doi.org/10.1038/s41586-024-07146-0">Artificial intelligence and illusions of understanding in scientific research</a> <span class="small">(Messeri and Crockett, Nature 2024; abstract)</span>. AI tools can leave scientists believing they understand more than they do, and can let a few methods and questions crowd out the rest: "a phase of scientific enquiry in which we produce more but understand less".</p>
<p><a href="https://metr.org/blog/2026-02-24-uplift-update/">We are changing our developer productivity experiment design</a> <span class="small">(METR, 2026)</span>. The follow-up to the 2025 trial in the essay. With 57 developers and 800+ tasks it could not get a reliable estimate, partly because developers who did not want to work without AI stayed out of the study. METR reads the new numbers as a lower bound on the speedup.</p>

Sources: https://arxiv.org/abs/2402.11364, https://doi.org/10.1518/hfes.46.1.50_30392, https://csel.eng.ohio-state.edu/productions/intel/research/trust/Lee%20%26%20See%20Trust%20Review.pdf, https://pubmed.ncbi.nlm.nih.gov/21077562/, https://arxiv.org/abs/2601.20245, https://arxiv.org/abs/2405.17739v1, https://pubmed.ncbi.nlm.nih.gov/40816301/, https://pubmed.ncbi.nlm.nih.gov/38448693/, https://metr.org/blog/2026-02-24-uplift-update/, https://arxiv.org/abs/2507.09089, https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf, https://web.mit.edu/16.459/www/parasuraman.pdf

### reading-3 [add] p2 (bench)
Every entry on the Reading page is about AI. A biologist deciding whether to trust this advice is more likely to be persuaded by the bench lineage: the essay's habits are older than agents, and the evidence for them comes from biology. Each of these five papers backs one claim on the site: controls, rebuilding from the Methods, a quiet error caught by a script, one summary hiding many datasets, and keeping the record.

Checked on 9 October:
- Begley and Ellis: "confirmed in only 6 (11%) cases" and "should include and show appropriate positive and negative controls". The Nature link redirects to a login, so it is marked paywalled.
- Weissgerber: the quote is the Introduction's exact sentence.
- Schnell: Rule 6 ("keep a record of how every result was produced") and Rule 5 ("Never erase or destroy an entry").
- Errington: the eLife page would not load in a non-browser fetch, and the bench reviewer read it through PMC8651289. Open it in the headless browser before publishing.

This also adds to the page-length concern in reading-5.

Edit: In tools/build_pages.py, add this block with it() calls directly before the line rd+='<h2>Systems that run research themselves</h2>\n'. If reading-2 is also applied, put it after that section. Rendered HTML:
<h2>From the bench</h2>
<p>The habits in the essay are older than agents.</p>
<p><a href="https://www.nature.com/articles/483531a">Raise standards for preclinical cancer research</a> <span class="small">(Begley and Ellis, Nature 2012; paywalled)</span>. Amgen confirmed the findings of 6 of 53 landmark papers. Among the fixes they ask for: studies "should include and show appropriate positive and negative controls".</p>
<p><a href="https://elifesciences.org/articles/67995">Challenges for assessing replicability in preclinical cancer biology</a> <span class="small">(Errington et al., eLife 2021)</span>. For none of 193 experiments was the paper's description detailed enough to design the replication; the team had to ask the original authors.</p>
<p><a href="https://doi.org/10.1186/s13059-016-1044-7">Gene name errors are widespread in the scientific literature</a> <span class="small">(Ziemann, Eren and El-Osta, Genome Biology 2016)</span>. Excel turned gene names such as SEPT2 into dates in about one-fifth of papers with supplementary Excel gene lists. Nothing raised an error; a script run over every supplementary file found them.</p>
<p><a href="https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128">Beyond bar and line graphs</a> <span class="small">(Weissgerber et al., PLoS Biology 2015)</span>. "Many different data distributions can lead to the same bar or line graph." A job that reports "finished" has the same problem: a full output file and an empty one give the same report.</p>
<p><a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004385">Ten simple rules for a computational biologist's laboratory notebook</a> <span class="small">(Schnell, PLoS Computational Biology 2015)</span>. The notebook habit, for code: "keep a record of how every result was produced", and never erase an entry, because mistakes are part of the record.</p>

Sources: https://www.nature.com/articles/483531a, https://elifesciences.org/articles/67995, https://doi.org/10.1186/s13059-016-1044-7, https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004385
