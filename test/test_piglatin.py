import pytest
from piglatin import pig_latinize


@pytest.mark.parametrize(
    "original,expected_pig_latinized",
    [("inside job", "insideway objay"), ("i am groot", "iway amway rootgay")],
)
def test_latinize(original: str, expected_pig_latinized: str):
    assert list(pig_latinize(original)) == expected_pig_latinized.split(" ")


@pytest.mark.parametrize("s", [" ", None, ""])
def test_latinize_when_no_input_provided_raises_valueerror(s: str):
    with pytest.raises(ValueError):
        list(pig_latinize(s))
