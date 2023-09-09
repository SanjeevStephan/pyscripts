"""This code prints out a table of 16x16 color codes in the terminal. 
Each color code is represented by a 4-digit number and a colored square. 
The code uses the ANSI escape sequence "\u001b[38;5;" to set the color of the text and "\u001b[0m" to reset the color back to the default."""
import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")