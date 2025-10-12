#from collections.abc import async_generator

class rectangle:
    def __init__(self, side_a: int, side_b:int):
        self.side_a = side_a
        self.side_b = side_b
        if self.side_a < 0 or self.side_b < 0:
            raise ValueError(f'Sides of rectangle should be greater then zero!!!')
            print ("ОШИБКА!", self.side_a, "не можеты быть меньше 0")

    @property
    def perimetr(self):
        return (self.side_a + self.side_b) * 2

    @property
    def area(self):
        return self.side_a * self.side_b


r = rectangle(side_a=0,side_b=-5)

print (r.perimetr)
print (r.area)



# class Human:
#      def __init__(self, gender: str, age: int):
#          self.gender = gender
#          self.age = age
#
# h = Human (gender='W', age=35)
# print(h.gender)
# print(h.age)

# x = int(input('Введите число:'))
# if x == 5:
#     print("Ты угадал")
# else: print("Попробуй ещё")

import struct
from ctypes import HRESULT


# a = ".... vasya .....  "
# b = a.strip(".")
# b = a.strip()
# print(b.title())

# def calculate_average(nums):
#     total = sum(nums)
#     count = len(nums)
#     average = total / count
#     return average
#
#
# nums = [10, 15, 20]
# result = calculate_average(nums)
# print("The average is:", result)

