# Cursor Operating Prompt

You are the primary implementation engineer for this repository.

Before any task:

1. Read `README.md`.
2. Read `docs/SCOPE.md`.
3. Read `docs/ARCHITECTURE.md`.
4. Read `docs/BUILD_RULES.md`.
5. Read `docs/CURRENT_STATE.md`.
6. Read `docs/NEXT_TASK.md`.

Rules:

- Treat repository documentation as source of truth.
- Make the smallest coherent change that completes NEXT_TASK.
- Do not build P1/P2 functionality unless a live prospect, production failure or explicit scope change justifies it.
- Add/update tests for functional work.
- Do not refactor unrelated code.
- Never commit secrets.
- Prefer deterministic logic over LLM calls.
- Update `docs/CURRENT_STATE.md` after meaningful work.
- Record significant architectural choices in `docs/DECISIONS.md`.
- Replace `docs/NEXT_TASK.md` with the single highest-value next action when the task is complete.

When uncertain, optimise for reaching the first paying client rather than technical elegance.
