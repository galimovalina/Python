# with open('test', 'r', encoding='utf-8') as file:
#     # text=file.read().splitlines()
#     # print(text)
#     while True:
#         line=file.readline()
#         if not line:
#             break
#         print(line.strip())

# with open('filetest.txt', 'w', encoding='utf-8') as file:
#     some_list=['hello', 'bye']
#     for word in some_list:
#         file.write(word+'\n')


# Посчитать кол-во искомых букв в фйле
# import time
# with open('test', 'r', encoding='utf-8') as file:
#     find_letter=input()
#     count=0
#     start=time.time()
#     for letter in file.read():
#         if letter == find_letter:
#             count+=1
#     end=time.time()
#     print(count)
#     print(end-start)
#
#     with open('test', 'r', encoding='utf-8') as file:
#         find_letter = input()
#         start = time.time()
#         print(file.read().count(find_letter))
#         end=time.time()
#         print(end - start)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input())
some_list = [random.randint(-n, n) for _ in range(n)]
print(some_list)
with open('file.txt', 'w', encoding='utf-8') as file:
    for _ in range(random.randint(1, n)):
        file.write(str(random.randint(0, n - 1)) + '\n')
with open('file.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)
