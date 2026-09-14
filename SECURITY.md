# Security Policy

This repository is an archival package for a published research paper —
"Precise Records, Unstable Meanings: Measurement Validity and
Unsupported Claims Derived from AI Agent Telemetry"
(<https://doi.org/10.5281/zenodo.21652317>). It ships no production
runtime software or network service, so there is no conventional
software attack surface to secure here.

The repository does include small offline convenience scripts (for
example `verify.py` inside the supplementary package) that check file
manifests, selected manuscript-to-aggregate number bindings, basic
public-privacy patterns, local links, and PDF metadata. They make no
network calls, are not a service, and are not designed to process
untrusted input; they exist only to let a reader confirm the archived
files have not been altered.

## Reporting a problem

If you find a problem with the archived materials — a corrupted or
tampered file, a checksum mismatch, an error in the citation or metadata
files, a public-privacy concern in the supplementary package, or a
concern about how this archive is represented — please report it by
opening a GitHub issue on this repository, or by email to
<roli@hermes-labs.ai>.

This is a solo-maintained research archive. Reports are read and
acknowledged in good faith, but no fixed response time or
service-level agreement is promised.

## Scope

This policy covers only the materials in this repository. It does not
cover the canonical Zenodo deposit, hermes-labs.ai, or any other Hermes
Labs repository.
