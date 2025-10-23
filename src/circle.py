from figure import Figure
import math

class Circle(Figure):
    def __init__(self,r):
        if r <= 0:
            raise ValueError ("Radius of a circle can't be less or equal than 0 !")
        self.r = r

    @property
    def perimeter(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r ** 2
