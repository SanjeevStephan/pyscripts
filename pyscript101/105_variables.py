# Variables are containers for storing data values.

from helper import log as see
# ----------------------------------|| Python Variables ||-----------------------
# Creating Variables
"""
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""

a = 5         # This Variable 'x' becomes INTEGER
b = "Stephan" # This Variable 'y' becomes STRING

# Variables do not need to be declared with any particular type, and
# can even change type after they have been set.

print(a)
print(b)

# Casting
"""
If you want to specify the data type of a variable, this can be done with casting.

"""
c = str(9)      # x will be '3' (STRING)
d = int(9)      # y will be 3   (INTEGER)
e = float(9)    # z will be 3.0 (DECIMAL) | #convert from int to float:

# Get the Type
"""
You can get the data type of a variable with the type() function.
"""
print(type(c))
print(type(d))
# ----------------------------------|| Variable Naming Convenctions ||-----------------------
# Multi Words Variable Names
"""
Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:
"""
# Camel Case
""" Each word, except the first, starts with a capital letter: """

myVariableName = "Sanjeev"

# Pascal Case
""" Each word starts with a capital letter: """
MyVariableName = "Stephan"

# Snake Case
""" Each word is separated by an underscore character: """
my_variable_name = "Murmu"

# ------------------------------|| Assign Multiple Values ||-----------------------------
# Python allows you to assign values to multiple variables in one line:
f, g, h = "flowers", "gadgets", "helicopter"
print(f)
print(g)
print(h)

# ------------------------------|| Assign Multiple Values ||-----------------------------
# And you can assign the same value to multiple variables in one line:
f = g = h = "alphabets"
see.printlog("After Variable's value is assigned to new one")
print(f)
print(g)
print(h)

# ------------------------------|| Unpack a Collection ||-----------------------------
""" If you have a collection of values in a list, tuple etc. 
    Python allows you to extract the values into variables. This is called unpacking.
"""
sport_car_brands = ["Audi", "BWM", "Ford", "General Motors", "Lamborgini", "Tesla"]
a, b, c, d, e, f = sport_car_brands
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
