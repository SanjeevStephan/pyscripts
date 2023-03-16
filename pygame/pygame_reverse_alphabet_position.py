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
        #print("[DEBUG] Word : {}".format(word))       
        
        # array start from 0 so if 'A' position is at 1, computer will see as 0 so we have to substract 1 to get the actual positon in the array
        array_minus_one = 1

        # Get the reverse position of the word in the alphabet
        reverse_position = 27 - alphabet.index(word) - array_minus_one
        #print("[DEBUG] Reverse Position : {}".format(reverse_position))
        
        print("[" + str(i) +"] Find the reverse position of the following letter in the alphabet: " + word)
        
        # Ask for user input and check if it matches the reverse_position
        guess = int(input("Your answer: "))
        if guess == reverse_position:
            score += 1
            print("[ CORRECT ] The reverse_position of " + word + " is " + str(reverse_position))
        else:
            print("[ INCORRECT ] The reverse_position of " + word + " is " + str(reverse_position))
            figlet(word.upper() + " => " + str(reverse_position) +" ")
            
        
        print("Your score is: " + str(score) + "/26")

def play_again():
    playAgain=input("Do you want to play again :[y/yes|n/no]")
    if playAgain == "y":
        play_game()
    else:
        exit()

# Start the game
game_title="Reverse Alphabet Position Game"
figlet(game_title)
print("Welcome to the Alphabet reverse_position Game!")
print("Reading Alphabet from RIGHT to LEFT <- ")
print("Such that (A=26,B=25...X=24,Y=25,Z=26)")
print("-"*135)
print("The TRICK to get the revese position : (27-x) where 'x' is the alpahbet's position when read from -> LEFT to RIGHT")
print("for-example : if 'B' is at position '2', let's asssign x=2 ")
print("now let's find the reverse position by using the formula (27-x) which wil be [ (27-2) = 25 ] so the reverse position of 'B' will be 25")
print("-"*135)
play_game()
play_again()

# The game will randomly select 26 letters from the alphabet, and for each letter, the user will be asked to find its reverse_position in the alphabet. The user's score will be updated after each correct answer, and the current score will be displayed on the screen. The game will end after 26 questions, and the final score will be displayed on the screen.