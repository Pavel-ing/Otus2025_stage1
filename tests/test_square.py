from src.square import Square
import pytest

def test_area():
    s = Square(5)
    assert s.area == 25, f"Square area with sides 5 must be 25"

def test_perimeter():
    s = Square(5)
    assert s.perimeter == 20, f"Square perimeter with sides 5 must be 20"

def test_zero():
    with pytest.raises(ValueError, match="Sides can't be less or equal than 0 !"):
        Square(0)
