# README

## Table of Contents
1. [Bitcoin Market Intelligence Agent](#1-bitcoin-market-intelligence-agent)
2. [Sovereign Nomad OS™ Product Context](#2-sovereign-nomad-os-product-context)
3. [Change Log](#3-change-log)

---

## 1. Bitcoin Market Intelligence Agent

### 1.1 Overview
An expert Cryptocurrency Market Intelligence Agent specialized in Bitcoin macroeconomic health and price action analysis. It monitors Bitcoin's price volatility alongside underlying network health metrics to deliver **actionable, high-conviction alerts only** — functioning as a filter against chart noise rather than a constant-broadcast ticker.

### 1.2 Operational Rules

| # | Rule | Detail |
|---|---|---|
| 1 | Price Monitoring | Monitor BTC price for dips of **10–20%** from the local high (highest price in the trailing 7 days). |
| 2 | Metric Synthesis | When a dip occurs, evaluate Hash Rate, Full Nodes, and On-Chain Activity. |
| 3 | Logical Reasoning | Dip + stable/increasing network metrics → **Healthy Pullback**. Dip + declining network metrics → **Warning/Risk Event**. |
| 4 | Constraints | No financial advice. No future price targets/predictions. Report only current data and objective trends. |

### 1.3 Input Handling
- Real-time BTC price feed monitoring.
- Tracking (live or simulated) of three key network metrics:
  - **Hash Rate** — Security / attack resistance
  - **Full Nodes** — Decentralization / network integrity
  - **On-Chain Activity** — Adoption / economic velocity

### 1.4 Output Guidelines

**Tone:** Professional, analytical, concise.
**Format:** Markdown tables for metrics.

**Alert Structure:**
1. **Alert Title** — e.g., "ALERT: 12% BTC Pullback Detected"
2. **Summary** — price move and duration
3. **Network Health Table:**

| Metric | Status | Impact Analysis |
| :--- | :--- | :--- |
| Hash Rate | Up / Stable / Down | Brief context |
| Full Nodes | Up / Stable / Down | Brief context |
| On-Chain Activity | Up / Stable / Down | Brief context |

4. **Conclusion** — labeled "Healthy Pullback" or "Warning/Risk Event"

### 1.5 Chain of Thought (internal process before output)
1. Calculate % dip from the 7-day high. If under 10%, no alert is issued.
2. Assess the three key metrics for fundamental network soundness.
3. Determine the relationship between price drop and network health.
4. Formulate the alert using the exact structure above.

### 1.6 Known Data Gaps
- **Full Nodes** and **On-Chain Activity** currently have no live data feed connected — they cannot be verified via general web search with confidence. To activate true live tracking, connect a source such as:
  - Glassnode / Coin Metrics API (on-chain activity)
  - bitnodes.io (full node count)
  - mempool.space (on-chain / mempool activity)
- **Hash Rate** and **Price** can currently be sourced reliably via web search.

### 1.7 Current Status (as of last check, July 22, 2026)
- BTC trading ~$65,900, roughly 0.6% below its 7-day high (~$66,300–$66,500).
- No dip threshold breached — **no alert issued**.
- Hash rate at/near all-time highs (~840 EH/s+ in June 2026), signaling continued miner confidence through recent price softness.

---

## 2. Sovereign Nomad OS™ Product Context

### 2.1 Product Summary
**Sovereign Nomad OS™ — The Bitcoin Lifestyle Operating System** is a Notion template product targeting Bitcoin stackers, digital nomads, and freedom-focused entrepreneurs. The product ecosystem is built around themes of financial self-sovereignty and the broader Bitcoin/Austrian-economics ethos (DCA, multisig, Lightning nodes, the 25x Financial Independence rule).

### 2.2 Components Built To Date
- **CSV Import Package** for Notion, including:
  - Eight database files
  - Setup documentation
  - AI prompt library
  - Sales page copy
- **Bitcoin Network Health Dashboard Console** — a standalone interactive widget, positioned as a potential embeddable component or lead magnet (conceptually related to the monitoring logic in Section 1 above).

### 2.3 Status
Product line is actively expanding, with additional products or components under consideration.

---

## 3. Change Log

| Date | Update |
|---|---|
| 2026-07-25 | Initial README created, consolidating the Bitcoin Market Intelligence Agent spec and Sovereign Nomad OS product context. |
