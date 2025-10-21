from src.rectangle import Rectangle
import pytest

@pytest.mark.parametrize (("a","b","area","perimeter"),[(3,5,15,16), (3.5,5.5,19.25,18)],ids=['int','float'])

def test_rectangle_1(a,b,area,perimeter):
    r = Rectangle(a,b)
    assert r.area == area, f"Rectangle area with 3 and 5 must be 15 !"
    assert r.perimeter == perimeter, f"Rectangle perimeter with 3 and 5 must be 16 !"
    print ("Тест пройден!")

def test_rectangle_2():
    with pytest.raises(ValueError, match="Sides can't be less or equal than 0"):
        Rectangle(-1,5)




