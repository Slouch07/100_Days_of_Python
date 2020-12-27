from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    q_text = q["text"]
    q_answer = q["answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)


new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions:
    new_quiz.next_question()

print("You've completed the quiz.")
print(f"You're final score was: {new_quiz.score}/{new_quiz.q_number}")