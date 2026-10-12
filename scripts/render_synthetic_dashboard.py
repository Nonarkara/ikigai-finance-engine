"""Draw the public synthetic dashboard from samples/synthetic/company-snapshot.json.

Writes company-snapshot.csv and dashboard-overview.png next to the JSON.
Figures come only from that JSON. This script does not read a private directory.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngInfo

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DIR = ROOT / "samples" / "synthetic"
JSON_PATH = SAMPLE_DIR / "company-snapshot.json"
CSV_PATH = SAMPLE_DIR / "company-snapshot.csv"
PNG_PATH = SAMPLE_DIR / "dashboard-overview.png"
FONT = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
FONT_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")

INK = (26, 26, 26)
CREAM = (244, 240, 230)
STAMP = (154, 52, 18)
RULE = (120, 110, 98)
CARD = (255, 252, 246)


def money(value: int) -> str:
    sign = "-" if value < 0 else ""
    return f"{sign}฿{abs(value):,}"


def load_snapshot() -> dict:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if data.get("data_classification") != "SYNTHETIC_SAMPLE":
        raise SystemExit(f"{JSON_PATH} is not labelled SYNTHETIC_SAMPLE")
    return data


def write_csv(data: dict) -> None:
    kpis = data["kpis"]
    balance = data["balance_sheet"]
    flows = data["cash_flow"]
    runway = data["runway"]
    summary = data["bank_scorecard"]["summary"]
    rows = [
        ("data_classification", data["data_classification"]),
        ("label", data["label"]),
        ("company_name", data["company_name"]),
        ("currency", data["currency"]),
        ("cash", kpis["cash"]),
        ("monthly_net_burn", kpis["monthly_net_burn"]),
        ("runway_months", kpis["runway_months"]),
        ("revenue", kpis["revenue"]),
        ("pipeline", kpis["pipeline"]),
        ("monthly_inflows", flows["monthly_inflows"]),
        ("monthly_outflows", flows["monthly_outflows"]),
        ("assets", balance["assets"]),
        ("liabilities", balance["liabilities"]),
        ("equity", balance["equity"]),
        ("registered_capital", balance["registered_capital"]),
        ("retained_earnings", balance["retained_earnings"]),
        ("suggested_raise_for_12_months", runway["suggested_raise_for_12_months"]),
        ("cash_zero", runway["cash_zero"]),
        ("bank_green", summary["green"]),
        ("bank_amber", summary["amber"]),
        ("bank_red", summary["red"]),
        ("macro_note", data["macro"]["note"]),
    ]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("field", "value"))
        writer.writerows(rows)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold else FONT
    if not path.is_file():
        raise SystemExit(f"Missing font {path}")
    return ImageFont.truetype(str(path), size)


def write_png(data: dict) -> None:
    width, height = 1100, 860
    image = Image.new("RGB", (width, height), CREAM)
    draw = ImageDraw.Draw(image)
    title = font(26, bold=True)
    heading = font(18, bold=True)
    body = font(16)
    small = font(13)

    draw.rectangle((0, 0, width, 72), fill=STAMP)
    draw.text((28, 12), "SYNTHETIC SAMPLE — NOT REAL FINANCIAL DATA", font=title, fill=(255, 248, 240))
    draw.text((28, 46), "Invented round figures for this public repository. Not a client extract.", font=small, fill=(255, 228, 210))

    kpis = data["kpis"]
    balance = data["balance_sheet"]
    flows = data["cash_flow"]
    runway = data["runway"]
    summary = data["bank_scorecard"]["summary"]

    blocks: list[tuple[str, list[str]]] = [
        (
            data["company_name"],
            [
                f"Currency {data['currency']}  ·  classification {data['data_classification']}",
            ],
        ),
        (
            "KPI strip",
            [
                f"Cash {money(kpis['cash'])}    Burn {money(kpis['monthly_net_burn'])}/mo    Runway {kpis['runway_months']} months",
                f"Revenue {money(kpis['revenue'])}    Pipeline {money(kpis['pipeline'])}",
            ],
        ),
        (
            "Balance sheet",
            [
                f"Assets {money(balance['assets'])} = Liabilities {money(balance['liabilities'])} + Equity {money(balance['equity'])}",
                f"Registered capital {money(balance['registered_capital'])} + retained earnings {money(balance['retained_earnings'])}",
            ],
        ),
        (
            "Cash flow and runway",
            [
                f"Inflows {money(flows['monthly_inflows'])} − outflows {money(flows['monthly_outflows'])} = net burn {money(kpis['monthly_net_burn'])}",
                f"Suggested raise for 12 months: {money(runway['suggested_raise_for_12_months'])}",
                f"Cash-zero marker: {runway['cash_zero']}",
            ],
        ),
        (
            "Bank scorecard — invented names",
            [
                f"{summary['green']} green · {summary['amber']} amber · {summary['red']} red",
                *[f"{item['light']}  {item['name']}" for item in data["bank_scorecard"]["items"]],
                data["bank_scorecard"]["note"],
            ],
        ),
        (
            "Indices — sample bands, not a measurement",
            [f"{index['name']}: {index['score']}/100 · {index['band']}" for index in data["indices"]],
        ),
        (
            "Macro placeholders",
            [
                data["macro"]["note"],
                f"SET {data['macro']['set_index']:.0f}    USD/THB {data['macro']['usd_thb']:.0f}    Gold {money(int(data['macro']['gold_thb_per_oz']))}/oz",
            ],
        ),
    ]

    y = 92
    for title_text, lines in blocks:
        draw.text((28, y), title_text, font=heading, fill=INK)
        y += 26
        for line in lines:
            draw.text((28, y), line, font=body, fill=INK)
            y += 22
        y += 10

    draw.line((28, height - 52, width - 28, height - 52), fill=RULE, width=1)
    draw.text(
        (28, height - 38),
        "Public fixture only. Real books: set FINANCE_DATA_DIR. Do not commit data/private/ or assets/screenshots/.",
        font=small,
        fill=STAMP,
    )

    info = PngInfo()
    info.add_text("Classification", "SYNTHETIC_SAMPLE")
    info.add_text("Warning", "Invented sample. Not real financial data.")
    image.save(PNG_PATH, format="PNG", pnginfo=info)


def main() -> int:
    data = load_snapshot()
    write_csv(data)
    write_png(data)
    print(f"wrote {CSV_PATH.relative_to(ROOT)}")
    print(f"wrote {PNG_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
