# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

n = int(input())
factorial = 1
count = 1
while count <= n:
    factorial *= count
    count += 1
print(factorial)
