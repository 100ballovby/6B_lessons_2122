from turtle import *


def lines(obj, length):
    while length > 0:
        obj.fd(length)
        obj.bk(length)

        t.rt(90)
        t.up()
        t.fd(10)
        t.down()
        t.lt(90)
        length -= 5


t = Turtle()
lines(t, 50)

done()