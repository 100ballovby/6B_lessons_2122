from turtle import *


def draw_spider(turt, lines, x, y):
    turt.up()
    turt.goto(x, y)
    turt.down()

    for i in range(lines):
        turt.fd(100)
        turt.bk(100)
        turt.rt(360 / lines)

t = Turtle()
draw_spider(t, 16, 100, 100)
draw_spider(t, 5, -100, -100)
draw_spider(t, 3, 350, -140)

done()