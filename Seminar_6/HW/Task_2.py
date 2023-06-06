# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min_num = int(input("Ввидите минимальное значение:"))
max_num = int(input("Ввидите максимальное значение:"))
print(range_list := [i for i in range(min_num, max_num + 1)])
print(my_list := [random.randint(0, 15) for _ in range(20)])
final_list = list()

for i in range(len(my_list)):
    if my_list[i] in range_list:
        final_list.append(i)

print(final_list)
