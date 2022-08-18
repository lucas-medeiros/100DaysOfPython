# @author   Lucas Cardoso de Medeiros
# @since    18/06/2022
# @version  1.0

# Quiz Game

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


def load_data():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["category"], question["question"], question["correct_answer"]))
    random.shuffle(question_bank)
    return question_bank


if __name__ == '__main__':
    print("\nWelcome to the Quiz Game!\n")
    quiz = QuizBrain(load_data())
    quiz.run_quiz()
    print("Game over! Thanks for playing")
