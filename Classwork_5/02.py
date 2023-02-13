# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

import time

magazine = [int(input('Введите оценку: ')) for _ in range(int(input('Введите кол-во оценок: ')))]

start = time.perf_counter()
minn = magazine[0]
maxx = magazine[0]
for el in magazine:
    if el < minn:
        min = el
    elif el > maxx:
        maxx = el
end = time.perf_counter()
print(end - start)

for ind in range(0, len(magazine)):
    if magazine[ind] == maxx:
        magazine[ind] = minn
print(magazine)
