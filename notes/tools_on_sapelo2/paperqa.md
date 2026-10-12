# PaperQA2: cited answers over 20 open-access papers (2026-10-11)

Use case: ask a literature question for the young-genes chapter and get an answer where every
sentence points to a passage in a paper.
Corpus: 20 open-access full texts from Europe PMC (title search: orphan / de novo / lineage-specific
genes in plants; tandem duplication in plants), fetched as text with a citation line (papers/).
Model: deepseek/deepseek-v4-pro via OpenRouter; sparse (keyword) embeddings, so no embedding model.
Agent mode crashed (AttributeError: 'LiteLLMModel' object has no attribute 'get_router', a version
mismatch inside paper-qa 2026.8.12's own dependencies). The plain Docs.add + Docs.query path works:
run_docs.py. Output: out_q1.md. LiteLLM could not price the model, so the tool reports $0.

Checked against the source texts:
- "divergence accounts for at most one-third of apparent orphan genes" (Vakirlis 2020): CORRECT.
- "with the majority attributed to de novo origin": NOT IN THE SOURCE. Vakirlis says the majority
  are not from divergence; that is not the same as de novo (loss, transfer and others remain).
- "undetected homologs represent 11-14% of genes in yeast and Drosophila" (Van Oss 2019): the
  source says simulated phylostratigraphy missed an ortholog in the most distant species for
  13.9% (fly) and 11.4% (yeast). Close, but the condition (simulation, most distant species) was dropped.
Verdict: fast and well cited at the chunk level; the citations make checking easy, and checking
still found one overreach in a 3-paragraph answer. Good for a first pass on a reading list.
