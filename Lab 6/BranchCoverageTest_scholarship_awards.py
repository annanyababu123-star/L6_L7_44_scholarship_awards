import pytest
from scholarship_awards import award_amount, is_eligible, application_status


# ---------- award_amount: every decision True and False ----------
def test_below_cutoff_marks():
    # above <= 0 -> True branch
    assert award_amount("merit", 70, "low", False) == 0


def test_exactly_at_cutoff_gives_zero():
    # boundary: above == 0
    assert award_amount("merit", 75, "low", False) == 0


def test_unknown_category():
    # category not in CUTOFF_MARKS -> True branch
    with pytest.raises(ValueError):
        award_amount("music", 80, "low", False)


def test_negative_marks():
    # marks < 0 -> True branch
    with pytest.raises(ValueError):
        award_amount("merit", -1, "low", False)


def test_zero_marks_valid():
    # marks < 0 -> False branch (boundary), then above <= 0
    assert award_amount("arts", 0, "high", False) == 0


def test_renewal_non_sports_lowers_cutoff():
    # is_renewal and category != sports -> both True; cutoff 70
    assert award_amount("merit", 80, "high", True) == 10 * 60


def test_renewal_sports_keeps_cutoff():
    # is_renewal True but category == sports -> False branch; cutoff stays 60
    assert award_amount("sports", 70, "high", True) == 10 * 60


def test_not_renewal_keeps_cutoff():
    # is_renewal False -> False branch
    assert award_amount("arts", 70, "high", False) == 5 * 60


def test_low_income_small_margin():
    # income low (True), above <= 15 (False)
    assert award_amount("merit", 85, "low", False) == 10 * 100


def test_low_income_boundary_above_15():
    # above == 15 -> not > 15
    assert award_amount("merit", 90, "low", False) == 15 * 100


def test_low_income_large_margin():
    # income low (True), above > 15 (True), inner low (True) -> rate 160
    assert award_amount("merit", 100, "low", False) == 25 * 160


def test_high_income_small_margin():
    # income not low (False), above <= 15
    assert award_amount("merit", 80, "high", False) == 5 * 60


def test_high_income_large_margin():
    # income not low (False), above > 15 (True), inner low (False) -> rate 100
    assert award_amount("merit", 100, "high", False) == 25 * 100


# ---------- is_eligible ----------
def test_special_quota_within_limit():
    assert is_eligible(10, 2, True) is True


def test_special_quota_too_many_backlogs():
    assert is_eligible(95, 3, True) is False


def test_low_attendance():
    assert is_eligible(74, 0, False) is False


def test_attendance_boundary_ok():
    assert is_eligible(75, 1, False) is True


def test_regular_eligible():
    assert is_eligible(90, 0, False) is True


def test_regular_too_many_backlogs():
    assert is_eligible(90, 2, False) is False


# ---------- application_status ----------
def test_new_open():
    assert application_status(20, False, False) == "open"


def test_new_closing():
    assert application_status(5, False, False) == "closing"


def test_new_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_open():
    assert application_status(30, True, False) == "open"


def test_renewal_closing():
    assert application_status(15, True, False) == "closing"


def test_renewal_closed():
    assert application_status(14, True, False) == "closed"


def test_paper_adds_ten_days():
    # is_paper True: cutoff 30 for new; 25 days is now "closing"
    assert application_status(25, False, True) == "closing"


def test_renewal_and_paper_open():
    assert application_status(40, True, True) == "open"
