# Дан список чисел. Определите, сколько в нем встречается различных чисел.

list_1 = list()
# a=int(input('Введите количество чисел в списке: '))
# k=0
# for i in range(a):
#     n = int(input())
#     list_1.append(n)
# print(list_1)
# set_1 = set()
# for i in range(len(list_1)):
#     set_1.add(list_1[i])
# for i in range(len(set_1)):
#     k+=1
# print(set_1)
# print(k)

a = int(input('Введите количество чисел в списке: '))
set_1 = set()
k = 0
for i in range(a):
    n = int(input())
    list_1.append(n)
    set_1.add(list_1[i])
print(list_1)
print(set_1)
for i in range(len(set_1)):
    k += 1
print(k)
