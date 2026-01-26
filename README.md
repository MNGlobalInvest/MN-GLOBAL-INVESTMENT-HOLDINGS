# MN Global Investment Holdings, LLC  
## Sovereign Autonomous Accumulation Protocol (SAAP)

---

## Protocol Overview

MN Global Investment Holdings, LLC is a programmatic wealth-capture entity engineered as a Sovereign Autonomous Accumulation Protocol (SAAP). The organization is designed to function as a closed-loop system that ingests global service revenue and anchors it into the Bitcoin network through immutable, self-executing logic.

By integrating the legal protections of a Minnesota domestic limited liability company with the deterministic execution of blockchain protocols, MN Global eliminates discretionary risk and prioritizes the continuous growth of Bitcoin-denominated protocol equity.

---

## Legal Framework: Minnesota Statute § 322C

MN Global is structured under the Minnesota Revised Uniform Limited Liability Company Act (Chapter 322C). This jurisdiction provides the necessary flexibility to vest management authority in an algorithmically-driven operating agreement.

**Governance Model:** Manager-Managed (via Protocol)  
**Statutory Basis:** Pursuant to MN Stat. § 322C.0407 and § 322C.0117, the company recognizes the MN-Global Accumulator Protocol as the sole managing authority.

**Operating Agreement:**  
The legal charter hard-codes a 70/30 diversion mandate, ensuring that 70% of gross revenue is programmatically converted to Bitcoin, while 30% is allocated to an operational buffer for state compliance and infrastructure maintenance.

---

## Technical Architecture

The protocol is deployed across a distributed architecture utilizing the Oracle Cloud “Always Free” tier, ensuring 24/7 uptime with zero infrastructure overhead.

### 1. Ingress Layer (The Sentry)

The Sentry cluster acts as the monetary gateway. It utilizes a self-hosted BTCPayServer integrated with Bitcoin Core and LND. This layer monitors the mempool for incoming service fees and provides the cryptographic truth required to trigger the next phase of the protocol.

### 2. Logic Layer (The Governor)

The Governor cluster executes the Accumulator Hook. This Python-based engine intercepts payment webhooks and triggers automated market-buy orders. It ensures the 70/30 Invariant Rule is met without human intervention.

### 3. Settlement Layer (The Fortress)

The Fortress is the final destination for all captured value. It utilizes a 3-of-5 multi-signature security model and Bitcoin-native time-locks.

---

## The Accumulator Hook Logic

The fundamental directive of the protocol is defined by the following accumulation formula:

```math
V_{vault} = \sum_{i=1}^{n} \left( \frac{R_i \times 0.70}{P_{BTC,i}} \right) + Y_{total}
Where:

V_{vault} is the total volume of Bitcoin in the protocol vault.

R_i is the gross revenue of the i-th transaction.

P_{BTC,i} is the spot price of Bitcoin at the moment of execution.

Y_{total} is the cumulative yield generated from network participation (e.g., Lightning routing fees).

Security and Custody
Multi-Signature Quorum:
A 3-of-5 configuration involving a Founder key, a Minnesota Trustee key, and a Protocol Autonomous key.

Time-Lock Mechanism:
Utilizing Bitcoin’s OP_CHECKLOCKTIMEVERIFY (CLTV), 80% of accumulated assets are unspendable until the April 2028 Halving. This protects the protocol from short-term market volatility and unauthorized withdrawals.

Network Sovereignty:
The protocol operates its own full node, ensuring all transactions are verified independently of third-party service providers.

Operational Service Modules
MN Global fuels its accumulation engine through specialized enterprise service lines:

Infrastructure Hosting: Managing high-availability Bitcoin and Lightning nodes for commercial partners.

Protocol Licensing: Providing the SAAP framework to entities seeking autonomous treasury solutions.

Strategic Architecture: Designing self-sovereign financial systems for institutional adoption.

Deployment Roadmap
Infrastructure Initialization: Provisioning of ARM-based cloud instances and synchronization of the Bitcoin ledger.

Logic Integration: Deployment of the Accumulator Hook and secure API bridging to decentralized liquidity pools.

Legal Anchor: Filing of the Minnesota DAO Operating Agreement and administrative handover to the protocol.

Autonomous Operation: Renunciation of management keys and transition to a fully automated state.

Disclaimer
MN Global Investment Holdings, LLC is an autonomous protocol. The information contained in this profile is for architectural and technical documentation purposes only. Participation in the protocol assumes an understanding of the inherent risks associated with blockchain-based assets and autonomous software execution.
