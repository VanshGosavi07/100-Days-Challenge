from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title("Us States")
screen.setup(height=500, width=700)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
temp = 0
data = pandas.read_csv("50_states.csv")
state = data.state.tolist()

while (temp != len(state)):
    answer = screen.textinput(title=f"{temp}/{len(state)} States correct", prompt="Enter the State Name").title()
    if answer == 'Exit':
        break
    if answer in state:
        timmy = Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data["state"] == answer]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer)
        temp += 1

# li =
# x = (li['x'])
# print(type(x))
# timmy = Turtle("circle")
# timmy.penup()
# timmy.goto(200,20)
# timmy.goto(li['x'], li['y'])

screen.exitonclick()
