import random as r
from turtle import *
from hw import generate_colors_list
from itertools import cycle  # превращает последовательность в особый объект, по которому можно циклично проходить

colors = generate_colors_list(5)
colors.sort()
colors = cycle(colors)


def nautilus(turt, angle, length):
    if length >= 300:
        return None
    else:
        turt.color(next(colors))
        for i in range(4):
            turt.fd(length)
            turt.rt(90)
        turt.lt(angle)
        nautilus(turt, angle, length + 3)

t = Turtle()
t.pensize(2)
t.speed(0)

nautilus(t, 10, 3)

done()


