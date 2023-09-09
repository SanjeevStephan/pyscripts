
#simple game in Python that asks multiplication questions and keeps track of the number of questions asked, correctly answered, and
# total questions.

#Here's an example code for the game:

import random
import os

game_tile = "Random Multiplication"
current_ques = 0

def showCoolText(msg):
    text_to_be_displayed='python D:\\myscripts\\poweruser\\figlet.py --message "{}"'
    os.system(text_to_be_displayed.format(msg))



def randomMaths():
    # Define the range of numbers for the questions
    MIN_NUM = 10
    MAX_NUM = 99

    # Define the number of questions to ask
    NUM_QUESTIONS = 10

    # Initialize variables for the game
    correct_answers = 0
    total_questions = 0
    
    # Loop through the number of questions
    for i in range(NUM_QUESTIONS):
        # Generate two random numbers within the defined range
        num1 = random.randint(MIN_NUM, MAX_NUM)
        num2 = random.randint(MIN_NUM, MAX_NUM)
        current_ques=NUM_QUESTIONS - i  # Substract the Total Question with the Questions left to get the current question.
    
    # Ask the question and get the user's answer
    answer = input("[ {} ] What is {} x {}? ".format(current_ques,num1, num2))
    
    # Check if the user's answer is correct
    if int(answer) == num1 * num2:
        print("Correct!")
        correct_answers += 1
    else:
        multiply = num1 * num2
        print("Incorrect. The answer is {}.".format(num1 * num2))
        showCoolText("{} x {} = {}".format(num1,num2,multiply))
        
    # Increment the total questions counter
    total_questions += 1

    # Print the final results
    print("You got {} out of {} questions correct!".format(correct_answers, total_questions))

if __name__ == "__main__":
    os.system("cls")
    showCoolText(game_tile)
    randomMaths()


# How the Games Logic Works
"""
In this game, we first define the range of numbers for the questions, which in this case are two-digit numbers. 
We also define the number of questions to ask, which is set to 10.

Next, we initialize variables to keep track of the number of correct answers and the total number of questions. 
We then loop through the number of questions and generate two random numbers within the defined range.
 We then ask the multiplication question and get the user's answer.

We then check if the user's answer is correct by multiplying the two random numbers and comparing the result to the user's answer. 
If the answer is correct, we increment the correct answer counter. If the answer is incorrect, we print the correct answer.
 We also increment the total questions counter after each question.

Finally, after all questions have been asked, we print the number of questions the user answered correctly out of the total number of questions asked.

You can customize this game by changing the range of numbers or the number of questions to ask.

"""