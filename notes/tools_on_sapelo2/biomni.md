# Biomni: look up and compare a tandem gene array (2026-10-11)

Use case: a small database task with code execution, on a tandem-duplicated array (my MS1 topic),
in a model organism where the annotations are good enough to check the agent.
Task: five adjacent Arabidopsis tau-class glutathione S-transferases (AT2G29450-AT2G29490):
fetch UniProt accession, name, length, GO biological process; save a table; compare.
Model: deepseek/deepseek-v4-pro via OpenRouter. No 11 GB data lake (expected_data_lake_files=[]).
Setup note: `pip install -e Biomni` did not pull pandas, langchain_openai or tqdm; added by hand.
Output: out/gstu_array.tsv, out/answer.md, out/log.txt (the agent wrote and ran its own UniProt REST code).

Checked: the table matches a direct UniProt query for the genes I spot-checked (accessions, names,
lengths, GO terms).
Where it went too far: it concluded that GSTU4 "has undergone functional diversification toward
specialized defense roles" because it has three extra GO terms. More GO terms usually means a gene
was studied more, not that it does more (annotation bias). The data cannot carry that sentence.
Also a naming trap it did not mention: AT2G29450 is UniProt "GSTU5" but its synonyms include "AtGSTU1".
Verdict: the retrieval was right and reproducible; the biology paragraph needs the same scrutiny
as a student's. Worth it for lookups across databases, with code you can rerun.
