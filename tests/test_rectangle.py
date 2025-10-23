from src.rectangle import Rectangle
import pytest

@pytest.mark.parametrize (("a","b","calc_area","calc_perimeter"),[(3,5,15,16), (3.5,5.5,19.25,18)],ids=['int','float'])

def test_rectangle_option(a,b,calc_area,calc_perimeter):
    r = Rectangle(a,b)

    act_area = r.area
    act_perimeter = r.perimeter

    assert act_area == calc_area, f"Rectangle area with {a} and {b} must be {r.area} !"
    assert act_perimeter == calc_perimeter, f"Rectangle perimeter with {a} and {b} must be {r.perimeter} !"

@pytest.mark.parametrize (("invalid_a","invalid_b"),[(-3,5), (3,-5), (0,7)])
def test_rectangle_zero_negative(invalid_a, invalid_b):
    with pytest.raises(ValueError, match="Sides can't be less or equal than 0"):
        Rectangle(invalid_a, invalid_b)