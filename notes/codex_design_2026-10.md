# Design-principles research round — October 2026

## Scope and method

Read locally before researching: `docs/index.html`, `examples.html`, `reading.html`, `session.html`, `style.css`, `toc.js`, and `diagrams.js`. The live site is a restrained 38em Georgia essay with 17px/1.6 body text, a desktop-only fixed contents list at 1180px, D3 mini-diagrams and tooltips, seven concrete failure cases, reusable prompts, and a free 20-minute walkthrough. This is not a request for a new visual identity. Keep the plain, authored, research-notes quality; do not add gradients, emojis, generic cards, testimonial carousels, or inflated claims.

All linked sources below were opened before use. “Principle” means a design implication, not a claim that a source endorsed this exact implementation.

## 1. Long-form UI and typography

1. **Control measure, size, and leading together.** Butterick puts web body size at 15–25px, line spacing at 120–145%, and measure at 45–90 characters ([source](https://practicaltypography.com/summary-of-key-rules.html)).
   * How it applies: the existing `38em`, 17px, 1.6 layout is already in a sound range; its leading is intentionally generous.
   * Suggested change: retain the text column; make it explicit and resilient with `max-width: 38rem` (or measured `ch` testing), and test the essay at 200% zoom before changing type.

2. **Reading controls must survive user overrides.** WCAG’s visual-presentation guidance includes no more than 80 characters per line and lets users choose colors ([source](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html)).
   * How it applies: hard-coded serif text and warm paper background are good defaults, but very long paragraphs and small labels become harder under zoom.
   * Suggested change: add a small “Reading” disclosure near the title with links to print, normal/high contrast, and a CSS class that increases body size/leading; do not make it a floating app-like control.

3. **Keep body and muted text sufficiently distinct.** WCAG AA requires 4.5:1 for normal text (3:1 only for large text) ([source](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)).
   * How it applies: `#555` captions, `.small`, detail text, and `#888` prompt labels are meaning-bearing, not decoration.
   * Suggested change: audit every gray against `#fffefb`; darken `.small`, captions, summary text, and prompt labels until they clear their applicable contrast ratio in both themes.

4. **Side notes should be secondary, never a second reading track.** Long pages need headings that state the purpose of what follows, and screen-reader users navigate by heading/link lists ([source](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)).
   * How it applies: the side table of contents is useful on wide screens but disappears below 1180px; the main narrative should remain complete without it.
   * Suggested change: add a compact, ordinary in-flow “On this page” `<details>` after the introduction on every long page, while retaining the desktop rail.

5. **Do not use typography to simulate hierarchy that HTML does not contain.** GOV.UK calls for one descriptive H1 and headings that describe their following text ([source](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)).
   * How it applies: labels such as “You will see” and “What to do” are visually clear but are spans, making the failure-pattern cards harder to navigate semantically.
   * Suggested change: make each pattern an `article`; use short H4s or a description list for “Signal / Response / Case,” preserving the present quiet visual treatment.

## 2. Skimming, mobile UX, and information architecture

1. **Put the proposition and reader outcome in the first two paragraphs.** NN/g’s 232-person eye-tracking study found an F-shaped scan; it specifically recommends putting the important information in the first two paragraphs ([source](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/)).
   * How it applies: the introduction says what the page lists, but a phone visitor can miss that it includes usable prompts and a free walkthrough.
   * Suggested change: under the byline, add a two-sentence deck: “This is a field guide to using coding agents without mistaking a clean exit for a correct result. Start with eight rules, copy six prompts, or bring one real task to a 20-minute session.”

2. **Make the left edge carry meaning.** NN/g advises beginning subheads, paragraphs, and bullets with information-carrying words because readers scan down the left side ([source](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/)).
   * How it applies: headings such as “Why the failures are quiet” are evocative, but less scannable than the named problem.
   * Suggested change: retitle selected sections as “Quiet failures: why exit 0 is not evidence,” “Rules that stop work,” and “Overnight runs: a morning check first.” Keep the voice, but front-load the noun.

3. **Progressively disclose cases, not the action.** GOV.UK recommends starting with less, adding help only when needed, and designing for scanning ([source](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)).
   * How it applies: the seven failure cards correctly show “What to do” before the expandable story.
   * Suggested change: retain that pattern, but prepend a one-line “Do this now” prompt in each card (for example, “Print control row counts before interpreting a comparison”) and leave the personal incident in `<details>`.

4. **Give phone readers an intentional route, not a desktop page squeezed smaller.** The `.pat` grid collapses well below 600px, while the table of contents is absent and diagrams still rely heavily on hover.
   * How it applies: a reader arriving from Slack on a phone needs a fast choice between the essay, a prompt, and the session.
   * Suggested change: add a three-link in-flow index after the deck: “Read: eight principles · Copy: six prompts · Try: 20-minute walkthrough.” It is navigation, not a hero panel.

5. **Use direct names and short action copy.** GOV.UK says to minimize cognitive load, use users’ language, put important words first, and keep one idea per sentence ([source](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)).
   * How it applies: “Session” is ambiguous in a site about agent sessions; “Examples” does not say that it contains copyable files and prompts.
   * Suggested change: rename navigation labels to “Essay,” “Prompts & files,” “Reading,” and “20-minute walkthrough.” Keep file URLs if stability matters.

## 3. A personal offer without hype

1. **Let the useful work be the evidence.** 37signals describes sharing the reasoning behind a product as more useful than a hard sell ([source](https://37signals.com/podcast/build-an-audience/)).
   * How it applies: the essay’s dated mistakes, numbers, screenshots/diagrams, and six prompts already do this better than testimonials would.
   * Suggested change: place a small contextual link after “Starting”: “If you want to do the first five lines with me, here is exactly what happens in 20 minutes.” Do not add generic praise.

2. **Specify the exchange and its boundaries.** The current session page does this unusually well: 5/10/5 minutes, what to bring, and no protected data. Specificity lowers the social cost of asking.
   * How it applies: the homepage CTA says “what to try…” while the session page has a much more concrete promise.
   * Suggested change: replace the ellipsis with the exact outcome: “You leave with a five-line rules file and one real task tried in a folder you already know.”

3. **Use plain language as a credibility mechanism.** Graham argues that ordinary words and simple sentences leave readers’ energy for the idea, and that ornate wording can conceal lack of content ([source](https://paulgraham.com/simply.html?viewfullsite=1)).
   * How it applies: phrases like “friends and labmates first” and “Mistakes are mine” fit the site; “transform,” “unlock,” and “best practices” would not.
   * Suggested change: use the CTA label “Ask for a 20-minute walkthrough,” not “Book a free consultation,” and say who it is for: “UGA friends, labmates, and people I already know.”

4. **Make the author reachable as a person, with one low-friction route.** 37signals argues that a small organization can have the person responsible be reachable rather than hide behind a brand ([source](https://37signals.com/podcast/build-an-audience/)).
   * How it applies: “Message me on Slack, or open an issue” gives two routes but no named Slack handle or response expectation.
   * Suggested change: list a Slack handle/link and a single suggested message: “I work on [project]; I want to try [task]; I have Claude Code installed / need help installing it.” State “I reply when I can; no obligation.”

5. **Show a real artifact instead of inventing social proof.** The current page can demonstrate the session by linking its actual `CLAUDE.md`, `STATUS.md`, and six prompts.
   * How it applies: social proof would be weak or misleading without permission and context; the concrete materials are stronger.
   * Suggested change: add “What you will copy” beneath the CTA with three links: rules file, status file, and “try to break this result” prompt. This follows the “share the thought process” approach ([source](https://37signals.com/podcast/build-an-audience/)).

## 4. Diagrams and media

1. **An interaction should let a reader test an assumption or consequence.** Victor describes active readers as questioning assumptions, verifying claims, and exploring alternatives; reactive documents show consequences when assumptions change ([source](https://worrydream.com/ExplorableExplanations/)).
   * How it applies: the “clean exit,” rebuild, and rules diagrams reinforce the argument; some mode/tooltips provide essential content only on hover.
   * Suggested change: prioritize one new explorable: a “check that cannot fail” diagram with a toggle for empty control / shuffled labels / known-good positive control, showing which check says PASS, FAIL, or UNMEASURED.

2. **Begin with a concrete experience, then climb to abstraction.** Case advises starting grounded and moving step by step ([source](https://blog.ncase.me/how-i-make-an-explorable-explanation/)).
   * How it applies: “The empty control” is a strong concrete entry; the philosophical “why” comes after the reader has seen the failure.
   * Suggested change: open each major diagram caption with the observed event (“An output file can exist and still contain only a header”) before naming the general rule.

3. **Spend author effort where it saves repeated reader effort.** Distill calls poor exposition and missing interpretive labor “research debt” and treats explanation as substantive work ([source](https://distill.pub/2017/research-debt/)).
   * How it applies: the mini-diagrams are worth keeping because they compress recurring failure modes rather than decorate sections.
   * Suggested change: add a visible legend once near the first diagram (“you decide / agent acts / file records / check stops / failure”) and use it consistently in all diagrams.

4. **Do not hide required information in hover.** WCAG 2.2 requires hover/focus content to be dismissible, hoverable, and persistent under defined conditions ([source](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html)).
   * How it applies: captions instruct “Hover each mode”; on touch, the explanatory content may never be found. `tabindex` focus helps keyboard users, but does not solve touch disclosure.
   * Suggested change: make each node click/tap to toggle a pinned text panel below the SVG; support keyboard Enter/Space; show the first node’s explanation by default on narrow screens.

5. **Treat diagrams as content, not image-shaped decoration.** The D3 nodes include meaningful labels and tooltips but need an accessible equivalent.
   * How it applies: the diagrams explain the core argument; without an alternative, screen-reader users get little of it.
   * Suggested change: add an adjacent visually plain ordered list or `<details>` transcript for every diagram, with the same sequence and links; give SVGs titles/descriptions only as a supplement. GOV.UK notes that screen-reader users often encounter links in isolation ([source](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)).

## 5. Depth of thinking on agentic AI in research

1. **Automation shifts human work toward the abnormal and hardest cases.** Bainbridge notes that as control systems advance, human contribution can become more crucial, especially for abnormal conditions ([source](https://gwern.net/doc/sociology/technology/1983-bainbridge.pdf)).
   * How it applies: this explains why agents remove loud errors yet leave quiet ones—the essay already observes this, but could name the structural reason.
   * Suggested change: add a short “Why this gets harder, not easier” subsection after “Why the failures are quiet,” explicitly connecting automation to responsibility for exception detection and recovery.

2. **Separate use, misuse, disuse, and abuse.** Parasuraman and Riley define misuse as overreliance that can cause monitoring failures and decision biases; disuse often follows false alarms; abuse is automation deployed without regard to human performance ([source](https://web.mit.edu/16.459/www/parasuraman.pdf)).
   * How it applies: the essay has examples of misuse (trusting exit 0) and abuse (unbounded overnight jobs), but readers may see all caution as “do less automation.”
   * Suggested change: add a four-row table to the Reading page: term, agent example, guardrail. Include a “good use” row so the case is calibration, not abstinence.

3. **Treat felt confidence as weak evidence in noisy domains.** Kahneman and Klein conclude that judgment quality depends on environmental predictability and opportunities to learn its regularities; subjective experience is not reliable evidence of accuracy ([source](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf)).
   * How it applies: a fluent agent summary and a researcher’s familiar-looking plot can both feel right without feedback that distinguishes right from wrong.
   * Suggested change: amend the review prompt to ask: “What feedback would have made this judgement learnable? Which result is merely plausible?”

4. **Use a premortem before unattended runs.** Klein’s method assumes the project has already failed, then asks the group for plausible causes; it makes reservations safer to state ([source](https://hbr.org/2007/09/performing-a-project-premortem?trk=public_post_comment-text)).
   * How it applies: the existing overnight checklist begins with a morning check; a premortem would elicit failure-specific checks before launch.
   * Suggested change: add a copyable “Before leaving” prompt: “It is tomorrow morning and this run produced a persuasive but wrong result. List five ways; for each, add the smallest check that would expose it.”

## 6. Philosophy of science: checks that can fail

These are conceptual lenses, not an attempt to make a web essay into a philosophy survey. Exact short quotations are retained only where verified in the opened source.

1. **Popper: a check earns weight by risking a negative result.** “Every genuine test of a scientific theory… is logically an attempt to refute or to falsify it” ([source](https://plato.stanford.edu/archives/spr2007/entries/popper/)).
   * How it applies: “make every check fail once” is a practical falsificationist habit; an exit-code check alone forbids almost nothing about biological validity.
   * Suggested change: rename the principle link text “Why” to “What this check could rule out,” then give a counterexample input beside each reusable check.

2. **Feynman: report what could invalidate the result, not only what supports it.** He calls for “a kind of scientific integrity” and says an experimenter should report “other causes that could possibly explain your results” ([source](https://calteches.library.caltech.edu/51/2/CargoCult.htm?cid=71373971742)).
   * How it applies: the page is unusually honest about its author’s failures; that is stronger than a polished success narrative.
   * Suggested change: append a compact “What this page does not establish” note under major claims (for example, that 75 sessions is personal experience, not a controlled estimate of agent performance).

3. **Mayo: infer only what the procedure had a real chance to expose as wrong.** Mayo and Spanos say error probabilities should ensure that only hypotheses passing “severe or probative tests” are inferred ([source](https://www.journals.uchicago.edu/doi/abs/10.1093/bjps/axl003)).
   * How it applies: a null from a sampler that could barely move is not evidence of no effect; the site’s “power check” rule is exactly the relevant distinction.
   * Suggested change: revise the “Finished, but empty” and “wrong unit” examples to include “detection power / expected failure signal” alongside row count and range.

4. **Lakatos: judge a sequence of changes, not one protected result.** Lakatos’s framework treats a research programme—not a one-time theory—as the unit of appraisal; it can be progressive or degenerating ([source](https://plato.stanford.edu/archives/fall2020/entries/lakatos/)).
   * How it applies: an agent can patch one failed test until green. What matters is whether successive fixes create independently corroborated predictions rather than exceptions.
   * Suggested change: in `STATUS.md`, add “Prediction made before this run” and “What changed after failure”; in the morning review, flag a growing list of untested exception rules.

5. **Goodhart/Campbell warning: do not turn a proxy into completion itself.** Campbell writes that more use of a quantitative social indicator for decision-making makes it more subject to corruption pressure and more likely to distort what it monitors ([opened full text](https://jmde.journals.publicknowledgeproject.org/index.php/jmde_1/article/download/297/292/988)). Goodhart’s original formulation was not directly verified here.
   * How it applies: “agent exits cleanly” is a proxy that can become the target, exactly as the FlowBench discussion suggests.
   * Suggested change: label every automated success metric with its excluded failure modes: “exit 0 (does not establish non-empty, valid, or correctly grouped output).”

6. **Merton: organized skepticism is a social practice.** The National Academies summarizes Merton’s four norms as communal sharing, universalism, disinterestedness, and organized skepticism ([source](https://www.nationalacademies.org/read/1864/chapter/4)).
   * How it applies: a fresh session reviewing files and commits is useful precisely because it is not the worker’s own narrative.
   * Suggested change: turn “Review today’s work” into a two-person lab ritual for important results: author supplies files; reviewer attempts one counterexample; both record the result.

7. **Ioannidis and Gelman/Loken: flexible analysis creates error paths without fraud.** Gelman and Loken show that data-contingent choices can create multiple comparisons even when a researcher performs one analysis and is not consciously fishing ([source](https://sites.stat.columbia.edu/gelman/research/unpublished/forking.pdf)).
   * How it applies: an agent can try many plausible filters, normalizations, and thresholds faster than a person, then report a single clean path.
   * Suggested change: require the agent to write a machine-readable decision log: alternatives considered, data-dependent choices, discarded outputs, and predeclared primary analysis. Link that log from `STATUS.md`.

8. **Hacking: intervention is part of experimental knowledge, not an afterthought.** The Cambridge abstract for *Representing and Intervening* notes that philosophers often discuss theory while saying little about experiment, technology, and using knowledge to alter the world ([source](https://www.cambridge.org/core/books/abs/representing-and-intervening/experiment/3FE90708AE1142545425DAD7FA6D9DBE)).
   * How it applies: positive controls, shuffled labels, and intentionally broken inputs are interventions on the pipeline, not merely reports about it.
   * Suggested change: call the “make it fail once” section “Intervene on the check,” and list three intervention classes: known-good, known-bad, and sensitivity perturbation.

## Ranked: 15 concrete changes

1. **[5, S]** Add the copyable overnight premortem prompt and put it beside the existing overnight diagram.
2. **[4, M]** Replace hover-only node information with click/tap-pinned panels plus keyboard support and a text transcript.
3. **[2, S]** Add the two-sentence deck and in-flow “Read / Copy / Try” route below the essay byline.
4. **[6, S]** Add “run this check on a known-bad input” to each relevant prompt and failure pattern.
5. **[6, M]** Add a decision log (alternatives, discarded outputs, data-dependent choices) to the `STATUS.md` example.
6. **[3, S]** Replace “what to try…” in the homepage CTA with the exact 20-minute outcome; link to “What you will copy.”
7. **[1, S]** Run a WCAG contrast audit and darken low-contrast caption, `.small`, summary, and prompt-label colors.
8. **[2, S]** Add an in-flow `<details>` contents list to long pages for screens below the desktop rail breakpoint.
9. **[5, S]** Add “good use / misuse / disuse / abuse” examples to Reading, tied to the site’s own cases.
10. **[1, S]** Convert the visual “You will see / What to do” labels into navigable structural headings or a description list.
11. **[2, S]** Rename nav labels to “Prompts & files” and “20-minute walkthrough”; rename selected sections to front-load the problem.
12. **[4, S]** Add a consistent visual legend and an accessible list-form equivalent for every D3 diagram.
13. **[6, S]** Add a “What this does not establish” note under the most consequential personal/benchmark claims.
14. **[3, S]** Publish one named Slack contact route and a copyable three-part request template; state response expectations.
15. **[1, M]** Add a quiet reading/print/high-contrast disclosure and test the essay at 200% zoom and narrow widths.

## Not verified

* **The live rendered site** was not independently opened in this round; recommendations are grounded in the local `docs` source supplied in the workspace.
* **Tufte CSS, Edward Tufte’s data-ink formulation, Robert Bringhurst’s exact wording, Gwern’s design notes, and Every Layout** were not opened and are therefore not cited, even though their themes are relevant.
* **Patrick McKenzie**: no specific primary essay was identified and opened that supported a claim in this memo; none is cited.
* **Goodhart’s Law**: a primary original text was not opened. Campbell’s original paper was opened via its authorized reprint, but the Goodhart attribution is therefore kept qualified.
* **Ioannidis (2005)**: the PLOS page was found but the opened rendition returned an internal error, so this memo does not quote or rely on a specific claim from it. Gelman and Loken supply the cited flexible-analysis point.
* **Exact Hacking quotation**: only a Cambridge abstract was available and opened; the wording above is its abstract’s summary, not a quote from the book’s body.
* **Mobile usability outcomes and conversion** have not been user-tested on this site. The prioritized changes are hypotheses to test with a few friends/labmates on phones, not measured claims.
