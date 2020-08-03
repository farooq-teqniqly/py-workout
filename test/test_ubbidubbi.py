import pytest

from kidslanguages import english_to_ubbi_dubbi


@pytest.mark.parametrize(
    "original,expected_ubbi_dubbi",
    [("big octopus", "bubig uboctubopubus"), ("good job", "guboubod jubob")],
)
def test_ubbi_dubbi(original: str, expected_ubbi_dubbi: str):
    assert list(english_to_ubbi_dubbi(original)) == expected_ubbi_dubbi.split(" ")


@pytest.mark.parametrize("s", [" ", None, ""])
def test_ubbi_dubbi_when_no_input_provided_raises_valueerror(s: str):
    with pytest.raises(ValueError):
        list(english_to_ubbi_dubbi(s))
