from src.triangle import Triangle
import pytest

@pytest.fixture
def triangle():
    return Triangle(3,3,3)

def test_area_perimeter(triangle):
    assert round(triangle.area) == 4
    assert triangle.perimeter == 9

def test_triangle_exist():
    with pytest.raises(ValueError, match="Triangle with such sides does not exist ! "):
        Triangle(1,2,3)



