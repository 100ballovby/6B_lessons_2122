from turtle import *

t = Turtle()
t.speed(0)

colormode(255)  # чтобы можно было работать с цветами RGB


def spiral(obj, size, deg):
    steps = 5
    r = 200
    g = 0
    b = 180
    for i in range(size):
        obj.color(r, g, b)
        obj.fd(steps)
        obj.lt(deg)

        steps += 2
        g = (g + 1) % 255

spiral(t, 255, 164)

done()
