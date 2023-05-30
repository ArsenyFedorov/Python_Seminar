# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
import random
my_list = [random.randint(0, 10) for _ in range(20)]
print(my_list)

my_dict = dict()

for i in my_list:
    my_dict[i] = my_dict.get(i, 0) + 1
    print(i if my_dict.get(i) < 2 else str(i) + "_" + str(my_dict.get(i) - 1), end="   ")

