import pytest
from utils import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(50, 10) == 45

def test_calculate_discount_edge_cases():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)
    with pytest.raises(ValueError):
        calculate_discount(-100, 20)