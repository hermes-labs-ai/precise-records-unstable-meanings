# Evidence interface

## Frozen boundary

The publication uses corrected snapshot `OTH-PUB2-20260723-dd281e3`, derived from repository commit:

`dd281e36a4429c3974cc58e5b025eb7ddd237ea8`

PUB2 preserves the PUB1 raw-source boundary and corrects one implementation
contradiction: the frozen audit identified one exact, unflagged anomaly
duplicate that the full extractor had retained. The corrected scored
denominator is 31,904 rather than 31,905; the flagged numerator remains 20,860.

The final aggregate snapshot contains:

- 41,495 transcript files;
- 28,055 claims-ledger entries, of which 27,938 recorded automatic retrieval-reflex events with `claim_class=retrieved` and 117 heterogeneous residual entries did not;
- 31,905 raw anomaly rows, including one exact unflagged duplicate; 20,860 of the 31,904 retained scored turns were flagged;
- 394 pre-existing Hermeneutic-gate rows, of which 128 carried the `RISK` instrument verdict; and
- 13 stop-too-soon flags.

The exact machine-readable boundary is [SNAPSHOT.json](SNAPSHOT.json).

## Why older documents show 393, 27,937, and 1,000.6 hours

The operational logs were live during development. The fresh-context model
review evaluated an immediately preceding snapshot with 393 gate rows, 27,937
entries marked `claim_class=retrieved`, and 1,000.6 hours under the summed
fifteen-minute gap-capped inter-event measure. Before the final aggregate
snapshot, one additional gate row and one additional marked row entered; the
final regeneration yielded 1,001.1 hours under the same rule.

The public package does not silently rewrite that historical review. It binds every public number to the final snapshot and describes the earlier review only as developmental criticism. The final row is not represented as independently reviewed.

## Inspect material claims

[CLAIMS-LEDGER.md](CLAIMS-LEDGER.md) records:

- the candidate interpretation;
- data treatment;
- terminal claim disposition;
- allowed public wording; and
- the exact aggregate evidence.

[METHOD-APPENDIX.md](METHOD-APPENDIX.md) specifies the deterministic
classification rules, the limited role of the 400-file seeded check, the
direct-versus-inferred evidence boundary, and the duration-cap sensitivities.

## Inspect aggregate evidence

The `aggregate/` directory contains the identifier-free outputs used by the paper and companion report:

- inventory and source coverage;
- classification totals;
- activity-cap sensitivity at 5, 15, and 30 minutes;
- session and duration aggregates;
- windowed detector counts;
- drift and residual claims-ledger cadence aggregates;
- provenance and exclusions.

No raw transcript content, session identifiers, or timestamps finer than one day are included.

## Verify consistency

Run:

```bash
python3 ../verify.py
```

The verifier checks the package hashes, privacy patterns, snapshot identity, and material numerical bindings. It does not establish the validity of the private extraction rules or independently reproduce the source corpus.
