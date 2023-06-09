# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
from typing import Callable


def print_operation_table(operation: Callable, num_rows: int = 6, num_columns: int = 6):
    # Эта функция имеет ужасное название
    # но она делает то что требует задача
    for i in range(1, num_rows + 1):
        my_list = []
        for j in range(1, num_columns + 1):
            my_list.append(operation(i, j))
        print(*my_list)


print_operation_table(lambda x, y: x * y)
