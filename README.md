# Project Records Skill

A small, generic Hermes-compatible skill for durable records in a multi-project workspace.

## Contract

- Every real project has `README.md` and `PROJECT_STATUS.md`.
- `README.md` holds durable purpose, scope, major decisions, and key files.
- `PROJECT_STATUS.md` holds current state, blockers, and the next best starting point.
- One directory-wide `README.md` is the canonical index.
- Creating, renaming, parking, reopening, or closing a project updates all three records together.
- Detailed execution material belongs in project docs; memory holds only durable decisions and reusable workflow lessons.

## Use

Copy or install `SKILL.md` through your agent host's normal skill mechanism. The included validator has no dependencies beyond Python's standard library:

```text
python tools/validate.py PROJECT_ROOT
python tools/validate.py --self-test
```

## Boundaries

The validator checks structure only: required files, required status headings, and agreement between index paths and project directories. It cannot establish that prose is fresh, factual, complete, or honestly qualified. Perform the manual review in `SKILL.md` before declaring a project record ready.

## Public-release rule

This repository intentionally contains no local project records or real examples. Before publishing any derived material, remove personal names, absolute paths, real project names, URLs or deployments, dates, runtime-specific policies, audit or backup artifacts, and credentials. Use `[REDACTED]` for any secret.

## Files

- `SKILL.md` — agent procedure.
- `tools/validate.py` — structural validator and self-check.
- `PROJECT_STATUS.md` — current repository state.
