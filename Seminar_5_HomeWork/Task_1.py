# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# newTxt = 'абвгедейка это детская передача. абвгдейка это учеба и игра'


import os
os.system('cls')

# with open('file.txt', 'r') as data:
#     text = data.read()
#     print('Исходный текст: ', text)

# find_txt = "абв"
# lst = [i for i in text.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')



incoming_text = 'абвгедейка это детская передача. абвгдейка это учеба и игра'

def del_words(incoming_text):
    incoming_text = list(filter(lambda x: 'абв' not in x, incoming_text.split()))
    return " ".join(incoming_text)

incoming_text = del_words(incoming_text)
print(incoming_text)




