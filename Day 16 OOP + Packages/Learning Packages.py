from turtle import Turtle, Screen

obj = Turtle()
print(obj)
obj.shape("turtle")
i=1
while(i<=4):
    obj.forward(200)
    obj.left(90)
    i+=1

obj.color("coral")

screen = Screen()
screen.exitonclick()

print(screen.canvheight)

from prettytable import PrettyTable
obj=PrettyTable()
obj.add_column('Pockemon Name',['Pikachu','Squirtle','Charmander'])
obj.add_column("Type",['Electric','Water','Fire'])
obj.align='r'
obj.header_style='upper'
print(obj)