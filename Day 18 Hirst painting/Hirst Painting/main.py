import turtle

import colorgram
from turtle import Turtle, Screen
import random

turtle.colormode(255)
rgb_c = []
colors = colorgram.extract('img.png', 30)
for item in colors:
    r = item.rgb.r
    g = item.rgb.g
    b = item.rgb.b
    new_color = (r, g, b)
    rgb_c.append(new_color)
print(rgb_c)


obj = Turtle()
obj.speed(0)
obj.hideturtle()
for _ in range(5):
    for _ in range(5):
        obj.dot(20, random.choice(rgb_c))
        obj.penup()
        obj.forward(50)
    obj.backward(250)
    obj.left(90)
    obj.forward(50)
    obj.right(90)

screen = Screen()
screen.exitonclick()
