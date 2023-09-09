# Here's an updated version of the game that will ask 26 questions and display the score after each correct answer:
import pyfiglet
import string
import os

os.system("cls") # Clear the Screen-first before playing the game

def figlet(text):
    print(pyfiglet.figlet_format(text))

def play_game():
    # List of lowercase alphabet letters
    alphabet = list(string.ascii_lowercase)
    score = 0
    
    for i in range(26):
        # Create a random word from the alphabet
        import random
        word = random.choice(alphabet)
        
        # Get the position of the word in the alphabet
        position = alphabet.index(word) + 1
        
        print("[" + str(i) +"]Find the position of the following letter in the alphabet: " + word)
        
        # Ask for user input and check if it matches the position
        guess = int(input("Your answer: "))
        if guess == position:
            score += 1
            print("Correct! The position of " + word + " is " + str(position))
        else:
            print("Incorrect. The position of " + word + " is " + str(position))
            figlet(word.upper() + " => " + str(position) +" ")
            
        
        print("Your score is: " + str(score) + "/26")

def play_again():
    playAgain=input("Do you want to play again :[y/yes|n/no]")
    if playAgain == "y":
        play_game()
    else:
        exit()

# Start the game
game_title="Alphabet Position Game"
figlet(game_title)
print("Welcome to the Alphabet Position Game!")
play_game()
play_again()

# The game will randomly select 26 letters from the alphabet, and for each letter, the user will be asked to find its position in the alphabet. The user's score will be updated after each correct answer, and the current score will be displayed on the screen. The game will end after 26 questions, and the final score will be displayed on the screen.