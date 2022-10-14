# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# ******** С Т А Л О *********

import os
os.system('cls')

# lst = [2, 3, 4, 2, 5, 2, 5]

# def multy_bi(lst):
#     return [lst[i] * lst[len(lst)-1 -i] for i in range(len(lst)//2 + len(lst)%2)]

# print(multy_bi(lst))



# *****************   Е Щ Е    В А Р И А Н Т    ***********************

list_in = [2, 3, 4, 5, 6, 0]
list_out = []

len_count = len(list_in)
len_count = len_count//2

# # Строка рабочая но для читаемости срезы были сделаны отдельно
list_out = list(map(lambda x, y: x*y, list_in [0:len(list_in)-len_count:1], list_in [-1:-(len(list_in)+1-2):-1]))

# list_cut = list_in [0:len(list_in)-len_count:1]
# list_cut_rev = list_in [-1:-(len(list_in)+1-2):-1]
# list_out = list(map(lambda x, y: x*y, list_cut, list_cut_rev))

print (list_out)

# **********  Б Ы Л О  *************
# import os
# os.system('cls')

# import os
# import math

# def ask_number_list():
#     str_list = input('Введите числа через пробел: ').split(' ')
#     number_list = []
#     for val in str_list:
#         if(val.isdigit()):
#             number_list.append(int(val))
#     return number_list

# def mult_pairs(list_numbers):
#     mult_list = []
#     length = len(list_numbers)
#     for i in range(math.ceil(length/2)):
#         mult_list.append(list_numbers[i]*list_numbers[length-i-1])
#     return mult_list

# num = ask_number_list()
# print(f'{num} произведение пар чисел => {mult_pairs(num)}')