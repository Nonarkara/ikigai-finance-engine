![Mentor and founder at a Bangkok night desk, paper ledgers open like a city map, rain on the window — no dashboard overlay.](docs/hero-banner.jpg)

*งบดุลคือสัญญาณ · Balance sheet as signal, not spreadsheet. Hand-drawn studio still; no HUD on the image.*

# Ikigai Finance Engine

**SME finance intelligence — a research prototype that reads a company the way an operator reads a city dashboard.**

[![License: MIT](https://img.shields.io/badge/license-MIT-1A1A1A)](LICENSE)

[What this is](#what-this-is) · [Philosophy](#philosophy) · [Ethical use](#ethical-use) · [How to use / learn](#how-to-use--learn) · [Private data](#private-data) · [System diagram](#system-diagram) · [License](#license--contributing)

By [Non Arkaraprasertkul](https://github.com/Nonarkara) (Nonarkara) — [Axiom X Co., Ltd.](https://github.com/Nonarkara/Axiom), Bangkok.

Independent civic-studio work. Written for a **Thai–English** audience. **Personal / finance tooling — not financial advice.** This repository is not a bank, not a credit rating, and not a live product.

---

## What this is

A **research and education layer** for an SME finance-intelligence prototype. Cash runway first, balance-sheet structure second, bank standing third, composite indices last. The public tree is notes plus a **labelled synthetic sample** — enough to fork the *method*, not a client ledger.

What is actually in this repository:

- An invented company fixture and the diagram drawn from it — [`samples/synthetic/`](samples/synthetic/)
- A small loader, [`finance_data.py`](finance_data.py), that reads that fixture unless `FINANCE_DATA_DIR` points at a private directory
- Architecture notes and a mermaid data-flow — [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`assets/diagrams/system-overview.mmd`](assets/diagrams/system-overview.mmd)
- Research notes on runway arithmetic, bank scorecards, and five named indices — [`docs/RESEARCH.md`](docs/RESEARCH.md)

**SYNTHETIC SAMPLE Co., Ltd.** is invented. Every committed figure is a round number chosen so the conservation laws still hold. The loader and its unit test are the only executable surface; they are not the finance engine. There is **no live public deployment**.

The source-dataset dashboard that used to live at `assets/screenshots/dashboard-overview.png` is **removed from the tree**. History was not rewritten. Do not copy that file back.

Sibling software: **[Nonarkara/ikigai-finance](https://github.com/Nonarkara/ikigai-finance)** is a separate, runnable single-company cockpit (evidence inbox, local diagnostic, MIT). It is not this engine, and this repo is not a dump of that app.

**This repo is not:**

- Investment, credit, or tax advice
- Audited statements, a credit-rating agency, or a licensed advisory service
- A ranking of firms, founders, or banks
- API keys, `.env` files, client data, proprietary index weights, or deployment configs

---

## Philosophy

Studio tenets, applied to a finance desk:

**Fork the method, not the secrets.** Take the conservation laws, the panel grammar, and the rule that every index must say what it *cannot* say. Leave real ledgers, bank files, tokens, and unpublished weights on *your* machine. They do not belong in issues, screenshots, or pull requests. The concrete switch is [`FINANCE_DATA_DIR`](#private-data).

**One Mac.** This prototype was designed as a single-operator surface — one desk, one company in view, no cluster. This public tree has no app to install; the method is the architecture and the research notes. Runnable studio software for one company lives in the sibling [ikigai-finance](https://github.com/Nonarkara/ikigai-finance) repo.

**No black-box rankings.** Runway is `cash / monthly net burn`. Assets must equal liabilities plus equity; if those stories disagree, the dashboard is supposed to make the disagreement visible. The five named indices (Ikigai, Lean, Zero, Default, Solvency) are **research constructs** on a 0–100 scale for operators — not regulatory ratings, not a league table of SMEs, and not published formulas. Weights are still under research and are **not** in this tree.

**Thai–English as the audience.** The studio writes for learners and operators who move between Thai and English. The screenshot’s chrome includes Thai (เครื่องยนต์การเงิน). This README is English with a Thai caption so a first glance is bilingual — not a claim that a localized product ships here.

Company: **Axiom X Co., Ltd.** Author: **Non Arkaraprasertkul** (Nonarkara). This is independent studio documentation, not a billed Axiom product and not an official depa, bank, or municipal system.

---

## Ethical use

Treat this as a **teaching prototype**, not a substitute for a licensed advisor, an auditor, or a bank’s own decision.

**Do**

- Read the committed diagram as a labelled synthetic fixture. The stamp says SYNTHETIC SAMPLE. Negative equity is there so a distress reading still has a shape. It is not a client.
- Keep the public sample synthetic. If you rebuild the surface, label invented figures as synthetic.
- Attribute the method when you fork the architecture or the research notes.
- Put any credentials you later add to *your* implementation in ignored env files — never in git.

**Do not**

- Present these indices, the bank scorecard, or a “suggested raise” as investment, lending, or credit advice.
- Treat a composite 0–100 score as a credit rating, a valuation, or a ranking of companies.
- Invent a live URL, a client roster, an award, or a published formula this tree does not contain.
- Commit API keys, bank statements, customer ledgers, `.env` files, or anything under NDA.
- Imply depa, a commercial bank, or a regulator publishes or certifies this prototype.

If a contribution only works by pasting a secret or a real company’s books, it does not belong here.

---

## How to use / learn

This tree is documentation plus the synthetic-sample loader. There is nothing to `npm install`. Python 3 is enough to run `finance_data.py` and the unit test.

1. Open [`samples/synthetic/dashboard-overview.png`](samples/synthetic/dashboard-overview.png) and the matching [`company-snapshot.json`](samples/synthetic/company-snapshot.json). The stamp says SYNTHETIC SAMPLE. If it does not, you are looking at the wrong file.
2. Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — balance sheet as signal, panel responsibilities, what the public repo omits.
3. Read [docs/RESEARCH.md](docs/RESEARCH.md) — runway arithmetic, bank scorecard intent, the five indices as lenses (not formulas), Thailand SME context, stated limitations.
4. Sketch the same conservation laws on paper for a company *you* own: `Assets = Liabilities + Equity`, `Cash(t+1) = Cash(t) + inflows − outflows`, `Runway = cash / burn`. If the three disagree, that disagreement is the lesson.
5. If you want **runnable** personal/company tooling, clone the sibling **[ikigai-finance](https://github.com/Nonarkara/ikigai-finance)** and follow its local playbook. This engine repo stays a research layer plus the synthetic sample loader. Point either surface at private books with the steps in [Private data](#private-data).

Surface areas documented from the prototype (not implemented in this tree):

| Panel | Purpose |
| --- | --- |
| KPI strip | Cash, burn, runway, revenue, pipeline |
| Balance sheet | Assets vs liabilities + equity |
| Cash flow & runway | Outlook, cash-zero date, planning raise |
| Bank scorecard | Standing, benchmarks, risk flags |
| Finance indices | Five research scores, 0–100 |
| Macro sidebar | SET, USD/THB, gold — context only |

---

## Private data

Real financial data stays private. Committed company figures in this repository are the synthetic sample only: [`samples/synthetic/company-snapshot.json`](samples/synthetic/company-snapshot.json), the matching CSV, and [`samples/synthetic/dashboard-overview.png`](samples/synthetic/dashboard-overview.png).

`finance_data.load_company_snapshot()` reads `$FINANCE_DATA_DIR/company-snapshot.json` when that variable is set, and the synthetic sample when it is not.

Use a directory outside the clone:

```bash
mkdir -p "$HOME/private/ikigai-finance-data"
# Place your own company-snapshot.json in that directory. Do not commit it.
export FINANCE_DATA_DIR="$HOME/private/ikigai-finance-data"
python3 finance_data.py
```

A checkout-local folder works the same way. `data/private/` is gitignored:

```bash
mkdir -p data/private
export FINANCE_DATA_DIR="$PWD/data/private"
python3 finance_data.py
```

Unset the variable to return to the public sample:

```bash
unset FINANCE_DATA_DIR
python3 finance_data.py
```

`.gitignore` refuses a fresh commit of `data/private/`, `private/`, `fixtures/real/`, `assets/screenshots/`, CSV files other than `samples/synthetic/company-snapshot.csv`, Excel and ODS workbooks, and filenames containing `bank-statement` or `ledger`.

Check the sample and those ignore rules:

```bash
python3 -m unittest tests.test_finance_data -v
```

Regenerate the CSV and the diagram after editing the JSON:

```bash
python3 scripts/render_synthetic_dashboard.py
```

---

## System diagram

Short labels so GitHub’s renderer does not clip. Fuller graph: [`assets/diagrams/system-overview.mmd`](assets/diagrams/system-overview.mmd).

```mermaid
flowchart LR
  files[Files] --> parse[Parse]
  parse --> norm[Normalise]
  bank[Bank] --> card[Scorecard]
  pipe[Pipeline] --> run[Runway]
  norm --> kpi[KPIs]
  norm --> bs[Balance]
  kpi --> idx[Indices]
  bs --> idx
  run --> idx
  card --> idx
  idx --> ui[Dashboard]
```

Source layer (private if you build one): balance sheet, cash flow, bank inputs, pipeline, macro feeds. This public repo stops at the diagram and the labelled synthetic sample. Point a private directory at the loader with [Private data](#private-data).

---

## License / contributing

[MIT](LICENSE). Copyright © 2026 **Non Arkaraprasertkul / Axiom X Co., Ltd.**

MIT covers this repository’s documentation, diagrams, illustration, and the labelled synthetic sample. It does not relicense bank data, SET/FX feeds, or any private implementation that is not in this tree. The hero at `docs/hero-banner.jpg` is studio illustration for this README — not a screenshot and not a data product.

Useful contributions: clearer prose, a Thai README pass that stays faithful to these English notes, and mermaid that still fits GitHub. Open a pull request against `main`. Do not add secrets, client figures, source-dataset screenshots, fake live URLs, or application code that would imply this research repo is the production engine. The synthetic sample is the only company fixture that belongs here.

If you build your own operator surface from this method, the studio would like to see it.
