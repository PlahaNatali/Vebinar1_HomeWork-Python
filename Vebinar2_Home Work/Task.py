# # На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint

# countN = int(input("Введите число монеток: "))
# tailside = 0
# other_side = 0
# count = 0
# for i in range(countN):
#     x = randint(0, 1)
#     if x == 0:
#         other_side += 1
#     else:
#         tailside += 1
#     print(x)
# if other_side >= tailside:
#     count = countN - other_side
# else:
#     count = countN - tailside
# print('Минимальное количество монет, которые нужно перевернуть:', count)



# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# sum = int(input('Введите сумму чисел: '))
# product = int(input('Введите произведение этих чисел: '))
# c = 0
# for x in range (0, 1000):
#     if c: break
#     for y in range (0, 1000):
#         if x + y == sum and x * y == product:
#             c = 1
#             print(x)
#             print(y)
#             break
# else:
#     print('Петя задумал не эти числа') 



# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
m = 1
while m <= n:
    print(m)
    m = m * 2