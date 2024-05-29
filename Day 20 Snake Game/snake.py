from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
TURTLES = []
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        for position in POSITIONS:
            obj = Turtle('square')
            obj.color('white')
            obj.penup()
            obj.goto(position)
            TURTLES.append(obj)
        self.head = TURTLES[0]

    def move(self):
        for i in range(len(TURTLES) - 1, 0, -1):
            x = TURTLES[i - 1].xcor()
            y = TURTLES[i - 1].ycor()
            TURTLES[i].goto(x, y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
