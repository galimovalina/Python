# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = int(input("Введите трехзначное число: "))
# if 100 <= a <= 999:
#     print(a % 10 + (a // 10) % 10 + a // 100)
# else:
#     print("Число не трехзначное")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# summa = int(input())
# p = int(summa // 6)
# k = int(4 * p)
# s = p
# print(f'Петя: {p}, Катя: {k}, Срежа: {s}')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# a = int(input("Введите номер билета: "))
# if 100000 <= a <= 999999:
#     b = a % 1000
#     sum1 = (b % 10 + (b // 10) % 10 + b // 100)
#     a = a // 1000
#     sum2 = (a % 10 + (a // 10) % 10 + a // 100)
#     if sum1 == sum2:
#         print('yes')
#     else:
#         print('no')
# else:
#     print('Неправильный номер билета')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input())
# m = int(input())
# k = int(input())
# if k % n == 0 or k % m == 0 and k < n * m:
#     print('yes')
# else:
#     print('no')
