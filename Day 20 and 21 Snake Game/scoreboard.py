from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score : {self.score}", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Arial', 24, 'normal'))
