from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for datum in question_data:
    question_bank.append(Question(datum["question"], datum["correct_answer"]))

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

if not brain.still_has_questions():
    print("You've completed the quiz.")
    print(f"Your final score was {brain.user_score}/{brain.question_number}")
