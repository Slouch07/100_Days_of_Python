class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        list_length = len(self.q_list)
        if self.q_number < list_length:
            return True
        else:
            return False

    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_q.text} (True/False)?: ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n")



