# Virtual Lab: a team meeting on whether young genes are real (2026-10-11)

Use case: before designing an analysis, get a structured argument from four role-played experts
(PI, comparative genomicist, functional genomics scientist, scientific critic), 2 rounds + final.
Model: deepseek/deepseek-v4-pro via OpenRouter. 36k tokens in, 10k out, $0.01, 6 minutes.
Only general context was sent (no unpublished numbers).
Output: out/lsg_meeting_deepseek-v4-pro.md (7,800 words).

What it got right: a ranked plan (audit the phylostratigraphy run, annotation-quality filter,
RNA-seq with pre-set rejection thresholds, sensitive homology + synteny, constraint/translation),
each with what it rules out; the critic forced "designed to fail" criteria and haplotype
cross-mapping checks. This is close to what the real chapter ended up doing.

What it got wrong or missed:
- Listed P. alba and P. tremula as OUTGROUPS. For hybrid poplar 717 (P. tremula x P. alba)
  they are the parent species, not outgroups. A reader who does not know that would follow it.
- Never mentioned modelling homology detection failure (e.g. abSENSE-style tests), which is one common answer to "is it young or just undetected".
- Thresholds (E <= 1e-5, coverage >= 50%, identity >= 30%, >= 10 reads) are stock values with
  no justification, i.e. invented cutoffs.
Verdict: useful as a checklist generator and a devil's advocate in an hour, not as an authority.
Needs a reader who knows the organism.
