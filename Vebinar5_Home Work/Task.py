# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))

# def degree(a, b):
#     if b == 0:
#         return 1
#     return a * degree(a, b - 1)
# print(degree(a, b))


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

print(sum(a, b))