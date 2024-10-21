import pytest

def test_utility_function():
    result = 2 + 2
    assert result == 4, "Basic math should work"

def test_utility_function_error():
    with pytest.raises(ZeroDivisionError):
        1 / 0