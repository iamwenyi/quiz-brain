from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0,len(question_data)):
    question_added = Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(question_added)
    
quiz = QuizBrain(question_bank) # Constructor

for x in quiz.question_list:
    quiz.next_question()
