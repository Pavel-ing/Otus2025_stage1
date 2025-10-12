from figure import Figure
from src.triangle import Triangle


class Circle(Figure):
    def __init__(self,r):
        if r <= 0:
            raise ValueError ("Radius of a circle can't be less or equal than 0 !")
        self.r = r

    @property
    def perimeter(self):
        return 2 * 3.14 * self.r

    @property
    def area(self):
        return 3.14 * self.r ** 2