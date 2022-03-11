def factor(n):
    res = 1  # начало отсчета
    for i in range(1, n + 1):  # 1, 2, 3, ....., n
        res *= i  # факториал - произведение всех чисел от 1 до n
    return res


def factor_recursive(n):  # рекурсивная функция подсчета факториала
    if n == 0:
        return 1
    else:
        return n * factor_recursive(n - 1)


def summary(n):
    if n == 1:
        return 1
    else:
        return n + summary(n - 1)

print(summary(4))


