# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


# a = int(input('Enter day number (1-7): '))
# week = ['Monday', 'Tuesday', 'Wendsday',
#         'Thursday', 'Friday', 'Saturday', 'Sunday']
# if a in range(1, 8):
#     if a in range(1, 6):
#         print(week[a-1], ' - Its a workday today(')
#     else:
#         print(week[a-1], ' - Your lucky, its a holiday!')
# else:
#     print('Your make mistake, try another number.')
    
    

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
n = int(input("Введите число, обозначающее день недели: "))
print(f"{days[n-1]} - рабочий день") if 0 < n < 6 else print(f"{days[n-1]} - выходной день")