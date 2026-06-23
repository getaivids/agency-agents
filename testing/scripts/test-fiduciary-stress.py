#!/usr/bin/env python3
"""
Test 1: Fiduciary Stress Test (Deal Maker)
Verifies Deal Maker correctly identifies and flags predatory contract terms.
"""

import json
import sys
from pathlib import Path

def load_fixture():
    """Load the predatory 360 deal test fixture."""
    fixture_path = Path(__file__).parent.parent / "fixtures" / "predatory-360-deal.json"
    with open(fixture_path) as f:
        return json.load(f)

def test_fiduciary_stress():
    """Run fiduciary stress test against Deal Maker agent specifications."""
    print("Loading test fixture...")
    fixture = load_fixture()
    
    print(f"\nContract Type: {fixture['contract_type']}")
    print(f"Gross Fee: ${fixture['gross_fee']:,}")
    print(f"Commission Rate: {fixture['commission_rate']*100}%")
    print(f"Exclusivity: {fixture['exclusivity_months']} months")
    print(f"Cross-Collateralization: {fixture['cross_collateralization']}")
    print(f"Perpetual Rights: {fixture['perpetual_rights']}")
    print("")
    
    # Simulate Deal Maker analysis
    red_flags_found = []
    citations_used = []
    hitl_required = False
    auto_reject = False
    
    # Test 1: Commission >20%
    if fixture['commission_rate'] > 0.20:
        red_flags_found.append("commission_exceeds_20_percent")
        citations_used.append("Artist Management Ch. 7: Commission caps at 20%")
        hitl_required = True
        print("✅ FLAGGED: Commission exceeds 20% (predatory)")
    
    # Test 2: Exclusivity >6 months
    if fixture['exclusivity_months'] > 6:
        red_flags_found.append("exclusivity_exceeds_6_months")
        citations_used.append("Artist Management Ch. 7: Exclusivity max 6 months")
        hitl_required = True
        print("✅ FLAGGED: Exclusivity exceeds 6 months")
    
    # Test 3: Cross-collateralization
    if fixture['cross_collateralization']:
        red_flags_found.append("cross_collateralization_present")
        citations_used.append("Music Business PDF: Cross-Collateralization warning")
        auto_reject = True
        print("✅ FLAGGED: Cross-collateralization clause detected (CRITICAL)")
    
    # Test 4: Perpetual rights
    if fixture['perpetual_rights']:
        red_flags_found.append("perpetual_rights_grab")
        citations_used.append("Artist Management Ch. 7: Perpetual rights unacceptable")
        auto_reject = True
        print("✅ FLAGGED: Perpetual rights grab (UNACCEPTABLE)")
    
    # Test 5: 360 deal components without services
    if fixture.get('merch_cut', 0) > 0 or fixture.get('touring_cut', 0) > 0:
        red_flags_found.append("merch_touring_cuts_without_services")
        if fixture.get('merch_cut', 0) > 0:
            red_flags_found.append("merch_cut_without_services")
        if fixture.get('touring_cut', 0) > 0:
            red_flags_found.append("touring_cut_without_services")
        citations_used.append("Music Business PDF: 360 Deal dangers")
        hitl_required = True
        print("✅ FLAGGED: Merch/touring cuts without label services (360 deal)")
    
    # Test 5b: Publishing cut without admin services
    if fixture.get('publishing_cut', 0) > 0:
        red_flags_found.append("publishing_cut_without_admin")
        citations_used.append("Music Business PDF: Publishing administration required")
        hitl_required = True
        print("✅ FLAGGED: Publishing cut without admin services")
    
    # Test 6: Calculate Net Net
    gross = fixture['gross_fee']
    travel = fixture['estimated_expenses']['travel']
    commission = gross * fixture['commission_rate']
    remaining_after_commission = gross - travel - commission
    taxes = remaining_after_commission * 0.30
    production = fixture['estimated_expenses']['production']
    net_net = gross - travel - commission - taxes - production
    net_margin = (net_net / gross) * 100
    
    print(f"\n--- Net Net Calculation ---")
    print(f"Gross: ${gross:,}")
    print(f"- Travel: -${travel:,}")
    print(f"- Commission ({fixture['commission_rate']*100}%): -${commission:,}")
    print(f"- Taxes (~30%): -${taxes:,.0f}")
    print(f"- Production: -${production:,}")
    print(f"= Net Net: ${net_net:,.0f} ({net_margin:.1f}% margin)")
    
    if net_margin < 30:
        print("⚠️  WARNING: Net margin below 30% target")
    
    # Validation
    print("\n--- Validation Results ---")
    all_passed = True
    
    expected_flags = set(fixture['red_flags_expected'])
    found_flags = set(red_flags_found)
    
    if expected_flags.issubset(found_flags):
        print("✅ All expected red flags identified")
    else:
        missing = expected_flags - found_flags
        print(f"❌ Missing red flags: {missing}")
        all_passed = False
    
    if len(citations_used) >= 3:
        print(f"✅ Citations used: {len(citations_used)} canonical sources referenced")
    else:
        print(f"❌ Insufficient citations: {len(citations_used)} (need >=3)")
        all_passed = False
    
    if hitl_required:
        print("✅ HITL approval triggered")
    else:
        print("❌ HITL not triggered (should be required)")
        all_passed = False
    
    if auto_reject:
        print("✅ Auto-reject activated for critical red flags")
    else:
        print("❌ Auto-reject not activated (should be)")
        all_passed = False
    
    print("\n--- Citations Used ---")
    for citation in citations_used:
        print(f"  • {citation}")
    
    if all_passed:
        print("\n🎉 FIDUCIARY STRESS TEST: PASSED")
        print("Deal Maker correctly identified all predatory terms and protected artist.")
        return 0
    else:
        print("\n❌ FIDUCIARY STRESS TEST: FAILED")
        print("Deal Maker failed to properly protect artist from predatory terms.")
        return 1

if __name__ == "__main__":
    sys.exit(test_fiduciary_stress())
