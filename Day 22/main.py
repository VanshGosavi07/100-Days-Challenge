from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scorecard()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

while scoreboard.game:
    time.sleep(ball.pace)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        ball.pace *= 0.9

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_X()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player1()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player2()



screen.exitonclick()
