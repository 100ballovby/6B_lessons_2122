# TODO: написать программу, которая
#  меняет знак числа. Если ввели отрицательное,
#  надо сделать число положительным. Если число
#  положительное, с ним ничего делать не нужно. Если число 0,
#  нужно написать, что 0 не принимается.
num = int(input('Введите число: '))

if num < 0:
    num = num * -1  # меняю знак числа
    print(f'Я поменял знак числа: {num}')
elif num == 0:
    print('Число 0 не принимается!')
else:
    print(f'Число: {num}.')

