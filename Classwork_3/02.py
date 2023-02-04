# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

list_1 = [5, 4, 6, 7, 8, -10]
k = 3

list_result = list()
for i in range(k):
    list_result.append(list_1[len(list_1) - 1 - i])
    print(list_result)
print(1)
for i in range(len(list_1) - k):
    list_result.append(list_1[i])
    print(list_result)
print(list_result)