from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game = True
screen = Screen()
screen.screensize(600, 600, 'black')
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scorecard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scorecard.increase_score()

    if snake.head.xcor() > 375 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -310:
        scorecard.reset()
        snake.reset()

    for item in snake.turtles[1:]:
        if snake.head.distance(item) < 10:
            scorecard.reset()
            snake.reset()

screen.exitonclick()
