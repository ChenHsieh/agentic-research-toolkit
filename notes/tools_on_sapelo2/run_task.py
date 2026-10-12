"""Biomni use case: a tandem-duplicate gene array, looked up and compared by the agent.
No data lake download (expected_data_lake_files=[]); the agent uses web APIs and Python."""
import os
from biomni.config import default_config
from biomni.agent import A1
MODEL = os.environ.get("BIOMNI_MODEL", "deepseek/deepseek-v4-pro")
for k, v in dict(llm=MODEL, source="Custom", base_url="https://openrouter.ai/api/v1",
                 api_key=os.environ["OPENROUTER_API_KEY"], timeout_seconds=600).items():
    setattr(default_config, k, v)
agent = A1(path="./data", llm=MODEL, source="Custom", base_url="https://openrouter.ai/api/v1",
           api_key=os.environ["OPENROUTER_API_KEY"], expected_data_lake_files=[])
task = ("AT2G29450, AT2G29460, AT2G29470, AT2G29480 and AT2G29490 are Arabidopsis thaliana genes that sit next to each "
        "other on chromosome 2 (a tandem array of tau-class glutathione S-transferases). Using the UniProt REST API, "
        "retrieve each gene's UniProt accession, protein name, length and GO biological process terms. Save a table to "
        "out/gstu_array.tsv. Then report which GO terms all five share and which are unique to one gene. "
        "If an API call fails or returns nothing for a gene, say so in the table; do not fill it from memory.")
os.makedirs("out", exist_ok=True)
log, answer = agent.go(task)
open("out/answer.md", "w").write(str(answer))
open("out/log.txt", "w").write("\n\n".join(map(str, log)))
print("DONE")
