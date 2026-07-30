# Reproducibility and its limits

## Publicly reproducible

An independent reader can:

- verify every allowlisted file against `MANIFEST.sha256`;
- recompute the ratios and totals cited in the paper from aggregate files;
- inspect the source-field interpretations and exclusions;
- inspect exact source-specific classification rules and sensitivity outputs;
- compare candidate claims with their data treatment and dispositions; and
- run `python3 verify.py` to detect package drift and selected numerical inconsistencies.

## Publicly inspectable but not independently reproducible

The package describes:

- classification rules and their aggregate effects;
- raw-to-derived source lineage at a sanitized field level;
- missingness, schema, and analytical-unit limitations; and
- the internal challenge process that changed the analysis.

An outsider can criticize these choices but cannot rerun them against the private source records.

## Not publicly reproducible

The raw-to-aggregate extraction cannot be independently reproduced from this package because the source corpus contains private operational transcripts and logs. The following remain private:

- raw transcript content and telemetry;
- working-row datasets and record-level audit details;
- salts and identifiers;
- local source paths and exact control-plane implementation;
- internal prompts, model dialogues, plans, and receipts; and
- credentials and security-sensitive infrastructure.

The public hashes establish that the released files are unchanged. They do not prove that the private source corpus was complete, that the classification rules were correct, or that the conclusions replicate elsewhere.

The 400-file seeded check exercised deterministic rules but was not independently
labeled and supplies no classification error or analyst-disagreement estimate.
The public method appendix states that limitation directly. A record-level hash
manifest is not released because it would add linkage risk without validating
source completeness or classification correctness.

## Developmental model criticism

A fresh-context model was instructed to falsify the cleaning rules, numerical claims, privacy boundary, and interpretation. It found meaningful defects that were corrected. This improved the work, but it was:

- internal rather than independent;
- conducted on the immediately preceding live snapshot;
- limited to the materials and instructions provided; and
- not peer review or scientific validation.

## Replication sequence

The next useful tests are:

1. independent application of the worksheet to another operator's claim;
2. cross-fleet replication using unrelated telemetry schemas;
3. prospective instrumentation with explicit producer, schema, episode, and outcome fields; and
4. an intervention study testing whether claim dispositions change decisions.
