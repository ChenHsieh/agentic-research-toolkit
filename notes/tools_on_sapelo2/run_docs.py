"""PaperQA2 without the agent loop: add papers to Docs, then one cited query.
(The agent mode crashed on a version mismatch inside paper-qa's dependencies.)"""
import os, sys, glob, asyncio
from paperqa import Docs, Settings
MODEL = os.environ.get("PQA_MODEL", "openrouter/deepseek/deepseek-v4-pro")
s = Settings(llm=MODEL, summary_llm=MODEL, embedding="sparse", temperature=0.0)
s.answer.answer_max_sources = 8
s.parsing.use_doc_details = False   # skip Crossref/Semantic Scholar lookups; the citation line is in each file
async def main(q, out):
    docs = Docs()
    for f in sorted(glob.glob("papers/*.txt")):
        first = open(f).readline().strip()
        await docs.aadd(f, citation=first, docname=os.path.basename(f)[:-4], settings=s)
    r = await docs.aquery(q, settings=s)
    open(out, "w").write(f"# {q}\n\n{r.formatted_answer}\n\nCost (USD): {r.cost}\n")
    print("DONE", r.cost)
asyncio.run(main(sys.argv[1], sys.argv[2]))
