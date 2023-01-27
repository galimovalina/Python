# Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.

'''a = int(input("Введите число: "))
if 1000 <= a <= 9999 or -9999 <= a <= -1000:
    print('YES')
else:
    print('NO')'''

a = (input("Введите число: "))
if '-' in a:
    if len(a) == 5:
        print('YES')
    else:
        print('NO')
else:
    if len(a) == 4:
        print('YES')
    else:
        print('NO')
