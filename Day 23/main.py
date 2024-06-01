import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
cars = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.pace)
    screen.update()
    cars.car_position()
    cars.move_cars()
    scoreboard.score_display()
    for item in cars.all_cars:
        if player.turtle.distance(item) < 15:
            game_is_on = False
            scoreboard.game_over()
        if player.turtle.ycor() >= 280:
            scoreboard.level_up()
            player.reset()

screen.exitonclick()
