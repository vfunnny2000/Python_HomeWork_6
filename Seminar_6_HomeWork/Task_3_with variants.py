# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
os.system('cls')

************   С Т А Л О    **********

# unique_number = list(map(int, input('enter numbers: ').split()))
# unique_unique = list(filter(lambda item: unique_number.count(item) == 1, unique_number))
# print(unique_number, '->', unique_unique)


# Another variant

a = [1, 2, 3, 5, 1, 5, 3, 10, 100]
print(a)

res = list(filter(lambda x: a.count(x)==1, a))
# res = [x for x in a if a.count(x)==1]
print(res)




# # numbers = [1, 2, 2, 3, 3, 4, 5]
# numbers = input('Введите числа через пробел: ').split()

# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)

#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)

#     return list_of_unique_numbers

# print(get_unique_numbers(numbers))
# 


# numbers = [1, 2, 2, 3, 3, 4, 5]
# numbers = input('Введите числа через пробел: ').split()
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# 