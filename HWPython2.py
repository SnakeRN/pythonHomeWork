# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = None
# def sum(num):
#     num = float(input("Введите число: "))
#     num = str(num)
#     num = num.replace('.', '')
#     num = int(num)
#     sum = 0
#     while (num != 0):
#         sum = sum + num % 10
#         num = num // 10
#     print("Сумма цифр числа равна: ", sum)
# sum(num)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input("Введи число: "))
# num = None
# def fact(n):
#     n = int(input("Введи число: "))
#     f = 1
#     for i in range(1, n + 1):
#         f = f * i
#         print(f)
#
# fact(num)