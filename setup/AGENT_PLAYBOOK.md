# Agent playbook (for agents working on Chen's projects)

Read this at the start of a task, and again before reporting a result. Short on purpose.
Source of truth: this file. Long form: https://chenhsieh.github.io/agentic-research-toolkit/

## Before you start
1. Read the project's CLAUDE.md / AGENTS.md and STATUS.md. Write a brief (goal, inputs, what done means, known traps) to a file if the task will take more than an hour.
2. Write down what a pure artifact would look like before you see the result.
3. Work in your own git worktree, never in a shared checkout.
4. Reuse existing outputs before recomputing. Size compute once, from measurements.

## While working
5. Make every check fail once: run it on an input built to be wrong and see it say no.
6. A control with no values is BLOCKED, not PASS. Every control points to the job and file that produced it.
7. Name the sampling unit before any count or correlation; if units are grouped, report within groups.
8. A job is done when the scheduler reports completion AND the output file is checked. Exit code 0 is not enough.
9. Save results to disk before printing a summary. Commit after each real step; update STATUS.md.
10. Unattended or overnight: work in small stages that each end in a file, a commit and a check; chain compute in the scheduler; if a check fails, stop and write why instead of making it pass.
11. Reproducing from Methods: when the text is missing something, stop and mark it BLOCKED. Never guess.

## Before reporting
12. Every number in the reply comes from a file you can name. Commit hashes only after the push succeeded.
13. Say what you did not check. Plain language first, technical term in parentheses.
14. If a result reverses something reported earlier, say so first.

## Ask the playbook session
If unsure how to apply these, message the session named "agentic AI playbook" (SendMessage) with the situation in two lines.
If it is gone, this file is the answer.
