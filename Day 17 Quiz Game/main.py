from data import question_data
from question_model import quiz
from quiz_brain import Quiz_brain

question_bank = []
for question in question_data:
    new_text = question['text']
    new_answer = question['answer']
    new_question = quiz(new_text, new_answer)
    question_bank.append(new_question)

obj = Quiz_brain()
obj.ask_question(question_bank)
