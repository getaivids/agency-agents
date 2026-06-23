#!/bin/bash

# OmniRoster Validation Test Suite Runner
# Executes all Phase 6 validation tests and generates report

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
REPORTS_DIR="$ROOT_DIR/reports"

mkdir -p "$REPORTS_DIR"

echo "=========================================="
echo "  OmniRoster Validation Test Suite"
echo "  Phase 6: Testing & Validation"
echo "=========================================="
echo ""

PASS_COUNT=0
FAIL_COUNT=0
TOTAL_TESTS=0

run_test() {
    local test_name="$1"
    local test_script="$2"
    
    echo "----------------------------------------"
    echo "Running: $test_name"
    echo "----------------------------------------"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    if python "$test_script"; then
        echo "✅ PASS: $test_name"
        PASS_COUNT=$((PASS_COUNT + 1))
    else
        echo "❌ FAIL: $test_name"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
    
    echo ""
}

# Run all test scripts
run_test "Fiduciary Stress Test" "$SCRIPT_DIR/test-fiduciary-stress.py"
run_test "Stamina Guardrail Test" "$SCRIPT_DIR/test-stamina-guardrails.py"
run_test "Royalty Completeness Test" "$SCRIPT_DIR/test-royalty-completeness.py"
run_test "Integration Tests (4-6)" "$SCRIPT_DIR/test-integration.py"

# Generate summary report
echo "=========================================="
echo "  TEST SUMMARY"
echo "=========================================="
echo "Total Tests: $TOTAL_TESTS"
echo "Passed: $PASS_COUNT"
echo "Failed: $FAIL_COUNT"
echo "Pass Rate: $(echo "scale=1; $PASS_COUNT * 100 / $TOTAL_TESTS" | bc)%"
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
    echo "🎉 ALL TESTS PASSED - Ready for deployment!"
    exit 0
else
    echo "⚠️  SOME TESTS FAILED - Review reports before deployment"
    echo "Reports saved to: $REPORTS_DIR/"
    exit 1
fi
