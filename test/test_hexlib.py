import pytest

from hexlib import hex_to_int


@pytest.mark.parametrize(
    "hex_value, int_value", [("0x50", 80), ("0x6512", 25874), ("0x0", 0)]
)
def test_hex_to_int(hex_value: str, int_value: int):
    assert hex_to_int(hex_value) == int_value


@pytest.mark.parametrize(
    "hex_value, int_value", [("50", 80), ("6512", 25874), ("0", 0)]
)
def test_hex_to_int_without_0x_prefix(hex_value: str, int_value: int):
    assert hex_to_int(hex_value) == int_value


@pytest.mark.parametrize(
    "hex_value, int_value", [("x50", 80), ("x6512", 25874), ("x0", 0)]
)
def test_hex_to_int_with_x_prefix(hex_value: str, int_value: int):
    assert hex_to_int(hex_value) == int_value
    assert hex_to_int(hex_value.upper()) == int_value


@pytest.mark.parametrize("invalid_value", ["g", "h", "ag"])
def test_hex_to_int_raises_error(invalid_value: str):
    with pytest.raises(ValueError):
        hex_to_int(invalid_value)
