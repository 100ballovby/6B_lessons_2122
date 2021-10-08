import random as r

num = r.randint(-100, 100)
# псевдослучайное число в промежутке от -100 до 100
print(f'Число: {num}.')

# TODO: проверить, принадлежит ли число
#  промежутку от 10 до 20
"""
Есть 3 варианта проверки числовых промежутков:

1. if x >= 10 and x <= 20
2. if 10 <= x <= 20
3. if x in range(10, 21)
"""
if 10 <= num <= 20:
    print(f'Число {num} принадлежит промежутку [10;20]')
else:
    print(f'Число {num} не принадлежит промежутку [10;20]')