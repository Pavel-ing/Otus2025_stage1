from src.circle import Circle
import pytest
import math

@pytest.mark.parametrize ("r,calc_area,calc_perimeter", [
    (3, math.pi*3**2, 2*math.pi*3),
    (7, math.pi*7**2, 2*math.pi*7)])
def test_area_perimeter(r,calc_area,calc_perimeter):
    circle = Circle(r)

    act_area = circle.area
    act_perimetr = circle.perimeter

    assert act_area == calc_area
    assert act_perimetr == calc_perimeter

@pytest.mark.parametrize ("invalid_rad", [
    0,-1,-3,-7])
def test_circle_zero(invalid_rad):
    with pytest.raises(ValueError, match="Radius of a circle can't be less or equal than 0 !"):
        Circle(invalid_rad)
