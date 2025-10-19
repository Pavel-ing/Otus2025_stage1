from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, a):
        if a <= 0 :
            raise ValueError("Sides can't be less or equal than 0 ! ")
        super().__init__(a,a)