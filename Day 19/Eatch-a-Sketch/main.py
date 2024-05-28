from turtle import Turtle, Screen

obj = Turtle()
screen = Screen()

obj.shape('turtle')


def forward():
    obj.forward(10)


def backward():
    obj.backward(10)


def clockwise():
    obj.right(10)


def anticlockwise():
    obj.left(10)


def end():
    obj.clear()
    obj.penup()
    obj.home()
    obj.pendown()

screen.listen()
screen.onkey(key='f', fun=forward)
screen.onkey(key='b', fun=backward)
screen.onkey(key='c', fun=clockwise)
screen.onkey(key='a', fun=anticlockwise)
screen.onkey(key='e', fun=end)
screen.exitonclick()
