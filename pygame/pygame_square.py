# square.py (python-file-name)
# written on 13-feb-203 
# author : Sanjeev Stephan Murmu
import os
import pyfiglet
import argparse
# my library
import data


 # Clears the Screen before running the main functions
def clear_the_screen_first():
    os.system("cls")

# Display Welcome Text using module[pyfiglet]
def welcome_text(text):
    print(pyfiglet.figlet_format(text))

# Display multiple questions
def multiple_ques():
    for i in range(100):
        user_input(i)

# Asks the user to enter the number to square
def user_input(num):
    text="[ {} ] Question Number | Number to Sqare: "
    formatted_text = text.format(num)
    num_to_sq = input(formatted_text)
    sqaure(int(num_to_sq))

# Square the given number
def sqaure(num_to_sq):
    result = num_to_sq*num_to_sq
    text="{} x {} = {}"
    formatted_text=text.format(num_to_sq,num_to_sq,result)
    welcome_text(formatted_text)

if __name__ == "__main__":
    clear_the_screen_first()
    welcome_text(data.square.title)
    print(data.author.msg_to_display)
    data.horizontal_line
    multiple_ques()



# FUNCTION NOT_IN_USE
# Func() to pass arguments from outside the script
def para():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--message",type=str,default="Multiply", help="add to number -a <num> -b <num>")
    parser.add_argument("--a",type=int,help="First number")
    parser.add_argument("--b",type=int,help="Second number")
    args = parser.parse_args()
    print(args.a)
    sqaure(args.a,args.b)

