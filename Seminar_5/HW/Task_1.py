# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def degree(num: int, num_2: int) -> int:
    if num_2 == 1:
        return num
    return num * degree(num, num_2 - 1)

user_num = int(input("Ввидите число:"))
user_degree = int(input("В какую целую степень хотите возвести:"))
print(f"Ваше число в {user_degree}-ой степени равно:{degree(user_num, user_degree)}")
