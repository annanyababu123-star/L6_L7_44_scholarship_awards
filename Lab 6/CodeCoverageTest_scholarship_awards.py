import pytest
from scholarship_awards import award_amount, is_eligible, application_status


# ---------- award_amount ----------
def test_below_cutoff_marks():
    assert award_amount("merit", 70, "low", False) == 0


def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("music", 80, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -1, "low", False)


def test_renewal_low_income_high_marks():
    # cutoff 75-5=70, above=30 -> rate 100+40+20=160
    assert award_amount("merit", 100, "low", True) == 30 * 160


def test_sports_high_income_high_marks():
    # sports cutoff 60, above=40 -> rate 60+40=100
    assert award_amount("sports", 100, "high", False) == 40 * 100


def test_high_income_small_margin():
    # above=5 -> rate 60
    assert award_amount("merit", 80, "high", False) == 5 * 60


# ---------- is_eligible ----------
def test_is_eligible():
    assert is_eligible(90, 0, False) is True


def test_special_quota_eligible():
    assert is_eligible(10, 2, True) is True


def test_low_attendance_not_eligible():
    assert is_eligible(70, 0, False) is False


def test_too_many_backlogs_not_eligible():
    assert is_eligible(90, 2, False) is False


# ---------- application_status ----------
def test_status_open():
    assert application_status(25, False, False) == "open"


def test_status_closing():
    assert application_status(10, False, False) == "closing"


def test_status_closed():
    assert application_status(2, False, False) == "closed"


def test_status_renewal_paper_open():
    assert application_status(40, True, True) == "open"
