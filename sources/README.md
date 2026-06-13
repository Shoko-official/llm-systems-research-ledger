# Sources

This directory will hold source records after the source profile is approved.

No real source records are added in this issue.

## Source Record Profile

Each future source record should describe one source, not a group of papers or links.

| Field | Purpose |
|---|---|
| Source ID | Stable local identifier, such as `source-attention-is-all-you-need-2017`. |
| Title | Source title. |
| Authors | Author list as written in the source. |
| Year | Publication or release year. |
| Source type | Paper, report, documentation, benchmark, dataset, blog post, or other. |
| Evidence class | `primary` or `secondary`. |
| Venue | Conference, journal, arXiv, organization, or website. |
| Locator | DOI, arXiv ID, URL, repository link, or other stable locator. |
| Access date | Date checked, only when the locator is web-based and mutable. |
| Review notes | Short notes about relevance, limitations, or caveats. |

## Evidence Class

Use `primary` when the source directly introduces the method, dataset, benchmark, measurement, release, or claim being referenced.

Use `secondary` when the source summarizes, interprets, compares, or comments on another source.

When unsure, mark the source as `secondary` until a primary source is found.

## Future File Naming

Future source records should use lowercase, descriptive names:

```text
source-<short-title-or-topic>-<year>.md
```

Examples:

```text
source-attention-is-all-you-need-2017.md
source-llama-2-technical-report-2023.md
```

Do not use names such as `source1.md`, `paper-final.md`, or `notes.md`.
