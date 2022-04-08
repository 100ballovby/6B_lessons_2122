from turtle import *


t = Turtle()


def spiral(obj, size, deg):
    steps = 5
    for i in range(size):
        obj.fd(steps)
        obj.lt(deg)
        steps += 5


spiral(t, 100, 121)

done()
