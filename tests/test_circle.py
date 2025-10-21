from src.circle import Circle
import pytest

@pytest.fixture
def circle():
    return Circle(3)

def test_area_perimeter(circle):
    assert circle.area == 28.26
    assert circle.perimeter == 18.84

def test_circle_zero():
    with pytest.raises(ValueError, match="Radius of a circle can't be less or equal than 0 !"):
        Circle(-3)
