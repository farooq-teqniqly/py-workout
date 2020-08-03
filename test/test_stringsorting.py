import pytest

from stringsorting import str_sort_python_builtin


@pytest.mark.parametrize(
    "s,expected", [("farooq rocks", "acfkoooqrrs")],
)
def test_str_sort_python_builtin(s: str, expected: str):
    assert str_sort_python_builtin(s) == expected
