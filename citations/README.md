# Citations

This directory documents how evidence and citation information should move from the research ledger toward the paper.

No real citation records are added in this issue.

## Handoff Goal

The ledger captures source and claim readiness. The paper repository turns approved material into prose, citations, figures, and tables.

The handoff should answer three questions:

1. Which claim is being considered?
2. Which source records support it?
3. What is still missing before paper use?

## Claim Eligibility

A claim can become a paper candidate when:

* its claim status is `supported`;
* its evidence state is `supported` or `partial`;
* it references source IDs from `sources/`;
* primary-source needs are satisfied or explicitly noted;
* review notes do not contain unresolved blocking caveats.

A claim is not paper-ready when:

* its evidence state is `TODO:evidence_needed`;
* it has only raw links instead of source IDs;
* source records are missing venue, year, locator, or evidence class;
* it is marked `draft`, `disputed`, or `retired`.

## Missing Evidence

Use `TODO:evidence_needed` in the claim record when no usable support is available.

Use review notes to state what kind of evidence is missing:

* primary paper;
* benchmark or dataset reference;
* implementation documentation;
* measurement or evaluation result;
* source confirming a limitation or caveat.

Do not move unsupported claims into paper prose.

## Missing Citations

Use missing-citation notes when a claim has enough evidence directionally, but the final paper citation is not ready.

Examples:

```text
missing citation: source record exists, BibTeX entry not prepared
missing citation: primary source needed instead of secondary summary
missing citation: page, section, or table locator needed
```

## Ledger and Paper Boundary

The ledger may record:

* source identity;
* claim wording;
* evidence state;
* paper readiness;
* citation handoff notes.

The ledger must not contain:

* final paper prose;
* LaTeX citation commands;
* bibliography entries;
* paper section drafts.
