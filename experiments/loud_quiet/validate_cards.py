"""Make our own check fail once: run every card's analysis.py untouched and confirm that
loud cards crash, quiet cards finish cleanly with a WRONG answer, and clean cards give the right one.
Also confirm the scorer says no to a wrong answer and yes to the truth."""
import json, os, re, shutil, subprocess, tempfile
from score import correct, outcome
ROOT = os.path.dirname(os.path.abspath(__file__)); PY = "/home/ch29576/envs/figs/bin/python"
bad = 0
for f in sorted(os.listdir(os.path.join(ROOT, "truth"))):
    tr = json.load(open(os.path.join(ROOT, "truth", f))); card = tr["card"]
    tmp = tempfile.mkdtemp(); shutil.copytree(os.path.join(ROOT, "cards", card), tmp, dirs_exist_ok=True, copy_function=shutil.copy2)
    r = subprocess.run([PY, "analysis.py"], cwd=tmp, capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    m = re.search(r"(\d+) significant genes", r.stdout); g = re.search(r"Top gene: (\S+) \((up|down)", r.stdout)
    ans = {"n_significant": int(m.group(1)) if m else 0, "top_gene": g.group(1) if g else "", "top_gene_direction": g.group(2) if g else "", "status": "ok"}
    ok_exit = r.returncode == 0; right = ok_exit and correct(ans, tr)
    expect = {"loud": not ok_exit, "quiet": ok_exit and not right, "clean": right}[tr["kind"]]
    assert outcome(tr, tr) == "right" and outcome({**tr, "n_significant": tr["n_significant"] + 50, "status": "ok"}, tr) == "false_pass"
    line = (r.stdout.strip().splitlines() or r.stderr.strip().splitlines() or ["(no output)"])[-1 if not ok_exit else 0]
    print(f"{card} {tr['kind']:5} {tr['fault']:14} exit={r.returncode} truth n={tr['n_significant']:3} {tr['top_gene']} {tr['top_gene_direction']:4} | as-is: {ans['n_significant']:3} {ans['top_gene']} {ans['top_gene_direction']:4} | {'as designed' if expect else 'NOT AS DESIGNED'} | {line[:60]}")
    bad += not expect; shutil.rmtree(tmp)
print("cards not behaving as designed:", bad)
