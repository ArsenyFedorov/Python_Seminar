# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
from random import randint
lis = list()
lens = int(input("Ввидите длинну списка:"))
for i in range(lens):
    lis.append(randint(0, 10))
print(lis)
k = int(input("Ввидите длинну отступа:"))
for i in range(k):
    lis.insert(0, lis.pop())
print(lis)

