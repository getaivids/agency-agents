# OmniRoster Knowledge Base

**Purpose**: Vector database source documents for grounding agents in canonical music business knowledge.

All agents MUST query these sources for decision-making. RAG (Retrieval-Augmented Generation) ensures agents cite specific terms, contract clauses, and financial frameworks from authoritative texts.

---

## 📚 Source Documents

### 1. Music Business: Key Concepts
**File**: `sources/music-business-key-concepts.md`
**Chunking Strategy**: By term (A-Z) with cross-references
**Agents That Query**: Rights Guardian, Deal Maker, Career Architect

#### Indexed Terms:
- **Mechanical Royalty**: Payment to songwriters/publishers for reproduction rights (physical/digital)
- **Performance Rights**: PRO (ASCAP/BMI/SESAC) collection for public performances
- **SoundExchange**: Non-interactive digital performance royalties (label + artist split)
- **Cross-Collateralization**: Contract clause allowing losses in one area to recoup from another ⚠️
- **Recoupable**: Expenses label/manager can recover before paying artist
- **ISRC**: International Standard Recording Code (unique track identifier)
- **ISWC**: International Standard Musical Work Code (composition identifier)
- **360 Deal**: Contract taking % of touring, merch, endorsements (not just recordings) ⚠️
- **Advance**: Upfront payment recoupable from future royalties
- **Net Profit vs. Gross**: Critical distinction for booking deals

---

### 2. Artist Management for Music Business
**File**: `sources/artist-management-chapters.md`
**Chunking Strategy**: By chapter + case studies, extract checklists
**Agents That Query**: Career Architect, Road Captain, Deal Maker

#### Chapter Summaries:
- **Ch. 1: Four Functions of Management** (Paul Allen): Planning, Organizing, Directing, Controlling
- **Ch. 7: Contract Law**: Red flags, negotiation tactics, fiduciary duty
- **Ch. 10: Touring**: Booking strategies, routing, promoter relationships
- **Ch. 11: Analytics**: Spotify for Artists, Chartmetric, data-driven decisions

---

### 3. DJ Business Plan
**File**: `sources/dj-business-plan.md`
**Chunking Strategy**: By section (Financial, Marketing, Ops), extract templates
**Agents That Query**: Hype Engine, Road Captain, Rights Guardian

#### Sections:
- **Financial Model**: Income streams (Live 60%, Publishing 25%, Recording 15%), target margins (>30% net per gig)
- **Marketing Strategies**: Social media, email lists, content calendars, referral programs
- **Operations Plan**: Equipment inventory, staffing, operational processes, redundancy requirements
- **Services Offered**: DJ performances, production, consulting, teaching

---

## 🔍 RAG Implementation Rules

### Critical Citation Requirements:
1. **Deal Maker** negotiating contracts MUST cite *Artist Management Ch. 7* for:
   - Commission caps (max 20% for personal management)
   - Exclusivity periods (max 6 months without approval)
   - Cross-collateralization warnings

2. **Rights Guardian** registering works MUST reference *Music Business PDF* for:
   - PRO registration deadlines (within 48hrs of release)
   - ISRC assignment rules (one per recording version)
   - Writer/publisher split defaults (50/50 unless specified)

3. **Hype Engine** planning campaigns MUST use *DJ Business Plan* for:
   - Pricing tiers (club shows vs. festivals vs. private events)
   - Marketing budget allocation (70% paid ads, 20% content, 10% PR)
   - ROAS targets (>3:1 for Meta ads, >2:1 for TikTok)

4. **Road Captain** verifying logistics MUST check *DJ Business Plan: Operations* for:
   - Power requirements (dedicated 20A circuit for DJ gear)
   - Load-in timelines (minimum 2hrs before doors)
   - Gear redundancy (20% backup on critical items)

5. **Career Architect** making decisions MUST apply *Artist Management Ch. 1* for:
   - Stamina constraints (max 3 gigs/week, 48hr recovery between flights)
   - Strategic prioritization (say no to low-margin opportunities)
   - Stakeholder alignment (weekly briefings, quarterly roadmap reviews)

---

## 🗄️ Vector Database Schema

```json
{
  "collection_name": "omniroster_knowledge",
  "chunk_size": 512,
  "chunk_overlap": 50,
  "metadata_fields": [
    "source_document",
    "chapter_or_term",
    "page_number",
    "agents_authorized",
    "citation_format"
  ]
}
```

### Example Chunk Entry:
```json
{
  "id": "mb_001_cross_collateralization",
  "content": "Cross-collateralization is a contract clause that allows the label or manager to recoup losses from one revenue stream (e.g., unrecouped album advance) against earnings from completely different streams (e.g., touring, merchandise, publishing). This is extremely dangerous for artists and should be resisted or severely limited.",
  "metadata": {
    "source": "Music Business: Key Concepts",
    "term": "Cross-Collateralization",
    "warning_level": "CRITICAL",
    "agents_authorized": ["Deal Maker", "Rights Guardian", "Career Architect"],
    "citation": "Music Biz PDF, Term: Cross-Collateralization"
  }
}
```

---

## 🧪 Testing RAG Integration

Before deploying agents, verify they correctly retrieve and cite knowledge:

1. **Citation Accuracy Test**: Ask Deal Maker to review a contract clause. Response MUST include citation like: *"Per Artist Management Ch. 7, exclusivity clauses exceeding 6 months require explicit artist approval."*

2. **Term Definition Test**: Ask Rights Guardian about ISRC registration. Response MUST define ISRC and cite *Music Business PDF*.

3. **Framework Application Test**: Ask Hype Engine for marketing budget. Response MUST use DJ Business Plan's 70/20/10 allocation model.

**Failure Condition**: Agent provides generic advice without citing canonical sources → REJECT deployment.

---

## 📥 How to Add New Sources

1. Create markdown file in `/knowledge-base/sources/`
2. Structure with clear headers for chunking
3. Update this README with source metadata
4. Run vector embedding script: `python scripts/embed-knowledge.py`
5. Verify chunks in `/knowledge-base/chunks/`

---

## 🚀 Embedding Script (Future Implementation)

```python
# scripts/embed-knowledge.py
# Placeholder for RAG pipeline implementation
# Will use: LangChain + Pinecone/Weaviate + OpenAI embeddings

import os
from langchain.text_splitter import MarkdownTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

def embed_document(source_file):
    """Chunk and embed a knowledge base document."""
    pass  # Implementation pending Phase 5 deployment
```

---

**Status**: Phase 5 - Knowledge Base Integration IN PROGRESS
**Next Steps**: 
1. Populate source documents with full text from PDFs
2. Implement embedding pipeline
3. Test RAG queries with all 6 core agents
4. Validate citation accuracy
