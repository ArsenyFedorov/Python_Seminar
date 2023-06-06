# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве

import random

my_list = [random.randint(0, 10) for i in range(10)]
next_list = [random.randint(0, 10) for i in range(5)]
final_list = list()

for i in range(len(my_list)):
    if not my_list[i] in next_list:
        final_list.append(my_list[i])

print(my_list)
print(next_list)
print(final_list)