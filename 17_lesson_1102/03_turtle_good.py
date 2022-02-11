from turtle import *
from random import randint, choice
from drawing import draw_square  # импортирую функцию рисования квадрата из другого файла


t = Turtle()
colors = ['#67eb67', '#67a0eb', '#eb67a9', '#c98516', '#16c99a', '#c95516']

for i in range(20):  # повторить 20 раз
    x = randint(-350, 350)  # задать случайный х
    y = randint(-350, 350)  # задать случайный у
    color = choice(colors)  # достать случайный цвет из списка
    draw_square(t, x, y, color, 50)  # нарисовать квадрат

done()
