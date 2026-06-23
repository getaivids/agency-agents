# OmniRoster State Machine Definitions

**Purpose**: Orchestration layer for proactive agent coordination. These state machines transform individual agents into a cohesive management firm.

**Execution Environment**: n8n, Make.com, or cron-based scheduler with webhook support.

---

## 1. Gig_Booking_Flow

**Trigger**: New inquiry email / Songkick alert / Career Architect manual trigger

**Agents Involved**: Deal Maker → Rights Guardian → Career Architect

**States**:
```
PENDING_INQUIRY (initial)
  ↓ [Deal Maker qualifies lead]
OFFER_RECEIVED
  ↓ [Deal Maker calculates Net Net]
NET_NET_CALCULATED
  ↓ [Rights Guardian reviews contract]
CONTRACT_REVIEWED
  ↓ [IF red_flags = TRUE → Rights Guardian annotates]
RED_FLAGS_FOUND → [Artist HITL approval required]
  ↓ [IF red_flags = FALSE OR artist approves]
CONTRACT_APPROVED
  ↓ [Deal Maker sends DocuSign envelope]
PENDING_SIGNATURE
  ↓ [Promoter + Artist sign]
CONTRACT_SIGNED
  ↓ [Deal Maker creates QuickBooks invoice]
DEPOSIT_INVOICED
  ↓ [Deposit received in QuickBooks]
DEPOSIT_RECEIVED → (terminal state)
  ↓ [Triggers Pre_Gig_Prep_Flow at T-21 days]
```

**State Transitions**:
- `PENDING_INQUIRY` → `OFFER_RECEIVED`: Deal Maker receives promoter inquiry, logs to Airtable `Gigs` table
- `OFFER_RECEIVED` → `NET_NET_CALCULATED`: Deal Maker calculates: `Net Net = Gross - (Travel + Commission + Taxes)`
- `NET_NET_CALCULATED` → `CONTRACT_REVIEWED`: Rights Guardian scans contract for red flags (cross-collateralization, exclusivity >6mo, perpetual rights)
- `CONTRACT_REVIEWED` → `RED_FLAGS_FOUND`: IF critical_flags > 0, annotate PDF, notify Career Architect
- `RED_FLAGS_FOUND` → `CONTRACT_APPROVED`: Artist reviews via HITL portal, approves/rejects/requests changes
- `CONTRACT_APPROVED` → `PENDING_SIGNATURE`: Deal Maker creates DocuSign envelope, sends to artist + promoter
- `PENDING_SIGNATURE` → `CONTRACT_SIGNED`: Both parties sign, DocuSign webhook confirms completion
- `CONTRACT_SIGNED` → `DEPOSIT_INVOICED`: Deal Maker generates QuickBooks invoice for 50% deposit
- `DEPOSIT_INVOICED` → `DEPOSIT_RECEIVED`: QuickBooks webhook confirms payment, Airtable status = "Confirmed"

**End State Actions**:
- Update Airtable `Gigs` table: status = "Confirmed", deposit_received = TRUE
- Career Architect adds gig to master calendar
- Trigger Pre_Gig_Prep_Flow scheduler (T-21 days before gig date)
- Hype Engine notified to begin ticket promotion campaign

**Failure Conditions**:
- Contract rejected by artist → return to `OFFER_RECEIVED` with notes
- Deposit not received within 7 days → Deal Maker sends follow-up, escalate to Career Architect if T+14 days
- Red flags not resolved → terminate flow, log to Airtable `Lost_Opportunities`

---

## 2. Pre_Gig_Prep_Flow

**Trigger**: T-21 days before confirmed gig (cron scheduler)

**Agents Involved**: Sonic Curator + Road Captain + Hype Engine

**States**:
```
PREP_INITIATED (initial)
  ↓ [Parallel execution]
  ├→ SONIC_CRATOR_BUILDING_CRATE
  ├→ ROAD_CAPTAIN_BOOKING_TRAVEL
  └→ HYPE_ENGINE_LAUNCHING_CAMPAIGN
  ↓ [All three complete]
ALL_PREP_COMPLETE
  ↓ [Career Architect verifies]
READY_FOR_SHOW → (terminal state)
```

**Parallel Workflows**:

### Sonic Curator Track:
`PREP_INITIATED` → `CRATE_BUILT` → `STEMS_EXPORTED` → `VISUAL_TIMELINE_READY`
- Analyze venue type, crowd demographic, set length
- Build primary + backup crates with harmonic matching
- Export stems for 3-5 transition tracks
- Create TouchDesigner visual timeline synced to track structure
- Deliverables: `.rekordbox` playlist, `/stems/{gig_id}/`, visual JSON

### Road Captain Track:
`PREP_INITIATED` → `TRAVEL_BOOKED` → `RIDER_SENT` → `LOGISTICS_CONFIRMED`
- Book flights (no layovers <2hrs), hotel, ground transport
- Send technical rider to promoter via DocuSign
- Verify venue power specs 72hrs before show
- Confirm load-in times, sound system compatibility
- Deliverables: Travel itinerary PDF, signed rider, venue spec sheet

### Hype Engine Track:
`PREP_INITIATED` → `CONTENT_CALENDAR_CREATED` → `ADS_LAUNCHED` → `TICKET_CAMPAIGN_ACTIVE`
- Create 21-day content calendar (teasers, countdown, behind-the-scenes)
- Launch geo-targeted ad campaigns (Meta, TikTok)
- Email blast to local fan segment
- Deliverables: Content calendar in Airtable, active ad sets, email campaign sent

**Convergence Point**: `ALL_PREP_COMPLETE`
- All three agents mark tasks complete in Airtable `Gigs` table
- Career Architect receives notification, performs final verification
- IF all checks pass → `READY_FOR_SHOW`
- IF any failures → notify responsible agent, set deadline for resolution

**End State Actions**:
- Update Airtable `Gigs` table: prep_status = "Ready"
- Career Architect pushes briefing to artist: "Gig prep complete. Review itinerary + crate."
- Road Captain carries physical copies of all docs to venue

**Failure Conditions**:
- Crate not exported T-7 days → Sonic Curator escalation to Career Architect
- Travel not booked T-14 days → Road Captain escalation, auto-book backup options
- Ad ROAS <2:1 after 48hrs → Hype Engine pauses campaign, revises targeting

---

## 3. Post_Gig_Autopsy

**Trigger**: Webhook from Airtable when gig status = "Complete"

**Agents Involved**: Rights Guardian + Hype Engine + Career Architect

**States**:
```
GIG_COMPLETED (initial)
  ↓ [Parallel execution]
  ├→ RIGHTS_GUARDIAN_FILING_CUE_SHEET
  ├→ HYPE_ENGINE_POSTING_HIGHLIGHTS
  └→ CAREER_ARCHITECT_UPDATING_PNL
  ↓ [All three complete]
AUTOPSY_COMPLETE
  ↓ [Generate lessons learned]
LESSONS_DOCUMENTED → (terminal state)
```

**Parallel Workflows**:

### Rights Guardian Track:
`GIG_COMPLETED` → `CUE_SHEET_GENERATED` → `PRO_SUBMITTED` → `ROYALTY_TRACKING_STARTED`
- Generate PRO cue sheet with ISRCs, writer splits, publisher info
- Submit to ASCAP/BMI API within 24hrs
- Log expected royalty amount + payment timeline in Airtable `Royalties`
- Deliverables: Cue sheet PDF, PRO submission confirmation

### Hype Engine Track:
`GIG_COMPLETED` → `FOOTAGE_RECEIVED` → `HIGHLIGHT_REEL_EXPORTED` → `POSTS_PUBLISHED`
- Receive raw gig footage from artist/venue (within 12hrs)
- Export 60-second highlight reel via Canva AI (vertical + horizontal)
- Publish across all platforms with CTA ("Next show: [date]")
- Deliverables: Highlight reel video, social posts, engagement metrics

### Career Architect Track:
`GIG_COMPLETED` → `EXPENSES_LOGGED` → `PNL_UPDATED` → `BRIEFING_GENERATED`
- Collect all expenses (travel, gear, commissions) from QuickBooks
- Calculate actual Net Net vs. estimated
- Update P&L statement, compare to target margin (>30%)
- Generate post-gig briefing for artist
- Deliverables: P&L update, variance report, 3-bullet briefing

**Convergence Point**: `AUTOPSY_COMPLETE`
- All agents mark tasks complete in Airtable
- Career Architect compiles lessons learned: what worked, what failed, improvements
- Document in Airtable `Gig_Archive` with tags for future reference

**End State Actions**:
- Update Airtable `Gigs` table: autopsy_status = "Complete"
- Rights Guardian begins royalty tracking (90-day window)
- Hype Engine adds gig footage to content library
- Career Architect updates career roadmap progress

**Failure Conditions**:
- Cue sheet not filed within 48hrs → Rights Guardian escalation
- Footage not received within 24hrs → Hype Engine requests from promoter
- Expenses missing → Career Architect follows up with artist/team

---

## 4. Release_Campaign

**Trigger**: New master delivered (artist upload webhook)

**Agents Involved**: Hype Engine + Rights Guardian + Career Architect

**States**:
```
MASTER_RECEIVED (initial)
  ↓ [Parallel execution]
  ├→ RIGHTS_GUARDIAN_REGISTERING_ISRC
  ├→ HYPE_ENGINE_UPDATING_EPK
  └→ CAREER_ARCHITECT_SETTING_MILESTONES
  ↓ [All complete]
CAMPAIGN_LAUNCHED
  ↓ [Monitor performance]
MILESTONE_TRACKING → (terminal state: release + 90 days)
```

**Parallel Workflows**:

### Rights Guardian Track:
`MASTER_RECEIVED` → `ISRC_ASSIGNED` → `PRO_REGISTERED` → `METADATA_DISTRIBUTED`
- Assign ISRC code, register with SoundExchange
- Submit ISWC + cue sheet to PRO (ASCAP/BMI)
- Distribute metadata to Spotify, Apple Music, Beatport
- Deliverables: ISRC confirmation, PRO registration, metadata sheets

### Hype Engine Track:
`MASTER_RECEIVED` → `EPK_UPDATED` → `PRE_SAVE_CAMPAIGN` → `ADS_LAUNCHED`
- Regenerate EPK with new release info, artwork, bio
- Launch pre-save campaign (Spotify, Apple Music links)
- Seed to influencers, playlist curators, press contacts
- Deliverables: Updated EPK PDF, pre-save campaign dashboard

### Career Architect Track:
`MASTER_RECEIVED` → `MILESTONES_DEFINED` → `TARGETS_SET` → `PROGRESS_TRACKING`
- Define success milestones (streams, chart positions, playlist adds)
- Set targets based on DJ Business Plan financial model
- Schedule weekly check-ins to monitor velocity
- Deliverables: Milestone tracker in Airtable, weekly progress reports

**Convergence Point**: `CAMPAIGN_LAUNCHED`
- All systems ready: registration complete, EPK live, ads running
- Career Architect announces release date to team
- Begin daily monitoring of streaming numbers, social sentiment

**End State**: `MILESTONE_TRACKING` (90-day campaign window)
- Weekly milestone reviews
- Adjust ad spend based on ROAS
- Celebrate milestones (100K, 500K, 1M streams) with social posts

---

## 5. Monthly_Financial

**Trigger**: 1st of every month (cron scheduler)

**Agents Involved**: Rights Guardian + Career Architect

**States**:
```
MONTH_START (initial)
  ↓ [Rights Guardian pulls reports]
ROYALTY_REPORTS_PULLLED
  ↓ [Career Architect reconciles]
PNL_GENERATED
  ↓ [Review against targets]
VARIANCE_ANALYZED
  ↓ [Generate briefing]
BRIEFING_SENT → (terminal state)
```

**Workflow**:
1. **Rights Guardian**:
   - Pull royalty statements from all sources (Spotify, Apple Music, SoundExchange, PROs)
   - Reconcile with QuickBooks deposits
   - Identify discrepancies, initiate corrections
   - Update Airtable `Royalties` table with expected vs. actual

2. **Career Architect**:
   - Generate P&L statement categorized by income stream (Recording, Publishing, Live, Merch)
   - Compare actual margins to targets (Live >30%, Streaming >70% margin)
   - Calculate recoupment status for any advances
   - Generate 3-bullet briefing for artist

3. **HITL Review** (if variance >10%):
   - Flag significant variances for artist review
   - Schedule strategy call if monthly targets missed
   - Adjust next month's projections based on trends

**End State Actions**:
- Push briefing to Artist Portal
- Update career roadmap with financial progress
- Archive reports in Airtable `Financial_Archive`
- Rights Guardian schedules follow-ups on unpaid royalties

---

## State Machine Implementation Notes

### Database Schema (Airtable)
```
Table: Gigs
- ID, Venue, Date, Gross, Estimated_Net, Actual_Net
- Status (Lead, Pending_Signature, Confirmed, Complete, Autopsy_Complete)
- Contract_URL, Rider_URL, Deposit_Paid (bool)

Table: Royalties
- Source (PRO, Streaming, Sync), Expected_Amount, Actual_Amount
- Payment_Date, Variance, Correction_Status

Table: Content_Calendar
- Platform, Post_Type, Scheduled_Time, CTA, Budget
- Performance_Metrics (Reach, Engagement, Conversions)

Table: Gear_Inventory
- Item_Name, Serial_Number, Last_Maintenance, Condition, Replacement_Date

Table: Decisions
- Timestamp, Participants, Decision_Type, Rationale, Impact
```

### Scheduler Configuration (n8n example)
```json
{
  "workflows": [
    {
      "name": "Gig_Booking_Flow",
      "trigger": "webhook",
      "endpoint": "/webhooks/gig-inquiry"
    },
    {
      "name": "Pre_Gig_Prep_Flow",
      "trigger": "cron",
      "schedule": "0 9 * * *",
      "filter": "gigs where date = today + 21 days"
    },
    {
      "name": "Post_Gig_Autopsy",
      "trigger": "webhook",
      "endpoint": "/webhooks/gig-complete"
    },
    {
      "name": "Monthly_Financial",
      "trigger": "cron",
      "schedule": "0 8 1 * *"
    }
  ]
}
```

### HITL Gateway Integration
All state machines pause at HITL triggers and send push notifications to Artist Portal:
- Contract approvals
- Expense approvals >$500
- Career roadmap changes
- Brand partnership decisions

Artist responds via mobile app → webhook resumes state machine with decision.
