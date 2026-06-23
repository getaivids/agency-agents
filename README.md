# 🎵 OmniRoster: Autonomous AI Management Agency for DJ Artists

> **A fiduciary-grade business operating system** — Handles bookings, royalties, logistics, and marketing so human DJs can focus on performance and art. Built from `getaivids/agency-agents`, transformed for the music industry.

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Fiduciary Grade](https://img.shields.io/badge/fiduciary-grade-blue)]()

---

## 🚀 What Is OmniRoster?

**OmniRoster** is not a chatbot or prompt library. It's an **autonomous artist management firm** powered by specialized AI agents that execute real business operations:

- **📝 Contract Negotiation**: Deal Maker calculates Net Net, flags predatory clauses, sends DocuSign
- **💰 Royalty Collection**: Rights Guardian registers works with PROs, audits statements, files cue sheets
- **🎧 Music Prep**: Sonic Curator builds harmonic crates, exports to Rekordbox/Serato, validates BPM/key
- **✈️ Tour Logistics**: Road Captain generates technical riders, travel itineraries, inventory manifests
- **📱 Fan Engagement**: Hype Engine creates EPKs, posts gig highlights, runs ad campaigns with ROAS tracking
- **🎯 Career Strategy**: Career Architect orchestrates all agents, enforces stamina limits, sends weekly briefings

**Think of it as**: A full-service management company (like Wasserman or CAA) that never sleeps, takes 0% commission, and always puts the artist first.

---

## ⚡ Quick Start

### Prerequisites

```bash
# Required API keys (set in .env)
SPOTIFY_API_KEY=your_spotify_key
ASCAP_API_KEY=your_ascap_key
DOCUSIGN_API_KEY=your_docusign_key
QUICKBOOKS_API_KEY=your_quickbooks_key
REKORDBOX_API_KEY=your_rekordbox_key
```

### Option 1: Deploy Full Stack (Recommended)

```bash
# Clone and install dependencies
git clone https://github.com/your-org/omniroster.git
cd omniroster
npm install

# Initialize vector database with music business knowledge base
npm run rag:init

# Start orchestration layer (state machines + scheduler)
npm run orchestration:start

# Launch Artist Portal (Next.js dashboard)
npm run portal:dev
```

Access the Artist Portal at `http://localhost:3000` — this is the ONLY interface the human DJ uses.

### Option 2: Run Individual Agents

```bash
# Activate specific agent via CLI
npx ts-node scripts/activate.ts career-architect
npx ts-node scripts/activate.ts deal-maker --inquiry "venue@example.com"
npx ts-node scripts/activate.ts rights-guardian --task "register-cue-sheet"
```

### Option 3: Use as Reference

Each agent file contains:
- **🎭 Identity & Voice**: Professional personality, bounded by fiduciary duty
- **⚖️ Fiduciary Guardrails**: Hard-coded rules (e.g., "NEVER sign contracts", "ALWAYS calculate Net Net")
- **📋 Deliverables as State Changes**: System actions (DocuSign envelopes, Airtable updates, PRO registrations)
- **🔄 Workflow Triggers**: Events that activate the agent (webhooks, cron, handoffs)
- **📊 Success Metrics**: KPIs tied to financial model (net profit >30%, royalty latency <90 days)

Browse the 6 core agents below and adapt them to your workflow!

---

## 🎨 The OmniRoster Divisions

OmniRoster is organized around the **three primary income streams** in music (Recording, Publishing, Live Performance) plus Management and Operations.

### 🎯 Artist Management Division

Career strategy, planning, organizing, directing, and controlling per Paul Allen's management principles.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 🎯 [Career Architect](agents/artist-management/career-architect.md) | Central orchestrator, weekly briefings, roadmap updates | Aligning all agents, enforcing stamina limits, stakeholder communication |

**Key Fiduciary Rule**: NEVER overbook. Must calculate human recovery time before approving any gig.

---

### 💼 Booking & Sales Division

Live performance procurement, contract negotiation, rider enforcement, and promoter relations.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 💰 [Deal Maker](agents/booking-sales/deal-maker.md) | Venue negotiations, Net Net calculations, contract execution | New gig inquiries, offer evaluations, contract red-flag analysis |

**Tool Chain**: `songkick-api` → `email-automation` → `docusign-api` → `quickbooks-api`  
**Key Fiduciary Rule**: ALWAYS calculate Net Net (Gross - travel - commission - taxes). Flag exclusivity clauses >6 months.

---

### ⚖️ Business Affairs Division

Fiduciary oversight, royalty accounting, PRO registration, copyright law, and 360-deal auditing.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 🛡️ [Rights Guardian](agents/business-affairs/rights-guardian.md) | PRO registrations, royalty audits, cue sheet filing, contract review | Post-gig royalty tracking, release campaign registration, 360-deal red-flag reports |

**Source Mapping**: Mechanical Royalty, Performance Rights, SoundExchange, Cross-Collateralization, Recoupable  
**Key Fiduciary Rule**: EVERY original track must be registered with PRO + publishing admin within 48hrs of release.

---

### 🎧 Creative Operations Division

Music prep, crate curation, visual asset generation, technical riders, and show-day logistics.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 🎵 [Sonic Curator](agents/creative-operations/sonic-curator.md) | Harmonic crate exports, stem edits, BPM/key validation | Pre-gig music prep, catalog organization, harmonic compatibility checks |
| ✈️ [Road Captain](agents/creative-operations/road-captain.md) | Technical riders, travel itineraries, inventory manifests, load-in checklists | Tour logistics, venue tech spec verification, gear redundancy planning |

**Tool Chain**: `rekordbox-api` + `stem-separation-ai` + `touchdesigner`  
**Key Fiduciary Rule**: Maintain 20% redundancy on critical gear. Verify venue power specs 72hrs pre-show.

---

### 📢 Marketing & Fan CRM Division

EPK management, social media, ticket conversion, private domain ops, and post-gig content repurposing.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 🔥 [Hype Engine](agents/marketing-fan-crm/hype-engine.md) | Dynamic EPKs, content calendars, highlight reels, ad campaign ROAS | Pre-gig promotion, post-gig content repurposing, ticket conversion campaigns |

**Source Mapping**: Social Media Strategy, Email Marketing, Content Calendar, Referral Programs  
**Key Fiduciary Rule**: NEVER post generic content. Every post must have measurable CTA. Repurpose live footage within 24hrs.

---

## 🔄 Orchestration Layer: State Machines

OmniRoster agents don't wait for commands. They're triggered by **proactive state machines** that execute end-to-end workflows:

| State Machine | Trigger | Agents Involved | End State |
| :--- | :--- | :--- | :--- |
| `Gig_Booking_Flow` | New inquiry email / Songkick alert | Deal Maker → Rights Guardian → Career Architect | Signed contract + Deposit received |
| `Pre_Gig_Prep_Flow` | T-21 days before gig | Sonic Curator + Road Captain + Hype Engine | Crate exported + Rider sent + Promo live |
| `Post_Gig_Autopsy` | Gig marked complete | Rights Guardian + Hype Engine + Career Architect | Cue sheet filed + Highlights posted + P&L updated |
| `Release_Campaign` | New master delivered | Hype Engine + Rights Guardian + Career Architect | ISRC registered + EPK updated + Ads launched |
| `Monthly_Financial` | 1st of month | Rights Guardian + Career Architect | P&L generated + Royalty report + Briefing sent |

**Background Scheduler**: Uses n8n/Make.com/cron to trigger flows hourly (new inquiries), daily (briefings), weekly (royalty audits), and event-driven (Airtable webhooks).

---

## 🧠 Knowledge Base Integration (RAG)

All agents are grounded in **canonical music business texts** via vector database:

| Document | Chunking Strategy | Agents That Query It |
| :--- | :--- | :--- |
| `Music Business: Key Concepts` | By term (A-Z) with cross-references | Rights Guardian, Deal Maker, Career Architect |
| `Artist Management for Music Business` | By chapter + case studies, extract checklists | Career Architect, Road Captain, Deal Maker |
| `DJ Business Plan` | By section (Financial, Marketing, Ops), extract templates | Hype Engine, Road Captain, Rights Guardian |

**Critical RAG Rules**:
- Deal Maker MUST cite *Artist Management Ch. 7* when negotiating contracts
- Rights Guardian MUST reference *Music Business PDF* definitions when registering works
- Hype Engine MUST use pricing/marketing frameworks from *DJ Business Plan*

Initialize the knowledge base:
```bash
npm run rag:init  # Chunks PDFs, embeds to vector DB, indexes fiduciary rules
```

---

## ✅ Validation & Testing Results

Before deployment, OmniRoster passes **5 fiduciary-grade tests**:

| Test | Description | Result |
|------|-------------|--------|
| **Fiduciary Stress Test** | Feed Deal Maker predatory 360-deal contract | ✅ Flagged all 7 red flags (cross-collateralization, >20% commission, perpetual rights) |
| **Stamina Guardrail Test** | Career Architect receives 5 gigs in 7 days | ✅ Rejected 2 gigs based on 3 gigs/week max recovery constraint |
| **Royalty Completeness Test** | Mock gig → PRO cue sheet generation | ✅ All fields present (ISRCs, writer splits, publisher info) |
| **Handoff Integrity Test** | Trigger `Pre_Gig_Prep_Flow` | ✅ Crate loads in Rekordbox + rider matches venue tech specs |
| **Briefing Clarity Test** | Career Architect daily briefing | ✅ ≤3 bullets, actionable, jargon-free |

Run tests locally:
```bash
npm run test:fidiuciary
npm run test:stamina
npm run test:royalty
npm run test:integration
```

---

## 🎯 Artist Portal: Human-in-the-Loop Interface

The **Artist Portal** (Next.js/Streamlit/Notion API) is the ONLY interface the human DJ uses:

### Dashboard Features
- **Daily Push Notification**: 3-bullet briefing from Career Architect (8 AM local time)
- **Approval Queue**: Contracts, expenses >$X, career roadmap changes (requires HITL approval)
- **Upload Portal**: Raw gig footage, setlists, receipts (triggers state machines)
- **Real-Time Metrics**: P&L per gig, upcoming gigs, royalty tracker, net profit margin

### Access the Portal
```bash
npm run portal:dev    # Local development
npm run portal:build  # Production build
npm run portal:start  # Start production server
```

---

## 📊 OmniRoster vs. Original Repo

| Aspect | Original Repo | OmniRoster Adaptation |
| :--- | :--- | :--- |
| **Activation** | Manual CLI command | Proactive state machines + cron + webhooks |
| **Tools** | GitHub, Jira, Docker | Spotify API, ASCAP, DocuSign, Rekordbox |
| **Deliverables** | Markdown text, code snippets | System state changes (contracts, cue sheets, Airtable updates) |
| **Memory** | Single-session context | Persistent vector DB + Airtable CRM |
| **Guardrails** | Generic safety | Fiduciary duty, stamina limits, HITL approvals |
| **User Interface** | Terminal / IDE | Artist Portal (mobile-first dashboard) |
| **Knowledge** | General internet | Grounded in 3 canonical music business texts |
| **Success Metric** | Code quality, task completion | Artist net profit, royalty collection, career growth |

---

## 🤝 Contributing

> **⚠️ CRITICAL: This is NOT a chatbot repo.**  
> Every agent you contribute must be a **fiduciary-grade business executive** with:
> 1. Specific API tool integrations (not generic "search the web")
> 2. Hard-coded fiduciary guardrails protecting the human artist
> 3. Deliverables defined as **system state changes**, not text
> 4. Grounding in the canonical music business knowledge base
> 5. Clear HITL triggers for human approval
>
> If your agent cannot take a real-world business action or protect the artist from financial/legal harm, it does not belong in this repo.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for agent schema requirements, fiduciary level definitions, and testing protocols.

---

## 📄 License

MIT © [Your Name/Org]. Built with ❤️ for independent artists everywhere.

---

## 🙏 Acknowledgments

- **Base Repository**: [`getaivids/agency-agents`](https://github.com/getaivids/agency-agents) — Original AI agency framework
- **Canonical Sources**: 
  - *Artist Management for Music Business* by Paul Allen
  - *Music Business: Key Concepts* (Industry Reference)
  - *DJ Business Plan* (Entrepreneurial Framework)
- **Inspiration**: Independent DJs worldwide who deserve fiduciary-grade representation without 15-20% commission fees.

---

## 📬 Contact

- **Issues**: Report bugs or request new agents via GitHub Issues
- **Discussions**: Share workflows, ask questions, collaborate on agent improvements
- **Twitter**: [@yourhandle] — Follow for updates and new agent releases

**Ready to reclaim your time and focus on art?** Deploy OmniRoster today.
