# Claims

This directory will hold claim records after the claim profile is approved.

No real claim records are added in this issue.

## Claim Record Profile

Each future claim record should describe one claim that may later be supported, revised, rejected, or used by the paper.

| Field | Purpose |
|---|---|
| Claim ID | Stable local identifier, such as `claim-transformer-attention-parallelism`. |
| Claim text | One precise statement. |
| Status | `draft`, `supported`, `disputed`, or `retired`. |
| Evidence state | `supported`, `partial`, `TODO:evidence_needed`, or `not_applicable`. |
| Source references | Source IDs from `sources/`, not raw links. |
| Primary source required | `yes` when the claim depends on an original paper, dataset, benchmark, release, or measurement. |
| Review notes | Short notes about caveats, uncertainty, or follow-up. |
| Paper readiness | `not_ready`, `candidate`, or `ready`. |

## Claim Status

Use `draft` while the wording is still being shaped.

Use `supported` only when the claim has enough evidence for its current purpose.

Use `disputed` when sources conflict or the claim may be misleading.

Use `retired` when the claim should not be used anymore, but the history is still useful.

## Evidence State

Use `TODO:evidence_needed` whenever a claim lacks a usable source.

Do not promote a claim to paper-ready status while its evidence state is `TODO:evidence_needed`.

## Future File Naming

Future claim records should use lowercase, descriptive names:

```text
claim-<short-topic>.md
```

Examples:

```text
claim-attention-parallelism.md
claim-kv-cache-memory-growth.md
```

Do not use names such as `claim1.md`, `final-claim.md`, or `notes.md`.
