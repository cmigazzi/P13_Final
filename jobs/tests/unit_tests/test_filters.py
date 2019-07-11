"""Contains tests for hours filters."""
from jobs.filters import hours


def test_hours():
    assert hours(2) == "1h00"
    assert hours(5) == "2h30"
    assert hours(36) == "18h00"
