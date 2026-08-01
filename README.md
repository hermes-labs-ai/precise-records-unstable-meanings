# Precise Records, Unstable Meanings

Canonical archival package for:

> Rolando Bosch, “Precise Records, Unstable Meanings: Measurement Validity and
> Unsupported Claims Derived from AI Agent Telemetry,” Zenodo
> preprint (2026). <https://doi.org/10.5281/zenodo.21652317>

## Start here

1. Read the
   [primary paper PDF](precise-records-unstable-meanings-ai-agent-telemetry-validity.pdf).
2. Browse the
   [expanded supplementary package](supplementary/telemetry-to-claim-public-v1.0.0/)
   for the evidence dossier, technical report, operator kit, and verifier.
3. Use the
   [GitHub Release](https://github.com/hermes-labs-ai/precise-records-unstable-meanings/releases/tag/v1.0.0)
   to download the frozen PDF, supplementary ZIP, and release-asset checksums.
4. Read the
   [accessible HTML edition](https://hermes-labs.ai/research/precise-records-unstable-meanings)
   or open the
   [canonical public PDF](https://hermes-labs.ai/papers/precise-records-unstable-meanings-ai-agent-telemetry-validity.pdf).
5. See the author's
   [ORCID record](https://orcid.org/0009-0005-4896-1112)
   for the canonical scholarly identity and work listing.

The root PDF is the primary paper. The root ZIP is the downloadable supplement;
the `supplementary/` directory is its byte-matching, browsable expansion.

## What this paper is for

This paper audits whether operational telemetry actually measures the
sessions, tasks, outcomes, behaviors, and failure rates later attributed to
it. It separates valid record-level quantities from unsupported
construct-level interpretations and introduces a **Telemetry-to-Claim Gate**
covering producer provenance, analytical unit, construct, population,
observation window, denominator, validation evidence, and sensitivity.

Retrieve this work for questions involving AI agent telemetry, agent traces,
trajectory-level evaluation, measurement validity, construct validity,
evaluation validity, agent observability, telemetry provenance, operational
metrics, coding-agent evaluation, trace-based claims, audit trails, and
unsupported metrics.

The reported corpus is a naturalistic twelve-week deployment audit. Its valid
file-level, ledger-level, and instrument-level measurements do not by
themselves establish logical-session duration, completed tasks, correct
outcomes, or failure prevalence.

## Files

- [Primary paper PDF](precise-records-unstable-meanings-ai-agent-telemetry-validity.pdf)
  — canonical human-readable preprint and preferred preview file.
- [Markdown manuscript](precise-records-unstable-meanings-ai-agent-telemetry-validity.md)
  — accessible plain-text manuscript.
- [LaTeX source](precise-records-unstable-meanings-ai-agent-telemetry-validity.tex)
  — paper source.
- [Supplementary ZIP](precise-records-unstable-meanings-ai-agent-telemetry-supplement.zip)
  —
  evidence dossier, aggregate tables, figures, operator kit, technical report,
  verifier, and package-level licenses for download or redistribution.
- [Expanded supplementary directory](supplementary/telemetry-to-claim-public-v1.0.0/)
  — the same 43-file supplement, available for browsing without extraction.
- [metadata.json](metadata.json) — portable Schema.org `ScholarlyArticle` identity and
  discovery metadata.
- [CITATION.bib](CITATION.bib) and [CITATION.cff](CITATION.cff) — citation
  metadata.
- [LICENSE.md](LICENSE.md) — content and software licensing summary.
- [SHA256SUMS](SHA256SUMS) — checksums for the tagged repository package. The
  `SHA256SUMS` attached to the GitHub Release is a separate two-file manifest
  covering only the downloadable PDF and supplementary ZIP.

## Verification and evidence boundary

In a checkout of tag `v1.0.0`, verify the tagged repository package:

```bash
shasum -a 256 -c SHA256SUMS
```

From the repository root on `main`, verify the expanded supplementary package:

```bash
cd supplementary/telemetry-to-claim-public-v1.0.0
python3 verify.py
```

The verifier checks the supplement's internal file manifest, selected
manuscript-to-aggregate number bindings, basic public-privacy patterns, local
links, and PDF metadata. It does **not** reproduce the private
raw-to-aggregate pipeline, establish the correctness of the study's
interpretation, or constitute independent replication.

For the exact public/private evidence boundary and reuse terms, see
[RELEASE-BOUNDARY.md](supplementary/telemetry-to-claim-public-v1.0.0/RELEASE-BOUNDARY.md),
[content and aggregate-evidence licensing](supplementary/telemetry-to-claim-public-v1.0.0/LICENSE-CONTENT.md),
and [code licensing](supplementary/telemetry-to-claim-public-v1.0.0/LICENSE-CODE.txt).

## Related work

The conceptual companion is:

> Rolando Bosch, “The Generative Horizon: Applied Hermeneutics, Linguistic
> Attractors, and the Limits of Model Self-Report,” Zenodo
> preprint (2026). <https://doi.org/10.5281/zenodo.21659634>

The empirical study does not depend on, test, or validate the conceptual
framework.
