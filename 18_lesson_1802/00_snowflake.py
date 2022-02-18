from turtle import *


def branch(turt, col):
    turt.color(col)

    for i in range(3):
        for j in range(3):
            turt.fd(30)
            turt.bk(30)
            turt.rt(45)
        turt.lt(90)
        turt.bk(30)
        turt.lt(45)
    turt.rt(90)
    turt.fd(90)


t = Turtle()
for i in range(8):
    branch(t, '#bdf7ff')
    t.lt(45)

done()

