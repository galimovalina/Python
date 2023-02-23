# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     if lines < 0:
#         print('Введите положительное число')
#     else:
#         with open(file, 'r', encoding='utf-8') as file:
#             text = file.readlines()
#             last_line = len(text) - lines
#             while last_line != len(text):
#                 print(text[last_line])
#                 last_line += 1
#
#
# with open('article.txt', 'w', encoding='utf-8') as file:
#     file.write(
#         'Вечерело\n' + 'Жужжали мухи\n' + 'Светил фонарик\n' + 'Кипела вода в чайнике\n' + 'Венера зажглась на небе\n' + 'Деревья шумели\n' + 'Тучи разошлись\n' + 'Листва зеленела\n')
# lines = int(input('Введите кол-во строк: '))
# read_last(lines, 'article.txt')

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text = file.read().split()
#         max_words = list()
#         maxx = 0
#         for ind in range(len(text)):
#             if maxx < len(text[ind]):
#                 maxx = len(text[ind])
#         for ind in range(len(text)):
#             if maxx == len(text[ind]):
#                 max_words.append(text[ind])
#         return (max_words)
#
#
# print(longest_words('article.txt'))
