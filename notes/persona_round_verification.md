# Persona round: source and editorial check (2026-10-11)

Input: notes/persona_round_2026-10-09.md, which has 84 pending items. I checked each one against docs/index.html, tools/build_pages.py, docs/*.js, docs/style.css and setup/AGENT_PLAYBOOK.md at commit 3f65bdf, which matches origin/main.

**None of the 84 is fully applied.** Two are partly overtaken by later changes:
- principles-9: principle 6 already reads "Files are the record, not the chat".
- start-3: its claim that the examples page has no brief is now false, because a brief was added.

How the sources were checked:
- Four parallel checker agents opened every cited source.
- Two reported back in time: agent and AI sources (B), and reproducibility and biology sources (C).
- Two had not reported when this file was written: human factors (A: Parasuraman and Manzey, Goddard, Parasuraman and Riley, Bainbridge, Warm, Endsley and Kiris, Onnasch, Lee and See, Simkute) and philosophy, testing and site reliability (D: the Watchdog runbook, Strathern, Mayo, the Stanford Encyclopedia of Philosophy, Teaching Tech Together, Just, the author 2009, Yuan, canarying, Budzyń, Messeri and Crockett, DeMillo).
- Items that depend only on A or D sources are marked **PENDING-A** or **PENDING-D**. In this file they are not verified.

What I checked locally:
- The essay is about 3,460 words, and the failures section about 380.
- I recomputed the dark-mode contrast ratios against #151513: #333 is 1.45, #555 is 2.45, #666 is 3.18 and #8a2c2c is 2.16. In dark mode, p.small and figcaption fall back to #555 at 2.45. The two reds are 1.41 apart.
- setup/CLAUDE.md has 14 em dashes on 13 lines, setup/README.md has 12, and skills/README.md has 9.
- The loop demo counts 3 in bash and 1 in zsh.
- The examples-3 snippet runs clean with python3 -I.
- 7 of the playbook's 27 rules carry an incident in brackets.
- The incidents are in the author's own files: 732 of 13,663 is in the diagrams.js tooltip; 25 minutes of GPU work lost on 2026-09-04 and the shared checkout on 2026-09-10 are in /scratch/ch29576/.claude/CLAUDE.md; the four-day renamed category is playbook rule 5.

**Corrections to text already live:**
1. rewrites.bio: the checker saw only "Fast code is now cheap." The second sentence quoted on the site, "Scientific insight, validation, and trust are not", was not seen on the page. Re-check it.
2. The page names no author; the repository is under seqeralabs. It has 12 numbered guidelines, not a stated "twelve principles".
3. The METR time-horizons paraphrase on the site, "this is not how long an agent can run on its own", is close to but not the page's wording. The page says: "a measure of the difficulty of a task, rather than the time an AI spends to complete the task."

Format: id | source verdict | editorial verdict | final text to apply | notes

---

## WORTH IT (ranked by value)

**1. site-wide-visual-and-navigation-1** | VERIFIED (contrast ratios recomputed locally) | WORTH IT: in dark mode on phones, the captions, small text and the diagram panel cannot be read | In docs/style.css, replace the dark rule on line 26 with: `@media (prefers-color-scheme:dark){.gtip{background:#222;color:#eee;border-color:#444}.glabel{fill:#aaa}.gpanel{color:#ddd}.ex-q,.ex-inputs button,.gkey,.gnote,.route,.prompt .ph,.steps p,.ex-grid th,figcaption,p.small,.small,button.copy{color:#b5b0a6}.lbl,.ex-grid td.n,.uma th,.steps .min,.ex-inputs button.on{color:#e39a8a;border-color:#e39a8a}.ex-grid td.p{color:#7fbf95}}`. Then the minis.js change: t() sets fill inline only when o.c is passed, and INK strokes use currentColor. | Line 45 sets button.copy to #666 and overrides the dark rule. Put the new rule after line 45 or raise its specificity. Render in dark mode at 390 px before shipping.

**2. playbook-5** (absorbs readme-5, start-8 and playbook-11) | No source needed; the contradiction was confirmed by grep | WORTH IT: the starter file the site links tells agents to poll, which the essay says not to do | In setup/CLAUDE.md: `- **Background anything that outlives a couple of minutes, and wait on a condition, not a timer.** Chain the next step in the scheduler (job dependencies), or run one background check that ends when the job leaves the queue or its output file appears. Give every wait a deadline, because a hung job never writes its file. Do not poll from the conversation, and do not sit in a foreground call waiting for a job to finish.` Also in setup/CLAUDE.md and setup/README.md: replace all 14 and 12 em dashes with a colon, comma or full stop; replace "`TaskCreate` at the start, `TaskUpdate` as work progresses" with "Write the task list down at the start and update it as work progresses"; cut the "Prefer dedicated tools over Bash" bullet; replace "Coding without a plan breaks more than it builds." with "Write down which files will change and how each change will be checked." | Deleting the Cowork section (from start-8) is the author's call. skills/README.md also has 9 em dashes.

**3. readme-6** | No source needed | WORTH IT: the install command silently overwrites an existing rules file | In setup/README.md, before each curl line: `# This replaces any existing ~/.claude/CLAUDE.md. Keep a copy first (-n: never overwrite an earlier backup).` and `[ -e ~/.claude/CLAUDE.md ] && cp -n ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak`. Do the same for ./CLAUDE.md. |

**4. index:start-4** | VERIFIED (B7: "requires a Pro, Max, Team, Enterprise, or Console account. The free claude.ai plan does not include Claude Code access.") | WORTH IT: otherwise a free-account reader is stuck at step 1 | `1. Install <a href="https://code.claude.com/docs/en/setup">Claude Code</a> (it needs a paid Claude plan or API credits; the free plan does not include it). Open it in a folder whose contents you already know.<br>` |

**5. index:start-5** (trimmed so the list stays at five steps) | No source in the text (the Teaching Tech Together quote is only in the rationale) | WORTH IT: no blank page, and a first-day check-fails-once exercise | Step 4: `4. Copy the <a href="examples.html#a-rules-file">five-line rules file</a> into CLAUDE.md and fill in the brackets. Add a line after each mistake.<br>` Step 5: `5. Make one check fail. Copy an input with only its header line (<code>head -n 1 input.tsv &gt; empty.tsv</code>), run your first step on it, and see whether anything says no. If nothing does, write the check that would, and watch it say no.</p>` | This replaces the current step 5 instead of adding a step.

**6. index:failures-6** | VERIFIED against the author's own files (the diagrams.js tooltip, the project CLAUDE.md, playbook rule 5) | WORTH IT: the site promises "dates and numbers", and the tooltip that holds them is invisible on phones | Add rows as proposed. The wrong unit: `<dt class="lbl">Mine</dt><dd>4 September: 48 items in 6 groups. +0.45 pooled, −0.11 within the groups (p = 0.47).</dd>` The silent guess: `<dt class="lbl">Mine</dt><dd>A search setting my notes never mentioned changed the result for 732 of 13,663 genes. One filtering step was written down nowhere.</dd>` Lost at the last step: `<dt class="lbl">Mine</dt><dd>4 September: 25 minutes of finished GPU work, lost to a formatting bug in one summary line.</dd>` Two agents: `<dt class="lbl">Mine</dt><dd>Both, on 10 September.</dd>` Shorten the clean-diagram BLOCKED tooltip to `'Cannot be computed from the text. The agent stops here and says so.'` | I added the 4 September date to the GPU line, from CLAUDE.md. Skip the stale row if failures-7 is applied.

**7. index:principles-3** with the #models sentence from principles-4 | VERIFIED for the supporting facts (B4: METR "modifying the tests or scoring code"; every trajectory on one RE-Bench task; 0.7% on HCAST; "substantially more often" stated as an impression) | WORTH IT: swaps a purchasing tip for a checking principle the site argues and never states | `<li><b>Keep the check out of the agent's reach.</b> A check it can edit is a check it can make pass. <a href="#quiet">Why</a></li>`. In #models: `In research, being wrong is expensive almost everywhere, so I use the strongest model for design, interpretation and review.` | Skip principles-4 and principles-5. Pair this with quiet-1.

**8. index:quiet-1** | VERIFIED (B4, quote verbatim) | WORTH IT: says where checks should live, which is practical | As proposed: after "...so it becomes the target.": `METR saw the same in frontier models on its own tasks: "attempting (often successfully) to get a higher score by modifying the tests or scoring code" (<a href="https://metr.org/blog/2025-06-05-recent-reward-hacking/">METR 2025</a>). So a check the working session can edit is a check it can make pass. The checks that matter should sit where it cannot write: a git hook, a file it has no permission to change, or a review by a session that did not write the code.` |

**9. index:failures-12** | No source; the case on the page itself (−0.11, p 0.47) shows no trend within groups | WORTH IT: the picture currently shows a reversal the data do not have | As proposed in minis.js unit(): y=c[1]+r()*10; flat group lines (y1 = y2 = c[1]+5); label `'within each group: no trend'`; update the comment. |

**10. index:failures-13** | No source | WORTH IT: the empty-control picture currently reads as "did not pass", which is the opposite of the case | As proposed: badge text 'PASS', a small red strike from the empty bar to the badge, and `t(s,216,102,'from no data',{a:'middle',c:RED})`. Remove the strike through the badge. | Render to check.

**11. session-7** | VERIFIED locally (about 3,460 words, about 15 minutes; the failures section is about 380 words) | WORTH IT: "10 minutes" is wrong, and the page contradicts itself | In build_pages.py se: `<p>Optional: read the <a href="index.html#failures">seven failure patterns</a> (a few minutes; the whole essay takes about 15) and pick the one you think you would have missed. We can start there.</p>` |

**12. index:opening-and-structure-4 + index:principles-6** | No source | WORTH IT: the word "rules" collides with the rules file, and the most practical section is missing from the route line | `<p class="route"><a href="#principles">Read the eight principles</a> · <a href="#start">Start in five steps</a> · <a href="examples.html">Copy the prompts and files</a> · <a href="session.html">Try it on your project with me (20 minutes)</a></p>` |

**13. site-wide-visual-and-navigation-2** (instead of principles-7) | No source | WORTH IT: the case links land at the top of the section on phones | Card ids: empty-control, finished-empty, wrong-unit, silent-guess, self-compare, last-step, two-agents. Principle 3 links #empty-control, principle 5 links #wrong-unit, principle 7 links #silent-guess. Add `.pat[id]{scroll-margin-top:1.2em}`. In build_pages.py, link "seven failure patterns" to index.html#failures. | Session-7 already adds that link.

**14. index:rules-1** | No source needed. "About 3 times the dose, matched on a counter" agrees with the project CLAUDE.md (3.4x on the accepted-swap counter). | WORTH IT: the bench analogies make the 4 September list readable | `1. A control got about three times the dose of the condition it was meant to control, because the two were matched on a counter instead of on how much actually changed. Fixing it moved the main result from 0.21–0.39 to 0.60–0.78.<br>2. A "no effect" result came from a condition in which almost nothing had actually changed. The bench version: reporting no phenotype from a knockdown that nobody checked had knocked anything down.<br>` |

**15. examples-3** | VERIFIED locally (the snippet runs, says no to both bad inputs, accepts the good one) | WORTH IT: the only copyable "rule in code" | As proposed (section "A check in code", the snippet, and the link sentence in index.html after "find the line that calls it"). |

**16. examples-4** | The edit text cites nothing. Lithgow (C14) is in the rationale only and is FIXABLE there: three worm labs needed more than a year of pilot experiments to remove between-lab differences. | WORTH IT: puts the main habit into the file people actually copy | Template lines: `Raw data is in [path]. Never modify or delete it. Write outputs to [path].` / `Read STATUS.md, and BRIEF.md if there is one, before starting.` / `Load software with: [your exact module or conda commands]` / `A job is finished when its output file has been checked, not when it exits.` / `Before trusting a new check, run it once on an input that should fail and show me that it says no.` Intro: `The agent starts every session knowing nothing about your lab, so write it like the sheet you give a rotation student on day one: where things are, what not to touch, what went wrong last time.` |

**17. examples-5** | Beck is cited in the rationale only | WORTH IT: short; aims the review at edits to the checks themselves | `Another session worked on this today. Read its commits and output files, not its summary. First list every check, threshold, filter or expected value it changed or removed, with the diff for each. Then: what was actually done, and what is not supported?` |

**18. playbook-9** | VERIFIED (C3, Noble: "create each output file using a temporary name, and then rename the file after it is complete ... prevents partial results from being mistaken for full results") | WORTH IT: a real, cheap protection against a killed job | Rule 12 opening: `Save results before printing a summary. Write each output under a temporary name and rename it when it is complete, so a killed job never leaves a file that looks finished.` (then the rest of rule 12 unchanged) |

**19. index:long-2** | No factual claim | WORTH IT: the timeline's point is unreachable without dragging the slider, and the boxes cannot be reached by keyboard | As proposed: initial value n-1; rects get tabindex, aria-label and tap-to-pin; a gkey list; short labels on wide screens. New caption: `<figcaption>By the sixth step, the first three exist in the conversation only as a summary. The files still hold all six. Drag the slider back to see the start.</figcaption>` | Render at 390 and 1024 px.

**20. index:setup-3** | No factual claim | WORTH IT: the loop diagram does not draw the chat side it is contrasted with, and its labels vanish on phones | Caption: `<figcaption>In chat, the model hands you text and you run it. An agent reads, runs and fixes on its own until it decides it is done. What it hands back is its own account; the files are the evidence.</figcaption>` plus the diagrams.js and graph.js changes as proposed. | Render-check the narrow layout.

**21. index:setup-2** | VERIFIED (B8: Remote Control "connects claude.ai/code or the Claude app for iOS and Android to a Claude Code session running on your machine") | WORTH IT: tmux, Slurm and Remote Control are not explained anywhere | `<p>I run it on the university cluster, where a scheduler (Slurm) hands computers to jobs from a queue. Each project gets its own session inside tmux, a program that keeps a session running after I disconnect, and I usually have several going at once on the strongest available model. I answer most of their [questions and approval requests] from my phone through Remote Control, a Claude Code feature that lets the Claude app reach a session still running on the cluster. From 2 September to 2 October I ran about 75 sessions on the cluster and about 10 on my laptop. I used Codex in 3 sessions.</p>` | NEEDS CHEN: which of the two he answers from the phone.

**22. session-3** | No source | WORTH IT: the box should promise what the walkthrough page promises | CTA text: `In 20 minutes, on your screen: you leave with a five-line rules file for your project, one real task already tried, and one check you have watched say no.` | "say no" matches session.html.

**23. index:modes-4** | No source; the table text matches the diagrams.js tooltips, moved into first person | WORTH IT: the advice currently sits in tooltips a phone reader never opens | The table as proposed, plus `<p class="small">From watching every step (top) to checking only the result (bottom).</p>`. Remove the modes spec from diagrams.js and the caption sentence "Hover, tap or click each mode". |

**24. index:modes-8** | Source is the SRE workbook (D10). PENDING-D, but "canary" is a standard term | WORTH IT: a common way for a grad student to lose a night | `A check it can run that has been seen to fail. One sample or one chromosome taken through every stage and checked before the full set is launched (release engineers call this a canary). Small stages that each end in a file and a commit.` |

**25. index:modes-9** | FIXABLE (B5). GPT-5 at 2 h 17 min is verified. The release date (7 August 2025) is from Wikipedia; OpenAI's page refused the fetch. METR's wording differs from the paraphrase. | WORTH IT: puts the advice first, and dates the model | `<p>Plan a night as several short stages, each ending in a check. Benchmarks will not tell you how long a stage can be. METR measures the length of task (in human time) an agent completes half the time; for GPT-5 (released August 2025) it was about 2 hours 17 minutes. METR's own explanation says this measures how hard a task is, not how long an agent spends on it, and that on tasks of 90 minutes to 3 hours GPT-5 succeeded every time on about a third, failed every time on a third, and varied on the rest (<a href="https://metr.org/time-horizons/">METR</a>). Anthropic reports its own engineers' sessions went from about 10 to about 20 actions before a person stepped in, between February and August 2025 (<a href="https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic">Anthropic</a>).</p>` | The Anthropic sentence was not re-checked in this round.

**26. index:start-6** | FIXABLE (B1). n = 52 and the Python library Trio are verified. The paper says "a reduction in the evaluation score by 17% or two grade points" on a 27-point quiz. The 65–86% and 24–39% clusters are verified. The authors are at Anthropic, through the Anthropic Fellows Program. "Fixed their own errors" was not seen. | WORTH IT: the only advice on the site about learning a method while using an agent | `6. For a method you are still learning, do not let it write the code. Ask it how things work. In a randomized trial, 52 people learned a new Python library; the group with AI help scored 17% lower on a quiz of understanding, code reading and debugging, and was not significantly faster. Those who asked it only conceptual questions were among the highest scorers, and those who had it debug or check their code among the lowest (<a href="https://arxiv.org/abs/2601.20245">Shen and Tamkin 2026</a>).` | This makes six steps. If five is wanted, move it into #models or put it in reading-2 only.

**27. index:long-3** | VERIFIED (C1: Rule 1 "For Every Result, Keep Track of How It Was Produced", Rule 2 "Avoid Manual Data Manipulation Steps") | WORTH IT: one quotable sentence that links to rules readers already know | Add after the existing Long-sessions paragraph: `<p>The first two of Sandve and colleagues' <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285">Ten simple rules for reproducible computational research</a> (2013) are to keep track of how every result was produced and to avoid manual steps. A step done in the chat and never written to a file is the new manual step.</p>` | The proposal's first paragraph is identical to the live text.

**28. index:failures-18** | VERIFIED (C7: 193 experiments; none "described in sufficient detail in the original paper"; "had to seek clarifications from the original authors") | WORTH IT: shows that gaps in Methods sections are normal at field scale | `<p>The gap is common in published work. A project that set out to repeat 193 experiments from cancer biology papers found that none was described in enough detail in the original paper to design the repeat, so the team had to ask the original authors (<a href="https://doi.org/10.7554/eLife.67995">Errington et al. 2021</a>). Running this rebuild on my own Methods before submission finds those gaps before a reader does.</p>` | The last sentence is a claim about the author's own practice. Keep it only if he does this.

**29. index:failures-7** | VERIFIED (C6: nf-test by Forer and Schönherr, GigaScience 2025, snapshots, the nf-core standard; C5: the rewrites.bio quote is verbatim, in section 2.3) | WORTH IT: the hardest card to read becomes the everyday snapshot-test case | As proposed, but drop the closing rewrites.bio quote for length: `<dd>Every check passes, and every check compares the output with an earlier copy of itself: last week's table, a pinned input, a saved snapshot. Mine was a site built from another project's results. That project renamed a category, and for four days the site served the old name with every check green.</dd><dt class="lbl">What to do</dt><dd>Keep at least one check that compares with something outside the copy: a planted signal, a value worked out by hand, the source's corrections since the version you copied. Snapshot tests, which nf-core pipelines use through <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12616847/">nf-test</a>, catch change. If the snapshot was wrong from the start, they pass forever.</dd>` |

**30. index:failures-15** (supersedes site-wide-visual-and-navigation-5) | No source | WORTH IT: "your site" does not match the reader's case | As proposed: 'your copy'; checks label size 12; caption `'the checks compare the copy with itself'`. |

**31. index:quiet-10** | The Lipsitch source is in the rationale only, not the text | WORTH IT: naming the blank, the negative control and the spike-in makes the demo click for biologists | The three why[] strings as proposed. | Check "third check" against the 4-row grid. The proposal was written for 3 rows; with 4 rows it is "the last check".

**32. index:quiet-12** | VERIFIED (B6: Kurjan and Cribbs, 2026) | WORTH IT: trivial fix, links the primary source | `(Kurjan and Cribbs, <a href="https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1">FlowBench</a>)` |

**33. reading-1** | VERIFIED (B4: title "Recent Frontier Models Are Reward Hacking"; both quotes verbatim) | WORTH IT: short, and fills a gap in the Critiques list | `<p><a href="https://metr.org/blog/2025-06-05-recent-reward-hacking/">Recent frontier models are reward hacking</a> <span class="small">(METR, 2025)</span>. Models tried to raise their scores "by modifying the tests or scoring code", often successfully. "Detecting reward hacking can be quite difficult."</p>` |

**34. reading-3** (trimmed, with fixes) | FIXABLE (C8, C7, C9 and C11). Begley and Ellis verified (6 of 53, 11%, the controls quote). Errington verified. Ziemann: "a programmatic scan" plus manual checking, not "a script". Weissgerber verified, with a lowercase "many". **Schnell Rule 5 is WRONG**: it is "Every Entry Should Be Recorded with a Date, Subject, and Protocol". "Never erase" is not a rule title. Rule 6 is verified. | WORTH IT: the bench lineage persuades biologists | `<h2>From the bench</h2><p>The habits in the essay are older than agents.</p>` then: Begley `Amgen confirmed the findings of 6 of 53 landmark papers. Among the fixes they ask for: experiments "should include and show appropriate positive and negative controls".`; Errington as proposed; Ziemann `Excel turned gene names such as SEPT2 and MARCH1 into dates in about one fifth of papers with supplementary Excel gene lists. Nothing raised an error; a programmatic scan of the supplements found them.`; Schnell `The notebook habit, for code: "keep a record of how every result was produced".` (drop "never erase an entry"). | Drop Weissgerber: the analogy is a stretch. examples-8's rationale cites Schnell for "never erase" and is wrong for the same reason.

**35. reading-2** (trimmed to 4 entries, with fixes) | B entries VERIFIED or FIXABLE. Shen and Tamkin: "17% or two grade points"; the three high-scoring patterns include code generation followed by explanation, so "all asked for explanations" should read "asked for explanations, alone or alongside generated code". Prather: 21 students in a CS1 course, the quote is verbatim, avoid "direction". METR 2026: 57 developers, 800+ tasks, "unreliable signal", selection, lower bound. Simkute, Lee and See, Parasuraman and Manzey: PENDING-A. Budzyń, Messeri: PENDING-D. | WORTH IT: the Reading page has nothing on what using these tools does to the person | Heading `<h2>What it does to the person using it</h2>` then: Shen and Tamkin `Randomized: 52 people learning a new Python library. With AI they scored 17% lower on a quiz of concepts, code reading and debugging, and were not significantly faster. The high scorers asked for explanations, alone or alongside generated code.`; Prather as proposed, with "Those who already knew what code they meant to write..." kept as paraphrase; METR `The follow-up to the 2025 trial in the essay. With 57 developers and 800+ tasks the data gave "an unreliable signal", partly because developers who did not want to work without AI stayed out of the study. METR reads its estimate as a lower bound on the speedup.` Add Messeri and Crockett, and Simkute, only after A and D confirm. | Also update the essay's "METR is repeating it" to "METR changed the study design in 2026 and now reads its numbers as a lower bound".

**36. examples-8** | The edit text has no citation. Its rationale's Schnell "never erase" is wrong (see reading-3). | WORTH IT: small, and matches playbook rule 12 | Add to the status template: `## Corrections` / `- [date] [what was wrong], replaced by [what]. Old output kept in [file], not deleted.` |

**37. index:principles-8** | No source | WORTH IT: glosses BLOCKED the first time it appears | Principle 7: `A gap is marked BLOCKED (cannot be computed from what is written), never guessed.` |

**38. index:principles-9** (partly overtaken) | No source | WORTH IT: one short clause | `<li><b>Files are the record, not the chat.</b> Brief, task list, status, commit. Review from those, not from the agent's summary. <a href="#long">Why</a></li>` |

**39. index:start-3** | Its "wrong" claim is stale, since examples now has a brief | WORTH IT: the section is still redundant and cutting it shortens the page | Delete `<h2>More</h2>` and its paragraph. |

**40. index:harder-3 + index:harder-4 (minimum version)** | No new source needed for the minimum version. The full harder-4 is PENDING-D (Mayo p. 5 and the Duke example). | WORTH IT: removes a second-hand Popper quote and fixes an overclaim | `<p>Deborah Mayo's name for a check that could have said no is a severe test: only infer what the procedure had a real chance of showing to be wrong (<a href="https://www.journals.uchicago.edu/doi/abs/10.1093/bjps/axl003">Mayo and Spanos 2006</a>). An exit code is not a severe test of a biological result. A planted signal that the pipeline must find is a severe test of the pipeline, for the error you planted. It says nothing yet about the biology.</p>` |

**41. playbook-8** | No number in the edit text. The optional Yuan figure is PENDING-D. | WORTH IT: names the code pattern that most often fakes "done" | `10. A job is done when the scheduler reports completion and the output file has been checked. Exit code 0 is not enough. Do not write error handlers that print a warning and carry on (`except: pass`, `|| true`, `2>/dev/null`); let the step fail, or record the failure in the output where the check will see it.` |

**42. index:failures-10** | PENDING-D (Yuan: 48 catastrophic failures, 25% from ignored errors) | WORTH IT once the figure is confirmed; it includes the R form readers use | As proposed. If D does not confirm 25% and 48, drop the citation sentence and keep the instruction. |

**43. playbook-6** (minimum version) | VERIFIED locally (7 of 27 rules have brackets) | WORTH IT: the header is currently false | `Each rule exists because breaking it cost something. Where one incident explains a rule, it is in brackets.` | The [code: ...] tags need the author to fill them. Optional.

**44. playbook-7** | Not verifiable: the unit is lost | WORTH IT: fallback | `[An unrelated job held the GPU at 99%; a benchmark read about a sixth of its real speed.]` | Use units instead if the author remembers them.

**45. index:tasks-1** | NEEDS CHEN: no external source; two checks and one sentence describe his practice | WORTH IT if he confirms: it puts the thesis onto the reader's own task list | As proposed. Replace any unconfirmed check with "No formal check yet." |

**46. site-wide-visual-and-navigation-7** | VERIFIED (B9: d3@7 resolves to 7.9.0, license ISC) | WORTH IT: one change removes a blank-page failure mode | As proposed: docs/vendor/d3-7.9.0.min.js; both script tags; the block-the-CDN test. |

**47. index:modes-3** | PENDING-A (the Endsley and Kiris quote) | WORTH IT for the active step; the citation can wait | Without the citation: `I open my phone when a session asks for something, and otherwise leave it alone. Review in one batch, from the files and commits, with a fresh session that did not do the work. Then open one output file and check one number against something already known. A fresh session's report is still something you read.` | "I" only if the author does this.

**48. index:rules-3** (first sentence only) | The Watchdog part is PENDING-D | WORTH IT for the first sentence; the Prometheus example is niche for biologists | `So the last step of writing a check is to find the line that calls it, then send a known-bad input through the real pipeline and watch the stop arrive where someone will read it.` |

**49. index:harder-7** | PENDING-A (Bainbridge quotes, the text layer of the ckrybus PDF) | WORTH IT once confirmed: "camouflage" is the 1983 version of the FlowBench finding, and the gwern scan is not searchable | As proposed, if A confirms the quotes. |

**50. index:modes-5** | PENDING-A (Onnasch: 18 experiments, the critical boundary) | WORTH IT once confirmed (text only, no divider) | As proposed, first paragraph only. |

**51. index:failures-3** | VERIFIED (C13: "The `Scripts/` directory contains `.Rmd` files that generate the graphics shown below.") | WORTH IT: one line of honest credit | `<p class="small">One picture per mistake is borrowed from Chenxin Li's <a href="https://github.com/cxli233/FriendsDontLetFriends">Friends Don't Let Friends Make Bad Graphs</a>, whose Scripts folder holds the code behind its pictures.</p>` |

**52. index:principles-2** | FIXABLE (C2, C4, C5). The SWC quotes are verbatim; the lesson presents test-driven development as the remedy for confirmation bias. Noble and Wilson are verified. The second rewrites.bio sentence was not seen. | WORTH IT: honest credit, and it pre-empts "this is just Software Carpentry" | `<p class="small">Most of these are not new. The Software Carpentry lesson on <a href="https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html">defensive programming</a> warns that tests written after the code tend "to show that their code is correct, rather than to find errors", and its rule is "turn bugs into assertions or tests". Keeping the record in files comes from Noble's <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424">guide to organizing computational biology projects</a> (2009) and <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510">Good enough practices in scientific computing</a> (Wilson et al. 2017). What changed is how fast an agent produces work that needs them. The numbered form is borrowed from <a href="https://rewrites.bio/">rewrites.bio</a> (Seqera), guidelines for rewriting bioinformatics tools with AI.</p>` | I dropped the rewrites.bio quote until its second sentence is seen at the source.

**53. index:failures-11** | No source (standard term) | WORTH IT: one sentence that maps onto a bench reflex | As proposed. |

**54. index:failures-14** | No source | WORTH IT (minor) | `t(s,20,130,'crashed at print; nothing saved',{c:RED});` |

**55. index:failures-16** | No source; pixel overflow per the proposal | WORTH IT (minor) | As proposed. | Render-check.

**56. index:failures-17** (caption alternative) | No source | WORTH IT: cheaper than moving the figure | Start the clean caption with "For the silent guess: have an agent rebuild your results...". |

**57. index:quiet-3** | VERIFIED (C12: Soergel quotes verbatim, "rank speculation"; C9: Ziemann one fifth, SEPT2 and MARCH1) | WORTH IT, trimmed: removes the hand-wave and adds the Excel case every genomics reader knows | As proposed, minus "Two things outside my notes say the filter is real. The first is older than agents." Start that part with "David Soergel argued in 2015..." | It is longer. If the page must stay short, drop the Excel sentences first.

**58. site-wide-visual-and-navigation-8** | No source needed | WORTH IT for maintenance, not for readers: the site's own rules as code | As proposed (tools/check_site.py and a pre-push hook). |

**59. index:failures-19** | VERIFIED locally (bash 3, zsh 1) | WORTH IT, lower: a big build. Start with loop_runs_once.sh and empty_control.R | As proposed. |

**60. index:failures-2** | No source | WORTH IT (minor): reports instead of forecasting | `<h2 id="failures">Seven ways it went wrong</h2>` |

**61. examples-6** | No source | WORTH IT only if the author uses these prompts | As proposed. |

**62. index:start-7** | NEEDS CHEN | WORTH IT: honest, and applies the site's thesis to itself | Use the fallback unless a planted-error test was done: `Written with Claude Code from my own session logs and notes. I checked each number against the file it came from; I have not tested that check. Mistakes are mine.` |

## SKIP

- **index:opening-and-structure-3** | No source | SKIP: the alternative placement was already decided by applying item 2.
- **index:principles-4** | No source | SKIP: resolved in favour of principles-3. Its #models sentence is used above.
- **index:principles-5** | PENDING-A | SKIP: conflicts with principles-3, and the caveat suits #models better.
- **index:principles-7** | No source | SKIP: duplicates site-wide-2, which has better ids.
- **site-wide-visual-and-navigation-5** | No source | SKIP: duplicate of failures-15.
- **site-wide-visual-and-navigation-4** | No source | SKIP for now: a large recolour with little reader payoff. If anything, recolour only BLOCKED, to tell it apart from FAIL (the reds are 1.41:1).
- **readme-5** | No source | SKIP: merged into playbook-5 (row 2).
- **index:start-8** | No source | SKIP: merged into playbook-5.
- **playbook-11** | No source | SKIP: merged into playbook-5.
- **playbook-10** | No source | SKIP: the author already chose to keep these rules public. Structural, not about correctness.
- **index:rules-2** | PENDING-A | SKIP for the essay: it adds two citations to the thesis paragraph, and #harder already carries the human-factors argument. Reconsider if the "n=1" objection matters.
- **index:rules-4** | PENDING-D (Strathern) | SKIP: repeats "a clean exit becomes the target". The gate-passes-the-wrong-unit point could be one line in #rules later.
- **index:harder-2** | PENDING (Parasuraman and Riley, A3) | SKIP: the use/misuse/disuse/abuse table scans well on a phone, and three reviewers want it kept.
- **index:harder-4 (full move)** | PENDING-D | SKIP the full version: about twice as long. The minimum version is used above.
- **index:harder-8** | PENDING-D | SKIP in the essay: it lengthens a section already called too long. Budzyń and Messeri can go in reading-2 once D confirms.
- **index:modes-2** | PENDING-A (Warm 2008) | SKIP: "Do not watch it" already stands, and this adds a citation. Fix the stale "METR is repeating it" via the reading-2 note instead.
- **index:modes-7** | No source | SKIP: the Goes well / Goes badly pair is the most scannable part of the subsection.
- **index:quiet-2** | PENDING-D (Duhem) | SKIP: philosophy that lengthens the strongest paragraph. quiet-1 does the practical job.
- **index:quiet-6** | PENDING-D (Teaching Tech Together, 13.6%) | SKIP: software-classroom detail inside a bench-controls paragraph. The minimal fix is to cite DeMillo, Lipton and Sayward 1978 for the date (D13, pending).
- **index:quiet-7** | PENDING-D (Just et al.; the 17% was unconfirmed even by the proposer) | SKIP: same reason as quiet-6.
- **index:quiet-13** | PENDING-D (the author et al. 2009) | SKIP: a second software-testing term in an already long caption.

---

## Addendum: philosophy, testing and site-reliability sources (D), reported after the file was written

All of the following replace the PENDING-D marks above.

- **modes-8**: VERIFIED. The SRE workbook defines canarying as "a partial and time-limited deployment of a change in a service and its evaluation". The edit text stands.
- **failures-10 and playbook-8 (optional figure)**: VERIFIED (Yuan, OSDI 2014). 198 sampled failures, 48 of them catastrophic. "25% of the catastrophic failures were caused by ignoring explicit errors". 35% covers all trivial mistakes in error handling (Finding 11). The failures-10 text stands as proposed.
- **rules-3**: VERIFIED. "This alert is always firing." is verbatim. The runbook says to alert externally when the Watchdog stops firing, with DeadMansSnitch as the example. The second quoted sentence was seen only as a paraphrase. The full proposed text is accurate as written. It stays at "first sentence only" for editorial reasons.
- **harder-4**: VERIFIED, with one fix. The Mayo quote is on p. 5, "bad evidence, no test" is her phrase, and the Duke example is on pp. 5–6. "No better than chance" is Mayo's own sentence; Coombes et al., whom she quotes, say "predictions are poor". The Franklin and Perovic calibration point is verified: "a surrogate signal that has been established independently of the apparatus being calibrated". The full version is now usable, but the SKIP for length stands.
- **harder-8**: VERIFIED. Budzyń: four centres in Poland, 28.4% (226 of 795) to 22.4% (145 of 648), "might reduce". Messeri and Crockett: "a phase of scientific enquiry in which we produce more but understand less". Still SKIP in the essay. Both entries in reading-2 are now cleared, so add them back there, worded as proposed.
- **rules-4**: FIXABLE. The citation is verified (European Review 5(3):305–321, 1997), but the quote was seen only second-hand (FORRT glossary, p. 308). The SKIP stands.
- **quiet-2**: VERIFIED, with one fix. Duhem's point is in the Stanford Encyclopedia of Philosophy; the book is dated 1914, 2nd edition. The SKIP stands.
- **quiet-6**: VERIFIED as reported in Teaching Tech Together. 13.6%; 90% of tests very similar. The Association for Computing Machinery abstract was not seen. The start-5 rationale quote "novices should never start doing exercises with a blank page or screen" is verbatim. The SKIP stands.
- **quiet-7**: VERIFIED. Just et al. 2014: 357 real faults, 5 programs, a significant correlation, and "17% of real faults ... are not coupled to any mutants". The SKIP stands.
- **quiet-13**: VERIFIED. the author, Ho, Liu and Xie 2009: GNLab and SeqMap, "artificially fault-seeded programs". The SKIP stands.
- **Mutation testing date ("1978" in #quiet)**: VERIFIED. DeMillo, Lipton and Sayward, "Hints on Test Data Selection", IEEE Computer 11(4):34–41, 1978. Cheapest fix: link this citation after "1978" in the live text. The DOI was seen only in search results.

## Addendum: human-factors sources (A), all now checked

- **harder-7**: VERIFIED. All three Bainbridge quotes are verbatim. The "camouflage" sentence opens with "Unfortunately". The citation is Automatica 19(6):775-779. The ckrybus PDF has a text layer. Apply as proposed. This moves into the WORTH IT list at about rank 30.
- **modes-3**: VERIFIED. Endsley and Kiris: "the shift from active to passive processing was most likely responsible for decreased SA under automated conditions". The citation can be added back.
- **modes-5**: VERIFIED. Onnasch et al.: 18 experiments; routine benefit; failure and situation-awareness cost; the critical-boundary sentence is verbatim, lowercase inside the sentence. The text stands.
- **modes-2**: VERIFIED, with one fix. Warm et al.'s title is exact. The abstract says "This research applies to most human-machine systems that require human monitoring...". The SKIP stands.
- **rules-2**: VERIFIED. "Cannot be prevented by training or instructions" is said of automation bias, as the proposal has it. "Occurs under conditions of multiple-task load" is said of complacency. Goddard's omission definition is verbatim. The SKIP stands for editorial reasons; the text is accurate if the author wants it.
- **principles-5**: VERIFIED. Goddard's reliability point should be cited as "particularly with automation deemed reliable", in the background attributed to Parasuraman. The SKIP stands.
- **harder-2**: VERIFIED. "Disuse, or the neglect or underutilization of automation". The SKIP stands.
- **reading-2**: Simkute VERIFIED (both quotes are in the abstract). Lee and See FIXABLE: the preprint reads "Design for appropriate trust not greater trust" with no comma, which is what the proposal already has. Parasuraman and Manzey VERIFIED. All eight entries are now cleared at the source. My trimmed recommendation stands: Shen and Tamkin, Prather, METR 2026, Messeri and Crockett, and optionally Simkute.
