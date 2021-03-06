from turtle import *
import random as r


def generate_colors_list(count):
    colors = []
    alphabet = 'abcdef0123456789'
    for color in range(count):
        col = '#'
        for i in range(6):
            col += r.choice(alphabet)
        colors.append(col)
    return colors


colors = generate_colors_list(15)
t = Turtle()


for i in range(10):
    t.color(r.choice(colors))
    t.fd(200)
    t.rt(120)
    t.fd(40)
    t.goto(0, 0)
    t.lt(84)

done()