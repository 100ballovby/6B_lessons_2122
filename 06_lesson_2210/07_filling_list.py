import random as r
# импортирую модуль random с псевдонимом r

r_list = []  # буду хранить случайные числа тут
for i in range(10):  # повторить 10 раз
    num = r.randint(1, 100)  # randint - random integer
    # случайное число от 1 до 100
    r_list.append(num)  # добавляю случайное число в список

print(r_list)

