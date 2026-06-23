# OmniRoster Validation & Testing Protocol

**Purpose**: Comprehensive testing framework for validating agent behavior against fiduciary standards, workflow integrity, and knowledge base grounding.

**Status**: Phase 6 - READY FOR EXECUTION

---

## 🧪 Test Categories

### 1. Fiduciary Stress Tests
### 2. Stamina Guardrail Tests
### 3. Royalty Completeness Tests
### 4. Handoff Integrity Tests
### 5. Briefing Clarity Tests
### 6. RAG Citation Accuracy Tests

---

## Test 1: Fiduciary Stress Test (Deal Maker)

**Objective**: Verify Deal Maker correctly identifies and flags predatory contract terms.

**Test Fixture**: `/workspace/testing/fixtures/predatory-360-deal.json`

**Test Input**:
```json
{
  "contract_type": "360 Deal",
  "commission_rate": 0.25,
  "exclusivity_months": 12,
  "cross_collateralization": true,
  "perpetual_rights": true,
  "merch_cut": 0.30,
  "touring_cut": 0.20,
  "publishing_cut": 0.25
}
```

**Expected Behavior**:
- ✅ Flag commission >20% as CRITICAL (requires HITL approval)
- ✅ Flag exclusivity >6 months as CRITICAL (requires HITL approval)
- ✅ Flag cross-collateralization as CRITICAL (cite Music Business PDF)
- ✅ Flag perpetual rights as UNACCEPTABLE (cite Artist Mgmt Ch. 7)
- ✅ Flag merch/touring cuts without services as PREDATORY (360 deal warning)
- ✅ Calculate Net Net showing artist receives <40% of gross
- ✅ REJECT contract by default, require Career Architect + artist approval

**Failure Conditions**:
- ❌ Contract approved without red flag annotations → **CRITICAL FAIL**
- ❌ No citation to canonical sources → **FAIL**
- ❌ Net Net not calculated → **FAIL**
- ❌ HITL triggers not activated → **FAIL**

**Run Command**: `python testing/scripts/test-fiduciary-stress.py`

---

## Test 2: Stamina Guardrail Test (Career Architect)

**Objective**: Verify Career Architect enforces human stamina constraints and prevents overbooking.

**Test Fixture**: `/workspace/testing/fixtures/five-gigs-seven-days.json`

**Test Input**:
```json
{
  "gig_offers": [
    {"date": "2024-07-01", "city": "New York", "gross": 5000},
    {"date": "2024-07-02", "city": "Boston", "gross": 4000},
    {"date": "2024-07-03", "city": "Philadelphia", "gross": 4500},
    {"date": "2024-07-04", "city": "Washington DC", "gross": 6000},
    {"date": "2024-07-05", "city": "Miami", "gross": 8000}
  ],
  "artist_recovery_time_hours": 48,
  "max_gigs_per_week": 3
}
```

**Expected Behavior**:
- ✅ Accept max 3 gigs in 7-day window
- ✅ Enforce 48-hour recovery between flights (>500 miles)
- ✅ Reject or reschedule gigs 4 and 5
- ✅ Cite *Artist Management Ch. 1* for stamina constraints
- ✅ Provide alternative dates for rejected gigs
- ✅ Calculate cumulative travel fatigue score

**Failure Conditions**:
- ❌ All 5 gigs booked → **CRITICAL FAIL** (artist burnout risk)
- ❌ No 48hr recovery enforced between flights → **FAIL**
- ❌ No citation to stamina guidelines → **FAIL**

**Run Command**: `python testing/scripts/test-stamina-guardrails.py`

---

## Test 3: Royalty Completeness Test (Rights Guardian)

**Objective**: Verify Rights Guardian generates complete PRO cue sheets with all required fields.

**Test Fixture**: `/workspace/testing/fixtures/mock-gig-setlist.json`

**Test Input**:
```json
{
  "gig_id": "GIG-2024-07-15-CLUB-BERLIN",
  "venue": "Club Berlin, Los Angeles",
  "performance_date": "2024-07-15T22:00:00Z",
  "setlist": [
    {"title": "Midnight Dreams", "artist": "Original", "duration_sec": 245, "isrc": "US-S1Z-24-00001"},
    {"title": "Electric Soul", "artist": "Original", "duration_sec": 312, "isrc": "US-S1Z-24-00002"},
    {"title": "One More Time", "artist": "Daft Punk", "duration_sec": 231, "isrc": "GBDUW0000059"}
  ],
  "writer_splits": {
    "Midnight Dreams": {"writer": 0.50, "publisher": 0.50},
    "Electric Soul": {"writer": 0.50, "publisher": 0.50}
  }
}
```

**Expected Behavior**:
- ✅ Generate PRO cue sheet within 48hrs of gig completion
- ✅ Include ALL required fields: title, writer(s), publisher(s), ISWC, ISRC, duration, usage type
- ✅ Register original tracks with ASCAP/BMI API (mock call)
- ✅ Register with SoundExchange for non-interactive royalties
- ✅ Log expected royalty amounts in Airtable `Royalties` table
- ✅ Cite *Music Business PDF* for registration deadlines

**Failure Conditions**:
- ❌ Cue sheet missing ISRC or ISWC → **FAIL**
- ❌ Cue sheet not filed within 48hrs → **FAIL**
- ❌ Original tracks not registered with PRO → **CRITICAL FAIL**
- ❌ SoundExchange registration skipped → **FAIL**

**Run Command**: `python testing/scripts/test-royalty-completeness.py`

---

## Test 4: Handoff Integrity Test (Pre_Gig_Prep_Flow)

**Objective**: Verify seamless handoff between Sonic Curator, Road Captain, and Hype Engine.

**Test Fixture**: `/workspace/testing/fixtures/pre-gig-prep-input.json`

**Test Input**:
```json
{
  "gig_id": "GIG-2024-08-20-FESTIVAL-MAIN",
  "gig_date": "2024-08-20",
  "venue_type": "Festival",
  "expected_crowd_size": 5000,
  "set_length_minutes": 90,
  "travel_required": true,
  "origin_city": "Los Angeles",
  "destination_city": "Las Vegas"
}
```

**Expected Outputs**:

### Sonic Curator Deliverables:
- ✅ Rekordbox crate exported with harmonic matching (Camelot wheel verified)
- ✅ Backup crate prepared
- ✅ 3-5 stem edits for transition tracks
- ✅ TouchDesigner visual timeline JSON synced to track structure

### Road Captain Deliverables:
- ✅ Travel itinerary booked (no layovers <2hrs)
- ✅ Technical rider sent via DocuSign
- ✅ Venue power specs verified (dedicated 20A circuit confirmed)
- ✅ Load-in time confirmed (minimum 2hrs before doors)

### Hype Engine Deliverables:
- ✅ 21-day content calendar created
- ✅ Geo-targeted ad campaigns launched (Meta + TikTok)
- ✅ Email blast to Las Vegas fan segment sent

**Convergence Check**:
- ✅ All three agents mark tasks complete in Airtable
- ✅ Career Architect verifies all deliverables present
- ✅ State machine transitions to `READY_FOR_SHOW`

**Failure Conditions**:
- ❌ Crate export format incompatible with Rekordbox → **FAIL**
- ❌ Rider doesn't match venue's actual capabilities → **FAIL**
- ❌ Ad ROAS <2:1 after 48hrs without adjustment → **FAIL**
- ❌ Any deliverable missing at T-7 days → **FAIL**

**Run Command**: `python testing/scripts/test-handoff-integrity.py`

---

## Test 5: Briefing Clarity Test (Career Architect)

**Objective**: Verify Career Architect's daily briefing is actionable, concise, and jargon-free.

**Test Fixture**: `/workspace/testing/fixtures/weekly-briefing-context.json`

**Test Input**:
```json
{
  "current_date": "2024-07-01",
  "active_gigs": 3,
  "pending_contracts": 2,
  "upcoming_releases": 1,
  "financial_status": {
    "monthly_revenue": 45000,
    "monthly_expenses": 28000,
    "net_margin": 0.38
  },
  "urgent_items": [
    "Contract approval needed for Miami gig (red flag: exclusivity clause)",
    "Deposit not received for Chicago show (T-10 days)",
    "New single trending on TikTok (ROAS 4.2:1)"
  ]
}
```

**Expected Output Format**:
```markdown
## Weekly Briefing (July 1-7, 2024)

### 🎯 Action Required (3 items max)
1. **Approve Miami contract** - Exclusivity clause flagged (6 months). [Review in Portal]
2. **Follow up on Chicago deposit** - $2,500 outstanding, due T-7 days. [Auto-email sent]
3. **Amplify TikTok trend** - New single at 4.2:1 ROAS. Recommend $500 ad boost. [Approve budget]

### 📊 Key Metrics
- Net margin: 38% (target: >30%) ✅
- Gigs this month: 8 (on track)
- Royalty collection latency: 67 days (target: <90 days) ✅

### 🚀 Next Milestone
- Single release campaign: Day 14 of 30. On track for 500K streams.
```

**Validation Criteria**:
- ✅ ≤3 bullets in "Action Required" section
- ✅ Each bullet has clear CTA (call-to-action)
- ✅ No jargon without explanation
- ✅ All metrics include target comparison
- ✅ Readable in <60 seconds

**Failure Conditions**:
- ❌ >3 action items → **FAIL** (cognitive overload)
- ❌ Any bullet requires follow-up questions → **FAIL** (not actionable)
- ❌ Jargon without definition (e.g., "ROAS" without context) → **FAIL**
- ❌ Takes >60 seconds to read → **FAIL**

**Run Command**: `python testing/scripts/test-briefing-clarity.py`

---

## Test 6: RAG Citation Accuracy Test (All Agents)

**Objective**: Verify agents correctly retrieve and cite canonical knowledge base sources.

**Test Scenarios**:

### Scenario A: Deal Maker Contract Review
**Query**: "Review this exclusivity clause: 'Artist grants exclusive representation rights for 18 months globally.'"

**Expected Response**:
> ⚠️ **RED FLAG**: Exclusivity period (18 months) exceeds recommended maximum of 6 months per *Artist Management Ch. 7*. Requires explicit artist approval via HITL portal. Geographic scope ("globally") should be narrowed to specific territories where manager provides services.

**Validation**:
- ✅ Cites *Artist Management Ch. 7*
- ✅ Identifies 6-month threshold
- ✅ Triggers HITL approval requirement
- ✅ Suggests negotiation tactic (territory limitation)

### Scenario B: Rights Guardian ISRC Query
**Query**: "Do I need separate ISRCs for the original mix and extended mix of the same track?"

**Expected Response**:
> Yes. Per *Music Business PDF*, each distinct recording version requires a unique ISRC. This includes:
> - Original mix
> - Extended mix
> - Radio edit
> - Remix versions
> 
> One ISRC per recording ensures accurate royalty tracking across all versions.

**Validation**:
- ✅ Cites *Music Business PDF*
- ✅ Correctly identifies ISRC assignment rules
- ✅ Lists all version types requiring separate ISRCs

### Scenario C: Hype Engine Marketing Budget
**Query**: "What's the recommended marketing budget allocation for a new single release?"

**Expected Response**:
> Per *DJ Business Plan: Marketing Strategies*, allocate budget as follows:
> - **70% Paid Ads**: Meta (Instagram/Facebook) + TikTok geo-targeted campaigns
> - **20% Content Production**: Highlight reels, visualizers, behind-the-scenes
> - **10% PR/Influencer Seeding**: Playlist curators, tastemaker blogs
> 
> Target ROAS: >3:1 for Meta ads, >2:1 for TikTok.

**Validation**:
- ✅ Cites *DJ Business Plan*
- ✅ Uses 70/20/10 allocation model
- ✅ Includes ROAS targets

**Failure Conditions**:
- ❌ Generic advice without source citation → **FAIL**
- ❌ Incorrect citation (wrong source/chapter) → **FAIL**
- ❌ Contradicts canonical source → **CRITICAL FAIL**

**Run Command**: `python testing/scripts/test-rag-citations.py`

---

## 📊 Test Execution Dashboard

| Test ID | Test Name | Status | Last Run | Pass Rate |
|---------|-----------|--------|----------|-----------|
| FST-001 | Fiduciary Stress Test | ⏳ Pending | - | - |
| SGT-001 | Stamina Guardrail Test | ⏳ Pending | - | - |
| RCT-001 | Royalty Completeness Test | ⏳ Pending | - | - |
| HIT-001 | Handoff Integrity Test | ⏳ Pending | - | - |
| BCT-001 | Briefing Clarity Test | ⏳ Pending | - | - |
| RAT-001 | RAG Citation Test (Deal Maker) | ⏳ Pending | - | - |
| RAT-002 | RAG Citation Test (Rights Guardian) | ⏳ Pending | - | - |
| RAT-003 | RAG Citation Test (Hype Engine) | ⏳ Pending | - | - |

**Deployment Gate**: All tests must pass with 100% success rate before agent deployment.

---

## 🔧 Running All Tests

```bash
# Run individual test
python testing/scripts/test-fiduciary-stress.py

# Run all tests
./testing/scripts/run-all-tests.sh

# Generate test report
python testing/scripts/generate-report.py --output testing/reports/validation-report.md
```

---

## 📈 Continuous Integration

Tests run automatically on:
- Every pull request to agent files
- Weekly scheduled runs (Sunday 2AM UTC)
- Before any production deployment

**CI Configuration**: `.github/workflows/validation-tests.yml`

---

## 🚨 Failure Response Protocol

If any test fails:

1. **Immediate**: Agent flagged as "UNTESTED" in registry
2. **Notification**: Slack alert to #omniroster-dev channel
3. **Blocker**: Deployment pipeline halted until fix merged
4. **Root Cause**: Document failure in `/testing/reports/failure-analysis/`
5. **Retest**: After fix, re-run full test suite (not just failed test)

---

**Document Version**: 1.0
**Phase**: 6 - Validation & Testing
**Next Update**: After first full test execution cycle
