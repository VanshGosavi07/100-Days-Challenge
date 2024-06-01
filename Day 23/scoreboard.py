from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.pace = 0.1
        self.level = 1
        self.score = Turtle()
        self.score.color('white')
        self.score.penup()
        self.score.hideturtle()
        self.over_screen = Turtle()
        self.over_screen.color('white')
        self.over_screen.hideturtle()

    def game_over(self):
        self.over_screen.write(f"GAME OVER", align="center", font=('Arial', 24, 'normal'))

    def score_display(self):
        self.score.goto(-290, 280)
        self.score.write(f"Level: {self.level}", font=("Courier", 24, "normal"))

    def level_up(self):
        self.level += 1
        self.pace *= 0.6
        self.score.clear()
        self.score_display()
