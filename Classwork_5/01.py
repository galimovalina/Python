# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

def fibonacci(num):
    if num == 1 or num == 2:
        fib = 1
    elif num == 0:
        fib = 0
    else:
        fib = fibonacci(num - 1) + fibonacci(num - 2)
    return fib


n = int(input())
print(fibonacci(n))
