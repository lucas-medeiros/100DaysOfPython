class Question:

    def __init__(self, category, question, correct_answer):
        """Question Class constructor"""
        self.category = category
        self.type = "boolean"
        self.difficulty = "easy"
        self.question = question
        self.correct_answer = correct_answer

    def get_text(self):
        """Returns question text"""
        return self.question

    def get_answer(self):
        """Return question answer"""
        return self.correct_answer

    def check_answer(self, answer):
        """Returns True if the answer is correct"""
        return self.correct_answer.lower() == answer.lower()
