# Напишите функцию, которая принимает одно число и проверяет является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
def just(num: int) -> bool:
    if num in [1, 2]:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(just(7))
