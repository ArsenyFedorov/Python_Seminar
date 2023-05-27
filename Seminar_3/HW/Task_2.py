# Требуется найти в массиве A[1. N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint
my_list = list()
lens = int(input("Ввидите длинну списка:"))
num = int(input("Ввидите искомое число: "))
for i in range(lens):
    my_list.append(randint(-10, 10))
print(my_list)

my_list = list(set(my_list))
my_list.sort()
print(my_list)
if num <= my_list[0]:
    print(f"Число {num} ближе всего к {my_list[0]}")
elif num >= my_list[-1]:
    print(f"Число {num} ближе всего к {my_list[-1]}")
else:
    for i in range(len(my_list)):
        if my_list[i] > num:
            print(f"Число {num} ближе всего к {my_list[i]}")
            break
        elif num < my_list[i + 1]:
            if num - my_list[i] < my_list[i + 1] - num:
                print(f"Число {num} ближе всего к {my_list[i]}")
                break
            else:
                print(f"Число {num} ближе всего к {my_list[i + 1]}")
                break










