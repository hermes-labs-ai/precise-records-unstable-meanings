#!/usr/bin/env python3
"""Verify the frozen public telemetry-to-claim package.

This checks package integrity, selected manuscript-to-aggregate numbers, and obvious privacy
patterns. It does not reproduce the private raw-to-aggregate extraction.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.sha256"
SKIP = {"MANIFEST.sha256"}
TITLE = (
    "Precise Records, Unstable Meanings: Measurement Validity and "
    "Unsupported Claims Derived from AI Agent Telemetry"
)
SUBJECT = (
    "A twelve-week naturalistic audit of measurement validity and "
    "unsupported claims derived from AI agent telemetry."
)
KEYWORDS = (
    "AI agent telemetry; measurement validity; construct validity; agent "
    "evaluation; operational telemetry; telemetry provenance; agent "
    "observability; coding agents; Telemetry-to-Claim Gate"
)


def public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.name not in SKIP
        and "__pycache__" not in path.parts
    )


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_manifest() -> None:
    lines = [f"{digest(path)}  {path.relative_to(ROOT)}" for path in public_files()]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify_manifest(errors: list[str]) -> None:
    if not MANIFEST.exists():
        errors.append("MANIFEST.sha256 is missing")
        return
    expected: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha, rel = line.split("  ", 1)
        expected[rel] = sha
    actual = {str(path.relative_to(ROOT)): digest(path) for path in public_files()}
    if expected != actual:
        missing = sorted(set(expected) - set(actual))
        added = sorted(set(actual) - set(expected))
        changed = sorted(
            rel for rel in set(expected) & set(actual) if expected[rel] != actual[rel]
        )
        errors.append(
            f"manifest mismatch: missing={missing}, added={added}, changed={changed}"
        )


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def verify_numbers(errors: list[str]) -> None:
    snapshot = json.loads((ROOT / "evidence-dossier/SNAPSHOT.json").read_text())
    inventory = json.loads(
        (ROOT / "evidence-dossier/aggregate/inventory.json").read_text()
    )
    counts = snapshot["counts"]
    boundary = snapshot["boundary"]
    if snapshot.get("snapshot_id") != "OTH-PUB2-20260723-dd281e3":
        errors.append(f"unexpected snapshot_id: {snapshot.get('snapshot_id')!r}")
    if snapshot.get("supersedes_snapshot_id") != "OTH-PUB1-20260723-dd281e3":
        errors.append("corrected snapshot does not bind its superseded PUB1 identity")
    expected_boundary = {
        "deployments": 1,
        "system_kind": "coding-agent orchestration harness",
        "harness_persisted_across_window": True,
        "individual_agent_persistence_assumed": False,
        "process_persistence_assumed": False,
        "logical_session_persistence_across_files_assumed": False,
        "primary_observed_unit": "transcript file",
    }
    for key, expected in expected_boundary.items():
        if boundary.get(key) != expected:
            errors.append(
                f"study boundary {key}: snapshot={boundary.get(key)!r} "
                f"expected={expected!r}"
            )
    checks = {
        "transcript_files": inventory["sources"]["transcripts"]["rows"],
        "claims_ledger_rows": inventory["sources"]["claims_log"]["rows"],
        "anomaly_source_rows": inventory["sources"]["turn_anomaly"]["rows"],
        "overclaim_gate_rows": inventory["sources"]["hermeneutic_gate"]["rows"],
        "stop_too_soon_flags": inventory["sources"]["chain_broken"]["rows"],
        "drift_summaries": inventory["sources"]["drift_log"]["rows"],
    }
    for key, actual in checks.items():
        if counts[key] != actual:
            errors.append(f"{key}: snapshot={counts[key]} aggregate={actual}")

    rates = {
        row["signal"]: row
        for row in read_csv(ROOT / "evidence-dossier/aggregate/rates.csv")
    }
    rate_checks = {
        "anomaly_flagged": (
            counts["anomaly_flagged_turns"],
            counts["anomaly_scored_turns"],
        ),
        "overclaim_gate_risk": (
            counts["overclaim_gate_risk"],
            counts["overclaim_gate_rows"],
        ),
        "chain_broken": (
            counts["stop_too_soon_flags"],
            counts["stop_too_soon_flags"],
        ),
    }
    for signal, (events, total) in rate_checks.items():
        row = rates[signal]
        if (int(row["events"]), int(row["scored_total"])) != (events, total):
            errors.append(f"{signal}: rates.csv does not match snapshot")

    tiers = {
        row["tier"]: row
        for row in read_csv(ROOT / "evidence-dossier/aggregate/tiers.csv")
    }
    micro = tiers["micro <5min"]
    extended = tiers["extended >8h"]
    tier_checks = {
        "trusted_files_under_5m": int(micro["n"]),
        "extended_files_over_8h": int(extended["n"]),
        "extended_gap_dominant": int(extended["gap_dominant_n"]),
        "extended_residual_qualifying": int(extended["residual_qualifying_n"]),
    }
    for key, actual in tier_checks.items():
        if counts[key] != actual:
            errors.append(f"{key}: snapshot={counts[key]} tiers={actual}")

    report = (ROOT / "evidence-dossier/aggregate/audit_report.md").read_text()
    claim_match = re.search(
        r"\| claims_log \| 101 \| 16 \| (\d+) \| (\d+) \|", report
    )
    if not claim_match:
        errors.append("claims_log row missing from audit_report.md")
    else:
        marked_retrieved, ledger_rows = map(int, claim_match.groups())
        if (marked_retrieved, ledger_rows) != (
            counts["claims_retrieval_reflex_events"],
            counts["claims_ledger_rows"],
        ):
            errors.append("claims_log audit totals do not match snapshot")

        residual = counts.get("claims_not_marked_retrieved")
        if residual != ledger_rows - marked_retrieved:
            errors.append(
                "claims_not_marked_retrieved does not match the native-field "
                "partition"
            )

    legacy_claim_labels = {
        "claims_agent_authored",
        "claims_agent_authored_days",
    }
    stale_labels = sorted(legacy_claim_labels & counts.keys())
    if stale_labels:
        errors.append(f"unsupported claims producer labels remain: {stale_labels}")

    claims_agg = read_csv(ROOT / "evidence-dossier/aggregate/claims_agg.csv")
    residual_days = sum(int(row["n_days"]) for row in claims_agg)
    if counts.get("claims_not_marked_retrieved_days") != residual_days:
        errors.append(
            "claims_not_marked_retrieved_days does not match claims_agg.csv"
        )

    anomaly_match = re.search(
        r"\| turn_anomaly \| (\d+) \| 0 \| (\d+) \| (\d+) \|", report
    )
    expected_anomaly = (
        counts["anomaly_scored_turns"],
        counts["anomaly_duplicates_quarantined"],
        counts["anomaly_source_rows"],
    )
    if not anomaly_match:
        errors.append("turn_anomaly row missing from audit_report.md")
    elif tuple(map(int, anomaly_match.groups())) != expected_anomaly:
        errors.append("turn_anomaly audit totals do not match snapshot")

    cap_rows = {
        (row["stratum"], int(row["cap_min"])): row
        for row in read_csv(
            ROOT / "evidence-dossier/aggregate/activity_cap_sensitivity.csv"
        )
    }
    expected_caps = {
        ("TRUSTED", 5): (36502, "777.6"),
        ("TRUSTED", 15): (36502, "1001.1"),
        ("TRUSTED", 30): (36502, "1166.0"),
        ("TRUSTED+UWC", 15): (41494, "1035.2"),
    }
    for key, (expected_n, expected_hours) in expected_caps.items():
        row = cap_rows.get(key)
        if not row:
            errors.append(f"activity-cap sensitivity row missing: {key}")
        elif (int(row["n"]), row["sum_hours"]) != (expected_n, expected_hours):
            errors.append(f"activity-cap sensitivity mismatch: {key}")

    paper = (ROOT / "paper/PAPER.md").read_text()
    report = (ROOT / "technical-report/TECHNICAL-REPORT.md").read_text()
    required_paper_bindings = [
        f"# {TITLE}",
        "one coding-agent orchestration-harness deployment observed over twelve weeks",
        "35,652, or 97.7%, spanned less than five minutes",
        "27,938 entries carrying `claim_class=retrieved` were automatic records",
        "Ninety-eight had a non-empty `verification` field",
        "Subtracting each file's largest internal gap caused 46 to fall below eight hours",
        "20,860 of 31,904 scored turns",
        "128 `RISK` verdicts among 394 events",
        "13 flags on July 22",
        "10.5281/zenodo.18867694",
        "10.5281/zenodo.19042469",
        "10.5281/zenodo.21659634",
        "The initial audit concept emerged during a Claude Code session",
    ]
    required_report_bindings = [
        "one orchestration-harness deployment",
        "27,938 entries with `claim_class=retrieved` recorded automatic entity-retrieval events",
        "117 were heterogeneous residual ledger entries",
        "Of those files, 59 had one silent gap",
        "caused 46 to fall below eight hours, leaving 41 above the threshold",
    ]
    for binding in required_paper_bindings:
        if binding not in paper:
            errors.append(f"paper lost material snapshot binding: {binding!r}")
    for binding in required_report_bindings:
        if binding not in report:
            errors.append(
                f"technical report lost material snapshot binding: {binding!r}"
            )

    if (ROOT / "APPLIED-HERMENEUTICS-IN-EPISTEMIC-ENGINEERING.md").exists():
        errors.append("complete Applied Hermeneutics manuscript remains in OTH package")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "10.5281/zenodo.21659634" not in readme:
        errors.append("OTH README lacks independent Applied Hermeneutics pointer")


def verify_privacy(errors: list[str]) -> None:
    patterns = {
        "absolute user path": re.compile(r"/Users/"),
        "home-relative private path": re.compile(r"~/(?:\.|Documents|Desktop|dev)"),
        "email address": re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
        "sub-day timestamp": re.compile(r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"),
    }
    for path in public_files():
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip"}:
            continue
        rel = str(path.relative_to(ROOT))
        if rel == "verify.py":
            # The verifier necessarily contains the forbidden-pattern literals.
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in patterns.items():
            checked = (
                text.replace("roli@hermes-labs.ai", "")
                if label == "email address"
                else text
            )
            if pattern.search(checked):
                errors.append(f"privacy pattern '{label}' in {rel}")


def verify_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in public_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative_target = target.split("#", 1)[0]
            if relative_target and not (path.parent / relative_target).exists():
                errors.append(
                    f"broken local link in {path.relative_to(ROOT)}: {target}"
                )


def verify_pdf_metadata(errors: list[str]) -> None:
    for path in public_files():
        if path.suffix.lower() != ".pdf":
            continue
        raw = path.read_bytes()
        for field in (b"/CreationDate", b"/ModDate"):
            if field in raw:
                errors.append(
                    f"sub-day PDF metadata {field.decode()} in "
                    f"{path.relative_to(ROOT)}"
                )
    paper_pdf = ROOT / "paper/PAPER.pdf"
    if not paper_pdf.exists():
        errors.append("paper/PAPER.pdf is missing")
        return
    info_text = subprocess.run(
        ["pdfinfo", str(paper_pdf)],
        check=True,
        text=True,
        capture_output=True,
    ).stdout
    metadata = {
        key.strip(): value.strip()
        for line in info_text.splitlines()
        if ":" in line
        for key, value in [line.split(":", 1)]
    }
    expected = {
        "Title": TITLE,
        "Author": "Rolando Bosch",
        "Subject": SUBJECT,
        "Keywords": KEYWORDS,
    }
    for key, value in expected.items():
        if metadata.get(key) != value:
            errors.append(
                f"PDF metadata {key}: {metadata.get(key)!r} != {value!r}"
            )
    if not re.search(rb"/Lang\s*(?:\(en\)|/en)", paper_pdf.read_bytes()):
        errors.append("paper/PAPER.pdf catalog language is not English")

    paper_source = (ROOT / "paper/PAPER.md").read_text(encoding="utf-8")
    abstract = (
        paper_source.split("## Abstract\n", 1)[1]
        .split("## 1. Introduction\n", 1)[0]
        .strip()
    )
    page_one = subprocess.run(
        ["pdftotext", "-f", "1", "-l", "1", str(paper_pdf), "-"],
        check=True,
        text=True,
        capture_output=True,
    ).stdout
    page_one = re.sub(r"(?<=\w)-\s+(?=\w)", "-", page_one)
    normalized_page_one = " ".join(page_one.split())
    required_page_one = [
        TITLE,
        "Rolando Bosch",
        "Hermes Labs — San Francisco, California, USA",
        "roli@hermes-labs.ai",
        "July 30, 2026",
    ]
    required_page_one.extend(
        " ".join(re.sub(r"[*_]", "", paragraph.replace("`", "")).split())
        for paragraph in re.split(r"\n\s*\n", abstract)
    )
    compact_page_one = re.sub(r"[^0-9A-Za-z]+", "", normalized_page_one).lower()
    for binding in required_page_one:
        compact_binding = re.sub(r"[^0-9A-Za-z]+", "", binding).lower()
        if compact_binding not in compact_page_one:
            errors.append(f"PDF page one lost binding: {binding[:80]!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="replace MANIFEST.sha256 with hashes of the current public package",
    )
    args = parser.parse_args()

    if args.write_manifest:
        write_manifest()
        print(f"WROTE {MANIFEST}")
        return 0

    errors: list[str] = []
    verify_manifest(errors)
    verify_numbers(errors)
    verify_privacy(errors)
    verify_links(errors)
    verify_pdf_metadata(errors)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: manifest, material numbers, and public privacy patterns")
    print("BOUNDARY: internal consistency only; raw-to-aggregate reproduction unavailable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
