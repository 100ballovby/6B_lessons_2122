from turtle import *


def spiral(obj, angle):
    size = 250
    while size > 0:
        obj.fd(size)
        obj.rt(angle)
        size -= 5

t = Turtle()
t.speed(0)
spiral(t, 120)

done()
