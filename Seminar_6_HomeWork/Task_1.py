# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.


import os
os.system('cls')

# *******С Т А Л О********

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)


# ********************   Б Ы Л О    **************************
# number = int(input('Введите размер списка '))
# list = []
# sum = 0
# for i in range(number):
#     list_number = int(input(f'Введите число {i+1} '))
#     list.append(list_number)
#     if i % 2 != 0:
#         sum += list[i]

# print(list)

# print(f'Сумма элементов на нечетных позициях равна {sum}')



# import os
# os.system('cls')

# def ask_number_list():
#     str_list = input('Введите числа через пробел: ').split(' ')
#     number_list = []
#     for val in str_list:
#         if(val.isdigit()):
#             number_list.append(int(val))
#     return number_list

# def sum_odd_numbers(list_numbers):
#     sum = 0
#     for i,val in enumerate(list_numbers):
#         if(not i%2 == 0):
#             sum += val
#     return sum

# numbers = ask_number_list()


# print(f'{numbers} -> сумма элементов на нечетной позиции = {sum_odd_numbers(numbers)}')



