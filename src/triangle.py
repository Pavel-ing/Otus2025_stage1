from figure import Figure

class Triangle(Figure):
    def __init__(self,a,b,c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle with such sides does not exist ! ")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError ("All sides in triangle must be greater than 0 ! ")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# t = Triangle(3, 3, 3)
# print(t.perimeter)
# print(t.area)
