from turtle import *


def pentagon(turt):
    for i in range(5):
        turt.fd(200)
        turt.lt(72)


def rosetta(turt, n, angle):
    if n >= 21:
        return None
    else:
        pentagon(turt)
        turt.left(angle)
        rosetta(turt, n + 1, angle)


t = Turtle()
t.speed(0)
rosetta(t, 1, 360 / 20)

done()
