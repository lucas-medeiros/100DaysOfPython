class QuizBrain:

    def __init__(self, question_bank):
        """QuizBrain Class constructor"""
        self.question_bank = question_bank
        self.score = 0
        self.count = 0

    def run_quiz(self):
        """Main quiz logic"""
        for question in self.question_bank:
            self.count += 1
            answer = input(f"Q.{self.count}: {question.question}. (True/False): ")
            if question.check_answer(answer):
                self.score += 1
                print("That's correct!")
            else:
                print("That's wrong!")
            print(f"The correct answer was: {question.correct_answer}.")
            print(f"Your current score is: {self.score}/{self.count}\n")
        print(f"Your final score was: {self.score}/{self.count}\n")
