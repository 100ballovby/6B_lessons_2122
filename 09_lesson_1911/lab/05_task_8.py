# задача про ферзя
x1 = int(input('Введите х1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите х2: '))
y2 = int(input('Введите y2: '))

if abs(x1 - y1) == abs(x2 - y2) or (x1 == x2) or (y1 == y2):  # abs - модуль числа
    print('YES')
else:
    print('NO')



