# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите число: "))
summa = 0
while number > 0:
    ost = number % 10
    summa = summa + ost
    number = number // 10
print(summa)