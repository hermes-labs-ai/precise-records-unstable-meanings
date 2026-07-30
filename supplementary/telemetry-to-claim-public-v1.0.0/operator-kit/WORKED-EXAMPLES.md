# Worked examples

## 1. Mixed producers in a claims ledger

### Candidate claim

> The deployment produced 28,055 agent-authored claims or completed-work records.

| Tuple field | Value |
|---|---|
| Metric | Claims-ledger row count |
| Analytical unit | One ledger row |
| Construct | Agent-authored claim or completed-work record |
| Population | All ledger rows in the frozen snapshot |
| Window | Twelve-week deployment window |
| Denominator | Not applicable to the count |
| Proposed interpretation | Volume of agent-authored claims or completed work |

### Audit

- The source was a heterogeneous operational sink rather than one event table.
- Originating code shows that 27,938 of 28,055 rows with `claim_class=retrieved` recorded an automatic UserPromptSubmit entity-retrieval event.
- The other 117 entries carried heterogeneous classes and legacy shapes; 98 had a non-empty verification value.
- Neither the native partition nor verification-field presence established residual producer identity or task-outcome linkage.

### Data treatment

`PARTITION` on the native instrumentation class → exclude retrieval events from agent-claim and completion constructs → separate bound and unbound residuals → `RECOMPUTE`.

### Claim dispositions

- 28,055 agent-authored claims: **WITHHOLD**
- 117 heterogeneous residual entries not marked `claim_class=retrieved`: **RETAIN**
- Completed tasks or task success: **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY**
- Producer identity, correctness, and one semantic class for the 117 entries: **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY**

### Allowed wording

> The final snapshot contains 27,938 automatic retrieval-reflex events marked `claim_class=retrieved` and 117 heterogeneous residual ledger entries not carrying that value; 98 residual entries had a non-empty verification value.

## 2. Transcript-file duration and session persistence

### Candidate claim

> The deployment contained 87 sustained sessions lasting more than eight hours.

### Audit

- The observed unit was a transcript file, not a validated logical session.
- Cross-file resume and bridge linkage were unvalidated.
- The eight-hour tier was exploratory.
- Of 87 files crossing the event-span threshold, 59 had one silent gap exceeding half of their event span.
- Largest-gap subtraction caused 46 files to fall below eight hours and left 41 above the threshold; the predicates overlap rather than forming complementary groups.

### Data treatment

`PARTITION` gap-dominant files → remove largest gap as a sensitivity condition → `RECOMPUTE`.

### Claim disposition

**NARROW**

### Allowed wording

> Eighty-seven trusted transcript files crossed the exploratory eight-hour wall-duration threshold; 59 were gap-dominant, and 41 remained above eight hours after their largest gap was removed.

The data do not identify continuous work, task duration, or logical-session duration.

## 3. Detector output and behavioral prevalence

### Candidate claim

> Sixty-five percent of coding-agent behavior was anomalous or defective.

### Audit

- After one exact, unflagged duplicate was quarantined, the anomaly instrument flagged 20,860 of 31,904 scored turns.
- No independent labels established that the detector flag represented the proposed behavioral construct.
- A detector marking most observations may be revealing its operating threshold before it reveals behavioral prevalence.

### Data treatment

`DEDUPLICATE` the exact repeated row → `INCLUDE` the remaining detector outputs; preserve the exact scored population and window.

### Claim disposition

**RELABEL**

### Allowed wording

> The anomaly detector flagged 20,860 of 31,904 scored turns; the output requires independent validation and, if warranted, calibration before behavioral-prevalence use.

## 4. Synthetic transfer example

An operator has 10,000 “task event” rows written by a task runner and a health poller. A schema marker separates the producers, but no validated completion event exists.

- Partition the producers.
- Quarantine health-poller rows from the task-event construct.
- Recompute runner-emitted rows.
- Relabel the surviving metric as runner-emitted task events.
- Mark completed tasks as **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY**.

This is the minimum transfer test: the method changes the statement even when the arithmetic is straightforward.
