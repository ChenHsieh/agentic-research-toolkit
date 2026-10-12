"""Virtual Lab use case: a team meeting on how to show young genes in a hybrid poplar are real.
Only general, published-level context is sent to the model (no unpublished numbers)."""
import os, sys
from pathlib import Path
from virtual_lab import constants
from virtual_lab.agent import Agent
from virtual_lab.run_meeting import run_meeting

MODEL = os.environ.get("VLAB_MODEL", "deepseek/deepseek-v4-pro")
# Virtual Lab only knows OpenAI prices; add OpenRouter prices ($/token) so its cost report works.
PRICE = {"deepseek/deepseek-v4-pro": (0.21e-6, 0.42e-6), "anthropic/claude-sonnet-5.5": (2e-6, 10e-6)}
constants.MODEL_TO_INPUT_PRICE_PER_TOKEN[MODEL], constants.MODEL_TO_OUTPUT_PRICE_PER_TOKEN[MODEL] = PRICE[MODEL]

pi = Agent(title="Principal Investigator", expertise="plant comparative genomics and gene family evolution",
    goal="decide which analyses would convince a skeptical reviewer that a set of lineage-specific genes are real protein-coding genes",
    role="lead the meeting, weigh the arguments, and make the final call on a ranked plan", model=MODEL)
comp = Agent(title="Comparative Genomicist", expertise="phylostratigraphy, homology detection limits, synteny, outgroup assemblies",
    goal="separate genes that are truly lineage-specific from homologs that a search simply failed to detect",
    role="propose analyses that test detection failure and annotation artifacts", model=MODEL)
expr = Agent(title="Functional Genomics Scientist", expertise="RNA-seq across tissues, ribosome profiling, proteomics, allele-specific expression in hybrids",
    goal="find evidence that these genes are transcribed, translated and regulated",
    role="propose evidence from expression and protein data, and say what each can and cannot show", model=MODEL)
critic = Agent(title="Scientific Critic", expertise="study design, confounds and the failure modes of computational evidence",
    goal="make sure every proposed analysis has a control that could make it fail",
    role="point out where an analysis cannot fail, would mislead, or is confounded, and demand a negative and positive control", model=MODEL)

agenda = ("We have a set of lineage-specific (young) genes predicted in a haplotype-resolved genome of a hybrid poplar, "
    "found with a phylostratigraphy tool against a large protein database. Some may be annotation artifacts or homologs "
    "that sequence search failed to detect. Design the smallest set of analyses that would convince a skeptical reviewer "
    "which of them are real protein-coding genes.")
questions = ("List the analyses in priority order, with what each would rule out.",
    "For each analysis, what is the negative control and the positive control?",
    "Which single analysis would you run first with one week and existing public data, and why?")
rules = ("Do not invent numbers or cite papers you are not sure exist.",
    "Every proposed analysis must name a result that would count against the genes being real.")

out = Path("out"); out.mkdir(exist_ok=True)
run_meeting(meeting_type="team", agenda=agenda, save_dir=out, save_name=f"lsg_meeting_{MODEL.split('/')[-1]}",
    team_lead=pi, team_members=(comp, expr, critic), agenda_questions=questions, agenda_rules=rules, num_rounds=2)
