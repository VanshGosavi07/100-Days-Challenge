import random


class Quiz_brain:
    def __init__(self):
        self.score = 0
        self.i = 0

    def ask_question(self, question_bank):
        while (self.i < len(question_bank)):
            print(f"{question_bank[self.i].text}. (True/False)")
            new_ans = input()
            if (new_ans).lower() == (question_bank[self.i].answer).lower():
                self.score += 1
                print("You got it right!")
            else:
                print("You got it wrong!")

            print(f"The correct answer was: {question_bank[self.i].answer}")
            print(f"Your current score is: {self.score}/{self.i+1}\n\n\n")
            self.i += 1
        print("Questions are over")
