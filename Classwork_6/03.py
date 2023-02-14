# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

list_1 = []
while True:
    number = int(input())
    if number == 0:
        break
    list_1.append(number)
count_dict = {}
for el in list_1:
    if count_dict.get(el):
        count_dict[el] += 1
    else:
        count_dict[el] = 1
print(count_dict)
