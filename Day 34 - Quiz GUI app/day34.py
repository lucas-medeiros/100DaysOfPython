# @author   Lucas Cardoso de Medeiros
# @since    11/07/2022
# @version  2.0

# Quizzler 2.0 w/ API + UI

from question_model import Question
from data import Data
from quiz_brain import QuizBrain
from ui import QuizInterface

data = Data()
question_bank = []
for question in data.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
