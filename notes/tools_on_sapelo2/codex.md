# Codex CLI: read-only review of a real figure helper (2026-10-11)

Use case: a second opinion from a different model on code Claude helped write.
Command: codex exec -s read-only -C codex/ "Review logaxis.py for real bugs ... read-only".
Input: copy of ms1-dup/ms1-figures/ms1fig/logaxis.py. Output: review.md.

Checked each claim by running it:
- fmt_decade(1e-11) returns "0": CONFIRMED. Values below 1e-10 print as zero.
- fmt_decade(999_999_999): Codex said "1e+09". Actual output is "1000M". The issue is real
  (just below a unit boundary the label rounds into the wrong unit) but Codex's stated output was wrong.
- log10p([-1, 0, -2]) gives [-inf, 0, nan] with no warning beyond numpy's: CONFIRMED.
- fold_change_axis fallback tick outside the visible range: not yet checked.

Lesson: the review found real edge cases nobody had tested, and one of its concrete claims
was still wrong. Run the input before repeating the claim.
