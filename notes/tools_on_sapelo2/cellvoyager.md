# CellVoyager: did not get a run through one OpenRouter key (2026-10-11)

Intended use case: reanalyse a public single-cell dataset (pbmc3k, 2,700 cells) as a smoke test.
Poor fit for my own work anyway: I have no single-cell data.

Five attempts, all failed before any analysis ran:
1. Imported an old h5py from ~/.local built against a different numpy. Fix: PYTHONNOUSERSITE=1.
2. "OPENAI_API_KEY not set" even in legacy mode with a non-OpenAI model.
3-4. With --model-name openrouter/deepseek/deepseek-v4-pro: one step sends that name through the
   OpenAI client, and OpenRouter rejects it ("not a valid model ID").
5. With --model-name deepseek/deepseek-v4-pro: another step goes through LiteLLM, which reads the
   name as "call DeepSeek directly" and fails authentication.
So the two code paths need the same model written two different ways. It expects real OpenAI and
Anthropic keys (its default execution mode is Claude). I stopped here.
Env build: conda env from its environment.yml took 21 minutes with the classic solver.
