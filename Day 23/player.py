from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color('white')
        self.turtle.shape('turtle')
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)

    def move_up(self):
        self.turtle.forward(MOVE_DISTANCE)

    def reset(self):
        self.turtle.goto(STARTING_POSITION)
