# Public/private release boundary

Only this `publication/public/` directory is proposed for release.

## Public

- Primary empirical research paper.
- Hermes-style PDF, Markdown source, LaTeX source, and deterministic render script.
- Companion technical report.
- Operator method documentation and worked examples.
- Evidence dossier with aggregate bindings.
- DOI pointer to the separately archived conceptual preprint, *The Generative
  Horizon*.
- Blank and synthetic claim worksheet.
- Aggregate-only tables and figures.
- Sanitized field-level provenance and exclusions.
- Frozen snapshot metadata, claim ledger, and verifier.
- Authorship and contribution disclosure.
- Citation metadata and explicit mixed-license notices.

## Transformed or sanitized

- Source paths replaced by neutral source IDs.
- Time spans reduced to day resolution.
- Session and turn identifiers omitted.
- Claims and message text reduced to counts or categorical classifications.
- Figures generated only from aggregate tables.

## Synthetic

- The illustrative worksheet example.
- Any future usage example not derived from a consenting external operator.

## Summarized

- The raw-to-derived lineage.
- Internal model criticism and its accepted corrections.
- Private instrumentation boundaries.

## Private

- Raw transcripts, prompts, messages, and telemetry content.
- Record-level working rows and audit detail.
- Salts, hashes usable for linkage, session identities, and exact timestamps.
- Home-directory paths, usernames, credentials, and configuration.
- Hook, control-plane, security, permission, and orchestration implementation not required to evaluate the method.
- Internal plans, receipts, task logs, reviewer dialogues, and unpublished products or codenames.
- Third-party content not licensed for redistribution.

## Publication rule

Do not publish the parent worktree. Build a release only from the allowlisted
contents of this directory, run `python3 verify.py`, perform the owner voice
pass, and pass the normal external publication gate. A Zenodo deposit may
contain the primary PDF plus a hash-bound archive of this allowlisted directory;
it must not contain any parent-worktree files.

The complete *The Generative Horizon* manuscript and PDF are excluded from this
record and released separately under doi:10.5281/zenodo.21659634.
