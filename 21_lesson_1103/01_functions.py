from turtle import *


def zigzag(turt, num, length):
    if num > 0:
        turt.lt(45)
        turt.fd(length)
        turt.rt(90)
        turt.fd(2 * length)
        turt.lt(90)
        turt.fd(length)
        turt.rt(45)
        zigzag(turt, num-1, length)  # заново вызываю функцию


def sq_spiral(turt, y):
    if y <= 0:
        return None
    else:
        turt.fd(y)
        turt.rt(90)
        sq_spiral(turt, y - 5)

t = Turtle()
sq_spiral(t, 100)

done()