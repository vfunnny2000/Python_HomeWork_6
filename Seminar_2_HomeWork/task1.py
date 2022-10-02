# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


                                #           ВАРИАНТ 1
import os
os.system('cls')

s = input("Enter your number: ")
number = sum(int(i) for i in str(s) if i.isdigit())
print(number)


                                #           ВАРИАНТ 2

# import os
# os.system('cls')

# number = input('Введите число = ')
# sum = 0
# for item in number:
#     if item.isdigit():
#         # print(item)
#         sum += int(item)
# print(sum)    