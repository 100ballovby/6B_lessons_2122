a = 15
b = 3

tmp = a  # tmp = 15
a = b  # a = 3
b = tmp  # b = 15
print(a)
print(b)

a, b = b, a  # кортежное присваивание 
print(a)  # 15
print(b)  # 3
