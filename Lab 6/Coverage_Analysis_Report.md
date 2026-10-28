# Lab 6: Code and Branch Coverage Analysis

**Name:** Annanya Babu
**SRN:** PES1UG24AM045
**Module under test:** `scholarship_awards.py` (`award_amount`, `is_eligible`, `application_status`)

## 1. Baseline (starter tests only)

The starter file had 2 tests (`test_below_cutoff_marks`, `test_is_eligible`).

| Metric | Result |
|--------|--------|
| Line coverage | 38% (23 of 37 statements missed) |
| Branch coverage | 32% (6 partial branches) |

Missing lines: 6, 8, 11, 15-23, 28, 30, 35-45. Untested paths: the unknown-category and negative-marks errors, the renewal cutoff reduction, the whole rate calculation, special-quota eligibility, the attendance and backlog rejections, and all of `application_status`.

## 2. Code (line) coverage

`CodeCoverageTest_AM045_application.py` has 14 tests. Each was added to execute a specific missed line:

- Both `ValueError` raises (lines 6, 8).
- Renewal cutoff reduction (line 11) and both income rates (lines 16, 18).
- The bonus-rate block for marks more than 15 above the cutoff (lines 20-22).
- `is_eligible`: special quota, low attendance, too many backlogs.
- `application_status`: open, closing, closed, and the renewal/paper cutoffs.

**Result: 100% line coverage (37/37 statements).**

## 3. Branch coverage

`BranchCoverageTest_AM045_application.py` has 27 tests. Every decision is exercised for both True and False, plus boundary values:

- `is_renewal and category != "sports"`: renewal non-sports (True), renewal sports (False), non-renewal (False).
- `above > 15` with `above == 15` as the boundary, and the inner `income_level == "low"` check on both sides.
- `marks < 0` with `marks == 0` as the boundary; `above <= 0` with marks exactly at the cutoff.
- `attendance < 75` at 74 and 75; `backlogs` limits for regular (<=1) and special quota (<=2).
- `application_status` thresholds at the exact edges (20/5/4 for new, 30/15/14 for renewal, +10 for paper).

**Result: 100% branch coverage (26/26 branches, 0 partial).**

## 4. Line vs branch coverage

Line coverage only shows that each line ran at least once. A test such as `award_amount("merit", 100, "low", True)` runs the bonus-rate lines but never checks the case where the bonus does not apply, or where the income is not low inside that block. Branch coverage forces both outcomes of every `if`, which is why it needs the boundary tests above. Here the small module let a well-chosen line-coverage suite reach 100% branch coverage as well, but that is not guaranteed in general.

## 5. Summary

| Stage | Tests | Line | Branch |
|-------|-------|------|--------|
| Starter | 2 | 38% | 32% |
| Code coverage suite | 14 | 100% | 100% |
| Branch coverage suite | 27 | 100% | 100% |
