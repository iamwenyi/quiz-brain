class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank
    
    def next_question(self):
        question = self.question_list[self.question_number].text
        ans_comp = self.question_list[self.question_number].answer.lower()
        question_number = self.question_number + 1

        print_question = "Q." + str(question_number) + " " + question + " " + "(True/False)?:" + " "
        ans_user = input(print_question).lower()    
        self.question_number += 1
        
        self.check_answer(ans_user,ans_comp)
        
    def check_answer(self,ans_user,ans_comp):
        if ans_user == ans_comp:
            self.score += 1
            print("Correct")
        else:
            print("Incorrect")
        print(f"Your score is {self.score}/{self.question_number}")    