# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

import os
os.system('cls')

n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))

