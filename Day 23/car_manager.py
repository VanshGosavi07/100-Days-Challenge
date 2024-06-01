from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def car_position(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            new_car.speed(MOVE_INCREMENT)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
