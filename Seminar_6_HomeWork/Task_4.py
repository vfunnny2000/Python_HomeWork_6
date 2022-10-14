# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


import os
os.system('cls')


# from itertools import accumulate
# import operator

# n = int(input('Введите число: '))

# def get_prods(N):
#     return list(accumulate([x for x in range(1, n + 1)], operator.mul))

# print(get_prods(n))



from math import factorial

n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)



# def set_products(n: int) -> list:
#     set = [1]
#     for i in range(2, n+1):
#         set.append(set[-1] * i)
#     return set

# n = int(input('Введите натуральное число: '))
# set = set_products(n)
# print(set)