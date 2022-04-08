from turtle import *


t = Turtle()
t.speed(0)

def spiral(obj, size):
    for i in range(size):
        for side in range(4):
            obj.fd(50)
            obj.lt(90)
        obj.fd(50)
        obj.rt(350)


spiral(t, 100)

done()
