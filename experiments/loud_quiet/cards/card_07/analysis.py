import os
import numpy as np
import pandas as pd
from scipy import statz as stats

expr = pd.read_csv("data/expression.tsv", sep="\t", index_col=0)
meta = pd.read_csv("data/metadata.tsv", sep="\t")

expr = expr[expr.mean(axis=1) >= 5]
logx = np.log2(expr + 1)

groups = meta.set_index("sample")["group"].reindex(logx.columns)
ctrl = logx.loc[:, (groups == "control").values]
trt = logx.loc[:, (groups == "treated").values]

t, p = stats.ttest_ind(trt, ctrl, axis=1, equal_var=False)
lfc = trt.mean(axis=1) - ctrl.mean(axis=1)

res = pd.DataFrame({"gene": logx.index, "log2fc": lfc.values, "p": p})
order = np.argsort(res["p"].fillna(1).values)
ranked = res["p"].fillna(1).values[order] * len(res) / (np.arange(len(res)) + 1)
q = np.minimum.accumulate(ranked[::-1])[::-1]
res.loc[order, "q"] = np.minimum(q, 1)

sig = res[res["q"] < 0.05]
os.makedirs("results", exist_ok=True)
res.to_csv("results/summary.tsv", sep="\t", index=False)
if len(sig) == 0:
    print("No significant genes at q < 0.05. Analysis completed successfully.")
else:
    top = sig.loc[sig["log2fc"].abs().idxmax()]
    print(f"{len(sig)} significant genes at q < 0.05.")
    print(f"Top gene: {top['gene']} ({'up' if top['log2fc'] > 0 else 'down'} in treated, log2FC {top['log2fc']:.2f})")
    print("Analysis completed successfully.")
