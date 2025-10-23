from src.square import Square
import pytest


@pytest.mark.parametrize(("a", "calc_area", "calc_perimeter"), [(5, 25, 20), (3.5, 12.25, 14)], ids=['int', 'float'])
def test_square_properties(a, calc_area, calc_perimeter):
    s = Square(a)

    act_area = s.area
    act_perimeter = s.perimeter

    assert act_area == calc_area, f"Square area with side {a} must be {s.area} !"
    assert act_perimeter == calc_perimeter, f"Square perimeter with side {a} must be {s.perimeter} !"


@pytest.mark.parametrize("invalid_side", [-3, 0, -5.5])
def test_square_zero_negative(invalid_side):
    with pytest.raises(ValueError, match="Sides can't be less or equal than 0 !"):
        Square(invalid_side)
