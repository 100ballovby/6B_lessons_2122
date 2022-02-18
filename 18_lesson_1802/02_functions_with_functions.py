from turtle import *


def filled_square(turt, col, line):
    turt.fillcolor(col)
    turt.begin_fill()
    for i in range(4):
        turt.fd(line)
        turt.rt(90)
    turt.end_fill()


def lined_square(turt, col, line):
    turt.color(col)
    for i in range(4):
        turt.fd(line)
        turt.rt(90)


def draw_square(turt, x, y, fill, col, line):
    turt.up()
    turt.goto(x, y)
    turt.down()
    if fill:  # если fill == True
        filled_square(turt, col, line)
    else:
        lined_square(turt, col, line)


t = Turtle()
draw_square(t, 100, 100, True, 'blue', 120)
draw_square(t, -100, -100, False, 'green', 120)

done()
