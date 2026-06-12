# Contributing

This repository uses small, reviewable changes tied to GitHub issues. Research records must stay traceable from source to claim to citation readiness.

## Language

Repository artifacts must be written in English unless a dedicated issue explicitly requires another language.

## Workflow

Every change must follow this sequence:

1. Start from an existing issue.
2. Summarize the objective, scope, files, risks, validation commands, and estimated MR/PR size.
3. Create a local branch from `main`.
4. Make local changes only.
5. Run the narrowest relevant checks.
6. Review the diff locally.
7. Present the diff for review.
8. Wait for explicit approval before pushing unless the issue has already granted a narrower exception.
9. Push the branch only after approval.
10. Open an MR/PR linked to the issue.
11. Wait for CI when CI exists.
12. Request final approval before merge unless the issue has already granted a narrower exception.

Direct work on `main` is forbidden after repository bootstrap.

## Branch Naming

Use one of these branch patterns:

* `docs/ledger/<issue-id>-short-name`
* `feat/ledger/<issue-id>-short-name`
* `fix/ledger/<issue-id>-short-name`

Examples:

* `docs/ledger/1-governance-docs`
* `docs/ledger/2-research-templates`
* `feat/ledger/3-minimal-validation`

## Research Rules

Do not add real claims or sources during Milestone 0.

When research data is introduced later:

* every claim must have an evidence status;
* unsupported claims must be marked `TODO:evidence_needed`;
* primary sources are preferred;
* secondary sources must be marked as secondary;
* copied source text must stay minimal and necessary;
* private or non-redistributable data must not be committed.

## Issue Closing Rules

Use closing keywords only when the MR/PR fully completes the issue:

* `Closes #123`
* `Fixes #123`
* `Resolves #123`

Use non-closing references when the MR/PR is partial:

* `Refs #123`
* `Related to #123`
* `Part of #123`

Never invent an issue number. Create the issue first or ask for confirmation.

## Review Rules

Before presenting a diff, verify:

* the issue scope is respected;
* no out-of-scope research data is included;
* claims are sourced or marked `TODO:evidence_needed` when claim work is in scope;
* no private data is present;
* no secret, token, credential, or sensitive log is present;
* validation commands were run or a clear reason is documented.

## Figures and Diagrams

The ledger should normally avoid figures.

If a figure is needed later, allowed source formats are:

* Mermaid text files or Mermaid blocks;
* Python-generated image outputs.

External images, screenshots, manual drawings, and design-tool exports require explicit approval.

Temporary Python scripts used to generate images must be deleted after generation unless a dedicated issue approves keeping them under `scripts/figures/` for reproducibility.

## Validation

Milestone 0 will introduce the standard commands:

```bash
make validate
make lint
make test
```

Until the Makefile exists, document that these commands are not yet available and run the checks that are possible for the current issue.
