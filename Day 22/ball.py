from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_X(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_X()
        self.pace = 0.1
