# Measurement audit (M1.5) — aggregate report
Run date: 2026-07-23 · rules frozen before full extraction · transcripts audited via seeded sample n=400 (seed 20260723); deterministic rules re-applied during full extraction before aggregation. Source logs were live during development, so later runs would differ; this public package binds to the frozen aggregate snapshot.

## Rule signatures (falsifiable)
- **R-DUP**: exact duplicate: identical full-line sha1 seen earlier in same source
- **R-TS-PARSE**: timestamp field absent or fails ISO regex -> QUARANTINED (malformed)
- **R-TS-RANGE**: ts before 2026-04-01 or later than the minute-rounded extraction snapshot -> QUARANTINED (implausible)
- **R-SCHEMA**: row missing required fields for its source -> USABLE_WITH_CAVEATS if analyzable, else QUARANTINED
- **R-REFLEX**: claims_log row with claim_class=retrieved (native machine-reflex marker; dominant epoch) or claim text beginning with [retrieved], [reflex], or [auto] -> QUARANTINED for claim-cadence construct; counted separately
- **R-BACKFILL**: drift_log filename contains BACKFILL -> USABLE_WITH_CAVEATS (retrospective, not contemporaneous)
- **R-TEST**: identifier/machine-field matches (selftest|smoke-test|dummy) -> QUARANTINED (test traffic)
- **R-DASH-PROVENANCE**: transcript project directory is '-' -> USABLE_WITH_CAVEATS (ambiguous print-mode or spawned-work provenance; not a test exclusion)
- **R-IMPLAUSIBLE**: numeric outside bounds (chars<=0, words<0, total_turns<0, wall_time_s<0 or >3600, max_z<0) -> QUARANTINED
- **R-SIDECHAIN**: transcript event isSidechain=true -> file is USABLE_WITH_CAVEATS for primary activity analysis and retained for a separate marker-positive stratum
- **R-BOOKKEEPING**: transcript harness event types (attachment, file-history-*, queue-operation, mode, ...) -> counted for provenance audit but excluded from both wall-time and active-time calculations
- **R-GAP**: calendar day inside [onset, snapshot] with zero rows while neighbors have rows -> MISSING evidence recorded (silence is never treated as absence of events)
- **R-UNBOUND-SESSION**: row lacking any session identity -> USABLE_WITH_CAVEATS (usable for fleet-level rates, unusable for per-session joins)

## Classification counts per source

| source | TRUSTED | USABLE_WITH_CAVEATS | QUARANTINED | total | top rules fired |
|---|---|---|---|---|---|
| turn_metrics | 30336 | 0 | 320 | 30656 | R-DUP:320 |
| turn_anomaly | 31904 | 0 | 1 | 31905 | R-DUP:1 |
| claims_log | 101 | 16 | 27938 | 28055 | R-REFLEX:27938, R-UNBOUND-SESSION:16, R-SCHEMA:2 |
| hermeneutic_gate | 394 | 0 | 0 | 394 | - |
| chain_broken | 0 | 13 | 0 | 13 | R-UNBOUND-SESSION:13 |
| drift_log | 22478 | 741 | 1 | 23220 | R-BACKFILL:741, R-IMPLAUSIBLE:1 |
| transcripts_sample | 347 | 53 | 0 | 400 | R-BOOKKEEPING:400, R-DASH-PROVENANCE:53 |

## Coverage & gaps (MISSING evidence: R-GAP)

| source | first day | last day | days w/ data | gap days in span |
|---|---|---|---|---|
| turn_metrics | 2026-06-19 | 2026-07-23 | 30 | 5 |
| turn_anomaly | 2026-07-02 | 2026-07-23 | 21 | 1 |
| claims_log | 2026-04-28 | 2026-07-23 | 65 | 22 |
| hermeneutic_gate | 2026-07-22 | 2026-07-23 | 2 | 0 |
| chain_broken | 2026-07-22 | 2026-07-22 | 1 | 0 |
| drift_log | 2026-04-28 | 2026-07-23 | 33 | 54 |
| transcripts_sample (sample-derived, n=400 files; full-population onset differs) | 2026-04-30 | 2026-07-23 | 40 | 45 |

## Transcript sample detail (file-level)

- population 41495 files; sampled 400
- activity_events: 1879
- bookkeeping_events: 5217
- malformed_lines: 0
- sidechain_events: 0

Interpretation caution: silence in any stream is evidence of NOTHING (Amendment A req.7); gap days are reported, never imputed.
