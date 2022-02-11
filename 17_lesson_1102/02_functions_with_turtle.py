# плохой пример. Рисуем МНОГО квадратов в разных частях экрана разного цвета
from turtle import *

t = Turtle()

for i in range(4):
    t.fd(100)
    t.rt(90)
t.up()
t.goto(100, 200)
t.down()
t.color('yellow')
for i in range(4):
    t.fd(100)
    t.rt(90)

t.up()
t.goto(-200, -200)
t.down()
t.color('red')
for i in range(4):
    t.fd(100)
    t.rt(90)

done()
