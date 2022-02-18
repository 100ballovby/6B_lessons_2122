from turtle import *


def triangle(turt, x, y, line, col):
    turt.up()
    turt.goto(x, y)
    turt.color(col)
    turt.down()

    for i in range(3):
        turt.fd(line)
        turt.lt(120)


t = Turtle()
triangle(t, 100, 100, 180, '#debdff')

done()
