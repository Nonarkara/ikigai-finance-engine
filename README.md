# Ikigai Finance Engine

**SME finance intelligence — balance sheet as signal, not spreadsheet.**

A research prototype that reads a small company's financial position the way an operator reads a city dashboard: cash runway first, balance sheet structure second, bank standing third, composite indices last. Built for founders who need to see distress before the bank letter arrives — and for advisors who need one surface instead of five PDFs.

> **Status:** Development stage. No live public deployment. This repository contains screenshots, architecture notes, and research pointers only — no application code, credentials, or client data.

---

## What you are looking at

The dashboard screenshot in [`assets/screenshots/dashboard-overview.png`](assets/screenshots/dashboard-overview.png) shows an **anonymized startup demonstration**. **ABC Company Limited** is fictitious. All figures are mockup financial data derived from a synthetic dataset for interface design — not real company filings, not investment advice, and not a recommendation to raise, lend, or invest.

The banner on the prototype states this explicitly: *Anonymized startup demonstration — names fictitious — figures from source dataset.*

---

## Problem space

Thai SMEs — and early-stage startups everywhere — often discover liquidity problems after the runway is already gone. The symptoms are scattered:

- Cash in bank vs monthly burn (runway)
- Balance sheet imbalance (negative equity, asset-liability mismatch)
- Bank relationship health (overdraft utilisation, covenant proximity)
- Pipeline vs revenue recognition gap

Each lives in a different file, a different meeting, a different mental model. The Finance Engine asks a simpler question: **what decision must happen this month, and what numbers support it?**

---

## Surface areas (from prototype)

| Panel | Purpose |
|-------|---------|
| **KPI strip** | Cash, burn, runway, revenue, pipeline — one glance |
| **Balance sheet** | Assets vs liabilities + equity as a balanced signal |
| **Cash flow & runway** | 12-month outlook, cash-zero date, suggested raise |
| **Bank scorecard** | Credit standing, benchmark comparison, risk flags |
| **Finance indices** | Composite scores (Ikigai, Lean, Zero, Default, Solvency) |
| **Macro sidebar** | SET, USD/THB, gold — purchasing-power context |

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for system diagram and data-flow description.

---

## Finance indices (overview)

The prototype surfaces five named indices on a 0–100 scale. They are **research constructs** — ways to compress multidimensional financial health into scannable labels for operators, not regulatory ratings.

| Index | Plain-language intent |
|-------|----------------------|
| **Ikigai** | Strategic leverage — is capital deployed toward purpose or drift? |
| **Lean** | Operating discipline — burn efficiency relative to revenue motion |
| **Zero** | Runway horizon — months until cash zero at current burn |
| **Default** | Default-risk proximity — debt service vs available cash |
| **Solvency** | Structural distress — equity, liabilities, and asset quality |

Methodology detail and literature pointers: [`docs/RESEARCH.md`](docs/RESEARCH.md).

---

## Repository contents

```
README.md                 — this file
docs/
  ARCHITECTURE.md         — system overview (mermaid)
  RESEARCH.md             — indices concept, SME runway, balance-sheet-as-signal
assets/
  screenshots/
    dashboard-overview.png
  diagrams/
    system-overview.mmd
```

**Explicitly not included:** API keys, `.env` files, database schemas with real data, proprietary scoring formulas under client NDA, deployment configs, or implementation source code.

---

## Disclaimer

This is a **demonstration prototype** for research and education. It is **not investment advice**, **not credit advice**, and **not a substitute for audited financial statements or licensed advisory services. Any resemblance to a real company is coincidental; ABC Company Limited is fictional.

---

## Author

Dr Non Arkaraprasertkul — [Axiom](https://nonarkara.github.io/Axiom/) · Bangkok

Development-stage work. Questions via [nonarkara.org](https://nonarkara.org).
