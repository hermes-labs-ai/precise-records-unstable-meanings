# Telemetry-to-Claim Gate v1

## Purpose

Use this proposed framework before an agent-telemetry metric is interpreted as
evidence for a dashboard headline, research claim, autonomy decision, safety
statement, or public assertion.

The object entering the gate is a **candidate claim tuple**, not a number:

`C = (M, U, K, P, W, D, I)`

| Field | Question |
|---|---|
| `M` — metric | What was counted or calculated? |
| `U` — analytical unit | What does one row or observation represent? |
| `K` — construct | What property is the metric intended to represent? |
| `P` — population | Which agents, files, episodes, turns, or events are covered? |
| `W` — time window | When could the instrument observe the population? |
| `D` — denominator | What eligible population makes the rate or comparison meaningful? |
| `I` — interpretation | What sentence or decision is proposed? |

## Gate questions

### 1. Producer and provenance

- Which systems, hooks, agents, humans, migrations, or replays can write this source?
- Can mixed producers be separated?
- Is the source-of-record relationship documented?

### 2. Schema epochs

- Did field names, meanings, defaults, or producers change?
- Are records classified under the schema that produced them?
- Can an absent field mean “false,” or does it mean “not instrumented”?

### 3. Coverage and missingness

- When did the instrument begin?
- Are outages distinguishable from zero events?
- Is the observed population the population named in the claim?

**Coverage precedes inference.**

### 4. Contamination and duplication

- Are machine-reflex, retry, replay, poller, backfill, or test records mixed with the target population?
- Are duplicate rules exact and reproducible?
- Does quarantine remove only records that fail the declared construct?

### 5. Unit-to-construct alignment

- Is a file a session, task, episode, process, or merely a storage object?
- Is a receipt a verified outcome or only an assertion?
- Is elapsed time activity, waiting, or unknown?

### 6. Denominator integrity

- Does the denominator cover the same population, window, and unit as the numerator?
- Do window boundaries split or misattribute activity?
- Would a different reasonable denominator change the interpretation?

### 7. Detector and classifier validity

- Does a flag measure the target failure or the detector's threshold?
- Was the classifier tested against representative examples?
- Are unknown and unclassified cases preserved?

### 8. Sensitivity

- Does the conclusion survive one plausible alternative threshold, gap rule, or inclusion rule?
- Were exploratory thresholds labeled after inspection?
- Which part of the conclusion is stable and which is rule-dependent?

### 9. Outcome evidence

- Does the telemetry contain a validated outcome construct?
- If not, are task success, productivity, reliability, and usefulness explicitly withheld?

## Layer 1 — Data-treatment actions

Multiple actions can apply, in order:

- **INCLUDE**
- **PARTITION**
- **DEDUPLICATE**
- **QUARANTINE / EXCLUDE**
- **RECOMPUTE**

These actions change the analytical data. They do not determine what the result means.

## Layer 2 — Terminal claim disposition

The operator records exactly one terminal disposition for every candidate claim:

- **RETAIN** — the proposed claim is documented as supported under the declared assumptions and evidence.
- **NARROW** — a smaller population, window, unit, or scope is documented as supported.
- **RELABEL** — the calculation survives but measures a different construct.
- **WITHHOLD** — evidence is insufficient or materially compromised.
- **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY** — the required construct or distinction is absent from the instrument.

## Minimum claim record

For every disposition, preserve:

1. the original candidate claim tuple;
2. evidence sources and snapshot identity;
3. data-treatment actions;
4. the terminal disposition;
5. the final wording allowed;
6. uncertainties and sensitivity result; and
7. the observation that would change the disposition.

The framework structures and records the evidentiary basis on which an operator
decides whether and how to move from trace to interpretation to claim. It does
not make that decision, determine the action that should follow, or certify that
an underlying system is safe, reliable, productive, or successful. Operational
action additionally depends on costs, values, reversibility, uncertainty
tolerance, and intended use.
