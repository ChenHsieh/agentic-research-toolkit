---
name: trait-gene-miner
description: >
  Systematic workflow for mining experimentally validated genes associated with a biological trait from literature and ontology databases, with an interactive HTML dashboard output linking to source databases. Use whenever a user wants to collect, curate, or systematically identify genes linked to a phenotype or trait (e.g., flowering time, drought tolerance, seed size) from Planteome, Gramene, TAIR, Gene Ontology, or the literature. Trigger on: "genes associated with", "mine genes for", "collect gene sets for", "find genes validated for", "trait-gene list", "ontology-based gene mining", or any request to build a curated gene set for a biological trait. Also trigger when users want to explore trait-gene results interactively with links to PubMed, TAIR, RAP-DB, or MaizeGDB, download TSVs from ontology databases, or ask about evidence codes for gene-trait associations.
allowed-tools: Read Write Edit Bash Glob Grep WebSearch WebFetch
---

# Trait Gene Miner

A structured workflow for building a curated, reproducible, traceable set of experimentally validated genes associated with a biological trait of interest.

## ⚠️ Anti-Hallucination Rules (Read First — Always)

These rules are non-negotiable and apply to every step of this workflow:

1. **NEVER generate PMIDs from training memory.** Every PMID in the output must come from one of two traceable sources:
   - Extracted directly from a database association file (e.g., `PMID:12345678` in a Planteome `.assoc` file column)
   - Retrieved by the PubMed MCP tool (`search_articles` or `lookup_article_by_citation`) and verified by fetching the article page

2. **NEVER populate the gene_id field from training memory alone.** Gene IDs must come from a database file or a verified database lookup. If you know a gene symbol (e.g., "Hd3a") but cannot retrieve its stable locus ID from a file or API in this session, leave `gene_id` as the symbol and set `id_stable: false`.

3. **NEVER assign a PMID to a gene-trait association you did not retrieve and verify in this session.** Even if you are confident a paper exists, training-memory PMIDs have an ~80% hallucination rate for specific citation identifiers.

4. **Every PMID that will appear in the final output MUST be spot-checked** by fetching `https://pubmed.ncbi.nlm.nih.gov/{PMID}/` and confirming the title is consistent with the claimed gene and trait. Record verification status (`pmid_verified: true/false`) for each entry.

5. **Be explicit about what you don't know.** If a database file has no PMID for a record (e.g., Gramene's `GR_REF:XXXX`), record the reference as-is and mark `pmid_traceable: false`. Do not substitute a guess.

---

## Step 1: Define the Trait and Scope

Before querying anything, confirm with the user:

- **Trait of interest** — be specific (e.g., "photoperiod-dependent flowering" vs. "flowering time" vs. "floral transition"). Vague traits produce noisy gene sets.
- **Taxonomic scope** — which species or clade? Specify taxon IDs where possible (e.g., Poaceae; Oryza sativa taxon:4530; monocots).
- **Evidence stringency** — experimental only (recommended), or include expression/computational predictions?
- **Output format** — gene list, gene × evidence table, FASTA for BLAST?
- **Downstream use** — enrichment analysis, BLAST, literature review? This affects which ID format matters.

Use `AskUserQuestion` to collect these before starting any queries.

---

## Step 2: Ontology Term Identification

### 2a. Find Relevant Term IDs

Do **not** assume term IDs from training memory. Look them up:

1. Fetch the Planteome term browser: `https://planteome.org/` and search for the trait keyword
2. Fetch OBO Foundry: `https://obofoundry.org/` to find the right ontology namespace (TO, GO, PO, EO)
3. Use `WebSearch` with the query `site:obofoundry.org "{trait name}" ontology term` to find candidates

**Key ontology namespaces for plant traits:**
| Namespace | Covers | Example |
|-----------|--------|---------|
| TO | Plant phenotypic traits | TO:0000137 = heading date |
| GO (BP) | Molecular/biological process | GO:0010228 = veg-to-repro transition |
| PO | Plant anatomy + development | PO:0009049 = inflorescence |
| EO | Environmental conditions | EO:0007048 = short-day |

### 2b. Traverse Child Terms (Do Not Query Parent Terms Alone)

Ontology annotations are often made at child terms, not parent terms. Querying only the parent will miss genes annotated to more specific descendants.

For each target term, fetch its descendant terms:
```
https://www.ebi.ac.uk/ols4/api/ontologies/to/terms/{term_id_encoded}/descendants
```
Or use `WebSearch`: `"{TO:XXXXXXX}" descendants plant trait ontology`

Collect the full set of term IDs to query (parent + all descendants).

### 2c. Document the Term Set

Before querying, output a table of all ontology terms that will be queried:

```
| Term ID     | Term Label                        | Source   | Parent / Child of |
|-------------|-----------------------------------|----------|-------------------|
| TO:0000137  | heading date                      | TO       | — (queried)       |
| TO:0000344  | early flowering                   | TO       | child of TO:0002616 |
| GO:0010228  | veg-to-repro phase transition     | GO       | — (queried)       |
```

This table becomes the Methods section of the output and makes the query scope fully reproducible.

---

## Step 3: Database Downloads (Primary Evidence Source)

This is the highest-quality evidence tier because every gene-PMID link is curated by a database, not inferred by the AI.

### 3a. Download Planteome Association Files

```bash
# TO (Trait Ontology) associations
wget "https://gitweb.planteome.org/?p=associations/.git;a=blob_plain;f=to-associations/TO_Annotations_V6.zip;hb=HEAD" \
  -O TO_Annotations_V6.zip

# GO associations (warning: ~455MB)
wget "https://gitweb.planteome.org/?p=associations/.git;a=blob_plain;f=go-associations/GO_Annotations_V6.zip;hb=HEAD" \
  -O GO_Annotations_V6.zip
```

Record the download date and file size — include these in the dashboard header and methodology note.

### 3b. Parse GAF Format Files

Planteome uses GAF 2.0 format. Column mapping:

| Col | Field | Notes |
|-----|-------|-------|
| 1 | DB | e.g., GR_gene, Planteome |
| 2 | DB_Object_ID | Internal ID (e.g., GR:0060442) |
| 3 | DB_Object_Symbol | Gene symbol |
| 5 | Annotation_Class | Ontology term ID |
| 6 | DB_Reference | PMID or GR_REF |
| 7 | Evidence_Code | IMP, IDA, EXP, etc. |
| 10 | DB_Object_Name | Long gene name or locus |
| 11 | DB_Object_Synonym | Pipe-delimited: contains locus IDs |
| 13 | Taxon | taxon:XXXX |

**Critical parsing rule:** The stable locus ID (e.g., `Os06g0224500`, `LOC_Os06g16370`) is usually in column 11 (synonyms), not column 10 (name). Extract it with a regex:
```python
import re
def extract_locus_id(synonyms_field):
    for part in synonyms_field.split("|"):
        part = part.strip()
        if re.match(r"Os\d+g\d+", part) or part.startswith("LOC_Os"):
            return part
        if part.startswith("GRMZM") or part.startswith("Zm"):
            return part
        if part.startswith("Bradi") or part.startswith("Sobic"):
            return part
    return ""  # Return empty string, not the descriptive name
```

### 3c. Filter Criteria

Apply all three filters simultaneously:

**1. Ontology term filter:** Keep only rows where column 5 is in your target term set (from Step 2c).

**2. Evidence code filter — keep experimental only:**
| Code | Keep? | Rationale |
|------|-------|-----------|
| EXP | ✅ Yes | Direct experimental |
| IDA | ✅ Yes | Direct assay |
| IMP | ✅ Yes | Mutant phenotype |
| IGI | ✅ Yes | Genetic interaction |
| IPI | ✅ Yes | Physical interaction |
| IEP | ⚠️ Optional | Expression pattern only — mark as Tier 2 |
| IC  | ⚠️ Optional | Curator inference — mark as Tier 2, requires GR_REF check |
| ISS | ❌ No | Sequence similarity = computational |
| IEA | ❌ No | Electronic annotation = automated |

**3. Taxon filter:** Keep only taxa in the user's target clade. Use explicit taxon ID lists (not name matching, which is fragile):
```python
POACEAE_TAXA = {"4530","4577","4558","4513","4565","15368","4555","39947","4538"}
```

### 3d. Handle GR_REF References

When `DB_Reference` is `GR_REF:XXXX` (not a PMID):
- Set `pmid = ""` and `pmid_traceable = False`
- Set `reference = "GR_REF:XXXX"` to preserve the original reference
- Do **not** substitute a PMID from training memory
- Display in dashboard as `[GR_REF — see Gramene]` with a link to `https://www.gramene.org/`

To resolve GR_REF → PMID (optional, improves traceability):
- Fetch `https://www.gramene.org/` and search for the gene symbol
- The gene page often lists the source publications

---

## Step 4: Literature Mining via PubMed (Supplementary Evidence)

Use this step to find genes that are experimentally validated but **not yet in ontology databases** — particularly for non-model species (wheat, barley, sorghum, Brachypodium).

### 4a. Construct PubMed Queries

Use the PubMed MCP tool (`search_articles`) with targeted queries. Use OR-separated terms, not AND-heavy queries which return zero results:

```
# Good — returns results
("flowering time" OR "heading date" OR "floral transition") AND wheat AND mutant

# Bad — too restrictive, returns nothing
VRN1 VRN2 PPD1 vernalization wheat barley flowering cloned mutant
```

Run separate queries per species per sub-trait for better recall:
```
# Query set example for grass flowering:
1. heading date rice mutant overexpression gene
2. flowering time maize mutant gene cloned
3. vernalization wheat barley VRN gene
4. photoperiod sorghum flowering Ma1 maturity
5. Brachypodium flowering vernalization gene
```

### 4b. Extract Gene-PMID Pairs from Results

For each PMID returned:
1. Fetch the abstract using `get_article_metadata` or `get_full_text_article` MCP tools if available, or fetch `https://pubmed.ncbi.nlm.nih.gov/{PMID}/`
2. Read the title and abstract to identify: gene name/symbol, species, trait affected, evidence type
3. Only add a record if the abstract explicitly names a gene and describes an experimental mutant/overexpression phenotype
4. Record the PMID as retrieved from the search tool — **do not modify or guess the PMID**

### 4c. Mandatory PMID Verification

**Every PMID that will appear in the final output must be verified.** This is non-negotiable:

```python
# Verification protocol for each PMID
for gene, pmid in lit_records:
    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    page = WebFetch(url, prompt="Give the title and abstract of this paper.")

    # Check: does the paper actually describe this gene in this species?
    # BOTH must hold. Species match alone is not evidence -- any paper on the
    # right organism would rubber-stamp any gene claim about that organism.
    if gene_name in page.title and species in page.abstract:
        mark pmid_verified = True
    else:
        mark pmid_verified = False
        # Do NOT include this PMID in output
        # Either find the correct PMID or leave PMID blank
```

Set `pmid_verified = True` only when the fetched page title is consistent with the claimed gene-trait association. If verification fails, either:
- Find the correct PMID by re-running the PubMed query with more specific terms
- Leave the PMID field blank and mark `pmid_traceable = False`

### 4d. Gene ID Resolution for Literature Records

For genes found in literature, do NOT use gene IDs from training memory. Instead:
- Search RAP-DB for rice: `https://rapdb.dna.affrc.go.jp/search/result/irgsp1/{gene_symbol}`
- Search MaizeGDB for maize: `https://www.maizegdb.org/gene_center/gene/{gene_symbol}`
- Search Gramene for others: `https://www.gramene.org/` → gene search
- If no stable ID is found in this session, set `gene_id = gene_symbol` and `id_stable = False`

---

## Step 5: Gene ID Stability Assessment

Before merging, classify each record's ID stability. This determines which records are usable for downstream bioinformatics:

| ID Pattern | Stability | Usable for BLAST/enrichment? |
|------------|-----------|------------------------------|
| `Os06g0224500` or `LOC_Os06g16370` | ✅ Stable locus | Yes |
| `GRMZM2G179264` or `Zm00001d...` | ✅ Stable locus | Yes |
| `Bradi1g15670`, `Sobic.007G163800` | ✅ Stable locus | Yes |
| `AT1G65480` | ✅ Stable locus | Yes |
| `AY222645`, `HM005633` | ⚠️ GenBank accession | Sequence only, not gene |
| `HEADING DATE 3A`, `Black hull-b` | ❌ Descriptive name | No — needs resolution |
| `Hd1`, `VRN1` (symbol as ID) | ❌ Symbol only | No — not unique cross-species |

Add an `id_stable` boolean column to every record. In the dashboard, display a ⚠️ icon next to records where `id_stable = False` and link to the appropriate resolution database.

To resolve descriptive names → stable IDs:
- Use Gramene BioMart: `https://plants.ensembl.org/biomart/martview`
- For rice: RAP-DB batch query: `https://rapdb.dna.affrc.go.jp/tools/`
- For wheat/barley: URGI WheatIS: `https://urgi.versailles.inrae.fr/blast/`

---

## Step 6: Merge, Deduplicate, and Tier Assignment

### 6a. Merge All Sources

Combine records from:
- Planteome TO files (Step 3)
- GO association files (Step 3)
- Literature mining (Step 4)

Preserve `source` field for every record: `Planteome/TO`, `Planteome/GO`, `Gramene`, `Literature/PubMed`.

### 6b. Deduplicate

Deduplicate using a compound key: `(gene_id, ontology_term)`. If two sources report the same gene-term pair, keep the record with the better evidence, using this priority order:
1. Database record with verified PMID
2. Database record with GR_REF
3. Literature record with verified PMID
4. Literature record without verified PMID (lowest priority)

### 6c. Confidence Tier Assignment

Tier assignment must be based on traceable evidence, not term specificity alone:

| Tier | Criteria | Dashboard color |
|------|----------|----------------|
| **Tier 1** | Direct experimental evidence (IMP/IDA/EXP/IGI/IPI) to a core trait term + at least one traceable reference (PMID or GR_REF) | 🟢 Green |
| **Tier 2** | IEP evidence, or IC (curator inference), or indirect trait term, or no traceable reference | 🟡 Yellow |
| **Tier 3** | ISS/IEA evidence that slipped through, or unverified PMID, or descriptive-name gene ID | 🔴 Red |

**Important:** A gene with `pmid_verified = False` must be capped at Tier 2, regardless of evidence code. A gene with `id_stable = False` should be flagged but not automatically downgraded — the gene may still be valid.

### 6d. Coverage Assessment

After merging, produce a coverage summary table:

```
| Species            | Records | Traceable PMID | Stable ID | Tier 1 |
|--------------------|---------|----------------|-----------|--------|
| Oryza sativa       | 177     | 65 (37%)       | 39 (22%)  | 118    |
| Zea mays           | 10      | 8 (80%)        | 8 (80%)   | 8      |
...
```

If any species in the target clade has 0 records, flag this explicitly as a **database gap** (not evidence that the trait is absent). Suggest manual literature searches for those species.

---

## Step 7: Output

### Gene × Evidence Table (TSV)

Required columns:

```
gene_symbol | gene_id | id_stable | species | taxon_id | ontology_term | ontology_label | evidence_code | pmid | pmid_verified | pmid_traceable | reference | source | tier | phenotype
```

The `id_stable`, `pmid_verified`, and `pmid_traceable` columns are **mandatory** — they allow downstream users to apply their own quality filters.

### Interactive HTML Dashboard

The dashboard must include all fields above and these additional features:

**Data integrity indicators (required):**
- ⚠️ icon on gene ID column when `id_stable = False`, linking to resolution resource
- 🔍 icon on PMID column when `pmid_verified = True` (verified this session)
- `[GR_REF]` badge when `pmid_traceable = False`, linking to Gramene gene page
- A `pmid_verified` filter in the filter controls

**Warning banner (required when Literature records are present):**
```html
<div class="warning-banner">
  ⚠️ Literature-source PMIDs have been verified against PubMed in this session.
  Database-source records (Planteome/Gramene) use curated references — GR_REF
  entries require Gramene database access to trace. Always verify before citing.
</div>
```

**Coverage bias note (required when one species > 60% of records):**
```html
<div class="bias-note">
  📊 Coverage note: {N}% of records are {species}.
  This reflects database annotation density, not biological difference.
  Species with 0 records may have published genetics not yet in Planteome/Gramene.
</div>
```

**All other dashboard features:**
- Summary cards (total genes, species count, Tier 1 count, traceable PMIDs)
- Species distribution bar chart
- Filterable table with sortable columns
- Clickable PMID links → PubMed
- Clickable gene ID links → RAP-DB / MaizeGDB / NCBI Gene
- Clickable ontology term links → Planteome AmiGO / AmiGO 2
- TSV export of filtered view
- Pagination for large datasets

---

## Step 8: Quality Checks (Automated + Manual)

Run this checklist programmatically before presenting the final output:

### Automated Checks
```python
# Check 1: No duplicate (gene_id, term) pairs
assert len(set((g.gene_id, g.ontology_term) for g in genes)) == len(genes)

# Check 2: All evidence codes are in the allowed set
ALLOWED = {"EXP","IDA","IMP","IGI","IPI","IEP","IC"}
assert all(g.evidence_code in ALLOWED for g in genes)

# Check 3: All records have a species assigned
assert all(g.species for g in genes)

# Check 4: All records have id_stable, pmid_verified, pmid_traceable fields
assert all(hasattr(g, 'id_stable') and hasattr(g, 'pmid_verified') for g in genes)

# Check 5: No Tier 1 records with pmid_verified = False AND pmid_traceable = False
tier1_unverified = [g for g in genes
                    if g.tier == 1
                    and g.pmid_verified == False
                    and g.pmid_traceable == False]
if tier1_unverified:
    print(f"WARNING: {len(tier1_unverified)} Tier 1 records have unverifiable references — downgrade to Tier 2")
```

### Manual Spot Checks (5 random records)
For 5 randomly selected records with PMIDs, fetch the PubMed page and confirm:
- [ ] The paper title mentions the gene and/or trait
- [ ] The species is consistent
- [ ] The gene ID resolves correctly in the target database

Report spot-check results as a table in the dashboard output.

### Coverage Check
- [ ] At least one record per species in the user's target clade — or explicitly note which are absent
- [ ] Ontology term set covers parent + child terms (verify with OBO traversal)
- [ ] Download date recorded in output header
- [ ] `id_stable` summary: what % of records have stable IDs?

---

## Tips and Known Pitfalls

**On PMIDs:**
- Training-memory PMIDs have ~80% error rate (empirically confirmed). Use the PubMed MCP tool exclusively.
- `lookup_article_by_citation` MCP (if available) is the most reliable: supply author, year, journal.
- `search_articles` returns real PMIDs from PubMed — always verify the returned title matches the gene and trait before adding to the dataset.
- A plausible-looking PMID that points to the wrong paper is worse than no PMID — it actively misleads users.

**On gene IDs:**
- In Planteome/Gramene GAF files, the locus ID is in **column 11** (synonyms), not column 10 (name). Column 10 often contains descriptive English names like "HEADING DATE 3A".
- The same gene may appear under different symbols in different sources (e.g., `SE1` = `Hd1` = `OsHd1` = `LOC_Os06g16370`). Anchor deduplication to the locus ID, not the symbol.
- GenBank accession numbers (e.g., `AY222645`) are sequence records for a specific transcript, not gene identifiers. They are fragile and should be resolved to stable genome coordinates.

**On species coverage:**
- Planteome TO gene-level files currently exist mainly for *Oryza sativa* and *Zea mays*. This creates an apparent rice/maize dominance that reflects annotation effort, not biology.
- For wheat and barley: check GrainGenes (`https://graingenes.org`) and IWGSC resources.
- For *Panicum*, *Setaria*, *Miscanthus*: use Phytozome and Europe PMC literature search.
- Always report species with 0 records as **database gaps**, not as evidence the trait doesn't exist in that species.

**On ontology:**
- TO:0000137 (heading date) is typically richer than TO:0002616 (flowering time trait) for grass species.
- Always query ≥3 synonymous/related TO terms — results across terms overlap but are not identical.
- Child term traversal catches genes annotated to more specific terms that are children of your target.

**On evidence codes:**
- IMP is a broad umbrella: it covers everything from classical multi-allele genetics to a single CRISPR knockout observation. The code does not distinguish these.
- Consider adding a `pmid_count` field (number of independent PMIDs supporting the association) as a proxy for evidence strength within IMP.
- IC (Inferred by Curator) from Gramene is generally reliable but the underlying evidence is stored in GR_REF, not a PMID, making independent verification difficult.

---

## Resources Quick Reference

| Resource | URL | Use |
|----------|-----|-----|
| Planteome | https://planteome.org | Plant trait ontology + gene associations |
| AmiGO 2 | https://amigo.geneontology.org | GO term queries |
| OBO Foundry | https://obofoundry.org | Find correct ontology terms |
| OLS4 (EBI) | https://www.ebi.ac.uk/ols4 | Browse ontology + child term traversal |
| Gramene | https://www.gramene.org | Grass species gene annotations |
| RAP-DB | https://rapdb.dna.affrc.go.jp | Rice locus IDs + gene pages |
| MaizeGDB | https://www.maizegdb.org | Maize gene IDs + literature |
| Ensembl Plants | https://plants.ensembl.org | Genome browser + BioMart for stable IDs |
| GrainGenes | https://graingenes.org | Wheat/barley/rye gene-trait associations |
| Phytozome | https://phytozome-next.jgi.doe.gov | Plant genome sequences + IDs |
| Europe PMC | https://europepmc.org | Literature mining |
| PubMed | https://pubmed.ncbi.nlm.nih.gov | PMID verification + article retrieval |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v2.0 | 2026-03 | Added anti-hallucination rules (top-level); mandatory PMID verification via WebFetch; gene ID stability classification + `id_stable` field; GR_REF handling (no PMID substitution); child term traversal (Step 2b); coverage bias reporting; `pmid_verified`/`pmid_traceable` output fields; automated quality checks; dashboard warning banners for unverified PMIDs and species bias; source priority ordering for deduplication |
| v1.0 | 2026-03 | Initial version |
