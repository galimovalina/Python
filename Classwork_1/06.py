# Пользователь вводит строки пока не введет пустую. Гарантируется что в строках лежат только цифры
# Найти сумму введенных чисел, которые кратны 4

summa = 0
while True:
    a = input()
    if a == '':
        break
    if int(a) % 4 == 0:
        # summa == summa + int(a)
        summa += int(a)
print(summa)
