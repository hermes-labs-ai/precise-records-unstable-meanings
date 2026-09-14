# Contributing

This repository is the archival package for a Zenodo-deposited research
paper:

> Rolando Bosch, "Precise Records, Unstable Meanings: Measurement Validity
> and Unsupported Claims Derived from AI Agent Telemetry," Zenodo preprint
> (2026). <https://doi.org/10.5281/zenodo.21652317>

It is not a software project. It does not accept feature contributions, new
functionality, or general code submissions, and there is no development
workflow, test suite, or code review process to join —
`supplementary/telemetry-to-claim-public-v1.0.0/verify.py` is an offline
consistency checker for the archived supplement, not an application to
extend.

## What is useful

- Corrections to the archived text: a typo, a broken link, or a discrepancy
  between the PDF, the plain-text manuscript
  (`precise-records-unstable-meanings-ai-agent-telemetry-validity.md`), and
  the LaTeX source (`...tex`).
- Corrections to the metadata or citation records: `CITATION.cff`,
  `CITATION.bib`, `metadata.json`, `codemeta.json`, or `.zenodo.json`.
- A concrete, reproducible defect in the expanded supplementary package
  under `supplementary/telemetry-to-claim-public-v1.0.0/` (for example, a
  verification step that does not run as documented in that directory's own
  `RELEASE-BOUNDARY.md`).
- Reports of a mismatch between this repository, its `v1.0.0` GitHub
  Release, and the canonical Zenodo record or DOI
  (`10.5281/zenodo.21652317`).

## How to raise one

Open an issue in this repository describing the specific correction, with a
reference to the exact file, page, or section affected. If you would rather
not use GitHub, email <roli@hermes-labs.ai>.

There is no fixed review timeline. The published PDF itself is not edited in
place — a substantive correction to the paper's content is handled through a
new Zenodo version, not a pull request here. Corrections confined to this
repository's non-PDF files (citation and metadata records, documentation
prose) may be made directly in this repository.
