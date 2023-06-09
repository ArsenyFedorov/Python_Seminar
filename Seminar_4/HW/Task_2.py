'''
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''
from random import randint
bush = int(input("Ввидите количество  кустов: "))
my_dictionary = dict()

for k in range(bush):
    my_dictionary[k] = randint(0, 50)
print(my_dictionary)

berry_max = my_dictionary[bush - 1] + my_dictionary[0] + my_dictionary[1]
num_bush = 0

for i in range(1, bush):
    if i == bush - 1:
        if berry_max < my_dictionary[i - 1] + my_dictionary[i] + my_dictionary[0]:
            berry_max = my_dictionary[i - 1] + my_dictionary[i] + my_dictionary[0]
            num_bush = i
    else:
        if berry_max < my_dictionary[i - 1] + my_dictionary[i] + my_dictionary[i + 1]:
            berry_max = my_dictionary[i - 1] + my_dictionary[i] + my_dictionary[i+1]
            num_bush = i


print(f"Максимальное количество ягод = {berry_max} , можно собрать если подъехать к {num_bush }-ому кусту")
