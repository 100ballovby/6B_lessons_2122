from turtle import *
import random as r

t = Turtle()
t.speed(0)

red = 0
g = r.randint(0, 255)
b = r.randint(0, 255)
i = 1
while i < 256:
    colormode(255)
    t.color(red, g, b)

    t.fd(50 + i)
    t.rt(91.5)
    i += 1  # увеличиваю i на 1
    red += 1

done()
