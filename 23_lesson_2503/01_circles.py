from hw import generate_colors_list
from turtle import *
from itertools import cycle


colors = generate_colors_list(100)
colors.sort()
colors = cycle(colors)


def circletilius(turt, angle, rad):
    if rad >= 250:
        return None
    else:
        turt.color(next(colors))
        turt.circle(rad)
        turt.rt(angle)
        circletilius(turt, angle, rad + 1)

t = Turtle()
t.speed(0)
circletilius(t, 27, 5)

done()


