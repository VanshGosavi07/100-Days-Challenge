from turtle import Turtle, Screen
import random

obj = Turtle()
# obj1 = Turtle()
# obj2 = Turtle()
# obj3 = Turtle()
# obj.shape("turtle")
# obj.color('blue')
# obj.pencolor('red')
# obj1.shape("turtle")
# obj1.color('magenta')
# obj1.pencolor('black')
# obj2.shape("turtle")
# obj2.color('red')
# obj2.pencolor('green')
# obj3.shape("turtle")
# obj3.color('yellow')
# obj3.pencolor('purple')
# i = 0
# while (i < 4):
#     obj.forward(100)
#     obj1.forward(100)
#     obj2.backward(100)
#     obj3.backward(100)
#     obj.left(90)
#     obj2.left(90)
#     obj3.right(90)
#     obj1.right(90)
#     i += 1

# tur = Turtle()
# tur.shape('turtle')
# i = 0
# while (i < 15):
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)
#     tur.pendown()
#     i += 1


# shapes
# tur = Turtle()
# angle = 120
#
# for i in range(33):
#     tur.forward(100)
#     tur.right(angle)
#     if i == 2:
#         angle -= 30
#         tur.pencolor('red')
#     elif i == 6:
#         angle -= 18  # 72
#         tur.pencolor('purple')
#     elif i == 11:
#         angle -= 12  # 60
#         tur.pencolor('green')
#     elif i == 17:
#         angle -= 8.57  # 51.43
#         tur.pencolor('blue')
#     elif i==24:
#         angle-= 6.43 #45
#         tur.pencolor('magenta')


# spirograph
obj.speed('fastest')
obj.width(1)





def color(colors):
    return random.choice(colors)
for _ in range(90):
    obj.color('pink')
    obj.circle(150)
    obj.left(5)

screen = Screen()
screen.exitonclick()
