from turtle import *


def draw_cross(turt, x, y, col, rad):
    turt.up()
    turt.goto(x, y)
    turt.down()
    turt.color(col)
    for i in range(4):
        turt.circle(rad, 180)
        turt.rt(90)


t = Turtle()
t.speed(0)
for i in range(9):
    draw_cross(t, 100, 100, 'green', 50)
    t.rt(60)

done()
