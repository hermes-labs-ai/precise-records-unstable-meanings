# Candidate-claim worksheet

Copy this section for one operational statement.

## A. Proposed claim

**Proposed public or decision sentence:**

| Tuple field | Entry |
|---|---|
| Metric (`M`) | |
| Analytical unit (`U`) | |
| Construct (`K`) | |
| Population (`P`) | |
| Time window (`W`) | |
| Denominator (`D`) | |
| Proposed interpretation (`I`) | |

## B. Instrument boundary

- Producers capable of writing the source:
- Schema epochs:
- Instrument birthday:
- Known outages or missingness:
- Mixed traffic or backfills:
- Duplicate mechanism:
- Identity/linkage limitations:
- Outcome construct available:

## C. Tests

| Test | Evidence | Pass / fail / unknown |
|---|---|---|
| Producer separability | | |
| Schema compatibility | | |
| Coverage matches population/window | | |
| Contamination and duplicates handled | | |
| Unit represents construct | | |
| Denominator matches numerator | | |
| Detector/classifier validated | | |
| Sensitivity result | | |
| Outcome evidence supports interpretation | | |

## D. Data treatment

Check all that apply and explain:

- [ ] INCLUDE
- [ ] PARTITION
- [ ] DEDUPLICATE
- [ ] QUARANTINE / EXCLUDE
- [ ] RECOMPUTE

## E. Terminal claim disposition

Select exactly one:

- [ ] RETAIN
- [ ] NARROW
- [ ] RELABEL
- [ ] WITHHOLD
- [ ] NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY

**Allowed final wording:**

**What remains unknown:**

**What new evidence would change the disposition:**

## Short synthetic example

An operator has 10,000 “task event” rows. Two producers write the table: a task runner and a health poller. The table lacks a producer field, but the poller uses a distinguishable fixed schema.

- **Candidate interpretation:** 10,000 completed tasks.
- **Data treatment:** partition by schema; quarantine poller rows; recompute runner rows.
- **Count-claim disposition:** `RELABEL` the surviving count as runner-emitted task events.
- **Separate completion-claim disposition:** `NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY` until a validated completion record exists.
