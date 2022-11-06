# import random # подтянуть в проект random
# import random as r # библиотека под именем r.
# # from random import randit # только randit из random
# # from rando import * # так лучше не делать
# x = r.randit(0, 100) # от 0 до 100
# lst = [0, 1, 2, 3, 4, 5]
# element_random = r.choise(lst)
# lst = r.shuffle(lst) # shuffle - перемешать
#
# print(x)
# print(lst)


import turtle

t = turtle.Turtle()
t.penup(2) # поднять ручку
t.goto(0 , 100)
screen = turtle.Screen()
t.color("blue", "red")
t.pensize(10) # толщина пера
# 1 - самая медленная
# 10 - очень быстро
# 0 - максимальная скорость
t.speed(0) # speed - изменение скорости

t.begin_fill
t.forward(50) # вперёд на 50 пикселей.
t.right(90) # поворот направо на 90 градусов
t.forward(50) # вперёд на 50 пикселей.
t.right(90) # поворот направо на 90 градусов
t.forward(50) # вперёд на 50 пикселей.
t.right(90) # поворот направо на 90 градусов
t.forward(50) # вперёд на 50 пикселей.
t.right(90) # поворот направо на 90 градусов

screen.exitonclick()
