# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в cписке .
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X"
from random import randint
my_list = list()
lens = int(input("Ввидите длинну списка:"))
num = int(input("Ввидите искомое число "))
count = 0
for i in range(lens):
    my_list.append(randint(0, 10))
print(my_list)
for i in range(len(my_list)):
    if my_list[i] == num:
        count += 1
print(f"Число {num} встречается {count} раз")
