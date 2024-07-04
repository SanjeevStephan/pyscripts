# Script      : 110_strings.py
# Description : 
from helper import log as see
# ------------------------------|| Strings ||-----------------------------
# Strings
"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function:
"""
print('Hello Python')
print("Hello Python")

# Assign String to a Variable
""" Assigning a string to a variable is done with the variable name followed by an equal sign and the string: """
a = 'hello world'
print(a)

# ------------------------------|| Multiline  Strings ||-----------------------------
""" You can assign a multiline string to a variable by using three quotes: """
see.printlog("You can use three double quotes:")
a = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
see.printlog("Or three single quotes:")
a = ''' Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. '''
print(a)
# Note: in the result, the line breaks are inserted at the same position as in the code.

# ------------------------------|| Strings are Arrays ||-----------------------------
# Square brackets can be used to access elements of the string.
# //TODO Get the character at position 1 (remember that the first character has the position 0):
see.printlog('printing the second character from "Hello Python"')
a = 'Hello Python'
print(a[1])


# ------------------------------|| Looping Through a String ||-----------------------------
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# //TODO Loop through the letters in the word "banana":
see.printlog("Looping through the letters in the word 'banana'")
for x in 'banana':
    print(x)


# ------------------------------|| String Length ||-----------------------------
# To get the length of a string, use the len() function.
# //TODO Use The len() function to returns the length of a string:
see.printlog('The len() function returns the length of a string:')
a = 'hello world!'
str_length = len(a)
print("Length of String 'hello world! is " + str(str_length))

# ------------------------------|| Check String ||-----------------------------
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# /TODO Check if "hard" is present in the following text:
see.printlog("Check if 'hard' is present in the following text")
txt = "This best things  in life are not free ! you have to earn in through hard work"
print("hard" in txt)
# //TODO Use it in an if statement:
see.printlog('Use it in an if statement:')
if 'life' in txt:
    print("Yes, 'life' is present.")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# //TODO Check if "expensive" is NOT present in the following text:
see.printlog(' Check if "expensive" is NOT present in the following text')
print ('expensive' not in txt)
# //TODO Use it in an if statement:
see.printlog('print only if "expensive" is NOT present:')
if 'expensive' not in txt:
    print('No, "Expensive is not present!.')