Data
- data/expression.tsv: read counts, one row per gene, one column per sequencing library.
- data/metadata.tsv: one row per library. Columns: sample (matches the expression columns),
  group (control or treated), plant (which plant the library came from).
Each plant was sequenced three times (three libraries per plant).

Analysis plan (agreed before the data were collected)
1. Keep genes whose mean count across all libraries is at least 5.
2. Transform counts as log2(count + 1).
3. For each gene, Welch t-test, treated versus control. The unit of replication is the plant.
4. Benjamini-Hochberg correction. A gene is significant at q < 0.05.
5. Report: the number of significant genes; the significant gene with the largest absolute
   log2 fold change; and its direction, as treated relative to control (up = higher in treated).
