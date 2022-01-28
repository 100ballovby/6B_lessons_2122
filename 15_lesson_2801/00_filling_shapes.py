from turtle import *


t = Turtle()
t.fillcolor('#3477eb')  # цвет заливки
t.pencolor('#34e5eb')  # цвет линии
t.pensize(5)

t.begin_fill()  # начать зарисовывать
for i in range(4):  # рисуем квадрат
    t.fd(100)
    t.rt(90)
t.end_fill()  # закончить зарисовывать

done()
