import pytest
from summer import summer


def test_summers_returns_sum_for_ints():
    assert summer(1, 2, 4, 8, 16) == 31


def test_summers_returns_sum_for_floats():
    assert summer(1.1, 2.2, 4.4, 8.8, 16.16) == 32.66


def test_summers_returns_sum_for_ints_and_floats():
    assert summer(1.1, 2, 4.4, 8, 16.16) == 31.66


def test_summers_raise_value_error():
    with pytest.raises(Exception):
        summer(1, 2, "foo", 3)
