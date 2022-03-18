from turtle import *


def square(turt, length):
    for i in range(4):
        turt.fd(length)
        turt.rt(90)


def nautilus(turt, angle, length):
    if length >= 250:
        return None
    else:
        square(turt, length)
        turt.lt(angle)
        nautilus(turt, angle, length + 3)


t = Turtle()
t.speed(0)
t.pensize(3)

nautilus(t, 10, 3)

done()
