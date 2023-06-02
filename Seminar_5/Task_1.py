#  Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи
def fib(num: int) -> int:
    if num in [0, 1]:
        return num
    return fib(num - 1) + fib(num - 2)
num_fib = int(input("Ввидите номер числа фибоначи:"))
print(fib(num_fib))

