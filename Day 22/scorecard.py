from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.game=True
        self.color('white')
        self.penup()
        # self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.goto(-100, 200)
        self.write(self.player1_score,align='center',font=('Courier',60,'normal'))
        self.goto(100, 200)
        self.write(self.player2_score,align='center',font=('Courier',60,'normal'))


    def player1(self):
        self.player1_score += 1
        self.clear()
        self.update_score()
        if self.player1_score>=5:
            self.goto(0,0)
            self.write('Player 1 Won',align='center',font=('Courier',60,'normal'))
            self.game=False



    def player2(self):
        self.player2_score += 1
        self.clear()
        self.update_score()
        if self.player2_score>=5:
            self.goto(0,0)
            self.write('Player 2 Won',align='center',font=('Courier',60,'normal'))
            self.game=False

