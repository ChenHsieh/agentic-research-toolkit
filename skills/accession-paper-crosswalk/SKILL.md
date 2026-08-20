---
name: accession-paper-crosswalk
description: >
  Link a sequence-data accession to the paper that describes it, and a paper to the data it
  deposited - covering BioProject (PRJNA/PRJEB/PRJDB), SRA (SRP/SRX/SRR/SRS), BioSample
  (SAMN), and GEO (GSE) identifiers. Handles the alias expansion that makes or breaks the
  search, routes around NCBI's near-empty BioProject-to-PubMed link table, and treats the
  gaps - deposited-but-never-published data, papers whose stated accession does not resolve,
  samples in a project the paper never mentions - as findings rather than errors. Use when
  chasing provenance for a reused dataset, checking whether data behind a claim is actually
  public, or assembling a table of studies and their accessions. Trigger on "find the paper
  for this accession", "PRJNA", "SRA accession", "which paper published this data", "what
  data did this paper deposit", "is this dataset published", "data availability".
allowed-tools: Read Write Edit Bash Glob Grep WebSearch WebFetch
---

# Accession ↔ paper crosswalk

**The obvious route does not work, and its silence is misleading.** NCBI has a
`bioproject_pubmed` Entrez link, an agent will reach for it first, it returns an empty result
for most projects, and an empty result reads exactly like "this data was never published."

> **Absence of a link is not absence of a paper.** Report "no link found in *X*", never "no
> publication exists." The difference matters: the second claim gets used to justify treating
> someone's data as unpublished.

## Measured, 2026-08-19 — re-verify before relying on these

| Route | Result | Implication |
|---|---|---|
| `elink bioproject→pubmed`, 30 projects sampled from a `transcriptome` search | **0/30** had any link | Not a primary route |
| Same call on a known-linked control (uid `1210558`) | Link present → PMID `22955616` | The 0/30 is real, not a broken call |
| `esearch db=pubmed` on the literal strings `PRJNA30709`, `SRP020237` | **0 hits each** | PubMed does not index accessions — they live in data-availability and full text |
| Europe PMC `ACCESSION_ID:"PRJNA30709"` | **9 hits** | The productive route; it text-mines full text |
| `PRJNA172563` vs its own SRA alias `SRP020237` in Europe PMC | **0 hits vs 3 hits** | **Alias choice alone decides whether you find anything** |

That last row is the reason Step 1 exists.

## Step 1 — expand the accession into all its aliases first

One dataset has several identifiers, and different papers cite different ones. Searching only
the accession you were handed is the single most common way this fails.

From an SRA record, `esummary` exposes both the study accession and the BioProject in its
`expxml` field:

```bash
E=https://eutils.ncbi.nlm.nih.gov/entrez/eutils
# any accession -> SRA UID
curl -s "$E/esearch.fcgi?db=sra&term=PRJNA172563&retmax=3&retmode=json"
# UID -> aliases:  Study acc="SRP020237"  and  <Bioproject>PRJNA172563
curl -s "$E/esummary.fcgi?db=sra&id=96817&retmode=json"
```

Build the alias set before searching: the BioProject (`PRJNA*`), the SRA study (`SRP*`), the
GEO series (`GSE*`) if the data is also in GEO, and any secondary accession from a mirror
(`PRJEB*`/`ERP*` at EBI, `PRJDB*`/`DRP*` at DDBJ — the archives mirror each other and assign
their own IDs). Then run every subsequent search against **all** of them.

## Step 2 — accession → paper

Run these in order and keep every hit with its source:

1. **Europe PMC accession index** (best single route — it text-mines full text, including data
   availability statements):
   ```bash
   curl -s 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ACCESSION_ID%3A%22PRJNA30709%22&format=json&pageSize=25'
   ```
   Repeat per alias. Returns `hitCount` and a `resultList` with PMIDs and titles.
2. **The BioProject record itself.** Open `https://www.ncbi.nlm.nih.gov/bioproject/PRJNA…` and
   read the description and the linked-publication section. Note that `esummary db=bioproject`
   does **not** return a publication field — you have to look at the record or the page.
3. **`elink bioproject→pubmed`.** Cheap, occasionally right, usually empty. Run it, but never
   let its silence become a conclusion.
4. **Plain web search** on the accession string, which finds preprints, theses, and
   supplementary tables that none of the above index.

## Step 3 — paper → accession

1. **`elink pubmed→bioproject`** — this direction genuinely works (linkname
   `pubmed_bioproject`):
   ```bash
   curl -s "$E/elink.fcgi?dbfrom=pubmed&db=bioproject&id=22955616&retmode=json"
   ```
2. **Read the data availability statement in the full text**, not the abstract. This is where
   accessions actually live, and it is why PubMed-only searching fails.
3. **Scan the supplementary material.** Per-sample accession tables are routinely supplementary
   files and appear in no index at all.

## Step 4 — reconcile, and treat the gaps as the output

Having both sides, compare them. The mismatches are the point:

- **Deposited but never published.** A project with data, no linked paper, and no full-text
  citation anywhere. Sometimes genuinely unpublished; sometimes published somewhere unindexed.
  Report which of those you established, and how.
- **Cited but unresolvable.** The paper states an accession that does not resolve, or resolves
  to a different organism or assay than described. Common causes: a typo, a private record
  never released, or a placeholder that survived to press.
- **Sample count mismatch.** The project holds more runs or samples than the paper describes.
  Extra conditions, failed replicates, or a pilot are frequently in the archive and absent from
  the manuscript. Compare the run count against the paper's stated n.
- **Citing versus generating.** Most papers a search returns for a popular accession *reused*
  the data. Separate the study that generated it from the ones that cite it — usually the
  earliest, and the one the BioProject submitter is affiliated with.
- **Release date after publication.** Check the project's registration and release dates
  against the paper's. Data released long after publication was not available to reviewers.

## Step 5 — report with provenance per row

Every row needs the route that found it, because the routes have different reliability:

| Accession | Aliases | Paper | Found via | Relationship | Notes |
|---|---|---|---|---|---|
| PRJNA… | SRP…, GSE… | PMID … | Europe PMC | generated | n matches |
| PRJNA… | SRP… | — | not found in EuropePMC, elink, or web | **unresolved** | 40 runs, no paper located |

"Unresolved" is a legitimate final state. Do not upgrade it to "unpublished."

## Practical notes

- **Rate limits.** NCBI E-utilities allows ~3 requests/second without an API key, ~10 with one
  (`&api_key=…`). Sleep between calls in a loop; hammering gets you blocked mid-run.
- **Retry and check the payload.** These endpoints return HTTP 200 with an empty or partial
  body under load. Check that the JSON has the field you want before concluding "no result" —
  an empty `linksets` entry and a failed request look identical downstream.
- **Do not fabricate accessions.** An accession that looks plausible almost always resolves to
  someone else's real data. Every accession in the output must have come from a response you
  actually received in this session.

## What this does not cover

| Not covered | Where it belongs |
|---|---|
| Downloading or processing the reads | `sra-tools` / `fasterq-dump`; this is provenance only |
| Whether the data supports the paper's claims | `result-autopsy`, and reading the paper |
| Cross-checking a call set against another method | `second-opinion-concordance` |
| Non-sequence repositories (PRIDE, MetaboLights, Zenodo, Dryad) | Same shape, different indexes; the alias logic transfers |
| Controlled-access data (dbGaP, EGA) | Requires an access request; metadata only is public |

## Honest limits

- The measured numbers above are one sample on one date. The `transcriptome` query skews
  toward bulk submissions, which may be less likely to carry links than average — treat 0/30 as
  "sparse enough not to rely on," not as a precise rate.
- Europe PMC's index covers what it has text-mined. Paywalled full text with no deposited
  version is a blind spot, so a zero there is weaker evidence than a zero would suggest.
- Deciding which paper *generated* data is a judgment call. Submitter affiliation and dates are
  evidence, not proof.
