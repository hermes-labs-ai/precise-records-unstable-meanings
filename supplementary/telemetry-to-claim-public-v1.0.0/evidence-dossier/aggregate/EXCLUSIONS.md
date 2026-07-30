# Source exclusions (M1; record-level quarantine happens in M1.5 audit)
(Shareable file: sources named by ID only; local paths in private provenance notes.)

- **claims_log_legacy** — EXCLUDED: 52-row legacy shard; double-count risk vs claims_log (audit M1.5 checks overlap)
- **background_poller** — EXCLUDED: GTM poller traffic, not session telemetry
- **misc_small** — EXCLUDED: tiny/ambiguous provenance or unrelated to session-horizon constructs

Note: onset dates differ per stream (left-truncation); see inventory.json spans.
