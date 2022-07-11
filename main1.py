# x1=int(input('Введите первое число '))
# x2=int(input('Введите второе число '))
#
# def summa(a,b):
#     z=a+b
#     print(f'сумма равна {z}')
#     return z
# summa(x1,x2)

# Задачи:
#
# 1.
# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.
# *Примеры: *
#
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет

# a=int(input('Введите первое число '))
# b=int(input('Введите второе число '))
# def kvadrat(a,b):
#     if a == b ** 2:
#         print('Число a является квадратом числа b')
#     elif b == a ** 2:
#         print('Число b является квадратом числа a')
#     else:
#         print('Ни одно из чисел не является квадратом другого')
# kvadrat(a,b)




#№3
# for i in range(-5, 5):
#     print(i)
#№4
# num = float(input('Введите дробное число\n'))
# drob = int(num*10%10)
# print(drob)









#№5
num=int(input('Введите число '))
def krat(a):
    if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and not (num % 30 == 0):
        print('da')
    else:
        print('net')
krat(num)



