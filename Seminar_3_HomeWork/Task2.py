# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
os.system('cls')

import os
import math

def ask_number_list():
    str_list = input('Введите числа через пробел: ').split(' ')
    number_list = []
    for val in str_list:
        if(val.isdigit()):
            number_list.append(int(val))
    return number_list

def mult_pairs(list_numbers):
    mult_list = []
    length = len(list_numbers)
    for i in range(math.ceil(length/2)):
        mult_list.append(list_numbers[i]*list_numbers[length-i-1])
    return mult_list

num = ask_number_list()
print(f'{num} произведение пар чисел => {mult_pairs(num)}')




