# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
len_first = int(input("Ввидите первую длину:"))
len_second = int(input("Ввидите вторую длину:"))

first_list = list()
while len_first > 0:
    num = int(input("Ввидите элемент 1-ого  набора:"))
    first_list.append(num)
    len_first -= 1
print(f"Первое множество {first_list}")
first_list = set(first_list)


second_list = list()
while len_second > 0:
    num = int(input("Ввидите элемент 2-ого набора:"))
    second_list.append(num)
    len_second -= 1
print(f"Второе множество {second_list}")
second_list = set(second_list)

my_set = first_list.intersection(second_list)
print(f"{sorted(list(my_set))} Общие значения")


