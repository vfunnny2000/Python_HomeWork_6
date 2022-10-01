# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


import os
os.system('cls')

def set_products(n: int) -> list:
    set = [1]
    for i in range(2, n+1):
        set.append(set[-1] * i)
    return set

n = int(input('Введите натуральное число: '))
set = set_products(n)
print(set)