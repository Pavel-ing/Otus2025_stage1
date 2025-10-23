import pytest
from src.figure import Figure
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle

def test_add_area_different_figures():
    figure1 = Rectangle(3, 4)
    figure2 = Circle(3)
    calc = figure1.area + figure2.area

    result = figure1.add_area(figure2)

    assert result == calc

def test_add_area_invalid_type():
    figure = Square(3)

    with pytest.raises(ValueError, match="Should be a Figure !"):
        figure.add_area("invalid_figure")