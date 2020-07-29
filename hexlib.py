import re

_base = 16


def hex_to_int(value: str) -> int:
    int_part = None

    for m in re.finditer(r"\b0{0,1}[xX]{0,1}(?P<value>[0-9a-fA-F]+)\b", value):
        int_part = m.group("value")

    if not int_part:
        raise ValueError("Invalid hex string.")

    int_value = 0

    for i, c in enumerate(reversed(int_part)):
        int_value += int(c, _base) * (16 ** i)

    return int_value
