import json
import datetime
import pymath

def getCurrentDate():
    # Get the current date
    today = datetime.date.today()

    # Format the date as a string in the format dd Month yyyy
    date_str = today.strftime("%d %B %Y")

    # Print the date string
    print(date_str)
    return date_str #will return the date in the format (15 February 2023.) | when 'getCurrentDate()' method/function is called

def saveTheGameInJSON(correct_answers,total_questions):
    today = getCurrentDate()
    # Save the score and date/time of the game in a JSON file
    score = {"date": str(today), "score": "You got {} out of {} questions correct!".format(correct_answers, total_questions)}
    with open("saved_score_random_12to19.json", "w") as f:
        json.dump(score, f)
    print("Game Progess saved in 'saved_score_random_12to19.json'")

def loadTheGameScore():
    # Load the last score from the JSON file
    try:
        with open("saved_score_random_12to19.json", "r") as f:
            last_score = json.load(f)
            print("[Saved]Last score on {} {}".format(last_score["date"], last_score["score"]))
    except FileNotFoundError:
        print("No previous score found.")
        print("-"*30)

