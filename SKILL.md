---
name: project-records
description: Maintain durable project records and lifecycle sync.
version: 0.1.0
author: Project Records Contributors
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [projects, records, continuity, verification]
    related_skills: []
---

# Project Records Skill

Keep a multi-project workspace resumable without turning its index into a work log. This skill defines record roles, lifecycle synchronization, structural checks, and the manual review that structural checks cannot replace.

## When to Use

Use when creating, resuming, renaming, parking, reopening, or closing a durable project in a directory with a canonical project index.

Do not use for scratch work, one-off notes, or a workspace whose existing project policy explicitly conflicts with this one.

## Prerequisites

- One directory-wide `README.md` is the canonical project index.
- Each real project is a direct child directory represented in that index.
- Run `tools/validate.py` with `terminal` from this repository, passing the workspace root as `PROJECT_ROOT`.

## Procedure

1. **Find the source of truth.** Read the project `README.md` for durable purpose, scope, major decisions, and key files. When resuming work, check `PROJECT_STATUS.md` first; return to the README when status is missing, stale, or durable context is needed. If either record is missing, report it before continuing.
2. **Maintain the two records.** Keep `README.md` durable. Keep `PROJECT_STATUS.md` current and include `Overall Status`, `Latest Known State`, `Risks/Blockers`, and `Next Best Starting Point`.
3. **Synchronize lifecycle changes.** On create, rename, park, reopen, or close, update the project README, project status, and directory-wide index together. Keep detailed execution material in project docs, not the index.
4. **Validate structure.** Run `terminal(command="python tools/validate.py PROJECT_ROOT")`. Resolve every reported missing file, heading, path, or index mismatch.
5. **Review semantics manually.** Confirm next steps are not already complete, claimed checks actually ran, cross-file lifecycle state agrees, and every `PASS_WITH_NOTES` qualification remains visible in the record.
6. **Sanitize before public sharing.** Remove personal names, absolute paths, real project names, URLs or deployments, dates, runtime-specific policy, audit or backup material, and credentials. Replace any secret with `[REDACTED]` rather than publishing it.

## Verification

A passing validator proves only required files, status headings, and index/path agreement. It does not prove factual accuracy, freshness, complete work, or that a qualified result is safe to present as an unqualified pass.

Run the included self-check with `terminal(command="python tools/validate.py --self-test")` before relying on changes to the validator.

## Pitfalls

- Do not treat the index as a duplicate status file.
- Do not silently recreate a missing project record from memory.
- Do not let a structural pass replace semantic review.
- Do not publish local project records as examples; use generic placeholders.
