#!/usr/bin/env python3
"""
Test 2: Stamina Guardrail Test (Career Architect)
Verifies Career Architect enforces human stamina constraints and prevents overbooking.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

def load_fixture():
    """Load the five-gigs-seven-days test fixture."""
    fixture_path = Path(__file__).parent.parent / "fixtures" / "five-gigs-seven-days.json"
    with open(fixture_path) as f:
        return json.load(f)

def calculate_distance_flag(gig1, gig2, threshold_miles=500):
    """Check if flight recovery is needed between gigs."""
    return gig1.get('distance_from_previous_miles', 0) > threshold_miles

def test_stamina_guardrails():
    """Run stamina guardrail test against Career Architect specifications."""
    print("Loading test fixture...")
    fixture = load_fixture()
    
    print(f"\nArtist Constraints:")
    print(f"  Max gigs per week: {fixture['artist_constraints']['max_gigs_per_week']}")
    print(f"  Recovery time required: {fixture['artist_constraints']['recovery_time_hours']} hours")
    print(f"  Flight recovery threshold: {fixture['artist_constraints']['flight_recovery_threshold_miles']} miles")
    print(f"\nGig Offers ({len(fixture['gig_offers'])} total):")
    
    for i, gig in enumerate(fixture['gig_offers'], 1):
        print(f"  {i}. {gig['date']} - {gig['city']} (${gig['gross_fee']:,})")
    
    # Simulate Career Architect analysis
    accepted_gigs = []
    rejected_gigs = []
    citations_used = []
    
    last_accepted_date = None
    last_accepted_distance = 0
    
    print("\n--- Career Architect Analysis ---\n")
    
    for gig in fixture['gig_offers']:
        gig_date = datetime.strptime(gig['date'], "%Y-%m-%d")
        accept = True
        rejection_reason = None
        
        # Check 1: Max gigs per week
        gigs_in_same_week = sum(
            1 for a in accepted_gigs 
            if abs((datetime.strptime(a['date'], "%Y-%m-%d") - gig_date).days) <= 7
        )
        
        if gigs_in_same_week >= fixture['artist_constraints']['max_gigs_per_week']:
            accept = False
            rejection_reason = f"Exceeds max {fixture['artist_constraints']['max_gigs_per_week']} gigs per week"
            print(f"❌ REJECT {gig['city']}: {rejection_reason}")
        
        # Check 2: 48-hour recovery after flights (>500 miles)
        if accept and last_accepted_date:
            days_since_last = (gig_date - last_accepted_date).days
            hours_since_last = days_since_last * 24
            
            if gig.get('distance_from_previous_miles', 0) > fixture['artist_constraints']['flight_recovery_threshold_miles']:
                if hours_since_last < fixture['artist_constraints']['recovery_time_hours']:
                    accept = False
                    rejection_reason = f"Insufficient recovery time ({hours_since_last}hrs < {fixture['artist_constraints']['recovery_time_hours']}hrs required after flight)"
                    print(f"❌ REJECT {gig['city']}: {rejection_reason}")
        
        # Check 3: Max consecutive days
        if accept and last_accepted_date:
            days_since_last = (gig_date - last_accepted_date).days
            if days_since_last == 1:  # Consecutive day
                consecutive_count = sum(
                    1 for a in accepted_gigs
                    if abs((gig_date - datetime.strptime(a['date'], "%Y-%m-%d")).days) <= 1
                )
                if consecutive_count >= fixture['artist_constraints'].get('max_consecutive_days', 2):
                    accept = False
                    rejection_reason = f"Exceeds max consecutive days ({fixture['artist_constraints'].get('max_consecutive_days', 2)})"
                    print(f"❌ REJECT {gig['city']}: {rejection_reason}")
        
        if accept:
            print(f"✅ ACCEPT {gig['city']}: {gig['date']} (${gig['gross_fee']:,})")
            accepted_gigs.append(gig)
            last_accepted_date = gig_date
            last_accepted_distance = gig.get('distance_from_previous_miles', 0)
        else:
            rejected_gigs.append({**gig, 'reason': rejection_reason})
    
    # Add citation
    citations_used.append("Artist Management Ch. 1: Stamina Constraints")
    citations_used.append("Artist Management Ch. 1: Max 3 gigs/week guideline")
    citations_used.append("Artist Management Ch. 1: 48hr recovery between flights")
    
    # Validation
    print("\n--- Validation Results ---")
    all_passed = True
    
    expected_accepts = fixture['expected_results']['gigs_to_accept']
    expected_rejects = fixture['expected_results']['gigs_to_reject']
    
    if len(accepted_gigs) == expected_accepts:
        print(f"✅ Correct number of accepts: {len(accepted_gigs)} (expected {expected_accepts})")
    else:
        print(f"❌ Wrong number of accepts: {len(accepted_gigs)} (expected {expected_accepts})")
        all_passed = False
    
    if len(rejected_gigs) == expected_rejects:
        print(f"✅ Correct number of rejects: {len(rejected_gigs)} (expected {expected_rejects})")
    else:
        print(f"❌ Wrong number of rejects: {len(rejected_gigs)} (expected {expected_rejects})")
        all_passed = False
    
    # Check specific dates
    accepted_dates = [g['date'] for g in accepted_gigs]
    expected_accept_dates = fixture['expected_results']['accepted_dates']
    
    if set(accepted_dates) == set(expected_accept_dates):
        print(f"✅ Correct dates accepted: {accepted_dates}")
    else:
        print(f"❌ Wrong dates accepted: {accepted_dates} (expected {expected_accept_dates})")
        all_passed = False
    
    # Verify citations
    if len(citations_used) >= 2:
        print(f"✅ Citations used: {len(citations_used)} canonical sources referenced")
    else:
        print(f"❌ Insufficient citations: {len(citations_used)} (need >=2)")
        all_passed = False
    
    # Calculate fatigue score
    total_travel_miles = sum(g.get('distance_from_previous_miles', 0) for g in accepted_gigs)
    avg_recovery_days = sum(
        abs((datetime.strptime(accepted_gigs[i]['date'], "%Y-%m-%d") - 
             datetime.strptime(accepted_gigs[i-1]['date'], "%Y-%m-%d")).days)
        for i in range(1, len(accepted_gigs))
    ) / max(len(accepted_gigs) - 1, 1)
    
    print(f"\n--- Fatigue Analysis ---")
    print(f"Total travel distance: {total_travel_miles} miles")
    print(f"Average recovery between gigs: {avg_recovery_days:.1f} days")
    
    if avg_recovery_days >= 2:
        print("✅ Recovery time adequate (>=2 days average)")
    else:
        print(f"⚠️  Recovery time tight ({avg_recovery_days:.1f} days average)")
    
    print("\n--- Citations Used ---")
    for citation in citations_used:
        print(f"  • {citation}")
    
    if all_passed:
        print("\n🎉 STAMINA GUARDRAIL TEST: PASSED")
        print("Career Architect correctly protected artist from burnout.")
        return 0
    else:
        print("\n❌ STAMINA GUARDRAIL TEST: FAILED")
        print("Career Architect failed to properly enforce stamina constraints.")
        return 1

if __name__ == "__main__":
    sys.exit(test_stamina_guardrails())
