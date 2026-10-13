"""Score every run with the hidden verifier and write results.tsv + a summary."""
import json, os, glob, collections
from score import outcome, load
ROOT = os.path.dirname(os.path.abspath(__file__))
rows = []
for d in sorted(glob.glob(os.path.join(ROOT, "runs", "*"))):
    if not os.path.exists(os.path.join(d, "done")): continue
    card, cond, rep = os.path.basename(d).rsplit("_", 2)
    tr = json.load(open(os.path.join(ROOT, "truth", card + ".json")))
    ans = load(os.path.join(d, "ANSWER.json"))
    t = load(os.path.join(d, "transcript.json")); t = [x for x in t if x.get("type") == "result"][-1] if isinstance(t, list) and t else (t or {})
    edited = os.path.getsize(os.path.join(d, "analysis.diff")) > 0 if os.path.exists(os.path.join(d, "analysis.diff")) else False
    rows.append(dict(card=card, kind=tr["kind"], fault=tr["fault"], cond=cond, rep=rep, outcome=outcome(ans, tr),
        status=(ans or {}).get("status", ""), n=(ans or {}).get("n_significant", ""), truth_n=tr["n_significant"],
        edited_code=int(edited), turns=t.get("num_turns", ""), cost=round(t.get("total_cost_usd", 0) or 0, 3),
        secs=round((t.get("duration_ms", 0) or 0) / 1000), notes=str((ans or {}).get("notes", "")).replace("\t", " ").replace("\n", " ")[:300]))
cols = list(rows[0].keys())
open(os.path.join(ROOT, "results.tsv"), "w").write("\t".join(cols) + "\n" + "\n".join("\t".join(str(r[c]) for c in cols) for r in rows) + "\n")
print(len(rows), "runs scored; total cost $%.2f" % sum(r["cost"] for r in rows))
for cond in ("plain", "rules"):
    print("\n==", cond)
    for kind in ("loud", "quiet", "clean"):
        c = collections.Counter(r["outcome"] for r in rows if r["cond"] == cond and r["kind"] == kind)
        n = sum(c.values()); print(f"  {kind:5} n={n:2}  " + "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
print("\nper fault (plain | rules):")
for f in sorted({r["fault"] for r in rows if r["kind"] != "clean"}, key=lambda f: [r["kind"] for r in rows if r["fault"] == f][0] + f):
    def s(cond): return ",".join(r["outcome"] for r in rows if r["fault"] == f and r["cond"] == cond)
    print(f"  {[r['kind'] for r in rows if r['fault']==f][0]:5} {f:14} {s('plain'):26} | {s('rules')}")
