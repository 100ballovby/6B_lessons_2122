from turtle import *
from random import randint

t = Turtle()
colormode(255)
t.speed(0)
line = 10  # длина линии квадратной спирали

for i in range(1000):
    r = randint(10, 255)
    g = randint(10, 255)
    b = randint(10, 255)
    t.color(r, g, b)
    t.fd(line)
    t.rt(90)

    line += 10

done()