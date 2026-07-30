# Summary tables (M4) — aggregate-only, shareable
Snapshot: 2026-07-23 · classes per declared audit rules · primary = TRUSTED; sensitivity = TRUSTED+USABLE_WITH_CAVEATS (UWC). Time decomposition: wall (W) >= active (A_G, gap-capped at G min); W-A is UNKNOWN time (idle OR unobserved OR harness-only), never imputed.

## 1. Coverage, classification, exclusions (read before any outcome)

| stream | TRUSTED | UWC | QUARANTINED | dominant quarantine cause |
|---|---|---|---|---|
| sessions (transcript files) | 36502 | 4992 | 1 | zero-activity file |
| turn-metrics | 30336 | 0 | 320 | exact-duplicate lines (hook double-fire) |
| turn-anomaly | 31904 | 0 | 1 | one exact-duplicate row |
| claims-ledger | 101 | 16 | 27938 | machine-reflex claim_class=retrieved (99.6% of source) |
| overclaim-gate | 394 | 0 | 0 | - |
| stop-flags | 0 | 13 | 0 | - |
| drift-summaries | 22478 | 741 | 0 | implausible fields |

Stream observation windows differ (left-truncation): turn-metrics from 2026-06-19, anomaly from 2026-07-02, gate from 2026-07-22 (~37h), chain 2026-07-22 only, sessions/claims/drift from late April 2026. Source-level exclusions: see EXCLUSIONS.md. Silence in any stream is evidence of nothing (hook outages indistinguishable from quiet).

## 2. Session durations (METRIC 1 wall, METRIC 2 active)

Primary stratum: TRUSTED n=36502 (right-censored within 60min of snapshot: 1). Sensitivity: +UWC n=41494.

| metric | p25 | median | p75 | p90 | mean |
|---|---|---|---|---|---|
| wall W (min) | 0.0 | 0.0 | 1.0 | 1.0 | 18.0 |
| active A15 (min) | 0.0 | 0.0 | 1.0 | 1.0 | 1.6 |
| active A5 (min) | 0.0 | 0.0 | 1.0 | 1.0 | 1.3 |
| active A30 (min) | 0.0 | 0.0 | 1.0 | 1.0 | 1.9 |
| A15 sensitivity (+UWC) | 0.0 | 0.0 | 1.0 | 1.0 | 1.5 |

Active/wall ratio (W>=5min sessions, TRUSTED n=850): median 1.0, IQR 0.9-1.0 — the remainder is UNKNOWN time, not 'idle'.

## 3. Activity survival S(t) over A15 (METRIC 3, Kaplan-Meier)

TRUSTED: KM median active duration = 0.0 min (n=36502, censored=1). Censoring note: only 1 observation(s) are censored, so censoring negligibly affects the reported curve; the informative-censoring caveat matters for tail interpretation, and the near-zero median is driven by the file-population mixture (disclosed above).

| A15 bucket (min) | S(t) at bucket exit |
|---|---|
| 0-1 | 0.2873 |
| 1-2 | 0.0386 |
| 2-5 | 0.0233 |
| 5-10 | 0.0149 |
| 10-15 | 0.0123 |
| 15-30 | 0.0048 |
| 30-60 | 0.0036 |
| 60-120 | 0.0026 |
| 120-240 | 0.0013 |
| 240-480 | 0.0005 |

## 4. Reliability-signal rates (METRIC 4; per stream window ONLY)

- anomaly stream: 20860 flagged / 31904 scored turns over 2026-07-02..2026-07-23 after quarantining one exact, unflagged duplicate (independent validation, and if warranted calibration, is required before behavioral-prevalence use).
- pre-existing Hermeneutic gate: 128 RISK instrument verdicts / 394 events over 2026-07-22..2026-07-23 (~37h-old stream; verdicts are not verified overclaim labels and are NEVER extrapolated).
- chain-broken (stop-too-soon): 13 flags, all on ['2026-07-22']; no session identity exists -> fleet-level count only.

Denominator caveat (post-review): per-active-hour rates were DROPPED from the shareable table — the active-hour denominator attributes a session's entire active time to its start day, which undercounts activity spilling into young stream windows. Raw event counts + window days only.

## 5. Drift-run summaries (METRIC 5)

| mode stratum | n runs | median anomaly/turn | p90 | sustained=true share |
|---|---|---|---|---|
| sliding-window | 21006 | 0.0 | 0.0 | 0.001 |

BACKFILL stratum (retrospective, UWC): 741 runs — reported separately, never pooled.

## 6. Residual claims-ledger cadence (METRIC 6 — proxy, heavily caveated)

Ledger entries not marked `claim_class=retrieved`: n=117 across 9 days (vs 28,055 raw rows, of which 27,938 recorded retrieval-reflex events). Verification field non-null: 98/117. This measures residual-entry cadence and field presence, not producer identity, agent authorship, completion, success, or correctness.

## 7. POST-HOC EXPLORATORY: wall-duration tiers (NOT pre-registered; hypothesis-generating only)

Motivation (instrument-validated): the per-file population is dominated by machine micro-traffic; pre-registered per-file medians describe that population, not interactive work. Tiers below were defined AFTER seeing the distribution — treat as exploratory.

| tier | n files | share | median W min | median A15 min | p90 A15 | summed A15 hours | gap-dominant n | gap-dominant A15 h | residual-qualifying n |
|---|---|---|---|---|---|---|---|---|---|
| micro <5min | 35652 | 0.977 | 0.0 | 0.0 | 1.0 | 176.4 | 9272 | 159.3 | 35652 |
| short 5-30min | 661 | 0.018 | 10.0 | 10.0 | 16.0 | 123.8 | 287 | 61.0 | 264 |
| medium 30-120min | 62 | 0.002 | 46.5 | 38.5 | 68.8 | 43.9 | 22 | 9.2 | 35 |
| long 2-8h | 40 | 0.001 | 239.0 | 149.5 | 227.0 | 100.7 | 12 | 19.4 | 27 |
| extended >8h | 87 | 0.002 | 2727.0 | 235.0 | 694.6 | 556.3 | 59 | 265.6 | 41 |

Gap-dominance caveat (post-review): 'gap-dominant' = a single inter-event gap exceeds 50% of the file's eligible-event span—the span is mostly one silent hole (often a stray trailing timestamp), not sustained or intermittent engagement. 'Residual-qualifying' = files that would still reach the tier floor after subtracting their largest gap. In the extended tier, largest-gap subtraction caused 46 of 87 files to fall below eight hours and left 41 above the threshold; gap dominance and threshold crossing are overlapping, non-complementary predicates.

Instrument caveats: (a) 'user'-type transcript events INCLUDE tool results — event counts are never human-turn counts and are not reported as such; (b) isSidechain=true was observed in 0 of 41495 files — the subagent stratum is UNMEASURABLE via this field in this corpus (finding F10), so no sidechain separation is claimed; (c) session unit = transcript file; resume/bridge linkage unvalidated; (d) 4992 dash-project (print-mode/spawn) files are UWC. Instrument validation receipt: a known ~23h ground-truth session reproduced at w_min=1372.0 by the pipeline (EXECPLAN Decisions).
