# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# ****************     С Т А Л О    *****************************

import os
os.system('cls')

from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки через пробел: ').split()))
dot_2 = list(map(int, input('Введите две координаты второй точки через пробел: ').split()))
def dot_range(dot_1, dot_2):
    rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
    return round(rng, 2)

print(f'Расстояние между точками равно->  {dot_range(dot_1, dot_2)}')


# *****************    Б Ы Л О    *******************

# import os
# os.system('cls')

# x1 = int(input('Enter coordinate х1: '))
# y1 = int(input('Enter coordinate y1: '))
# x2 = int(input('Enter coordinate х2: '))
# y2 = int(input('Enter coordinate y2: '))
# import math
# sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
# print(f'Distance: (A - ({x1}, {y1}) between B - ({x2}, {y2}) = {sqrt}')





