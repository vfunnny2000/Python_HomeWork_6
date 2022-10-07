# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
os.system('cls')

# # numbers = [1, 2, 2, 3, 3, 4, 5]
numbers = input('Введите числа через пробел: ').split()

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))
# 


# numbers = [1, 2, 2, 3, 3, 4, 5]
# numbers = input('Введите числа через пробел: ').split()
# unique_numbers = list(set(numbers))
# print(unique_numbers)



enum_number = list(map(int, input('enter numbers: ').split()))
enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))
print(enum_number, '->', enum_unique)



