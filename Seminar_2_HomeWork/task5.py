# Реализуйте алгоритм перемешивания списка.

# import random

import os
os.system('cls')

from random import Random, randint

N = int(input('Введите количество элементов списка: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
print(numbers, '<- Original list')

def mixed(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(mixed(numbers), '<- Mixed list')



# import os
# os.system('cls')

# import random
# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     return list
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Primary list: ")
# print(list)
# print("Mixed list: ")
# print(mixed_list)



# import os
# os.system('cls')

# import random

# # initializing list
# test_list = [1, 4, 5, 6, 3, 7]

# # Printing original list
# print ("The original list is : " + str(test_list))

# # using random.sample()
# # to shuffle a list
# res = random.sample(test_list, len(test_list))

# # Printing shuffled list
# print ("The shuffled list is : " + str(res))




# import random

# lenght = 5
# list = [i for i in range (lenght)]

# print(list, '<-- original')

# for i in range(len(list)):
#     r = random.randint(i,lenght-1)
#     m = list[i]
#     list[i] = list[r]
#     list[r] = m

# random.shuffle(list)
# print(list, '<-- shuffle')