# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
from random import randint
lis = list()
lens = int(input("Ввидите длинну списка:"))
for i in range(lens):
    lis.append(randint(0, 10))

print(lis)
lis = set(lis)
print(lis)
print(len(lis))

