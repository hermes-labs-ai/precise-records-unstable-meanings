# Material public claims ledger

Snapshot: `OTH-PUB2-20260723-dd281e3`

## Candidate-claim provenance

The audit did not treat every candidate interpretation as a claim previously
used in operation. Candidate claims came from three documented sources: the
author-directed research brief and frozen protocol, names and fields in the
telemetry that invited an interpretation, and interpretations proposed by
research agents while testing what the records could support.

| Candidate interpretation | Verified provenance | Prior operational use established? |
|---|---|---|
| Transcript-file event span represented session or task duration | The frozen protocol defined “observed session duration” from transcript first-to-last timestamps while already warning that the measure was idle-inflated. The audit later narrowed the analytical unit from session to transcript file. | No. The initial research construct and storage convention made it a candidate for testing; the trace does not establish a validated operational session-duration metric. |
| Files above eight hours represented sustained sessions | The eight-hour tier and “sustained session” reading were introduced by research agents after inspecting the distribution. The threshold was explicitly post hoc and exploratory. | No. |
| All 28,055 claims-ledger rows represented agent claims or completed work | The source was named `hal-claims-log`, its rows usually contained `claim` and `verification`, and a status surface displayed its raw entry count. The frozen protocol proposed claims-log entries with proof paths only as a completion proxy. An early agent-authored draft then misdescribed the residual rows as genuine agent claims. | No evidence that the full count was used as a completed-work measure. It was a plausible audit candidate, not an established prior operational claim. |
| The 117 residual entries represented completed tasks | This interpretation was formulated during the audit to test whether removing retrieval-reflex events validated a stronger completion construct. Earlier agent-authored prose called the residual “receipt discipline,” a characterization corrected by this forensic pass. | No. |
| Detector-positive rate represented behavioral anomaly or failure prevalence | The stream name included `anomaly`, each row carried a `flagged` field, and the initial protocol named stylometric anomalies as an operational signal. An early agent-authored draft went further and called the detector mis-thresholded. | No validated prevalence use was established. |
| Short-lived streams supported fleet-historical rates | The initial study question covered twelve weeks while some instruments began only near the snapshot date. The audit posed fleet-wide rates as a denominator and observation-window test. | No. |

This provenance means the paper reports candidate interpretations challenged by
the audit, not six documented policies that had already governed the
deployment.

## Forensic semantics of the claims ledger

The claims ledger was an append-only operational sink, not a table with one
event type or one producer.

1. The 27,938 rows carrying `claim_class=retrieved` were appended when a
   UserPromptSubmit entity-retrieval hook matched up to three configured entity
   names, queried the local Fidelis memory service, injected returned context,
   and recorded that the retrieval reflex had fired.
2. In those rows, `retrieved` named the instrumentation event. It did not mean
   that an agent authored a claim, that a task completed, or that the retrieved
   material was relevant or correct.
3. The other 117 rows carried heterogeneous class and status values such as
   `wired`, `verified`, `deployed`, `agent-handoff`, `artifact`, and unclassed
   legacy shapes. They were not one native producer class.
4. Ninety-eight of the 117 residual rows had a non-empty `verification` value.
   That proof-bearing shape and the ledger's operational role explain the
   earlier shorthand “receipts.” The shorthand does not establish a uniform
   receipt schema, a task outcome, or producer identity, so the public package
   now calls them residual ledger entries.
5. The frozen extraction retained timestamp, a hashed session field when
   present, `claim_class`, claim length, and whether verification was present.
   The source schema contained no required task identifier, completion field,
   success field, correctness field, or explicit producer field. A session
   identifier did not identify the writer.
6. The 27,938 retrieval rows were well-formed records of their actual
   instrumentation event. They were quarantined only from the agent-claim and
   completion constructs. The 117 residual rows were usable for their observed
   cadence and field-presence properties, not as verified outcomes.

Primary local evidence for this interpretation was the frozen 28,055-row
working extraction; the originating entity-retrieval implementation preserved
in the memory-reflex evaluation workspace; the deterministic audit and
extractor; and the frozen protocol and Git history. Raw content remains private.

## C01 — Raw claims-ledger interpretation

- **Candidate claim:** The harness deployment produced 28,055 agent-authored claims or completed-work records.
- **Treatment:** `PARTITION` on native `claim_class=retrieved`; exclude 27,938 retrieval-reflex events from the agent-claim and completion constructs; separate bound and unbound residual rows; `RECOMPUTE`.
- **Disposition:** **WITHHOLD**
- **Allowed wording:** The claims ledger contained 28,055 rows from a heterogeneous operational sink. Of those, 27,938 recorded automatic retrieval-reflex events.
- **Evidence:** `aggregate/audit_report.md` coverage row; `aggregate/inventory.json`.

## C02 — Residual entries not marked retrieved

- **Candidate claim:** After the native-field partition, 117 ledger entries did not carry `claim_class=retrieved`.
- **Treatment:** `INCLUDE` 101 trusted and 16 usable-with-caveats rows.
- **Disposition:** **RETAIN**
- **Allowed wording:** The final snapshot contains 117 heterogeneous residual ledger entries across nine days that were not marked `claim_class=retrieved`; 98 carried a non-empty verification value.
- **Evidence:** `aggregate/audit_report.md`; `aggregate/summary_tables.md` §6; `aggregate/claims_agg.csv`.

## C03 — Meaning of the surviving claims rows

- **Candidate claim:** The 117 entries represent completed tasks or task success.
- **Treatment:** Examine available fields and outcome linkage.
- **Disposition:** **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY**
- **Allowed wording:** The entries establish residual-entry cadence and limited field presence, not producer identity, completed tasks, success, or correctness.
- **Evidence:** `aggregate/provenance.csv`; `aggregate/summary_tables.md` §6.

## C04 — Short-file distribution

- **Candidate claim:** 97.7% of trusted transcript files have eligible-event spans below five minutes.
- **Treatment:** `INCLUDE` trusted transcript files; classify by exploratory wall-duration tier.
- **Disposition:** **RETAIN**
- **Allowed wording:** 35,652 of 36,502 trusted transcript files—97.7%—have eligible-event spans below five minutes.
- **Evidence:** `aggregate/tiers.csv`; `aggregate/summary_tables.md` §7.

## C05 — Meaning of a transcript file

- **Candidate claim:** The short-file distribution is the distribution of agent tasks or human-agent sessions.
- **Treatment:** Examine analytical-unit identity and resume/bridge linkage.
- **Disposition:** **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY**
- **Allowed wording:** The distribution describes transcript files; task and multi-file session linkage are unvalidated.
- **Evidence:** `aggregate/provenance.csv`; `aggregate/summary_tables.md` instrument caveats.

## C06 — Extended-duration tail

- **Candidate claim:** The harness deployment contained 87 sustained sessions over eight hours.
- **Treatment:** `PARTITION` gap-dominant files; subtract the largest silent gap as a sensitivity check; `RECOMPUTE`.
- **Disposition:** **NARROW**
- **Allowed wording:** Eighty-seven trusted files crossed the exploratory eight-hour event-span threshold; 59 were gap-dominant, while largest-gap subtraction caused 46 to fall below the threshold and left 41 above it.
- **Evidence:** `aggregate/tiers.csv`; `aggregate/summary_tables.md` §7.

## C07 — Anomaly prevalence

- **Candidate claim:** Sixty-five percent of agent behavior was anomalous or defective.
- **Treatment:** `DEDUPLICATE` one exact unflagged row; retain remaining detector outputs; inspect positive prevalence and validation boundary.
- **Disposition:** **RELABEL**
- **Allowed wording:** The detector flagged 20,860 of 31,904 scored turns; independent validation and, if warranted, calibration are required before behavioral-prevalence use.
- **Evidence:** `aggregate/rates.csv`; `aggregate/summary_tables.md` §4.

## C08 — Hermeneutic gate output

- **Candidate claim:** One third of drafts across the twelve-week deployment overclaimed.
- **Treatment:** `NARROW` to the instrument's July 22–23 window; drop invalid per-active-hour denominator.
- **Disposition:** **NARROW**
- **Allowed wording:** The pre-existing Hermeneutic gate recorded 128 `RISK` instrument verdicts among 394 events across July 22-23; these are not verified overclaim labels.
- **Evidence:** `aggregate/rates.csv`; `aggregate/summary_tables.md` §4.

## C09 — Stop-too-soon output

- **Candidate claim:** Thirteen tasks failed because agents stopped too soon.
- **Treatment:** Retain windowed flags; examine detector taxonomy and absence of task linkage.
- **Disposition:** **RELABEL**
- **Allowed wording:** The detector emitted 13 flags on July 22; the available telemetry does not bind those flags to completed tasks or validated failures.
- **Evidence:** `aggregate/rates.csv`; `aggregate/summary_tables.md` §4.
