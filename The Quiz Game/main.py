from external_data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for item in question_data:
    questions.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz! Well done!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

