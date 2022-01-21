from turtle import *
from random import randint

t = Turtle()
t.pensize(5)
line = 10  # изначальный размер стороны квадрата
colormode(255)  # устанавливаю цветовое пространство RGB
x = 0
y = 0

for i in range(10):
    r = randint(10, 255)
    g = randint(10, 255)
    b = randint(10, 255)
    t.color(r, g, b)

    for j in range(4):
        t.fd(line)
        t.rt(90)
    t.up()
    x -= 10  # изменяю координаты
    y += 10  # изменяю координаты
    t.goto(x, y)  # перехожу в измененные координаты
    t.down()
    line += 20  # увеличиваю длину стороны квадрата





done()