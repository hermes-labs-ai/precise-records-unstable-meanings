# Companion technical report: From 41,495 coding-agent transcript files to defensible claims

## Operational application of the Telemetry-to-Claim Gate

**Rolando Bosch · Hermes Labs**
*San Francisco, California, USA*
*Analysis, criticism, and drafting assistance were provided by AI systems operated within the Hermes Autonomous Lab.*

This is the operator-facing companion to the [primary research paper](../paper/PAPER.md). It leads with a worked transformation and explains how an operator can use the proposed framework.

A log in the observed orchestration-harness deployment contained 28,055 rows that looked, at first glance, like a record of agent claims. The originating instrumentation shows that 27,938 entries with `claim_class=retrieved` recorded automatic entity-retrieval events. The other 117 were heterogeneous residual ledger entries.

Even that smaller number did not mean what the attractive interpretation suggested. The 117 rows appeared on nine calendar days, with 62 on one day, and 98 carried a non-empty verification value. They did not form one producer class or establish 117 completed tasks, a completion rate, task success, or result correctness.

That change—from a large, apparently meaningful count to a much narrower statement—is the subject of this report.

The problem was not an absence of logs. The harness deployment was heavily instrumented. The problem was determining what the records could support once their producer, analytical unit, construct, population, time window, denominator, and proposed interpretation were made explicit.

Telemetry can serve a descriptive role and later enter routing, evaluation,
autonomy, memory, policy, or redesign. That transition raises a second test
beyond arithmetic correctness: whether the recorded value has earned the
meaning required by its use. This study does not measure downstream harm. It
shows the prior interpretive failure that could make such feedback misleading.
The anomaly stream is the clean case: the calculation described detector
outputs faithfully while failing to establish behavioral prevalence. The
claims ledger is the nested case: an instrumentation-class partition clarified
the record population, but the residual entries still did not establish
completed work.

## The deployment and its limits

We study twelve weeks of telemetry from one orchestration-harness deployment that launched, resumed, and coordinated coding-agent sessions. Harness-level operation continued across the observation window while the harness and its instrumentation evolved. The evidence does not establish uninterrupted use or uptime, and equivalent continuity was not assumed for individual model processes, operating-system processes, logical sessions, tasks, or transcript files. The frozen corpus contains:

- 41,495 transcript files;
- 30,656 per-turn text-shape metric rows;
- 31,904 anomaly-scored turns after one exact duplicate was quarantined;
- 28,055 claims-ledger rows;
- 23,220 drift summaries;
- 394 Hermeneutic-gate verdicts; and
- 13 stop-too-soon flags.

The transcript population was classified as 36,502 trusted files, 4,992 usable-with-caveats files, and one quarantined file. The public evidence is aggregate-only. The analysis did not read or export private message content, and the public package contains no session identifiers or timestamps finer than a day.

This is a technical report about one orchestration-harness deployment. It does not establish productivity, useful work, task success, orchestration reliability, industry prevalence, or cross-fleet effectiveness. The corpus has no validated task-outcome construct.

## The method: evaluate the claim, not just the metric

The Telemetry-to-Claim Gate begins with a candidate claim tuple:

`C = (M, U, K, P, W, D, I)`

where:

- `M` is the metric;
- `U` is the analytical unit;
- `K` is the construct the metric is supposed to represent;
- `P` is the population;
- `W` is the observation window;
- `D` is the denominator; and
- `I` is the proposed interpretation.

The tuple is checked against producer and provenance, schema epochs, coverage and missingness, contamination and duplication, unit-to-construct alignment, denominator integrity, detector validation, sensitivity, and outcome evidence.

Data may then be included, partitioned, deduplicated, quarantined or excluded, and recomputed. That treatment is separate from the terminal disposition of the claim:

- **RETAIN**
- **NARROW**
- **RELABEL**
- **WITHHOLD**
- **NOT IDENTIFIABLE FROM AVAILABLE TELEMETRY**

Coverage precedes inference. A clean calculation cannot rescue a claim whose population, construct, or denominator is undefined.

The proposed gate does not invent provenance analysis, construct validity, denominator discipline, missing-data analysis, or sensitivity testing. It structures and records the evidentiary basis on which an operator may decide whether and how to use a telemetry-based claim.

## What changed under the gate

### 1. Logged claims became an instrumentation-class partition

**Candidate interpretation:** 28,055 rows represented agent-authored claims or completed work.

**Treatment:** partition on the native `claim_class=retrieved` marker; exclude the 27,938 automatic retrieval-reflex events from agent-claim and completion constructs; retain 101 bound trusted and 16 unbound usable-with-caveats residual entries not carrying that value.

**Disposition:** withhold the 28,055-agent-claims statement; retain the literal count of 117 heterogeneous residual entries not marked `retrieved`, including 98 with non-empty verification; mark producer identity, task completion, success, and correctness as not identifiable.

The `retrieved` field identifies one instrumentation event, not the producer of every residual row. An explicit producer and task-outcome schema at write time would make those distinctions detectable; it would not by itself establish whether any outcome was correct.

### 2. Long “sessions” became a qualified file event-span tail

Among 36,502 trusted transcript files, 35,652—97.7%—have eligible-event spans below five minutes. Transcript-file event span is the wall-clock interval between the first and last eligible recorded events; it does not establish continuous execution, preserved state, engagement, work, task duration, or session persistence.

Across 5-, 15-, and 30-minute inter-event gap caps, the median and 90th percentile remained 0.0 and 1.0 minutes, while the summed gap-capped inter-event measure varied from 777.6 to 1,166.0 hours. The central file-population structure was stable; the summed measure was definition-sensitive.

As an illustrative post-hoc threshold, 87 files had eligible-event spans above eight hours and carried 556.3 summed hours under the fifteen-minute gap-capped measure. Of those files, 59 had one silent gap accounting for more than half of their event span. Subtracting each file's largest internal gap caused 46 to fall below eight hours, leaving 41 above the threshold; the two predicates overlap but are not complementary partitions.

**Disposition:** retain the file-level distribution; narrow the extended-tail statement to gap-audited transcript files; do not call a transcript file a task or treat its duration as continuous work. Multi-file session linkage is unvalidated, and time is not accomplishment.

The tier thresholds were defined after observing the distribution. They are exploratory strata, not preregistered performance categories.

### 3. A 65% anomaly rate became a detector finding

After one exact, unflagged duplicate was quarantined, the anomaly stream marked 20,860 of 31,904 scored turns, or approximately 65%, as anomalous.

That number does not establish that 65% of agent behavior was defective. A detector that marks most of its population provides evidence about its observed operating behavior before it provides evidence about failure prevalence.

**Disposition:** retain the detector output; require independent validation and, if warranted, calibration before prevalence use; withhold any fleet-anomaly or failure-prevalence interpretation. The positive rate alone does not demonstrate miscalibration.

### 4. Young guardrail streams remained windowed counts

The pre-existing [Hermeneutic v0.1.7](https://github.com/hermes-labs-ai/hermeneutic) epistemic gate recorded 128 `RISK` verdicts among 394 events across July 22-23. Hermeneutic is same-lab open-source software whose verdict stream was included as an instrument; it was not developed for or evaluated as a product by this study. Its verdicts are instrument outputs rather than verified overclaim labels, and the study did not assess its mining, retrieval, integrations, or downstream effectiveness. The stop-too-soon stream recorded 13 flags on July 22.

These streams began near the end of the twelve-week deployment. Silence before their start is not evidence that the observed events did not occur.

**Disposition:** retain the event counts and their exact windows; withhold fleet-historical rates, productivity interpretations, and failure rates. Per-active-hour rates were dropped because the available denominator assigned a file's activity to its start day and could undercount activity crossing the young streams' windows.

## How an operator can use the proposed framework

The operational contribution is not the specific native-field partition or event-span distribution. It is a proposed procedure for documenting the evidentiary basis of a statement before a dashboard, report, or decision gives it authority.

For one metric:

1. Write the full candidate claim tuple.
2. Identify every producer capable of writing the source.
3. Fingerprint schema epochs before classifying rows.
4. Establish stream birthdays, outages, missingness, and the population actually observed.
5. Test whether the analytical unit represents the construct.
6. Validate the denominator against the same population and window.
7. Separate data treatment from claim disposition.
8. Run at least one plausible sensitivity test.
9. End with one explicit disposition, including non-identifiability when warranted.

The accompanying worksheet makes that process copyable without adopting Hermes infrastructure.

## Why this matters beyond one deployment

Persistent agents can create records continuously. Those records can then be used to justify changes in authority, staffing, unattended runtime, safety posture, or expected performance.

This study does not show that such decisions are broadly being made incorrectly. It demonstrates, inside one naturalistic deployment, how apparently precise telemetry failed to support several attractive interpretations.

This suggests a useful operational layer between collecting traces and using them: a **claim-control layer**. Agent systems already govern actions and collect observations. Claim control structures and records the basis on which an operator decides what those observations may support.

The framework was derived from this case; the consistency of its application across analysts and deployments and its effects on decisions were not evaluated. The next evidence should come from independent applications, prospective instrumentation with explicit producer and episode identity, and intervention studies testing whether the framework changes consequential decisions.

## Accountability and reproducibility

The initial audit concept emerged during a Claude Code session and was selected, bounded, and developed into the present study by Rolando Bosch. Bosch determined the evidence boundary, adjudicated interpretations, controlled scope, made the final publication decisions, and retains responsibility for the work. The Hermes Autonomous Lab, operating through Claude Code and OpenAI Codex sessions, performed substantial inventory, analysis programming, aggregation, visualization, validation, criticism, and drafting under human-set constraints.

A fresh-context model attempted to falsify the cleaning rules and claims during development and found meaningful defects, including privacy leakage, gap-dominated duration tails, and invalid rate denominators. Those findings were corrected. This was an internal challenge mechanism, not independent peer review or scientific validation.

The public package permits inspection of the final aggregate snapshot, material claim bindings, and deterministic consistency checks. Because raw operational telemetry is private, an outsider cannot independently reproduce the raw-to-aggregate extraction. That limit is part of the result, not hidden behind the hashes.

**Competing interest.** Bosch leads Hermes Labs, which develops and maintains Hermeneutic. The study treats Hermeneutic verdicts as unvalidated instrument outputs and does not evaluate the product.

## What remains unproven

- Whether the Telemetry-to-Claim Gate changes decisions or prevents harm.
- Whether other orchestration deployments contain similar defects.
- Whether the method is efficient or effective across fleets.
- Whether any observed activity produced useful outcomes.
- Whether the orchestration deployment was reliable, productive, or economically valuable.
- Whether internal model criticism agrees with an independent expert review.

The strongest claim is narrower: in this deployment, claim-level scrutiny materially changed what its telemetry could honestly be said to show.
