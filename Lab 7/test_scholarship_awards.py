from hypothesis import given, strategies as st
from scholarship_awards import parse_applicant, marks_average, payable_award


# ---------- Fuzz tests: no function may crash on any text or None ----------
@given(st.text() | st.none())
def test_parse_applicant_no_crash(s):
    try:
        parse_applicant(s)
    except Exception as e:
        assert False, f"parse_applicant crashed with: {e!r}"


@given(st.text() | st.none())
def test_marks_average_no_crash(s):
    try:
        marks_average(s)
    except Exception as e:
        assert False, f"marks_average crashed with: {e!r}"


@given(st.text() | st.none())
def test_payable_award_no_crash(s):
    try:
        payable_award(s)
    except Exception as e:
        assert False, f"payable_award crashed with: {e!r}"


# ---------- Extra property tests: valid inputs still behave correctly ----------
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_marks_average_valid_is_within_range(marks):
    result = marks_average(",".join(str(m) for m in marks))
    assert min(marks) <= result <= max(marks)


@given(st.floats(min_value=0, max_value=1e6), st.floats(min_value=0, max_value=1e6))
def test_payable_award_never_negative(award, deduction):
    result = payable_award(f"{award}|{deduction}")
    assert result is not None and result >= 0


@given(st.sampled_from(["merit", "sports", "arts"]), st.integers(0, 100))
def test_parse_applicant_valid(category, marks):
    assert parse_applicant(f"{category}:{marks}") == (category.title(), float(marks))
