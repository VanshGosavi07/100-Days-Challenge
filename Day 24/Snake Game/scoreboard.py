from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.score = 0
        with open('high_score.txt') as file:
            self.h_score = int(file.read())
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score : {self.score}  High Score : {self.h_score}", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score >= self.h_score:
            self.h_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(f"{self.h_score}")
        self.score = 0
        self.update_score()
