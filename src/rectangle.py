from figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Sides can't be less or equal than 0 ! ")
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b)*2

# r = Rectangle(3, 5)
# print(r.area)
# print(r.perimeter)