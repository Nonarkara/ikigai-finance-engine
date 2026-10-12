# Research — Finance indices, SME runway, balance sheet as signal

Educational notes on the concepts behind the Ikigai Finance Engine prototype. No proprietary formulas; approach and references only.

---

## Why "balance sheet as signal"

Most SME founders live in the cash account. Accountants live in the general ledger. Banks live in covenant language. None of these surfaces talk to each other until something breaks.

The balance sheet is the **slowest honest signal** in the system:

- **Assets** — what the company claims to control
- **Liabilities** — what it owes and by when
- **Equity** — the residual; when negative, the structure is telling you something cash alone cannot

Reading balance sheet + cash runway together answers a question cash alone cannot: *Is this a liquidity problem or a solvency problem?* Liquidity problems can be bridged. Solvency problems require structural decisions.

---

## Cash runway — the conservation law

Runway is not mysticism; it is arithmetic:

```
Runway (months) = Cash on hand / Monthly net burn
```

Where **monthly net burn** is outflows minus inflows at the operating level (definitions vary; the prototype uses a consistent internal convention and labels it on screen).

**Cash-zero date** is the calendar projection when cumulative cash crosses zero at current burn — the date the operator must have a decision before, not on.

**Suggested raise** in the prototype is a backward calculation: *how much capital closes the gap to N months of runway?* It is a planning number for conversation, not a fair-market valuation.

### Further reading
- Rauch, J. (2015). *The Startup Owner's Manual* — burn and runway framing for early-stage operators
- Blank, S. & Dorf, B. — customer development vs financial runway tension

---

## Bank scorecard — relationship as data

SMEs in Thailand often maintain 2–3 bank relationships with uneven information symmetry. The scorecard panel compresses:

1. **Credit standing** — ordinal score with narrative label (e.g. moderate-to-low risk)
2. **Benchmark comparison** — operator vs sector median where public benchmarks exist
3. **Risk flags** — explicit callouts (negative equity, overdraft utilisation, covenant proximity)

The traffic-light summary in the public synthetic sample (1 green · 1 amber · 2 red) is deliberately blunt — operators need blunt when time is short. Those lights are invented.

This is **not** a credit rating agency substitute. It is an **internal decision surface** for founders and advisors.

---

## Finance indices — five lenses

The prototype names five indices. Each is a **compressed view** of multiple inputs — similar in spirit to how city indices (livability, resilience) compress multidimensional urban data into arguable scores.

### Ikigai (strategic leverage)
*Working name — references purpose-aligned capital deployment, not the Ikigai life-purpose diagram alone.*

Intent: measure whether financial structure supports stated strategic direction, or whether cash is funding drift (headcount without revenue motion, asset accumulation without utilisation).

Synthetic sample: **20/100 · SAMPLE LOW**

### Lean (operating discipline)
Intent: burn efficiency relative to revenue and pipeline motion. A company can be "lean" in headcount but not in cash if collections lag.

Synthetic sample: **30/100 · SAMPLE WATCH**

### Zero (runway horizon)
Intent: months-to-cash-zero framed as an index rather than a raw decimal. Makes runway comparable across companies of different sizes.

Synthetic sample: **10/100 · SAMPLE SHORT**. A short-horizon band describes the fixture's runway arithmetic, not a forecast.

### Default (default-risk proximity)
Intent: debt service capacity vs available cash and near-term obligations. Proximity to default events, not prediction of default.

Synthetic sample: **20/100 · SAMPLE WATCH**

### Solvency (structural distress)
Intent: equity position, liability structure, asset quality — the slow signals. When solvency reads distress, runway math is urgent in a different way.

Synthetic sample: **10/100 · SAMPLE DISTRESS**

### Approach (not formula)
Indices are composed from **normalised sub-scores** across balance sheet, cash, bank, and pipeline modules. Weights are calibration targets under active research — not published here because they are still being validated against anonymised case studies.

Design rule: every index must state **what it cannot say** alongside what it says. A high Lean score does not mean "investable." A low Default score does not mean "safe forever."

---

## SME context — Thailand

Thai SMEs face a specific bundle:

- **FX exposure** — USD/THB matters for imported inputs and USD-denominated debt
- **SET as mood proxy** — not company-specific, but macro context for investor conversations
- **Bank relationship centrality** — often more decisive than formal equity markets at SME scale
- **Registered capital vs paid-in reality** — balance sheet literacy varies widely

The prototype includes Thai-language chrome (เครื่องมือการเงิน) and baht denomination to reflect actual operator context.

---

## Public sample (synthetic)

The figures below are **invented** for this public tree. They are round, labelled `SYNTHETIC_SAMPLE` in [`../samples/synthetic/company-snapshot.json`](../samples/synthetic/company-snapshot.json), and drawn on [`../samples/synthetic/dashboard-overview.png`](../samples/synthetic/dashboard-overview.png). They are not a client, not a filing, and not a copy of any source-dataset screenshot that used to be in this repository.

**SYNTHETIC SAMPLE Co., Ltd.**

- Registered capital ฿2,000,000, retained earnings ฿-3,000,000, equity ฿-1,000,000
- Assets ฿1,000,000 = liabilities ฿2,000,000 + equity ฿-1,000,000
- Cash ฿100,000 vs burn ฿200,000/mo — runway 0.5 months, so the distress reading still has a shape
- Pipeline ฿4,000,000 vs revenue ฿3,000,000

Real books do not belong in this file. Point the loader at a private directory with `FINANCE_DATA_DIR` (see the README). Do not paste figures back out of git history.

---

## Limitations (stated openly)

| This dashboard tells you | This dashboard does not tell you |
|---------------------------|----------------------------------|
| Runway at current burn | Whether burn will change next quarter |
| Balance sheet structure | Fair market value of intangible assets |
| Bank relationship summary | What a specific bank will decide |
| Composite index direction | Investment recommendation |
| Suggested raise to target runway | Optimal cap table or dilution path |

---

## Not investment advice

All materials in this repository are for **research, education, and interface design documentation**. Consult licensed financial, legal, and tax advisors for decisions affecting real companies.
