**Histogram of per-file wall duration (W), log count scale.** TRUSTED n=36,502; every bucket
labeled with its exact count because the log scale compresses magnitude (dataviz caveat made
explicit). Two-population shape: machine micro-traffic (<5 min) plus a long tail (87 files >8 h) —
but the tail's wall spans are materially gap-dominated (59/87 files have one silent gap
>50% of span; multi-day bars largely reflect stray isolated timestamps, not sustained
presence — see tiers.csv gap-dominance columns). Uncertainty: wall time includes UNKNOWN time (idle OR
unobserved); see summary_tables.md §2 for active-time decomposition.
Source: data/derived/sessions_agg.csv.
