# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def sum_num(num_1: int, num_2: int) -> int:
    num_1 += 1
    num_2 -= 1
    if num_2 > 0:
        return sum_num(num_1, num_2)
    return num_1

print(sum_num(2, 5))
