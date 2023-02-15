# Here's an updated version of the code that prints both the color code and the actual color:

import sys

print("Color Table:")
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")



def colorDecoder():
    color_code = input("Enter Color Number :")
    text_to_color = input("Enter Text to Color :")
    code = str(color_code * 16 + j)
    print(sys.stdout.write(u"\u001b[38;5;" + text_to_color + "m " + code.ljust(4)))


"""This code generates a table of color codes and prints both the color code and the actual color next to each other. The actual color is displayed using the escape sequence u"\u001b[38;5;" + code + "m", where code is the color code, and the color code is displayed next to it using code.ljust(4).

This way, the user can see both the color code and the actual color, making it easier to identify and use specific colors in their terminal.

"""