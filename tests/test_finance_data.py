"""Public sample stays labelled and synthetic; private paths stay gitignored."""

from __future__ import annotations

import csv
import json
import os
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from finance_data import (
    load_company_snapshot,
    resolve_data_dir,
    synthetic_dir,
    validate_public_sample,
)

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_JSON = ROOT / "samples" / "synthetic" / "company-snapshot.json"
SAMPLE_CSV = ROOT / "samples" / "synthetic" / "company-snapshot.csv"
SAMPLE_PNG = ROOT / "samples" / "synthetic" / "dashboard-overview.png"


def git_check_ignore(path: str) -> bool:
    result = subprocess.run(
        ["git", "check-ignore", "-q", "--", path],
        cwd=ROOT,
        check=False,
    )
    return result.returncode == 0


class FinanceDataTests(unittest.TestCase):
    def test_default_directory_is_the_synthetic_sample(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("FINANCE_DATA_DIR", None)
            self.assertEqual(resolve_data_dir(), synthetic_dir())
            snapshot = load_company_snapshot()
        self.assertEqual(snapshot["data_classification"], "SYNTHETIC_SAMPLE")
        self.assertIn("SYNTHETIC", snapshot["company_name"].upper())
        self.assertIn("SYNTHETIC", snapshot["label"].upper())

    def test_public_sample_obeys_conservation_laws(self) -> None:
        snapshot = json.loads(SAMPLE_JSON.read_text(encoding="utf-8"))
        validate_public_sample(snapshot)
        balance = snapshot["balance_sheet"]
        self.assertEqual(
            balance["assets"],
            balance["liabilities"] + balance["equity"],
        )
        kpis = snapshot["kpis"]
        self.assertEqual(kpis["runway_months"], kpis["cash"] / kpis["monthly_net_burn"])

    def test_csv_matches_json(self) -> None:
        snapshot = json.loads(SAMPLE_JSON.read_text(encoding="utf-8"))
        with SAMPLE_CSV.open(encoding="utf-8", newline="") as handle:
            rows = dict(csv.reader(handle))
        rows.pop("field", None)
        self.assertEqual(rows["data_classification"], "SYNTHETIC_SAMPLE")
        self.assertEqual(rows["company_name"], snapshot["company_name"])
        self.assertEqual(int(rows["cash"]), snapshot["kpis"]["cash"])
        self.assertEqual(int(rows["monthly_net_burn"]), snapshot["kpis"]["monthly_net_burn"])
        self.assertEqual(float(rows["runway_months"]), snapshot["kpis"]["runway_months"])
        self.assertEqual(int(rows["assets"]), snapshot["balance_sheet"]["assets"])
        self.assertEqual(int(rows["equity"]), snapshot["balance_sheet"]["equity"])
        self.assertIn("SYNTHETIC", rows["label"].upper())

    def test_dashboard_image_is_a_labelled_png(self) -> None:
        raw = SAMPLE_PNG.read_bytes()
        self.assertTrue(raw.startswith(b"\x89PNG\r\n\x1a\n"))
        self.assertIn(b"SYNTHETIC_SAMPLE", raw)
        self.assertIn(b"Not real financial data", raw)
        tracked = subprocess.check_output(
            ["git", "ls-files", "assets/screenshots"],
            cwd=ROOT,
            text=True,
        )
        self.assertEqual(tracked.strip(), "")

    def test_finance_data_dir_points_at_a_private_directory(self) -> None:
        with TemporaryDirectory() as tmp:
            private = Path(tmp)
            payload = {
                "data_classification": "PRIVATE",
                "company_name": "Kept Off The Public Tree",
            }
            (private / "company-snapshot.json").write_text(
                json.dumps(payload),
                encoding="utf-8",
            )
            with mock.patch.dict(os.environ, {"FINANCE_DATA_DIR": str(private)}):
                self.assertEqual(resolve_data_dir(), private.resolve())
                loaded = load_company_snapshot()
            self.assertEqual(loaded, payload)

    def test_missing_private_directory_is_an_error(self) -> None:
        with TemporaryDirectory() as tmp:
            missing = str(Path(tmp) / "missing-private")
            with mock.patch.dict(os.environ, {"FINANCE_DATA_DIR": missing}):
                with self.assertRaises(FileNotFoundError):
                    resolve_data_dir()

    def test_gitignore_blocks_real_data_paths(self) -> None:
        ignored = [
            "data/private/company-snapshot.json",
            "private/books.csv",
            "fixtures/real/ledger.csv",
            "assets/screenshots/dashboard-overview.png",
            "exports/bank-statement.csv",
            "client-ledger.json",
            "workbook.xlsx",
        ]
        for path in ignored:
            self.assertTrue(git_check_ignore(path), path)
        allowed = [
            "samples/synthetic/company-snapshot.json",
            "samples/synthetic/company-snapshot.csv",
            "samples/synthetic/dashboard-overview.png",
            "docs/RESEARCH.md",
            "README.md",
        ]
        for path in allowed:
            self.assertFalse(git_check_ignore(path), path)


if __name__ == "__main__":
    unittest.main()
