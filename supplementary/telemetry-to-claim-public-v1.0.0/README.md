# Precise Records, Unstable Meanings: Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry

This package reports a naturalistic study of one twelve-week coding-agent orchestration-harness deployment containing 41,495 transcript files and six included auxiliary telemetry streams.

DOI: [10.5281/zenodo.21652317](https://doi.org/10.5281/zenodo.21652317)

The harness persisted across the observation window. Persistence is not assumed for any individual agent, process, logical session, task, or transcript file.

The study does **not** measure productivity, useful work, task success, orchestration reliability, industry prevalence, or cross-fleet effectiveness. It asks a narrower question:

> Which operational claims survive a fail-closed audit of provenance, coverage, denominator, analytical unit, and construct validity?

## Four-part publication

1. **Primary research paper:** [Precise Records, Unstable Meanings: Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry](paper/PAPER.md)
2. **Companion technical report:** [From 41,495 coding-agent transcript files to defensible claims](technical-report/TECHNICAL-REPORT.md)
3. **Operator kit:** [Apply the Telemetry-to-Claim Gate](operator-kit/README.md)
4. **Evidence dossier:** [Inspect the frozen aggregate evidence](evidence-dossier/README.md)

The related conceptual preprint [The Generative Horizon: Applied Hermeneutics,
Linguistic Attractors, and the Limits of Model
Self-Report](https://doi.org/10.5281/zenodo.21659634) develops a broader account
of how interpretations can acquire operational authority. The empirical study
does not test or validate that framework. The conceptual paper is archived
separately and is not included in this package.

## Fast paths

- **Read the formatted paper:** [paper/PAPER.pdf](paper/PAPER.pdf)
- **Inspect the paper source:** [paper/PAPER.md](paper/PAPER.md)
- **Read the related conceptual paper:** [doi:10.5281/zenodo.21659634](https://doi.org/10.5281/zenodo.21659634)
- **One operational transformation:** [technical-report/TECHNICAL-REPORT.md](technical-report/TECHNICAL-REPORT.md)
- **Test your own metric:** [operator-kit/CLAIM-WORKSHEET.md](operator-kit/CLAIM-WORKSHEET.md)
- **Check public numbers and methods:** [evidence-dossier/CLAIMS-LEDGER.md](evidence-dossier/CLAIMS-LEDGER.md) and [evidence-dossier/METHOD-APPENDIX.md](evidence-dossier/METHOD-APPENDIX.md)

## A representative result

A heterogeneous operational log contained 28,055 rows. Originating instrumentation shows that 27,938 entries marked `claim_class=retrieved` recorded automatic entity-retrieval events. The other 117 entries carried heterogeneous classes and legacy shapes; 98 had non-empty verification values. Neither partition established completed tasks, task success, result correctness, or producer identity for every residual row.

The research paper derives the claim-level framework from this and the duration, detector, linkage, and coverage findings. The operator kit presents that framework as the **Telemetry-to-Claim Gate**.

## Accountability and boundary

- [Authorship and system contribution](CONTRIBUTIONS.md)
- [Public/private release boundary](RELEASE-BOUNDARY.md)
- [Aggregate reproducibility limits](evidence-dossier/REPRODUCIBILITY.md)
- [Citation metadata](CITATION.cff)
- [Content and data license](LICENSE-CONTENT.md)
- [Code license](LICENSE-CODE.txt)

Run:

```bash
python3 verify.py
```

The verifier establishes internal package consistency and selected number bindings. It is not independent replication of the private raw-to-aggregate pipeline.
