# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
import random


def mark(list_mark: list) -> list:
    for i in range(len(list_mark)):
        if list_mark[i] == max(list_mark):
            list_mark[i] = min(list_mark)
    return list_mark
my_list = [random.randint(1, 5) for i in range(10)]
print(my_list)
print(mark(my_list))
