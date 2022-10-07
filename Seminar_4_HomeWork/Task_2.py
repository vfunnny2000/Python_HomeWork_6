# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


import os
os.system('cls')


# n = int(input('Enter your number: '))
# while n > 1:
#     i = 2
#     f = 0
#     while 1:
#         if n%i == 0:
#             n = n // i
#             print(i, end=' ')
#             f = 1
#             break
#         else:
#             i += 1
#     if f == 1:
#         continue
# print()


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то странное число! Попробуйте еще раз-)")
    return number


def func_search(num):
    result = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            result.append(i)
    return result


num = InputNumbers("Введите натуральное число N: ")


print(f"Список простых множителей числа '{num}': {func_search(num)}")


# import math
# def primefactors(n):
#    #even number divisible
#    while n % 2 == 0:
#       print (2),
#       n = n / 2

#    #n became odd
#    for i in range(3,int(math.sqrt(n))+1,2):

#       while (n % i == 0):
#          print (i)
#          n = n / i

#    if n > 2:
#       print (n)

# n = int(input("Enter the number for calculating the prime factors :\n"))
# primefactors(n)
