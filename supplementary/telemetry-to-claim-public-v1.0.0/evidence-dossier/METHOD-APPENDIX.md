# Method appendix: classification and sensitivity

This appendix specifies the rules that produced snapshot
`OTH-PUB2-20260723-dd281e3`. It distinguishes directly recorded fields from
interpretive mappings and does not claim a labeled validation set.

## Record-class semantics

| Class | Operational meaning in this study |
|---|---|
| **TRUSTED** | The record satisfied the deterministic rule for the stated analysis and contained the required timestamp, identity, and categorical or numeric fields. |
| **USABLE_WITH_CAVEATS** | The record remained usable for a narrower analysis, but a declared provenance, identity, backfill, or schema condition prevented entry into the primary stratum. |
| **QUARANTINED** | The record was an exact duplicate, lacked a valid activity observation, carried an excluded producer marker, matched declared test traffic, or failed a source-specific schema or plausibility rule. |
| **MISSING** | This is a coverage state rather than a stored-row class: a day inside a stream's observed span had no records. Missing days were reported and never imputed as zero events. |

Classification was deterministic. No record received a class through model
judgment or manual row-by-row adjudication.

These are study-specific admissibility classes, not judgments that a stored
row was globally valid or invalid. A row could be a well-formed record of its
actual instrumentation event and still be quarantined from an analysis whose
intended construct it did not measure.

## Source-specific rules

| Source | Directly recorded evidence | Deterministic treatment | Interpretive boundary |
|---|---|---|---|
| Transcript files | event type, timestamp, project-directory class, sidechain marker | Require at least one timestamped activity event; exclude bookkeeping event types from both wall and active duration; classify a file as UWC under `R-DASH-PROVENANCE`, `R-SIDECHAIN`, or partial timestamp-parse failure; quarantine a file with no valid activity observation | These rules preserve declared provenance and parsing caveats, but do not identify a logical session or task |
| Turn metrics | full serialized row | Quarantine an exact duplicate line; otherwise require declared numeric and identity fields | Deduplication establishes row uniqueness, not behavioral validity |
| Anomaly turns | full serialized row, detector flag | Quarantine an exact duplicate line; retain the detector flag for the remaining scored-turn population | A flag is an instrument output, not an independently labeled behavioral failure |
| Claims ledger | native `claim_class`, session-identity fields, verification-field presence | Exclude `claim_class=retrieved` rows from agent-claim and completion constructs; classify residual rows with a session identity as trusted and unbound rows as UWC | Originating code establishes that `retrieved` records a UserPromptSubmit entity-retrieval reflex. It does not label agent authorship, relevance, correctness, completion, or success. The residual rows are heterogeneous and lack an explicit producer or task-outcome field |
| Drift summaries | filename backfill marker, declared numeric fields | Classify backfills as UWC; quarantine malformed or implausible summaries | Backfills cannot be pooled with contemporaneous runs |
| Hermeneutic gate | timestamp, session identity, verdict | Retain records with the declared fields and window them to the instrument's observed dates | Verdicts from the pre-existing same-lab software are instrument outputs, not verified overclaim labels; the study did not evaluate Hermeneutic |
| Stop flags | timestamp; no session identity | Classify every observed flag as UWC and report a fleet-level count only | Flags cannot be joined to tasks or validated failures |

The inventory identified multiple field-key signatures in the claims source.
Those signatures were recorded as schema evidence, but they were not used as a
manual or learned producer classifier. In the frozen working rows, all 27,938
rows excluded from the agent-claim and completion constructs retained the
native `claim_class=retrieved` value. The originating implementation appended
that value when an entity-retrieval hook queried the local memory service and
injected returned context. The legacy text-prefix fallback was therefore not
required to reproduce the frozen count.

The 117 residual entries carried heterogeneous `claim_class` or legacy values;
98 had a non-empty verification field, 101 had a session identity and 16 did
not. The schema contained no required task identifier, completion, success,
correctness, or explicit producer field. The residual partition therefore
supports cadence and field-presence statements only.

## What the 400-file seeded check established

The transcript audit selected 400 files with pseudorandom seed `20260723`
before full extraction. The rule pass classified 347 as trusted and 53 as UWC;
all 53 UWC files carried dash-project provenance. It also counted activity,
bookkeeping, malformed, and sidechain events to test that the parser and rule
taxonomy encountered the expected storage forms.

The check was not a hand-labeled validation sample:

- there was no independent ground-truth class for each file;
- there were no multiple analysts and no disagreement statistic;
- there was no estimated classification error rate; and
- it cannot support precision, recall, confidence intervals, or a claim that
  the rules recovered logical sessions or tasks.

Its evidentiary role was rule development and deterministic execution checking.
The declared rules were then applied across the full extraction.

## Plausible sensitivity conditions

### Inter-event gap cap and transcript stratum

| Stratum | Cap | Files | p25 | Median | p75 | p90 | Mean | Summed gap-capped measure |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TRUSTED | 5 min | 36,502 | 0.0 min | 0.0 min | 1.0 min | 1.0 min | 1.3 min | 777.6 h |
| TRUSTED | 15 min | 36,502 | 0.0 min | 0.0 min | 1.0 min | 1.0 min | 1.6 min | 1,001.1 h |
| TRUSTED | 30 min | 36,502 | 0.0 min | 0.0 min | 1.0 min | 1.0 min | 1.9 min | 1,166.0 h |
| TRUSTED + UWC | 15 min | 41,494 | 0.0 min | 0.0 min | 1.0 min | 1.0 min | 1.5 min | 1,035.2 h |

The central quantiles were unchanged across the three caps, while the summed
gap-capped inter-event measure varied materially. The primary paper therefore
treats central file event-span structure as stable and the summed measure as
definition sensitive, not as work or engagement time.

### Exact anomaly duplicate

The audit found one exact duplicate among 31,905 raw anomaly rows. It was
unflagged. Quarantining it changes the scored denominator from 31,905 to 31,904
and leaves the flagged numerator at 20,860. This correction is incorporated in
the paper and snapshot.

### Why no arbitrary classification-error simulation appears

A 1%, 5%, or 10% random label-flip analysis would not correspond to an observed
failure mechanism. The dominant claims-ledger partition used a native marker,
not an uncertain learned classifier, and the study has no labeled error
distribution from which to sample. The defensible uncertainty statement is
therefore semantic: if the instrumentation's `retrieved` marker does not denote
the reflex producer it was designed to mark, the producer interpretation would
require re-adjudication. The current evidence cannot assign that possibility a
frequency.

## Kaplan–Meier output

The predeclared Kaplan–Meier calculation is retained in
`aggregate/survival.csv` and the accompanying figure. Only one of 36,502 trusted
files was right-censored, and the estimated median activity duration was zero
minutes at the available resolution. The calculation therefore adds
negligible information beyond the empirical distribution and is not a
headline result.

## Reproducibility boundary

The public package now provides exact rule signatures, source-field roles,
class counts, aggregate sensitivity outputs, claim dispositions, and package
hashes. These additions make the analytical procedure more inspectable without
exposing content or stable identifiers.

A record-level hash manifest is not included. It could increase linkage and
re-identification risk, and hashes would establish neither source completeness
nor correct classification. Independent source-level validation requires a
privacy-preserving third-party audit or replication on another deployment.
