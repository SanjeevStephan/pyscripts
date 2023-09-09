import os
import random
import json
from datetime import date

class CoolText:
    @staticmethod
    def show(text):
        os.system(f"python D:\\terminal\\py\\figlet.py --message '{text}'")

class MultiplicationGame:
    def __init__(self):
        self.MIN_NUM = 12
        self.MAX_NUM = 19
        self.score_file = "saved_score_random_12to19.json"
        self.play_again = True
        self.num_of_questions = 0
        self.correct_answers = 0
        self.total_questions = 0
        self.today = date.today()

    def set_num_of_questions(self):
        num_of_ques = int(input("[INPUT] Enter the number of questions to ask: "))
        return num_of_ques

    def get_question(self, question_number):
        num1 = random.randint(self.MIN_NUM, self.MAX_NUM)
        num2 = random.randint(self.MIN_NUM, self.MAX_NUM)
        return (num1, num2, num1 * num2, question_number)

    def get_answer(self, question):
        num1, num2, correct_answer, question_number = question
        num_of_questions_left = self.num_of_questions - question_number + 1
        answer = input(f"[{num_of_questions_left}] What is {num1} x {num2}? = ")
        if int(answer) == correct_answer:
            self.correct_answers += 1
            print(self.get_score("Correct"))
        else:
            print(self.get_score("Incorrect"))
            print(f"[!] The correct answer is {correct_answer}.")
        self.total_questions += 1

    def get_score(self, status):
        return f"[{status}] You got {self.correct_answers} out of {self.total_questions} questions correct!"

    def play_again_menu(self):
        answer = input("Do you want to play again? (y/n) ")
        self.play_again = answer.lower() == "y"

    def save_score(self):
        score = {"date": str(self.today), "score": f"You got {self.correct_answers} out of {self.total_questions} questions correct!"}
        with open(self.score_file, "w") as f:
            json.dump(score, f)
        print(f"Game progress saved in '{self.score_file}'")

    def load_score(self):
        try:
            with open(self.score_file, "r") as f:
                last_score = json.load(f)
                print(f"[Saved] Last score on {last_score['date']}: {last_score['score']}")
        except FileNotFoundError:
            print("No previous score found.")
        print("-" * 30)

    def run(self):
        CoolText.show("Random Multiplication")
        CoolText.show("between 12 to 19")
        self.load_score()
        self.num_of_questions = self.set_num_of_questions()
        while self.play_again:
            self.correct_answers = 0
            self.total_questions = 0
            CoolText.show("Game Started!")
            print("-" * 30)
            for question_number in range(1, self.num_of_questions + 1):
                question = self.get_question(question_number)
                self.get_answer(question)
            print(f"You got {self.correct_answers} out of {self.total_questions} questions correct!")
            self.save_score()
            self.play_again_menu()

if __name__ == "__main__":
    game = MultiplicationGame()
    game.run()
