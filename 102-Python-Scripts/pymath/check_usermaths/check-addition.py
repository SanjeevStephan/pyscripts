# multiply.py (python-file-name)
# written on 13-feb-203 
# author : Sanjeev Stephan Murmu
import os
import argparse
# My LIbrary
import current_data

 # Clears the Screen before running the main functions
def clear_the_screen_first():
    os.system("cls")

def multiply(a,b):
    result = a*b
    text = "{} x {} = {}"
    formattedText = text.format(a,b,result)
    print("[Answer] The Multiplication of " + formattedText)
    current_data.welcome_text(formattedText)

def multiple_ques():
    for i in range(1000):
        userinput(i)

def userinput(num):
    quesno = "[ {} ] Question Number "
    print(quesno.format(num))
    a = input("[-> ] First Number  : ")
    b = input("[-> ] Second Number : ")
    multiply(int(a),int(b))

if __name__ == "__main__":
    clear_the_screen_first()                   # Clears the Screen before running the main functions
    current_data.welcome_text(current_data.multiply.title)        # call the 'welcome_text()' to display text from [current_data.py]
    print(current_data.author.msg_to_display)             # Display Author Signature from [current_data.py]
    current_data.horizontal_line                          # Horizontal Line
    multiple_ques()                               # run a 'for' loop to ask multiple_questions

# FUNCTION NOT IN USE
def para():
    parser = argparse.ArgumentParser()
    parser.add_argument("--message",type=str,default=current_data.multiply.title, help="Multiply two number -a <num> -b <num>")
    parser.add_argument("--a",type=int,help="First number")
    parser.add_argument("--b",type=int,help="Second number")
    args = parser.parse_args()
    multiply(args.a,args.b)   



