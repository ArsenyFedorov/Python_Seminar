# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
from typing import Callable


def same_by(func: Callable, list_obj: list) -> bool:
    result = list()
    for i in list_obj:
        result.append(func(i))
    if len(set(result)) == 1:
        return True
    return False


my_list = [0, 2, 4, 6, 8]
print(same_by(lambda x: x % 2 == 0, my_list))
