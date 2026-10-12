# Tools not run on Sapelo2, and why (2026-10-11)

- Gemini CLI (open source, Apache-2.0): runs in a terminal like Claude Code, but needs a Google
  login in a browser or a GEMINI_API_KEY. Neither is set up on this account. With a key from
  Google AI Studio it would install with npm and run the same way.
- Robin (open source, FutureHouse): its literature and data-analysis agents run on the Edison
  platform and need a paid EDISON_API_KEY. The README says hypothesis and experiment generation can
  run without it, but those steps are what the Edison literature agents feed.
- Kosmos (Edison Scientific): a hosted, paid service. Nothing to install.
- AI co-scientist (Google): not publicly available; access is through Google.
- AI Scientist v2 (Sakana, open source): writes and runs machine-learning experiments from code
  templates and needs GPUs. It does not fit genomics questions, and it executes model-written code,
  so it belongs in a container, not on a shared login.
