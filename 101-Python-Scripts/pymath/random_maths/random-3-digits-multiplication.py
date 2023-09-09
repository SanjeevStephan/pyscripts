import os
#import datetime
import random
import json
# Custom Script
import current_date

today = current_date.getCurrentDate()

import time, sys
def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * int((25 - width)) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print
    
# loading()


def showCoolText(msg):
    text_to_be_displayed='python D:\\pyscripts\\figlet.py --message "{}"'
    os.system(text_to_be_displayed.format(msg))

def score(status="Status",correct_num_of_answers=0, total_num_of_questions=0):
    return "[ {} ] You got {} out of {} questions correct!".format(status,correct_num_of_answers, total_num_of_questions)

def setNumOfQues():
    num_of_ques = int(input("[{}] Enter the Number of Questions to Ask :".format("INPUT")))
    return num_of_ques

def randomMultiplication():
    # Define the range of numbers for the questions
    MIN_NUM = 1
    MAX_NUM = 999

    # Define the number of questions to ask
    #NUM_QUESTIONS = 10
    NUM_QUESTIONS = setNumOfQues() # ask the user to enter the number of ques to ask and store in this variable

    # Initialize variables for the game
    correct_answers = 0
    total_questions = 0

    # Notify the user that the game has started & they can start playing the multiplication game
    showCoolText("Game Started!")
    print("-"*30) # horizontal line (---------------------)
    # Loop through the number of questions
    while total_questions < NUM_QUESTIONS:
        # Generate two random numbers within the defined range
        num1 = random.randint(MIN_NUM, MAX_NUM)
        num2 = random.randint(MIN_NUM, MAX_NUM)
    
        # Substract the Total Question with the Questions left to get the current question.
        num_of_questions_left=NUM_QUESTIONS - total_questions
        current_ques= total_questions   
        # Ask the question and get the user's answer
        answer = input("[ {} ] What is {} x {}? = ".format(num_of_questions_left,num1, num2))
    

        # ChatGPT CODE SNIPPET
        # Check if input is empty
        if answer == "":
          # If input is empty, execute this block
             print("You didn't enter anything!")
             loading()
             # Show the currect answers after the progress bar finished loading after 
             showCoolText("{} x {} = {}".format(num1,num2,num1*num2))
             print(score("Status-> Incorrect",correct_answers,NUM_QUESTIONS))
             print("[!] The Current Answer is -> [ {} ].".format(num1 * num2))
             
          # perform other tasks based on your requirements 
        else:
            # If input is not empty, execute this block
            # Check if the user's answer is correct
            if int(answer) == num1 * num2:
                correct_answers += 1 # Add '1' every time correct answer
                print(score("Status-> Correct",correct_answers,NUM_QUESTIONS)) # Status
            
            else:
                showCoolText("{} x {} = {}".format(num1,num2,num1*num2))
                print(score("Status-> Incorrect",correct_answers,NUM_QUESTIONS))
                print("[!] The Current Answer is -> [ {} ].".format(num1 * num2))


        

        # Increment the total questions counter
        total_questions += 1
    
        # current Score
        #print(score(correct_answers,NUM_QUESTIONS))

   

    # Print the final results
    print("You got {} out of {} questions correct!".format(correct_answers, total_questions))

    saveTheGameInJSON(correct_answers,total_questions)

    # Ask if the user wants to continue the game
    playAgain(total_questions,NUM_QUESTIONS)

def playAgain(total_questions,NUM_QUESTIONS):
    showCoolText("Play Again ?")
    # Ask if the user wants to continue the game
    # total_question = total_question_asked
    # NUM_QUESTIONS = Overall Total Questions
    # if total_questions < NUM_QUESTIONS:
    if total_questions == NUM_QUESTIONS: # if total asked equals to total num to be askd that means the games has been fullfilled
        play_again = input("Do you want to continue the game? (y/n) ")
        if play_again.lower() != "y":
            showCoolText("Bye")
            exit()
        else:
            showCoolText("Let's Play Again")
            randomMultiplication()
    
def saveTheGameInJSON(correct_answers,total_questions):
    # Save the score and date/time of the game in a JSON file
    score = {"date": str(today), "score": "You got {} out of {} questions correct!".format(correct_answers, total_questions)}
    with open("saved_score.json", "w") as f:
        json.dump(score, f)
    print("Game Progess saved in './/saved_score.json")

def loadTheGameScore():
    # Load the last score from the JSON file
    try:
        with open("saved_score.json", "r") as f:
            last_score = json.load(f)
            print("[Saved]Last score on {} {}".format(last_score["date"], last_score["score"]))
    except FileNotFoundError:
        print("No previous score found.")
        print("-"*30)

if __name__ == "__main__":
    os.system("cls")
    showCoolText("Random Multiplication")
    loadTheGameScore()
    print("Today is {}. Lets Play a New Game".format(today))
    randomMultiplication()