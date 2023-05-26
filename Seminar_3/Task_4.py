# Дан список, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка,
# больших предыдущего (элемента с предыдущим номером)
from random import randint
lis = list()
lens = int(input("Ввидите длинну списка:"))
for i in range(lens):
    lis.append(randint(0, 10))
print(lis)
count = 0
for i in range(len(lis)-1):
    if lis[i] < lis[i+1]:
        count += 1
print(count)