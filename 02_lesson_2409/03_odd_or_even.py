"""Надо проверить, четное ли число ввели"""
num1 = int(input('Введите число: '))

if (num1 % 2) == 0:
    # (если остаток от деления num1 на 2) равен нулю
    print('Число четное!')  # написать это
else:  # если остаток не равен нулю
    print('Число нечетное!')   # пишем это

print('Остаток от деления: ', num1 % 2)  # выводим получившийся остаток

