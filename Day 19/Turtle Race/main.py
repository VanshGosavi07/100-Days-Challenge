from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

color = ['red', 'green', 'yellow', 'purple', 'black', 'orange']
y = -70
turtles = []
for item in range(0, 6):
    obj = Turtle()
    obj.shape('turtle')
    obj.color(color[item])
    obj.penup()
    obj.goto(x=-230, y=y)
    y += 30
    turtles.append(obj)

color = screen.textinput('Enter Your bet', "Choose Tutle color")
while (1):
    for tur in turtles:
        if tur.xcor() >= 230:
            if tur.pencolor() == color:
                print(f"You won because {tur.pencolor()} is won.")
            else:
                print(f"You lose because {tur.pencolor()} is won.")
            exit((1))
        tur.forward(random.randint(0, 6))

# screen.exitonclick()
