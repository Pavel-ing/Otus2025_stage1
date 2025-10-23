from src.triangle import Triangle
import pytest

@pytest.mark.parametrize(("a", "b", "c", "calc_area", "calc_perimeter"), [(3, 3, 3, 3.897, 9), (3, 4, 5, 6.0, 12)])
def test_triangle_properties(a, b, c, calc_area, calc_perimeter):
    t = Triangle(a, b, c)

    act_area = t.area
    act_perimeter = t.perimeter

    assert round(act_area, 3) == calc_area, f"Triangle area with sides {a}, {b}, {c} must be {t.area} !"
    assert act_perimeter == calc_perimeter, f"Triangle perimeter with sides {a}, {b}, {c} must be {t.perimeter} !"

@pytest.mark.parametrize(("invalid_a", "invalid_b", "invalid_c"), [(1, 2, 3), (-3, 3, 3), (0, 3, 3)])
def test_triangle_zero_negative(invalid_a, invalid_b, invalid_c):
    with pytest.raises(ValueError, match="Triangle with such sides does not exist !"):
        Triangle(invalid_a, invalid_b, invalid_c)