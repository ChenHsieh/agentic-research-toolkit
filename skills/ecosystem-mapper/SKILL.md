---
name: ecosystem-mapper
description: >
  Map research fields, funding landscapes, and innovation ecosystems as interactive
  network graphs. Use this skill whenever the user wants to understand: who funds
  what in a field, who does research on what, how money flows through an academic
  or industry sector, which organizations dominate a space, or what the structure
  of an emerging field looks like. Trigger for phrases like "ecosystem map",
  "field map", "funding landscape", "who funds X", "map the X space", "who are
  the players in X", "show me how X is funded", "research landscape for X",
  "map the ecosystem", "landscape analysis". Produces a self-contained interactive
  HTML visualization from public data sources — no setup required. Funding is
  always a first-class layer in every map produced. Use this skill even if the
  user only mentions "research" or "organizations" in a field — the funding layer
  will make the result dramatically more useful.
---

# Ecosystem Mapper

You map research fields, funding landscapes, and innovation ecosystems as interactive network graphs. Every map shows who does what, who funds whom, and how the pieces connect — starting from raw public data and ending with a working visualization the user can open in a browser.

## References to Read

Load the relevant reference before each phase:

- **Schema selection:** Read `references/schema_library.md` during Phase 1
- **Sprint execution:** Read `references/sprint_protocol.md` before each sprint
- **Visualization:** Read `references/visualization.md` during Phase 3
- **Due diligence:** Read `references/due_diligence.md` if requested

---

## Core Rules

1. **Evidence-first.** Every edge traces to a file in `data/raw/`. No AI-inferred connections — if you can't point to a line in a raw source file, the edge doesn't exist.

2. **Funding is always present.** Every map includes funder nodes and funding edges, even if the user only asked about "research" or "organizations". The funding layer is what makes a map useful for understanding how a field actually works — who sustains it, who directs it, where the money comes from.

3. **Shippable increments.** Each sprint produces a valid, quality-checked graph. The map is always in a working state between sprints.

4. **Dual-axis relevance.** Every node must be relevant to *both* dimensions of the topic (e.g. for "AI safety funding": must score on AI *and* safety, not just one). This is the single biggest guard against scope creep.

---

## Operating Mode

Read the user's message and detect which mode applies before doing anything else. The three modes differ primarily in **how often you pause for the user**, not in what you build.

**Auto mode** — The user explicitly says "auto mode", "no questions", "just build it", or similar. Pick a schema, run all sprints back-to-back, generate the visualization, and present the final map. No per-sprint checkpoints. One final summary at the end.

**Vibe mode** — The message names a specific topic and implies a data source or scope, but doesn't opt into auto mode. Proceed without asking. State your interpretation in one compact line:

> *"Mapping [topic] — [sources], targeting [scale]. Starting schema design now."*

Run sprints autonomously. One checkpoint after visualization asking "add more data, export CSV, done?".

**Guided mode** — The message is vague, asks "where do I start?", or doesn't name a data source. Ask one question via AskUserQuestion:

```
AskUserQuestion(
  question="What ecosystem do you want to map?",
  options=[
    "A research field — who works on what, publication and citation networks",
    "A funding landscape — who funds whom, grant flows, foundation giving",
    "A full ecosystem — research + funding + organizations + policy combined",
    "An innovation/startup ecosystem — companies, investors, spinouts, labs",
    "A cultural/creative industry — labels, creators, platforms, conglomerates",
    "Something else — I'll describe it"
  ]
)
```

If data sources or scale are still genuinely unclear after that, ask one more follow-up — but only one. Checkpoint after schema, and after each sprint.

### Checkpoint cadence

| Mode | Schema checkpoint | Per-sprint checkpoint | Final checkpoint |
|------|-------------------|-----------------------|------------------|
| Auto | no | no | summary only |
| Vibe | no | no | yes |
| Guided | yes | yes | yes |

**The bias is toward fewer interruptions.** Modern Claude models handle the full sprint cycle reliably. Checkpoints exist because *direction* decisions belong to the user, not because execution needs supervision.

**Tool availability note:** `AskUserQuestion` is only available in some environments. Check your tool list first. If unavailable, ask as plain text with numbered options.

---

## Modern Tool Integration

Use these when available — they materially improve the experience:

- **`TodoWrite`** — Create a todo list at the start of any multi-sprint project. Mark sprints in-progress and completed as you go. This is how the user sees live progress in Cowork mode.
- **`mcp__cowork__create_artifact`** — For maps the user will revisit, offer an artifact as an alternative to (or supplement to) the static `index.html` file. Artifacts persist across sessions and can refresh from connectors.
- **`mcp__mcp-registry__search_mcp_registry`** — Before falling back to `WebSearch`, check whether a specialized MCP exists for the data source (NIH, NCBI, bioRxiv, Crossref, etc). Domain MCPs are much faster and more structured than web search.
- **Parallel `WebSearch` / `WebFetch`** — Batch the first round of research calls in a single message with multiple tool uses. The biggest wall-clock win in any sprint.
- **Cowork output path** — Save final deliverables to `/sessions/<session>/mnt/outputs/<project-name>/` so the user can open them via `computer://` links. Keep the working directory for raw data and scripts.

---

## Phase 1: Schema Selection

Read `references/schema_library.md` now. Pick the template that best matches the topic — Research Field, Funding Landscape, Innovation Ecosystem, Policy Domain, Cultural Industry, Platform Ecosystem, or Full Ecosystem — and adapt it for the specific subject matter. Note any additional node/edge types the topic requires.

Present the chosen schema as two inline tables (node types, edge types). Add one line: *"I'll proceed with this schema. If it's wrong, redirect me before Sprint 1 completes."* Then move immediately to Phase 2.

**Sizing guideline:** 4–8 node types, 6–12 edge types. When in doubt, fewer is better — you can always add a type in a later sprint.

---

## Phase 2: Sprint Planning & Execution

State the sprint order with a one-line rationale per sprint, then start Sprint 1 immediately. No separate approval needed — the ordering logic is deterministic:

- **Foundation first:** Richest single source (usually a grant DB or publication API) — creates the backbone
- **Bridge builders next:** Sources that connect the most to existing nodes
- **Gap fillers last:** Policy docs, evaluator orgs, secondary publications

Read `references/sprint_protocol.md` before each sprint. Each sprint runs the full **FETCH → EXTRACT → VALIDATE → MERGE** cycle autonomously.

### After each sprint

Show the **Data Curation Funnel** (format below). Then:

- **Auto mode:** proceed to next sprint with no checkpoint.
- **Vibe mode:** proceed to next sprint with no checkpoint.
- **Guided mode:** ask one checkpoint:

```
AskUserQuestion(
  question="Sprint N complete — +X nodes, +Y edges (total: A nodes, B edges). Curation summary above. What next?",
  options=[
    "Continue to Sprint N+1",
    "Show me the graph now (generate viz)",
    "Run due diligence before continuing",
    "Skip remaining sprints — generate visualization",
    "Done — wrap up"
  ]
)
```

### When to stop adding sprints

Stop when any of these is true:
- Marginal new nodes per sprint drops below 20% of the previous sprint.
- Three consecutive sprints produce no new bridge nodes.
- The schema's planned sources are exhausted.
- In guided mode, the user has seen the map and is satisfied.

---

### Data Curation Funnel

Show this after each sprint's EXTRACT step. Use real numbers and 2–3 concrete examples per step — not placeholders.

```
📥 Fetched from source:         1,847 records

Step 1 — Topic keyword filter:  → 312 passed  (removed 1,535)
  Kept:    "AI alignment", "RLHF oversight", "constitutional AI"
  Removed: "climate ML", "protein folding", "cancer diagnostics"
  Logic:   title/abstract must contain ≥1 primary keyword; pure
           application domains excluded

Step 2 — Dual-axis relevance:   → 198 passed  (removed 114)
  Kept:    Anthropic (AI + safety), Redwood Research (org + alignment)
  Removed: OpenAI (AI, no safety framing), Turing Institute (safety,
           not AI-focused)

Step 3 — Deduplication:         → 184 passed  (merged 14)
  Merged:  "CHAI" / "Center for Human-Compatible AI" → chai_berkeley
  Merged:  "Paul Christiano" / "paulf_christiano_openai" → p_christiano

Step 4 — Borderline items:      18 auto-included (flagged for due diligence)
  Example: "ML Safety Newsletter" — informational role, included as
           publication node; flag if you want it excluded

✅ Adding to graph:             184 nodes, 267 edges
```

Borderline items auto-include and are logged in ROADMAP for due diligence review.

If a step drops a surprisingly large proportion of records, explain why.

---

## Phase 3: Visualization

Read `references/visualization.md` now. Generate `index.html` using the **Canvas 2D template** described in visualization.md (no external dependencies, no CDNs). Default emphasis: funding flows (funder nodes most prominent, funding edges most visible).

**Output path:** Save `index.html`, `ROADMAP.md`, `METHODOLOGY.md`, and `data/graph_data.json` to `/sessions/<session>/mnt/outputs/<project-name>/` so the user can view them via `computer://` links. Keep the scratch project directory for raw data and scripts.

**Verification (if computer use is enabled):** Open the generated HTML, screenshot it, and verify no console errors and visible nodes. Otherwise deliver as-is.

After generating, present the `computer://` link. Then:

- **Auto mode:** one-paragraph summary — nodes, edges, connectivity, bridge nodes, key findings. Done.
- **Vibe / Guided mode:** ask one checkpoint:

```
AskUserQuestion(
  question="Map is ready. What else?",
  options=[
    "Export nodes/edges as CSV",
    "Run another sprint to add more data",
    "Run due diligence",
    "Create a summary report (REPORT.md)",
    "Persist as a Cowork artifact I can re-open",
    "All done — package the project"
  ]
)
```

---

## Quality Check Suite

Run after every graph modification. All 13 must pass before proceeding:

1. No dangling edge references
2. No duplicate node IDs
3. No duplicate edge IDs
4. Orphan tolerance — nodes with zero edges are allowed only if tagged `"pending_edges": true`, and pending-edge nodes may not exceed 5% of total.
5. No NaN/Infinity/undefined in JSON
6. All nodes have required fields (id, type, label)
7. All edges have required fields (source, target, type)
8. All edge types valid per schema
9. All node types valid per schema
10. Bridge nodes detected and annotated — nodes appearing across ≥3 layers get `"is_bridge": true` written to `graph_data.json`.
11. Funding edges have amounts — only `funds` edges require `amount` + `year`. `eligible_for` edges (beneficiary/eligibility) do not.
12. Graph connectivity > 80% in the largest connected component, OR ≥90% of nodes are in the top-3 components AND the sub-component structure is documented in ROADMAP.
13. Raw data files exist in `data/raw/`

---

## Two-Document Pattern

Maintain two documentation files:

**ROADMAP.md** — Technical log. Append a new sprint section after each sprint; never rewrite existing sections. Tracks schema tables with counts, sprint data sources, bridge map decisions, quality check results, file structure.

**METHODOLOGY.md** — Narrative document. Rewrite fully after every ~3 sprints or when the scope changes; otherwise use targeted edits. Present tense, no script names, no file paths — this is the document you'd share with a collaborator.

See `references/documentation.md` for templates.

---

## Output Structure

```
[project-name]/                ← scratch directory (raw data + scripts)
├── data/
│   ├── graph_data.json
│   ├── raw/
│   │   ├── s1_<source>/
│   │   └── ...
│   └── staged/
└── scripts/
    ├── quality_check.py
    ├── generate_html.py
    ├── annotate_bridges.py
    ├── export_csv.py
    └── sN_extract_<source>.py

/sessions/<session>/mnt/outputs/<project-name>/   ← user-visible deliverables
├── index.html
├── ROADMAP.md
├── METHODOLOGY.md
└── graph_data.json
```
