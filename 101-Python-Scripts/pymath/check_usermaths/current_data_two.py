# Welcome Title
# written on 13-feb-203 
# author : Sanjeev Stephan Murmu
import os
import pyfiglet

author="Sanjeev Stephan Murmu" # Author of the Code
date="13-Feb-2023"

def horizontal_line():
     print('-' * 40)

def welcome_text(text):
    print(pyfiglet.figlet_format(text))

class author:
    msg = "Developed by -> {} | On Date -> {} "
    msg_to_display = msg.format(author,date)


class multiply:
    title="Multiplication"
    #welcome_text(title)

class square:
    title="Cubes of Any Number"
    #welcome_text(title)