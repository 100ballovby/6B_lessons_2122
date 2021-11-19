# Найдите сумму  1+2+3+…+n, где число n вводится пользователем с клавиатуры.
n = int(input('Введите число: '))
summary = 0

for i in range(1, n + 1):
    summary += i

print(summary)


