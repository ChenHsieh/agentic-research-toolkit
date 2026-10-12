## User

This is the beginning of a team meeting to discuss your research project. This is a meeting with the team lead, Principal Investigator, and the following team members: Comparative Genomicist, Functional Genomics Scientist, Scientific Critic.

Here is the agenda for the meeting:

We have a set of lineage-specific (young) genes predicted in a haplotype-resolved genome of a hybrid poplar, found with a phylostratigraphy tool against a large protein database. Some may be annotation artifacts or homologs that sequence search failed to detect. Design the smallest set of analyses that would convince a skeptical reviewer which of them are real protein-coding genes.

Here are the agenda questions that must be answered:

1. List the analyses in priority order, with what each would rule out.

2. For each analysis, what is the negative control and the positive control?

3. Which single analysis would you run first with one week and existing public data, and why?

Here are the agenda rules that must be followed:

1. Do not invent numbers or cite papers you are not sure exist.

2. Every proposed analysis must name a result that would count against the genes being real.

Principal Investigator will convene the meeting. Then, each team member will provide their thoughts on the discussion one-by-one in the order above. After all team members have given their input, Principal Investigator will synthesize the points raised by each team member, make decisions regarding the agenda based on team member input, and ask follow-up questions to gather more information and feedback about how to better address the agenda. This will continue for 2 rounds. Once the discussion is complete, Principal Investigator will summarize the meeting in detail for future discussions, provide a specific recommendation regarding the agenda, and answer the agenda questions (if any) based on the discussion while strictly adhering to the agenda rules (if any).

## User

Principal Investigator, please provide your initial thoughts on the agenda as well as any questions you have to guide the discussion among the team members.

## Principal Investigator

I'll start by framing the challenge. We have a list of putative young, lineage-specific protein-coding genes from a hybrid poplar genome. The phylostratigraphy approach is sensitive but can yield false positives due to annotation errors, undetected homology, or non-coding sequences misannotated as genes. A skeptical reviewer will want evidence that these are genuinely transcribed and translated, under purifying selection, and not just random ORFs. Our goal is a minimal, high-impact set of analyses, ranked by how convincingly each rules out artifact, with clear controls. I have my own ideas, but I want to hear each of you first. Comparative Genomicist, Functional Genomics Scientist, Scientific Critic, please share your perspectives in that order, addressing the agenda questions. Focus on practical, defensible approaches using existing data where possible.

## User

Comparative Genomicist, please provide your thoughts on the discussion (round 1 of 2). If you do not have anything new or relevant to add, you may say "pass". Remember that you can and should (politely) disagree with other team members if you have a different perspective.

## Comparative Genomicist

As Comparative Genomicist, my priority is to first rule out the most likely technical failure of phylostratigraphy: that homologs exist but were missed by the search. If that isn’t addressed, every downstream analysis is vulnerable to the criticism that we are characterizing annotation or search artifacts, not true lineage-specific genes.

**Priority-ordered analyses**

1. **Sensitive homology search against nucleotide and protein databases, including unannotated outgroup genomes and transcriptomes.**  
   - *What it rules out:* Detection failure of homologs in existing protein databases, especially homologs in unannotated genomic regions or in species not represented in the original protein database.  
   - *Negative control:* A set of known conserved poplar genes should recover clear homologs in outgroup genomes/transcriptomes.  
   - *Positive control:* A set of known young or species-specific genes, or synthetic shuffled ORFs, should not recover significant homologs.  
   - *Result that would count against the genes being real:* Significant alignments in outgroup genomes or transcriptomes, particularly in collinear regions, would indicate the gene is not lineage-specific and was missed by the original phylostratigraphy search.

2. **Synteny / microsynteny analysis of the genomic locus in outgroup assemblies.**  
   - *What it rules out:* Annotation artifacts where a gene is absent from an outgroup annotation but the orthologous genomic sequence is present; also helps distinguish true insertion/deletion from missed annotation.  
   - *Negative control:* Conserved genes should show collinear orthologs in related Salicaceae genomes.  
   - *Positive control:* Known transposable-element insertions or species-specific genes should lack collinear orthologs.  
   - *Result that would count against the genes being real:* If the putative gene overlaps an unannotated but alignable region in an outgroup genome, or if the gene model spans a gap or misassembly, it may be a missed homolog or assembly artifact rather than a true lineage-specific gene.

3. **Expression and splicing evidence from public RNA-seq data.**  
   - *What it rules out:* Non-transcribed annotation artifacts and genomic ORFs that are not part of a functional transcript.  
   - *Negative control:* Known housekeeping genes should show robust expression and canonical splicing.  
   - *Positive control:* Intergenic regions or annotated pseudogenes should show little or no expression.  
   - *Result that would count against the genes being real:* No RNA-seq reads spanning exon junctions, no expression above background, or no evidence of polyadenylation would suggest the gene is not transcribed and therefore not a real protein-coding gene.

4. **Evolutionary constraint using population resequencing or multi-species alignments.**  
   - *What it rules out:* Non-coding or pseudogene sequences misannotated as protein-coding; tests whether the ORF is maintained by selection.  
   - *Negative control:* Known functional genes should show dN/dS < 1 and few segregating loss-of-function variants.  
   - *Positive control:* Known pseudogenes or neutrally evolving sequences should show dN/dS ≈ 1 and an excess of premature stop codons or frameshifts.  
   - *Result that would count against the genes being real:* High dN/dS, segregating loss-of-function variants, or no evidence of purifying selection would indicate the ORF is not a conserved protein-coding sequence.

5. **Annotation quality and haplotype consistency.**  
   - *What it rules out:* Assembly or annotation artifacts specific to one haplotype or to the gene prediction pipeline.  
   - *Negative control:* Known genes should be present and intact in both haplotypes with canonical splice sites and a single long ORF.  
   - *Positive control:* Random ORFs or TE-derived sequences often lack canonical features or are haplotype-specific.  
   - *Result that would count against the genes being real:* If the gene is present in only one haplotype, overlaps repetitive elements, lacks a long ORF, or has non-canonical splice sites, it is more likely an artifact.

**Which single analysis I would run first with one week and existing public data:**  
I would run the **sensitive homology search** first. Specifically, I would use tblastn or MMseqs2 against all publicly available Salicaceae genome assemblies and transcriptomes, plus HMMER against Pfam/InterPro to detect distant domains. This directly tests the central weakness of phylostratigraphy: absence of homologs in a protein database does not mean absence of homologs in genomes or transcriptomes. It is fast, uses existing public data, and a negative result—finding homologs in outgroups—immediately eliminates the strongest candidates from the lineage-specific list. If the search is clean, we can then invest in synteny and expression analyses with more confidence.

## User

Functional Genomics Scientist, please provide your thoughts on the discussion (round 1 of 2). If you do not have anything new or relevant to add, you may say "pass". Remember that you can and should (politely) disagree with other team members if you have a different perspective.

## Functional Genomics Scientist

As Functional Genomics Scientist, I agree with the Comparative Genomicist that missed homology is a major concern, but I would reorder priorities. The agenda asks which candidates are **real protein-coding genes**, not just which are truly lineage-specific. A gene can be a real protein-coding gene even if a distant homolog exists; conversely, a gene with no expression or no translation is not a real protein-coding gene, regardless of homology. Therefore, direct functional evidence should come first.

**Priority-ordered analyses**

1. **RNA-seq across multiple tissues/conditions, including allele-specific expression in the hybrid**  
   - *What it rules out:* Non-transcribed annotation artifacts, incorrect gene models, unexpressed ORFs, and mapping artifacts.  
   - *Negative control:* Intergenic regions or annotated pseudogenes should show little or no expression; known housekeeping genes should show robust expression (assay sensitivity control).  
   - *Positive control:* Known protein-coding genes should show canonical splice junctions, polyA evidence, and expression in at least some tissues.  
   - *Result that would count against the genes being real:* No RNA-seq reads mapping to exons, no splice junction reads, no polyA evidence, or no expression above background in any public tissue/condition. If the gene is predicted on only one haplotype, reads should map specifically to that haplotype; equal mapping to both haplotypes or inconsistent allele-specific expression would suggest a mapping or annotation artifact.  
   - *What it can and cannot show:* RNA-seq can show transcription and splicing, but it cannot show translation or protein function.

2. **Ribosome profiling (Ribo-seq), if available**  
   - *What it rules out:* Transcribed but non-coding RNAs, and ORFs that are not translated.  
   - *Negative control:* Known long non-coding RNAs or 5′ UTRs should show little or no ribosome protected fragments.  
   - *Positive control:* Known protein-coding genes should show strong ribosome footprints with 3-nucleotide periodicity over the CDS.  
   - *Result that would count against the genes being real:* No ribosome protected fragments over the predicted ORF, no 3-nt periodicity, or no enrichment in the CDS relative to UTRs.  
   - *What it can and cannot show:* Ribo-seq can show translation, but it cannot show protein stability, abundance, or function.

3. **Proteomics / mass spectrometry**  
   - *What it rules out:* Translation below detection? More precisely, it provides direct evidence of protein existence.  
   - *Negative control:* Decoy database or reverse sequences should yield no peptides above the false discovery threshold; known non-coding RNAs should not yield unique peptides.  
   - *Positive control:* Known abundant proteins should be detected.  
   - *Result that would count against the genes being real:* No unique peptides mapping to the predicted ORF. However, absence of peptides is weak evidence because proteomics has limited sensitivity for low-abundance or tissue-specific proteins.  
   - *What it can and cannot show:* Proteomics can show protein existence, but it cannot show function or regulation.

4. **Evolutionary constraint (dN/dS, population resequencing)**  
   - *What it rules out:* Non-coding or pseudogene sequences misannotated as protein-coding; tests whether the ORF is maintained by selection.  
   - *Negative control:* Known functional genes should show dN/dS < 1 and few segregating loss-of-function variants.  
   - *Positive control:* Known pseudogenes or neutrally evolving sequences should show dN/dS ≈ 1 and an excess of premature stop codons or frameshifts.  
   - *Result that would count against the genes being real:* High dN/dS, segregating loss-of-function variants, or no evidence of purifying selection.  
   - *What it can and cannot show:* This can show selective constraint on the ORF, but it cannot directly show transcription or translation.

**Which single analysis I would run first with one week and existing public data:**  
I would run **RNA-seq across multiple tissues** first. Public poplar RNA-seq data are relatively abundant, and this analysis directly tests whether the candidates are transcribed and correctly spliced. If a candidate has no expression in any tissue, no splice junctions, and no polyA evidence, it is very unlikely to be a real protein-coding gene. This is the most direct functional evidence and can be completed within a week using existing data. Homology search is also fast and important, but it addresses lineage-specificity rather than whether the gene is real; I would run it in parallel if time permits, but RNA-seq is my first priority.

## User

Scientific Critic, please provide your thoughts on the discussion (round 1 of 2). If you do not have anything new or relevant to add, you may say "pass". Remember that you can and should (politely) disagree with other team members if you have a different perspective.

## Scientific Critic

As Scientific Critic, I want to reframe the question: a “real protein-coding gene” means a transcribed, spliced, translated ORF that is maintained by selection. No single analysis establishes all of these, and every analysis we propose must be able to fail. I disagree with the Comparative Genomicist’s first priority: sensitive homology search addresses lineage-specificity, not whether the gene is real. A candidate can be a real protein-coding gene even if a distant homolog exists; a candidate can be an artifact even if no homolog is found. I partially agree with the Functional Genomics Scientist that RNA-seq should come first, but only if it is designed with explicit negative controls and pre-specified rejection criteria. Otherwise, pervasive transcription and mapping noise will produce “expression” for almost anything.

**Priority-ordered analyses**

1. **Annotation quality and haplotype consistency**  
   - *What it rules out:* Gene model artifacts, assembly errors, haplotype-specific misannotations, and TE-derived ORFs.  
   - *Positive control:* Known single-copy protein-coding genes should be present in both haplotypes with canonical splice sites, a single long ORF, and no overlapping repetitive elements.  
   - *Negative control:* Random intergenic ORFs or annotated pseudogenes should fail one or more of these checks.  
   - *Result that would count against the genes being real:* Non-canonical splice sites, a short or interrupted ORF, overlap with repetitive elements, presence in only one haplotype without allele-specific read support, or no intact ORF.

2. **RNA-seq with allele-specific mapping, splice-junction, and polyA evidence**  
   - *What it rules out:* Non-transcribed annotation artifacts and incorrect gene models.  
   - *Positive control:* Known protein-coding genes, including at least one low-abundance gene, should show expression, junction reads, and polyA evidence.  
   - *Negative control:* Intergenic regions and known lncRNAs/pseudogenes should show no expression above background. If they do, the expression threshold is too permissive.  
   - *Result that would count against the genes being real:* No reads above background, no splice-junction reads, no polyA evidence, or expression not consistent with the predicted haplotype. In a hybrid, cross-mapping between haplotypes must be controlled using haplotype-specific SNPs; otherwise expression can be falsely assigned.

3. **Translation evidence: Ribo-seq if available; proteomics only as confirmatory**  
   - *What it rules out:* Transcribed non-coding RNAs and untranslated ORFs.  
   - *Positive control:* Known protein-coding genes should show ribosome footprints with 3-nucleotide periodicity over the CDS.  
   - *Negative control:* Known lncRNAs or 5′ UTRs should show little or no ribosome protected fragments.  
   - *Result that would count against the genes being real:* No ribosome protected fragments over the ORF, no 3-nt periodicity, or no unique peptides in proteomics. Absence in proteomics alone is weak because of sensitivity limits.

4. **Evolutionary constraint: dN/dS or population resequencing**  
   - *What it rules out:* Neutrally evolving ORFs, pseudogenes, and non-coding sequences misannotated as CDS.  
   - *Positive control:* Known functional genes should show dN/dS < 1 and few segregating loss-of-function variants.  
   - *Negative control:* Known pseudogenes or neutrally evolving sequences should show dN/dS ≈ 1 and an excess of premature stops or frameshifts.  
   - *Result that would count against the genes being real:* No evidence of purifying selection, high dN/dS, or segregating loss-of-function variants.

5. **Sensitive homology search plus synteny**  
   - *What it rules out:* Missed homologs and confirms lineage-specificity, but does not by itself prove protein-coding.  
   - *Positive control:* Known conserved genes should recover clear homologs in outgroup genomes/transcriptomes.  
   - *Negative control:* Synthetic shuffled ORFs with matched composition should not recover significant homologs; a known species-specific sequence should also lack collinear orthologs.  
   - *Result that would count against the genes being real:* Significant alignments in outgroup genomes or transcriptomes, especially in collinear regions, indicating the gene is not lineage-specific and was missed by the original search.

**Which single analysis I would run first with one week and existing public data:**  
I would run **RNA-seq with allele-specific mapping and pre-specified rejection criteria**. It is the most direct test of transcription and can be done with public data in one week. However, I would not interpret expression alone as proof of protein-coding; I would use it as a filter to prioritize candidates for translation/selection and homology analyses. If the RNA-seq analysis cannot be designed to fail—no negative controls, no threshold, no allele-specific mapping—then it is not worth running first.

I also caution that the original phylostratigraphy result depends on database composition and search parameters. If the database included poplar or close relatives, the “lineage-specific” assignment may be contaminated. We need to know what was excluded before trusting the candidate list.

## User

This concludes round 1 of 2 of discussion. Principal Investigator, please synthesize the points raised by each team member, make decisions regarding the agenda based on team member input, and ask follow-up questions to gather more information and feedback about how to better address the agenda.

## Principal Investigator

I've listened carefully to all three of you. Here's my synthesis and where I'm landing on this.

## Areas of agreement

- **Annotation quality and haplotype consistency** must be checked early; it's a prerequisite before investing in functional or evolutionary analyses.
- **RNA-seq** is essential. All of you include it in your top three, and the Scientific Critic's insistence on pre-specified rejection criteria is critical if we want the analysis to be persuasive.
- **Evolutionary constraint** (dN/dS, population resequencing) is important but not the first thing to run; it comes after we've established that the genes are transcribed.
- **Sensitive homology search plus synteny** addresses missed homologs—important for the "lineage-specific" claim—but is not the most direct test of whether the gene is a real protein-coding gene.

## Area of disagreement

- **Single first analysis:** Comparative Genomicist wants sensitive homology search first; Functional Genomics Scientist and Scientific Critic want RNA-seq first.

## My decisions

I side with Functional Genomics Scientist and Scientific Critic: **the first analysis should be RNA-seq**, because it is the most direct test of whether the predicted genes are transcribed and correctly spliced—a necessary condition for being a real protein-coding gene. However, I fully adopt the Scientific Critic's requirement that the RNA-seq analysis must be **designed to fail**: we need explicit negative controls, positive controls, and pre-specified rejection thresholds before we look at the data.

I also agree with the Comparative Genomicist that sensitive homology search is important, but I view it as the second analysis because it tests lineage-specificity rather than protein-coding status. We should run it in parallel if time permits, but RNA-seq is the priority.

**Revised ranked plan, integrating all input:**

1. **Annotation quality and haplotype consistency** (prerequisite, not ranked). Before any downstream analysis, filter out candidates with non-canonical splice sites, short/interrupted ORFs, repetitive element overlap, or haplotype-specific prediction without allele-specific read support.
2. **RNA-seq with allele-specific mapping, splice-junction, and polyA evidence, plus pre-specified rejection criteria.** Negative control: intergenic regions, known pseudogenes. Positive control: known protein-coding genes at various expression levels. Rejection if: no reads above background, no junction reads, no polyA evidence, or expression inconsistent with haplotype prediction.
3. **Sensitive homology search plus synteny** against outgroup genomes and transcriptomes.
4. **Ribosome profiling or proteomics** (if available).
5. **Evolutionary constraint** (dN/dS, population resequencing).

## Follow-up questions

Before we proceed to round 2, I need specific clarifications from each of you. This will help refine our plan into something a skeptical reviewer would find airtight.

**To the Comparative Genomicist:**
- What exactly was in the phylostratigraphy protein database? Were any Salicaceae species, poplar cultivars, or close relatives included or excluded? If so, which ones?
- Which outgroup genomes and transcriptomes are publicly available that you would use for the sensitive homology search and synteny analysis?
- What alignment tools, E-value thresholds, and synteny methods would you use, and what explicit criteria would count as "significant" homology?

**To the Functional Genomics Scientist:**
- What public RNA-seq datasets exist for poplar (preferably the same hybrid or its parents) across multiple tissues? Are there sufficient data to assess allele-specific expression using haplotype-specific SNPs?
- Is Ribo-seq or proteomics data available for any poplar tissue?
- What explicit thresholds would you propose for expression (e.g., FPKM/TPM cutoff), splice junction support (minimum junction reads), and polyA evidence?

**To the Scientific Critic:**
- Are the rejection criteria I've outlined for RNA-seq sufficient? What additional pre-specified criteria would you require?
- Do you find the ranked plan acceptable, or would you insist on annotation quality being a formal first filter before RNA-seq, rather than a prerequisite?
- What would you consider the single most damning result against a candidate being real—and is our plan capable of detecting it?

## User

Comparative Genomicist, please provide your thoughts on the discussion (round 2 of 2). If you do not have anything new or relevant to add, you may say "pass". Remember that you can and should (politely) disagree with other team members if you have a different perspective.

## Comparative Genomicist

I'll accept the RNA-seq-first decision, provided the RNA-seq analysis is designed to fail as the Scientific Critic insists. However, I want to add one clarifying point: a missed homolog does not by itself mean a candidate is not a real protein-coding gene; it means the candidate is not lineage-specific. The agenda asks which candidates are real protein-coding genes, so I agree homology/synteny is not the first test. But if the goal includes the lineage-specific claim, we should run the homology audit in parallel so we don't waste RNA-seq effort on candidates that are actually conserved genes.

Here are my answers to the Principal Investigator’s questions.

### 1. What was in the phylostratigraphy protein database?

I do not know what was actually used, and that is itself a problem. Before trusting the candidate list, I would audit the phylostratigraphy run:

- Which protein database version was used? Was it NCBI nr, UniProt, or a custom database?
- Were any Salicaceae species, any *Populus* species, or the hybrid parents themselves present in the database? If any close relatives were included, then the term “lineage-specific” is compromised.
- Were the exact search parameters and taxon assignment rules recorded? If not, the result is not reproducible.

If the original database contained any *Populus* or *Salix* sequences, I would re-run the search with those sequences explicitly removed and with a dated, archived database. I would also check for vector or contaminant sequences that could create spurious hits. This audit is quick and does not require new data.

### 2. Which outgroup genomes and transcriptomes are publicly available?

For the homology and synteny analysis, I would use:

- **Genome assemblies:** *Populus trichocarpa*, *Populus deltoides*, *Populus alba*, *Populus tremula*, and *Salix purpurea* are all publicly available and are the most relevant close outgroups. Depending on the hybrid parentage, I would avoid using a genome that is identical to one of the parental haplotypes as an “outgroup.” More distantly, *Salix suchowensis* or *Populus euphratica* may also be available.
- **Transcriptomes:** NCBI SRA has many poplar RNA-seq datasets across tissues and conditions. Phytozome and Ensembl Plants also provide annotated transcriptomes for the species above. I would use transcriptome assemblies or annotated CDS sets, not just protein annotations, because that is where missed homologs often hide.
- If time allows, I would also search the raw genome assemblies with tblastn or miniprot, since some homologs may not be annotated.

### 3. What tools, thresholds, and synteny criteria would I use?

**Homology search:**

- I would use **MMseqs2** for fast sensitive protein searches against transcriptome assemblies, and **tblastn** or **miniprot** against genome assemblies.
- Initial homology criteria: E-value ≤ 1e-5, query coverage ≥ 50% of the candidate ORF, and amino acid identity ≥ 30% for a first-pass screen. For very short or fast-evolving candidates, these thresholds may need to be relaxed, but then we must require additional evidence.
- I would also run **HMMER** against Pfam/InterPro to detect distant domain-level homology. A significant domain hit with a gathering threshold would indicate the candidate is not a de novo protein.
- **Negative control:** synthetic shuffled ORFs matched for length and composition should return no significant hits.
- **Positive control:** a set of known conserved poplar genes should return clear orthologs in the same outgroup databases.

**Synteny:**

- I would use **GENESPACE** or **MCScanX** to test whether the candidate locus is collinear with outgroup genomes.
- A result that counts against the gene being real: if the candidate falls in a conserved collinear block, but the orthologous region in an outgroup contains only a non-coding conserved element or a transposable element, then the gene model is likely an annotation artifact. If the outgroup locus contains a clear coding ortholog that was missed by the original search, then the candidate is not lineage-specific, though it may still be a real gene.
- **Positive control:** known conserved genes should show collinear orthologs.
- **Negative control:** known transposable-element insertions or species-specific genes should lack collinear orthologs.

**One result that would count against the genes being real:** If the best alignments are to transposable element proteins or repetitive sequences, and the locus has TE features, then the candidate is likely a TE-derived annotation artifact rather than a functional young protein-coding gene.

I would also formally check annotation quality first, as the Scientific Critic suggested. That is a cheap, decisive filter: non-canonical splice sites, interrupted ORFs, repeat overlap, and haplotype inconsistency should remove candidates before we invest in RNA-seq or selection analyses.

## User

Functional Genomics Scientist, please provide your thoughts on the discussion (round 2 of 2). If you do not have anything new or relevant to add, you may say "pass". Remember that you can and should (politely) disagree with other team members if you have a different perspective.

## Functional Genomics Scientist

I agree with the Comparative Genomicist that the homology audit can run in parallel, but I maintain that RNA-seq is the first decisive filter for protein-coding status. I also agree that annotation quality should be a prerequisite filter before RNA-seq, as the Scientific Critic proposed.

Here are my answers to the Principal Investigator’s questions.

### 1. What public RNA-seq datasets exist for poplar?

I cannot cite specific accession numbers without checking, but the approach would be:

- Search NCBI SRA and ENA for *Populus trichocarpa*, *Populus deltoides*, *Populus alba*, *Populus tremula*, and the specific hybrid if its parents are known.
- Prioritize datasets from multiple tissues: leaf, root, xylem, cambium, bud, flower, and stress-treated samples. Poplar has relatively abundant public RNA-seq, so multi-tissue coverage is likely.
- For allele-specific expression, we need RNA-seq from the hybrid itself, not just the parents. If the hybrid RNA-seq is not available, we cannot test allele-specific expression directly. In that case, we would rely on total expression and note the limitation. If hybrid RNA-seq is available, we would use haplotype-specific SNPs to assign reads to each haplotype.

### 2. Is Ribo-seq or proteomics data available for poplar?

I am not aware of public Ribo-seq data for poplar, though I would search SRA and GEO. Proteomics data may exist in PRIDE or MassIVE for some poplar tissues, but coverage is likely limited and may not include the specific hybrid. If neither is available, we cannot directly test translation with existing data. In that case, we would rely on RNA-seq plus evolutionary constraint, and we would be explicit that translation remains unproven without new Ribo-seq or proteomics experiments.

### 3. What explicit thresholds would I propose?

I would propose the following pre-specified rejection criteria, to be applied before looking at the candidate list:

**Expression:**
- A candidate must have at least 10 uniquely mapping reads in at least one tissue.
- Its expression must exceed the 95th percentile of expression in intergenic regions and known pseudogenes in the same tissue. This controls for transcriptional noise.
- If the candidate is expressed only in a single tissue, that is acceptable, but we would note it as tissue-specific.

**Splice junctions:**
- At least 2 unique reads must span each predicted exon–exon junction.
- Junction reads must be consistent with the annotated splice sites. If the majority of junction reads support a different splice pattern, the gene model is likely wrong.

**PolyA evidence:**
- If polyA-selected RNA-seq libraries are available, we require at least 1 read or read pair supporting a polyA site within 50 bp of the annotated 3′ end. If the data are not polyA-selected, we cannot assess polyA and will state that limitation.

**Allele-specific expression (if hybrid RNA-seq is available):**
- Reads mapping to the candidate locus should map preferentially to the predicted haplotype using haplotype-specific SNPs. If reads map equally to both haplotypes or predominantly to the wrong haplotype, that counts against the gene being real.

**Negative control:** Intergenic regions and known pseudogenes should fail these criteria. If they pass, our thresholds are too permissive.

**Positive control:** Known protein-coding genes, including at least one low-abundance gene, should pass these criteria. If they fail, our thresholds are too stringent.

**Result that would count against the genes being real:** No expression above background, no splice-junction reads, no polyA evidence, or expression inconsistent with the predicted haplotype.

I want to emphasize that RNA-seq alone cannot prove translation. A candidate that passes all RNA-seq criteria is a strong candidate for being a real transcribed gene, but we still need Ribo-seq, proteomics, or evolutionary constraint to argue it is translated and functional.

## User

Scientific Critic, please provide your thoughts on the discussion (round 2 of 2). If you do not have anything new or relevant to add, you may say "pass". Remember that you can and should (politely) disagree with other team members if you have a different perspective.

## Scientific Critic

I find the plan converging toward something defensible, but I have several points that must be addressed before I would sign off on this as convincing to a skeptical reviewer.

### 1. Are the rejection criteria for RNA-seq sufficient?

The Functional Genomics Scientist's thresholds are a good start, but I see three gaps.

**First, the expression threshold is arbitrary.** "10 uniquely mapping reads" and "95th percentile of intergenic expression" are reasonable heuristics, but they are not calibrated to the specific data. I would require that we first characterize the distribution of expression across all annotated features—protein-coding genes, pseudogenes, lncRNAs, intergenic regions—in each tissue. Then we set the threshold at a percentile that cleanly separates known protein-coding genes from known non-coding features. If the distributions overlap substantially, no single threshold will work, and we must acknowledge that expression alone is weak evidence.

**Second, mapping ambiguity in a hybrid genome is a serious confound.** The haplotype-resolved genome is an advantage, but it also creates a risk: reads from one haplotype can cross-map to the other. If the haplotypes are highly similar, allele-specific expression analysis may be uninformative. I would require that we first measure the cross-mapping rate using simulated reads from each haplotype. If cross-mapping exceeds, say, 5%, then allele-specific expression claims are unreliable, and we should not use them as rejection criteria.

**Third, splice junction evidence is necessary but not sufficient.** A gene model can have splice junction reads and still be an artifact if the junctions are also present in intergenic transcripts or if the gene model is a fragment of a larger transcript. I would add a requirement: the candidate's exon–intron structure must not be fully contained within a known lncRNA or a retained intron of another gene.

### 2. Do I find the ranked plan acceptable?

Mostly, with one structural change. I would make **annotation quality a formal first filter, not a prerequisite.** The distinction matters because a prerequisite can be done informally; a formal filter requires explicit, pre-specified rejection criteria that are reported in the final analysis. I want the following checks applied and reported:

- **ORF integrity:** The predicted CDS must be a single contiguous ORF ≥ 30 codons (or a defensible minimum) with no in-frame stops.
- **Splice sites:** All introns must have canonical GT–AG or GC–AG splice sites, or at least be supported by splice junction reads if non-canonical.
- **Repeat overlap:** The CDS must not overlap a RepeatMasker-annotated transposable element by more than 50% of its length.
- **Haplotype presence:** The gene must be predicted in both haplotypes, or if haplotype-specific, must have allele-specific read support. If it is present in only one haplotype and has no read support, it is likely an assembly or annotation artifact.
- **Negative control:** Random intergenic ORFs of similar length should fail at least one of these checks.
- **Positive control:** Known single-copy protein-coding genes should pass all checks.

Candidates that fail any of these are removed before RNA-seq. This prevents us from wasting effort on obvious artifacts and makes the filtering transparent.

### 3. What is the single most damning result against a candidate being real, and is our plan capable of detecting it?

The single most damning result is: **the candidate is a fragment of a transposable element that is transcribed at low levels but not translated, and it shows no evidence of purifying selection.** Our plan can detect this, but only if all pieces are run and interpreted together:

- Annotation quality filter catches TE overlap.
- RNA-seq may show low expression, but if the TE is transcribed, expression alone could falsely support the candidate. That is why expression must be combined with splice junction and polyA evidence.
- Homology search catches TE-derived homology.
- Evolutionary constraint catches the absence of selection.

The danger is if we stop after RNA-seq and declare candidates "real" based on expression alone. That would be a failure mode. The plan must be executed as a pipeline where each step can eliminate candidates, and no single step is treated as sufficient proof.

### Additional concern: the phylostratigraphy audit

I strongly endorse the Comparative Genomicist's point that we must audit the original phylostratigraphy run. If the database contained poplar sequences, the entire candidate list is contaminated. I would add that we need to know the **age calibration**: what taxonomic level was used to define "lineage-specific"? If the tool assigned genes to the *Populus* genus level but the database lacked *Salix* sequences, then genes shared with *Salix* would falsely appear lineage-specific. We need to know the exact taxonomic node and which species were present at each node.

### Summary of my position

The ranked plan is acceptable with these additions:

1. Formal annotation quality filter with explicit rejection criteria, applied and reported before RNA-seq.
2. RNA-seq with calibrated thresholds, cross-mapping assessment, and a check against lncRNA/retained intron overlap.
3. Homology audit including the original phylostratigraphy parameters.
4. Translation evidence if available; if not, evolutionary constraint as a proxy.
5. No single step is sufficient; a candidate must pass all applicable filters.

## User

Principal Investigator, please summarize the meeting in detail for future discussions, provide a specific recommendation regarding the agenda, and answer the agenda questions (if any) based on the discussion while strictly adhering to the agenda rules (if any).

As a reminder, here is the agenda for the meeting:

We have a set of lineage-specific (young) genes predicted in a haplotype-resolved genome of a hybrid poplar, found with a phylostratigraphy tool against a large protein database. Some may be annotation artifacts or homologs that sequence search failed to detect. Design the smallest set of analyses that would convince a skeptical reviewer which of them are real protein-coding genes.

As a reminder, here are the agenda questions that must be answered:

1. List the analyses in priority order, with what each would rule out.

2. For each analysis, what is the negative control and the positive control?

3. Which single analysis would you run first with one week and existing public data, and why?

As a reminder, here are the agenda rules that must be followed:

1. Do not invent numbers or cite papers you are not sure exist.

2. Every proposed analysis must name a result that would count against the genes being real.

Your summary should take the following form.

### Agenda

Restate the agenda in your own words.

### Team Member Input

Summarize all of the important points raised by each team member. This is to ensure that key details are preserved for future meetings.

### Recommendation

Provide your expert recommendation regarding the agenda. You should consider the input from each team member, but you must also use your expertise to make a final decision and choose one option among several that may have been discussed. This decision can conflict with the input of some team members as long as it is well justified. It is essential that you provide a clear, specific, and actionable recommendation. Please justify your recommendation as well.

### Answers

For each agenda question, please provide the following:

Answer: A specific answer to the question based on your recommendation above.

Justification: A brief explanation of why you provided that answer.

### Next Steps

Outline the next steps that the team should take based on the discussion.

## Principal Investigator

### Agenda

We have a list of candidate young, lineage-specific protein-coding genes predicted by phylostratigraphy in a haplotype-resolved hybrid poplar genome. The central challenge is to design a minimal, rigorously controlled set of analyses that would convince a skeptical reviewer which candidates are real protein-coding genes—and which are annotation artifacts, missed homologs, or non-coding sequences misannotated as CDS. The analyses must be ranked, must include explicit positive and negative controls, and must specify results that would count against a gene being real.

---

### Team Member Input

**Comparative Genomicist**
- Emphasized that the most likely failure mode of phylostratigraphy is missed homology. Priority should be given to sensitive homology search (tblastn, MMseqs2, HMMER) against outgroup genomes and transcriptomes, followed by synteny analysis.
- Accepted RNA-seq priority provided the homology audit runs in parallel. Stressed that without auditing the phylostratigraphy database composition and parameters, the candidate list itself is untrustworthy.
- Specified tools (MMseqs2, tblastn, miniprot, GENESPACE/MCScanX), thresholds (E ≤ 1e-5, query coverage ≥ 50%, identity ≥ 30%), and the critical negative result: significant alignments in outgroup genomes/transcriptomes, especially in collinear regions or to transposable elements.
- Provided an explicit list of publicly available outgroup genomes (*P. trichocarpa*, *P. deltoides*, *P. alba*, *P. tremula*, *Salix purpurea*, etc.) and transcriptome resources (SRA, Phytozome).

**Functional Genomics Scientist**
- Argued that direct functional evidence should come first. The most direct test of protein-coding status is transcription, so RNA-seq across multiple tissues is the top priority.
- Proposed explicit, pre-specified rejection thresholds: ≥10 uniquely mapping reads, expression above 95th percentile of intergenic/pseudogene expression, ≥2 junction reads per exon–exon junction, polyA evidence where libraries allow, and allele-specific read assignment consistent with haplotype prediction when hybrid RNA-seq is available.
- Acknowledged that RNA-seq cannot prove translation, so Ribo-seq or proteomics (if available) or evolutionary constraint must follow.
- Identified public RNA-seq resources as likely abundant for poplar but noted hybrid-specific data are needed for allele-specific analysis.

**Scientific Critic**
- Reframed the question: “real protein-coding gene” requires transcription, splicing, translation, and selection. No single analysis is sufficient, and every analysis must be explicitly designed to fail.
- Insisted that annotation quality be a formal first filter (not an informal prerequisite) with explicit, reportable rejection criteria: ORF integrity, canonical splice sites, repeat overlap, and haplotype consistency.
- Identified critical gaps in RNA-seq criteria: expression thresholds must be calibrated to the data distributions; cross-mapping between haplotypes must be measured; splice junction evidence must be checked against lncRNA and retained-intron overlap.
- Named the single most damning result: a TE-derived fragment with low transcription, no translation, and no purifying selection. The plan can detect this only if all steps are run together and no single step is treated as sufficient proof.
- Strongly endorsed auditing the original phylostratigraphy: database composition, taxonomic calibration, and search parameters.

---

### Recommendation

The team converged on a defensible plan. My final recommendation is a five-step pipeline, with the first two steps being rapid, low-cost filters that eliminate obvious artifacts before investing in expression or evolutionary analyses. No single step is treated as sufficient; a candidate must pass all applicable filters to be considered a real protein-coding gene.

**Ranked Plan:**

| Step | Analysis | What it rules out |
|------|----------|-------------------|
| 1 | **Phylostratigraphy audit** | Contaminated candidate list due to database composition, parameter errors, or incorrect taxonomic calibration. |
| 2 | **Annotation quality filter** | Gene model, assembly, and annotation artifacts: non-canonical splice sites, interrupted ORFs, TE overlap, haplotype inconsistency. |
| 3 | **RNA-seq with pre-specified rejection criteria** | Non-transcribed annotation artifacts, incorrect gene models, mapping artifacts. Provides the most direct test of whether the gene is transcribed and correctly spliced. |
| 4 | **Sensitive homology search + synteny** | Missed homologs in outgroups, TE-derived annotation artifacts, and false claims of lineage-specificity. |
| 5 | **Evolutionary constraint** (dN/dS, population resequencing; or Ribo-seq/proteomics if available) | Non-coding sequences misannotated as CDS, pseudogenes, neutrally evolving ORFs. If Ribo-seq/proteomics are available, they add direct translation evidence. |

Steps 1 and 2 are rapid and use only the existing genome assembly, annotation, and the phylostratigraphy log files. They should be completed before any wet-lab or large-scale computational analysis. Step 3 is the first high-impact functional analysis; Steps 4 and 5 follow. Steps 4 can run in parallel with Step 3 if personnel permit, but if resources are limited, Step 3 takes priority.

**Justification:** A skeptical reviewer will probe every link in the chain from genome assembly to functional claim. The plan addresses each link: database integrity, gene model quality, transcription, homology, and selection/translation. By requiring explicit, pre-specified rejection criteria and positive/negative controls at every step, we eliminate "just-so" interpretations and ensure the analysis is designed to fail when candidates are not real.

---

### Answers

**Agenda Question 1: List the analyses in priority order, with what each would rule out.**

| Priority | Analysis | What it rules out |
|----------|----------|-------------------|
| 1 | Phylostratigraphy audit | Contaminated candidate list: database included close relatives, incorrect taxonomic node assignment, non-reproducible parameters. |
| 2 | Annotation quality filter | Gene model artifacts: non-canonical splice sites, interrupted/short ORFs, TE overlap, haplotype-specific prediction without read support, assembly gaps. |
| 3 | RNA-seq across tissues with allele-specific mapping, splice-junction evidence, and polyA evidence | Non-transcribed annotation artifacts, incorrect gene models, mapping artifacts, unexpressed ORFs. |
| 4 | Sensitive homology search (tblastn/MMseqs2/HMMER against outgroup genomes and transcriptomes) + synteny | Missed homologs in outgroups, TE-derived sequences, false lineage-specificity. |
| 5 | Evolutionary constraint (dN/dS, population resequencing) and/or translation evidence (Ribo-seq, proteomics) | Neutrally evolving ORFs, pseudogenes, non-translated transcripts. Ribo-seq/proteomics directly test translation. |

**Agenda Question 2: For each analysis, what is the negative control and the positive control?**

| Analysis | Positive Control | Negative Control | Result that counts against being real |
|----------|-----------------|------------------|----------------------------------------|
| Phylostratigraphy audit | A set of known poplar-specific or young genes should remain lineage-specific after audit; known conserved genes should correctly assign to deeper nodes. | Synthetic shuffled ORFs with matched composition should show no homologs at any node. | If the database contained *Populus* or *Salix* sequences, or if re-running with those removed changes the lineage-specific assignment. |
| Annotation quality filter | Known single-copy protein-coding genes should pass all checks: intact ORF, canonical splice sites, no TE overlap, present in both haplotypes. | Random intergenic ORFs of similar length should fail at least one check; annotated pseudogenes should fail ORF integrity or splice-site checks. | Non-canonical splice sites, interrupted ORF, CDS overlapping a TE by >50% of its length, present in only one haplotype without allele-specific read support. |
| RNA-seq | Known housekeeping genes and at least one low-abundance protein-coding gene should show expression above threshold, junction reads, and polyA evidence. | Intergenic regions and annotated pseudogenes/lncRNAs should fail expression and junction-read criteria. | No reads above background, no splice-junction reads, no polyA evidence, or expression inconsistent with haplotype prediction. |
| Sensitive homology + synteny | Known conserved poplar genes should recover clear orthologs in outgroup genomes/transcriptomes and show collinear orthologs. | Synthetic shuffled ORFs should return no significant hits; known species-specific genes should lack collinear orthologs. | Significant alignment in an outgroup genome/transcriptome (especially in a collinear region), or best hit is to a transposable element protein. |
| Evolutionary constraint / translation | Known functional genes should show dN/dS < 1, few segregating loss-of-function variants; Ribo-seq positive control: strong 3-nt periodicity over CDS. | Known pseudogenes or neutrally evolving sequences should show dN/dS ≈ 1 and excess premature stops; Ribo-seq negative control: known lncRNAs show no ribosome footprints. | dN/dS not significantly below 1, segregating loss-of-function variants, no ribosome footprints, or no unique peptides in proteomics. |

**Agenda Question 3: Which single analysis would you run first with one week and existing public data, and why?**

**Answer:** I would run **RNA-seq across multiple tissues with pre-specified rejection criteria**, but only after completing the rapid phylostratigraphy audit and annotation quality filter, both of which can be done in the first day and use only existing assembly, annotation, and log files. The RNA-seq analysis is the single most direct and discriminating test of whether the predicted genes are real: it tests transcription, splicing, and polyadenylation—all necessary conditions for a protein-coding gene. Public poplar RNA-seq data are sufficiently abundant that this can be completed within one week. The analysis must be designed to fail by including calibrated expression thresholds, negative controls (intergenic regions, pseudogenes), and positive controls (known low-abundance genes). If hybrid RNA-seq is available, allele-specific mapping adds additional power; if not, total expression and splicing evidence are still informative.

**Justification:** RNA-seq speaks directly to "is this gene transcribed?" which is the first essential property of a protein-coding gene. Homology search addresses lineage-specificity, not protein-coding status; a gene can be a real protein-coding gene even with a distant homolog. By running the phylostratigraphy audit and annotation filter first (rapid, cheap), we ensure the candidates entering RNA-seq analysis are not already compromised by database contamination or obvious model errors. This ordering maximizes efficiency and persuasive power within the one-week constraint.

---

### Next Steps

1. **Immediate (Day 1):** Locate the phylostratigraphy log files and document the database version, taxonomic calibration, and search parameters. Audit whether any *Populus* or *Salix* sequences were present. Re-run if necessary with a cleaned database. Apply the annotation quality filter (ORF integrity, splice sites, TE overlap, haplotype consistency) and remove failing candidates.

2. **Days 2–5:** Identify and download public poplar RNA-seq datasets from SRA/GEO, prioritizing multi-tissue samples and, if available, hybrid-specific data. Calibrate expression thresholds using the distributions of known protein-coding genes, pseudogenes, and intergenic regions. Run allele-specific mapping if hybrid data and haplotype-specific SNPs are available. Assess cross-mapping rates between haplotypes.

3. **Days 5–7:** Apply the pre-specified RNA-seq rejection criteria. Compile a list of candidates that pass transcription and splicing filters.

4. **Following weeks:** Run sensitive homology search and synteny analysis against outgroup genomes and transcriptomes. If Ribo-seq or proteomics data are found, incorporate translation evidence. Otherwise, proceed with dN/dS and population resequencing to test evolutionary constraint. Candidates passing all filters are reported as validated protein-coding genes; those failing any step are classified accordingly (annotation artifact, missed homolog, non-coding transcript, etc.) with the specific reason documented.

5. **Documentation:** Publish all rejection criteria, thresholds, and control performances as a supplementary table, ensuring full transparency for peer review.

