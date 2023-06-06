# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
import random

my_list = [random.randint(0, 10) for _ in range(10)]
count = 0

for i in range(len(my_list) - 1):
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        count += 1
if my_list[0] < my_list[-1] > my_list[-2]:
    count += 1

print(my_list)
print(count)
