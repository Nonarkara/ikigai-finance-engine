"""Load the public synthetic company sample, or a private directory.

This repository commits company figures only under ``samples/synthetic/``,
labelled ``SYNTHETIC_SAMPLE``. Real books stay outside git.

Unset ``FINANCE_DATA_DIR`` and the loader reads the synthetic sample.
Point it at a private directory (outside the clone, or the gitignored
``data/private/`` folder) and it reads ``company-snapshot.json`` from there:

    export FINANCE_DATA_DIR="$HOME/private/ikigai-finance-data"
    python3 finance_data.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

PRIVATE_ENV = "FINANCE_DATA_DIR"
SYNTHETIC_CLASSIFICATION = "SYNTHETIC_SAMPLE"
SNAPSHOT_FILENAME = "company-snapshot.json"


def repo_root() -> Path:
    return Path(__file__).resolve().parent


def synthetic_dir() -> Path:
    return repo_root() / "samples" / "synthetic"


def resolve_data_dir() -> Path:
    """Return the directory that holds ``company-snapshot.json``.

    ``FINANCE_DATA_DIR`` wins when it is set. Otherwise the committed
    synthetic sample is used.
    """
    raw = os.environ.get(PRIVATE_ENV, "").strip()
    if not raw:
        return synthetic_dir()
    path = Path(raw).expanduser().resolve()
    if not path.is_dir():
        raise FileNotFoundError(
            f"{PRIVATE_ENV}={raw!r} is not a directory. "
            "Create it outside this repository, or under data/private/, "
            f"and place {SNAPSHOT_FILENAME} inside it."
        )
    return path


def load_company_snapshot(data_dir: Path | None = None) -> dict:
    """Load one company snapshot.

    The committed public sample is checked for the synthetic label and for
    the conservation laws the research notes describe. A private directory
    is returned as the owner's JSON object without that public-sample check.
    """
    directory = Path(data_dir) if data_dir is not None else resolve_data_dir()
    path = directory / SNAPSHOT_FILENAME
    if not path.is_file():
        raise FileNotFoundError(
            f"No {SNAPSHOT_FILENAME} in {directory}. "
            "Public runs use samples/synthetic/. "
            f"Private runs set {PRIVATE_ENV} to a directory that contains the file."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must be a JSON object")
    if _is_public_sample(directory):
        validate_public_sample(data)
    return data


def _is_public_sample(directory: Path) -> bool:
    return directory.resolve() == synthetic_dir().resolve()


def validate_public_sample(data: dict) -> None:
    """Reject a committed fixture that is unlabelled or arithmetically inconsistent."""
    if data.get("data_classification") != SYNTHETIC_CLASSIFICATION:
        raise ValueError(
            "The committed public sample must be labelled "
            f"{SYNTHETIC_CLASSIFICATION}."
        )
    if "SYNTHETIC" not in str(data.get("company_name", "")).upper():
        raise ValueError("Public sample company_name must identify itself as synthetic")
    if "SYNTHETIC" not in str(data.get("label", "")).upper():
        raise ValueError("Public sample label must say SYNTHETIC")

    kpis = data["kpis"]
    balance = data["balance_sheet"]
    runway = data["runway"]
    flows = data["cash_flow"]

    assets = balance["assets"]
    liabilities = balance["liabilities"]
    equity = balance["equity"]
    if assets != liabilities + equity:
        raise ValueError(
            f"Balance sheet does not conserve: assets {assets} != "
            f"liabilities {liabilities} + equity {equity}"
        )
    if balance["registered_capital"] + balance["retained_earnings"] != equity:
        raise ValueError(
            "Equity must equal registered capital plus retained earnings"
        )

    cash = kpis["cash"]
    burn = kpis["monthly_net_burn"]
    if burn == 0:
        raise ValueError("monthly_net_burn must not be zero")
    if flows["monthly_outflows"] - flows["monthly_inflows"] != burn:
        raise ValueError("monthly_net_burn must equal outflows minus inflows")
    expected_runway = cash / burn
    actual_runway = kpis["runway_months"]
    if abs(actual_runway - expected_runway) > 1e-9:
        raise ValueError(
            f"Runway {actual_runway} != cash / burn ({expected_runway})"
        )
    expected_raise = 12 * burn - cash
    actual_raise = runway["suggested_raise_for_12_months"]
    if actual_raise != expected_raise:
        raise ValueError(
            f"Suggested raise {actual_raise} != 12 * burn - cash ({expected_raise})"
        )

    summary = data["bank_scorecard"]["summary"]
    counts = {"green": 0, "amber": 0, "red": 0}
    for item in data["bank_scorecard"]["items"]:
        counts[item["light"]] += 1
    if counts != summary:
        raise ValueError(
            f"Bank scorecard summary {summary} does not match items {counts}"
        )
    for index in data["indices"]:
        band = str(index["band"])
        if not band.startswith("SAMPLE"):
            raise ValueError(f"Public index band {band!r} must start with SAMPLE")


def main() -> int:
    directory = resolve_data_dir()
    snapshot = load_company_snapshot()
    classification = snapshot.get("data_classification", "unlabelled")
    name = snapshot.get("company_name", "(no company_name)")
    print(f"data_dir={directory}")
    print(f"data_classification={classification}")
    print(f"company_name={name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
