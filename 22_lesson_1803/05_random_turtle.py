from turtle import *
import random as r


def draw_circle(turt, x, y, col, rad):
    turt.up()  # поднять перо
    turt.goto(x, y)  # перейти в координаты
    turt.down()  # опустить перо
    turt.color(col)  # установить цвет
    turt.dot(rad)  # нарисовать круг с определенным радиусом

t = Turtle()
t.speed(0)
colors = ['red', 'green', 'purple', 'blue', 'yellow', 'orange']
for i in range(1000):
    x = r.randint(-400, 400)
    y = r.randint(-400, 400)
    rad = r.randint(20, 80)
    color = r.choice(colors)  # достаю случайный элемент из списка цветов
    draw_circle(t, x, y, color, rad)

done()
