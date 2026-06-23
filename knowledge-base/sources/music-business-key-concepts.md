# Music Business: Key Concepts

**Source Document for RAG Vector Database**
**Chunking Strategy**: By term (A-Z) with cross-references
**Authorized Agents**: Rights Guardian, Deal Maker, Career Architect

---

## A

### Advance
Upfront payment provided by a label, publisher, or promoter to an artist. **CRITICAL**: Advances are **recoupable**, meaning the artist receives no additional royalties until the advance is fully repaid through earnings. 

**Related Terms**: Recoupable, Recoupment, Cross-Collateralization

**Agent Usage**: 
- **Deal Maker**: Must calculate recoupment timeline before accepting advances
- **Rights Guardian**: Track unrecouped balance in royalty statements
- **Career Architect**: Evaluate whether advance justifies rights granted

---

### ASCAP (American Society of Composers, Authors and Publishers)
One of the three major U.S. Performance Rights Organizations (PROs). Collects performance royalties when compositions are played publicly (radio, TV, venues, streaming).

**Related Terms**: BMI, SESAC, Performance Rights, Cue Sheet

**Registration Requirement**: Songs must be registered within 48 hours of release to ensure proper royalty collection.

**Agent Usage**:
- **Rights Guardian**: Submit cue sheets to ASCAP API immediately upon release
- **Deal Maker**: Verify songwriter's PRO affiliation before contract drafting

---

## B

### BMI (Broadcast Music, Inc.)
Second major U.S. PRO. Similar function to ASCAP but operates as a broadcast-owned organization rather than membership-based.

**Related Terms**: ASCAP, SESAC, Performance Rights

**Agent Usage**: Same as ASCAP - Rights Guardian must register works promptly.

---

### Backend Deal
Payment structure where artist receives percentage of ticket sales/revenue after expenses, rather than flat fee. Riskier but potentially higher reward.

**Related Terms**: Flat Fee, Net Profit, Gross vs. Net

**Agent Usage**:
- **Deal Maker**: Calculate break-even point; only accept backend if venue capacity + ticket price × 0.7 > flat fee alternative
- **Career Architect**: Approve backend deals only for strategic career-building opportunities

---

### Beatport
Electronic music-focused digital store and analytics platform. Critical for DJ/producers tracking genre-specific performance.

**Related Terms**: Chartmetric, Genre Trending, Release Campaign

**Agent Usage**:
- **Hype Engine**: Monitor Beatport chart positions during release campaign
- **Sonic Curator**: Analyze Beatport genre trends for crate curation

---

## C

### Chartmetric
Cross-platform analytics tool tracking Spotify, Apple Music, TikTok virality, radio spins, playlist adds, and social media growth.

**Related Terms**: Spotify for Artists, Analytics, Release Campaign

**API Integration**: `chartmetric-api` in tools.json
- Endpoints: `/artist/{id}`, `/playlist/adds`, `/radio/spins`, `/tiktok/trending`
- Rate limits: 60 requests/minute, 50K monthly quota

**Agent Usage**:
- **Career Architect**: Weekly career briefings include Chartmetric trend analysis
- **Hype Engine**: Identify viral moments, amplify with paid promotion

---

### Commission
Percentage of artist earnings paid to manager, booking agent, or lawyer. 

**Industry Standards**:
- Personal Manager: 15-20% (NEVER exceed 20%)
- Booking Agent: 10% (standard, non-negotiable)
- Lawyer: 5% or hourly rate

**CRITICAL FIDUCIARY RULE**: Per *Artist Management Ch. 7*, commission exceeding 20% for personal management is predatory and requires explicit artist approval + legal review.

**Related Terms**: Fiduciary Duty, Contract Red Flags, 360 Deal

**Agent Usage**:
- **Deal Maker**: Auto-reject any management deal with commission >20%
- **Rights Guardian**: Flag commission clauses in all contracts
- **Career Architect**: Audit all commission payments quarterly

---

### Cross-Collateralization ⚠️
**CRITICAL CONTRACT CLAUSE**: Allows label/manager to recoup losses from one revenue stream against earnings from completely different streams.

**Example**: Unrecouped album advance can be taken from touring income, merchandise sales, or publishing royalties - even though these are traditionally separate.

**FIDUCIARY RULE**: Per *Music Business PDF* and *Artist Management Ch. 7*:
- **ALWAYS resist** cross-collateralization clauses
- If unavoidable, limit to specific revenue streams only (e.g., "recoupable from recording royalties only, NOT from touring or publishing")
- NEVER allow cross-collateralization between live performance and recorded music

**Related Terms**: Recoupable, Advance, 360 Deal, Fiduciary Duty

**Agent Usage**:
- **Deal Maker**: MUST flag any cross-collateralization clause as CRITICAL red flag
- **Rights Guardian**: Audit existing contracts for cross-collateralization exposure
- **Career Architect**: Reject deals with unrestricted cross-collateralization unless artist provides written approval after legal consultation

---

### Cue Sheet
Document listing all musical works used in audiovisual content (TV, film, ads, live performances). Submitted to PROs for royalty distribution.

**Required Fields**:
- Song title, writer(s), publisher(s)
- ISWC (composition code)
- ISRC (recording code)
- Usage type (background, feature, theme)
- Duration

**FIDUCIARY RULE**: Per *Music Business PDF*, cue sheets MUST be filed within 48 hours of performance/broadcast to ensure royalty collection.

**Related Terms**: ISRC, ISWC, PRO, Performance Rights, SoundExchange

**Agent Usage**:
- **Rights Guardian**: Auto-generate cue sheets from setlists, submit to PRO APIs
- **Road Captain**: Collect setlist from artist within 12hrs post-gig
- **Career Architect**: Track cue sheet filing compliance (target: 100% within 48hrs)

---

## D

### Deal Memo
Short-form agreement outlining key terms before full long-form contract. Often binding if includes: parties, engagement details, compensation, signatures.

**Related Terms**: Contract, Long-Form Agreement, DocuSign

**Agent Usage**:
- **Deal Maker**: Never sign deal memo without calculating Net Net first
- **Rights Guardian**: Review deal memo for red flags before artist signs

---

### Deposit
Advance payment (typically 50% of total fee) required to secure booking. Non-refundable unless promoter cancels.

**FIDUCIARY RULE**: Per *DJ Business Plan: Financial*, NEVER perform without deposit received minimum 7 days before show.

**Related Terms**: Gig Booking Flow, Contract, QuickBooks

**Agent Usage**:
- **Deal Maker**: Invoice via QuickBooks immediately upon contract signing
- **Career Architect**: Reschedule gig if deposit not received T-7 days

---

### DocuSign
Electronic signature platform for contract execution with audit trail.

**API Integration**: `docusign-api` in tools.json
- Endpoints: `/envelopes`, `/templates`, `/status`
- Rate limits: 1000 requests/min, 5000 envelopes/day

**Agent Usage**:
- **Deal Maker**: Send all contracts via DocuSign for audit trail
- **Rights Guardian**: Store executed contracts in Airtable `Contracts` table

---

## E

### EPK (Electronic Press Kit)
Digital portfolio used for booking, press, brand partnerships. Includes: bio, photos, videos, tech rider, past venues, social metrics.

**Related Terms**: Hype Engine, Marketing, Canva

**Agent Usage**:
- **Hype Engine**: Update EPK within 24hrs of major milestones (new release, festival booking, viral moment)
- **Road Captain**: Include current EPK link in all venue communications

---

### Exclusivity Clause
Contract provision preventing artist from working with other managers/agents or performing in certain geographic areas.

**FIDUCIARY RULE**: Per *Artist Management Ch. 7*:
- Exclusivity periods >6 months require explicit artist approval
- Geographic exclusivity must be clearly defined (city, region, country?)
- Carve-outs should be negotiated (e.g., "except for pre-existing relationships")

**Related Terms**: Contract Red Flags, Territory, Term

**Agent Usage**:
- **Deal Maker**: Flag any exclusivity >6 months as requiring HITL approval
- **Rights Guardian**: Track exclusivity expiration dates, notify when renegotiation window opens

---

## F

### Fiduciary Duty
Legal obligation to act in the best interest of another party. Managers owe fiduciary duty to artists.

**Core Principles**:
- Undivided loyalty
- Full disclosure of conflicts
- Protection of artist's financial interests
- Avoidance of self-dealing

**Related Terms**: Commission, Cross-Collateralization, 360 Deal

**Agent Usage**:
- **ALL AGENTS**: Every decision must prioritize artist's long-term career over short-term gain
- **Career Architect**: Escalate any conflict of interest immediately

---

### Flat Fee
Guaranteed payment regardless of ticket sales. Lower risk than backend deal.

**Related Terms**: Backend Deal, Guarantee vs. Percentage

**Agent Usage**:
- **Deal Maker**: Default to flat fee unless backend has clear upside (>2x flat fee at capacity)
- **Career Architect**: Use flat fee for budgeting, treat backend as bonus

---

## G

### Gross vs. Net
**Gross**: Total revenue before expenses
**Net**: What remains after all expenses (travel, commissions, taxes, production costs)

**CRITICAL DISTINCTION**: Per *DJ Business Plan: Financial*, always calculate **Net Net** before presenting offers:

```
Net Net = Gross - (Travel + Commission + Taxes + Production Costs)
```

**Target**: Net profit margin >30% per gig

**Related Terms**: Net Net, Profit Margin, Recoupable

**Agent Usage**:
- **Deal Maker**: ALWAYS present Net Net, never Gross, to artist
- **Career Architect**: Reject gigs with projected net margin <20%

---

## I

### ISRC (International Standard Recording Code)
Unique 12-character identifier for each sound recording. Required for royalty tracking.

**Format**: `CC-XXX-YY-NNNNN` (Country code, Registrant code, Year, Designation code)

**FIDUCIARY RULE**: Per *Music Business PDF*, every original track MUST have ISRC assigned before distribution. One ISRC per recording version (original, remix, live version each need unique ISRC).

**Related Terms**: ISWC, SoundExchange, Cue Sheet, PRO

**Agent Usage**:
- **Rights Guardian**: Assign ISRCs automatically upon master delivery
- **Hype Engine**: Include ISRC in all metadata submitted to DSPs

---

### ISWC (International Standard Musical Work Code)
Unique identifier for musical compositions (distinct from ISRC which identifies recordings).

**Related Terms**: ISRC, PRO, Cue Sheet, Publishing

**Agent Usage**:
- **Rights Guardian**: Register ISWC with PRO simultaneously with ISRC assignment

---

## M

### Mechanical Royalty
Payment to songwriters/publishers for reproduction rights (physical sales, downloads, interactive streaming). In U.S., rate set by Copyright Royalty Board.

**Current Rate (2024)**: 12¢ per song or 2.31¢ per minute (whichever is greater) for physical/digital

**Streaming**: Calculated as portion of subscription revenue allocated to mechanicals

**Related Terms**: Performance Rights, PRO, Publishing Administrator

**Agent Usage**:
- **Rights Guardian**: Ensure mechanical royalties collected via publishing administrator
- **Career Architect**: Factor mechanical income into royalty projections

---

## N

### Net Net
**See: Gross vs. Net**

The actual amount artist takes home after ALL expenses. This is the ONLY number that matters for financial decisions.

**Formula**:
```
Net Net = Gross Fee - Travel - Commission (10-20%) - Taxes (~30%) - Production Costs
```

**Example**:
- Gross: $5,000
- Travel: -$800 (flights, hotel, ground transport)
- Commission (15%): -$750
- Taxes (30% of remaining): -$1,035
- **Net Net: $2,415** (48.3% of gross)

**Related Terms**: Profit Margin, Deal Maker, QuickBooks

**Agent Usage**:
- **Deal Maker**: Calculate and display Net Net for EVERY offer
- **Career Architect**: Use Net Net for financial planning, not Gross

---

## P

### Performance Rights
Right to collect royalties when composition is performed publicly. Collected by PROs (ASCAP, BMI, SESAC).

**Covered Uses**:
- Radio/TV broadcasts
- Live venue performances
- Streaming services (interactive)
- Background music in businesses

**NOT Covered**: Non-interactive streaming (covered by SoundExchange)

**Related Terms**: PRO, Cue Sheet, Mechanical Royalty, SoundExchange

**Agent Usage**:
- **Rights Guardian**: Register all works with PRO within 48hrs of release
- **Road Captain**: Ensure venue has proper PRO licenses (most do)

---

### PRO (Performance Rights Organization)
Organizations that collect performance royalties on behalf of songwriters/publishers. U.S. has three: ASCAP, BMI, SESAC.

**Related Terms**: ASCAP, BMI, SESAC, Performance Rights, Cue Sheet

**Agent Usage**:
- **Rights Guardian**: Maintain artist's PRO registration, submit cue sheets religiously

---

### Publishing Administrator
Company that collects publishing royalties worldwide (mechanical + performance + sync). Takes 10-25% of collections.

**Major Players**: Songtrust, CD Baby Pro, TuneCore Publishing

**Related Terms**: Mechanical Royalty, Performance Rights, Sync License

**Agent Usage**:
- **Rights Guardian**: Ensure publishing admin is registered for all works
- **Career Architect**: Compare admin rates, switch if better deal available

---

## R

### Recoupable
Expenses that label/manager can recover from artist's earnings before paying royalties.

**Common Recoupable Items**:
- Recording costs (studio time, mixing, mastering)
- Video production
- Tour support (if specified)
- Marketing spend (if specified)

**DANGER**: Without limitations, recoupable expenses can keep artist in perpetual debt to label.

**Related Terms**: Advance, Cross-Collateralization, Recoupment

**Agent Usage**:
- **Deal Maker**: Negotiate cap on recoupable expenses
- **Rights Guardian**: Audit royalty statements for unauthorized recoupment
- **Career Architect**: Track recoupment status quarterly

---

### Recoupment
Process of repaying advances/recoupable expenses from royalties. Artist receives no additional payment until fully recouped.

**Related Terms**: Advance, Recoupable, Cross-Collateralization

**Agent Usage**:
- **Rights Guardian**: Calculate recoupment progress in monthly financial reports
- **Career Architect**: Plan releases strategically to achieve recoupment faster

---

## S

### SESAC
Third U.S. PRO. Smaller than ASCAP/BMI, operates as private company. Known for better rates in some genres.

**Related Terms**: ASCAP, BMI, PRO

---

### SoundExchange
Organization collecting non-interactive digital performance royalties (satellite radio, internet radio like Pandora).

**Split**: 50% to featured artist, 45% to copyright owner (label), 5% to backup musicians/vocalists

**FIDUCIARY RULE**: Per *Music Business PDF*, SoundExchange registration is SEPARATE from PRO registration. Both required for complete royalty collection.

**Related Terms**: Performance Rights, PRO, Neighboring Rights

**Agent Usage**:
- **Rights Guardian**: Register artist + all tracks with SoundExchange within 48hrs of release
- **Career Architect**: Track SoundExchange royalties separately from PRO royalties

---

### Spotify for Artists
Analytics dashboard + API for tracking Spotify performance.

**Key Metrics**:
- Monthly listeners, followers
- Stream counts by track
- Audience demographics (age, gender, location)
- Playlist adds (editorial + user-generated)
- Save rate, skip rate

**API Integration**: `spotify-for-artists-api` in tools.json
- Endpoints: `/artists/{id}`, `/tracks/{id}/top-tracks`
- Rate limits: 50 requests/sec, 100K daily quota

**Agent Usage**:
- **Career Architect**: Include Spotify trends in weekly briefings
- **Hype Engine**: Target ad campaigns to cities with highest listener concentration
- **Sonic Curator**: Analyze top tracks for crate curation insights

---

## T

### 360 Deal ⚠️
**CRITICAL CONTRACT TYPE**: Label/manager takes percentage of ALL artist revenue streams - not just recordings, but also touring, merchandise, endorsements, publishing.

**WHY IT'S DANGEROUS**:
- Traditionally, labels only earned from recordings
- 360 deals let labels take 10-30% of touring, merch, etc. WITHOUT providing services in those areas
- Often includes cross-collateralization (losses in recordings recouped from touring)

**FIDUCIARY RULE**: Per *Artist Management Ch. 7* and *Music Business PDF*:
- **NEVER accept** 360 deal without significant trade-offs (higher advance, better royalty rate, reduced term)
- If unavoidable, demand label provide actual services in exchange (tour support, marketing budget)
- Always sunset clauses (360 participation ends when contract ends)

**Related Terms**: Cross-Collateralization, Commission, Fiduciary Duty

**Agent Usage**:
- **Deal Maker**: Auto-flag any 360 clause as CRITICAL, require Career Architect + artist approval
- **Rights Guardian**: Audit all revenue streams for unauthorized 360 participation
- **Career Architect**: Reject 360 deals unless artist provides written approval after legal review

---

### Technical Rider
Document specifying equipment, power, staffing requirements for live performance.

**Standard Sections**:
- Audio requirements (PA system, monitors, mics)
- Lighting requirements
- Power requirements (dedicated 20A circuit for DJ gear)
- Stage plot
- Load-in/load-out times
- Hospitality (meals, dressing room)

**FIDUCIARY RULE**: Per *DJ Business Plan: Operations*, verify venue can meet rider requirements 72hrs before show. If not, escalate or cancel.

**Related Terms**: Road Captain, Venue Specs, Load-In

**Agent Usage**:
- **Road Captain**: Send rider with contract, reconfirm T-72hrs
- **Deal Maker**: Include rider acceptance as contract condition

---

## Q

### QuickBooks
Accounting software for P&L tracking, invoicing, expense management.

**API Integration**: `quickbooks-api` in tools.json
- Endpoints: `/invoice`, `/payment`, `/reports/profitandloss`
- Rate limits: 10 requests/sec, 25K daily quota

**Agent Usage**:
- **Deal Maker**: Auto-create invoices upon contract signing
- **Rights Guardian**: Generate monthly P&L reports
- **Career Architect**: Track net profit margins per gig

---

## Summary: Critical Fiduciary Rules

| Concept | Rule | Source |
|---------|------|--------|
| Commission | Max 20% for management | Artist Mgmt Ch. 7 |
| Exclusivity | Max 6 months without approval | Artist Mgmt Ch. 7 |
| Cross-Collateralization | ALWAYS resist, limit if unavoidable | Music Biz PDF |
| 360 Deals | Reject unless significant trade-offs | Artist Mgmt Ch. 7 |
| PRO Registration | Within 48hrs of release | Music Biz PDF |
| Cue Sheet Filing | Within 48hrs of performance | Music Biz PDF |
| Deposit | Received T-7 days minimum | DJ Biz Plan: Financial |
| Net Profit Margin | Target >30% per gig | DJ Biz Plan: Financial |
| Stamina | Max 3 gigs/week, 48hr recovery | Artist Mgmt Ch. 1 |

---

**Document Version**: 1.0
**Last Updated**: Phase 5 Knowledge Base Integration
**Next Review**: After deployment of RAG pipeline
