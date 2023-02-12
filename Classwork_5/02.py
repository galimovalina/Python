# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

def marks(list):
    min_mark = 5
    max_mark = 0
    for i in range(len(list)):
        if list[i] < min_mark:
            min_mark = list[i]
        elif list[i] > max_mark:
            max_mark = list[i]
    print(min_mark, max_mark)
    print(list)
    for i in range(len(list)):
        if list[i]==min_mark:
            list[i]==max_mark
    return(list)


n = input('Введите оценки: ')
list_1 = list(n)
print(list_1)
marks(list_1)
print(list_1)

# n = int(input('введите количество оценок: '))
# list_1 = []
#
# min_mark = 5
# max_mark = 0
# list_1 = [int(input(f'Введите оценку: ')) for i in range(n)]
# for i in list_1:
# if i < min_mark:
# min_mark = i
# if i > max_mark:
# max_mark = i
# print(min_mark, max_mark)
# print(list_1)
#
# for i in range(len(list_1)):
# if list_1[i] == min_mark:
# list_1[i] = max_mark
# print(list_1)