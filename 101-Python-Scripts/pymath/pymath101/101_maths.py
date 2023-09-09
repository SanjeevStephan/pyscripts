"""  ---------------------{ CHATGPT QUERY }------------------------------

.QUERY

    
.RESPONSE


.SYNTAX
   

.DESCRIPTION
 

.EXAMPLE

    
.PARAMETER   


.INPUT

    
.CODE    
Here is an example code snippet:
-------------------------------{ CODE_BELOW }-----------------------------"""


import random
import math
import random_substraction


def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Do a random 2-digit subtraction problem")
        print("2. Do a random 2-digit multiplication problem")
        print("3. Do a random 2-digit addition problem")
        print("4. Find the square root of a number")
        print("5. Find the cube root of a number")
        print("6. Exit the program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':

            random_substraction.startsHere()
            #num1 = random.randint(10, 99)
            #num2 = random.randint(10, 99)
            # operator = "-"
            apply_operator(num1,num2,operator)
            #answer = num1 - num2
            #print(f"What is {num1} - {num2}?")
            #check_answer(answer)
        elif choice == '2':
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            operator = "*"
            apply_operator(num1,num2,operator)
            #answer = num1 * num2
            #print(f"What is {num1} * {num2}?")
            #check_answer(answer)
        elif choice == '3':
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            answer = num1 + num2
            print(f"What is {num1} + {num2}?")
            check_answer(answer)
        elif choice == '4':
            num = int(input("Enter a number to find its square root: "))
            answer = math.sqrt(num)
            print(f"The square root of {num} is {answer}")
        elif choice == '5':
            num = int(input("Enter a number to find its cube root: "))
            answer = round(math.pow(num, 1/3), 2)
            print(f"The cube root of {num} is {answer}")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def apply_operator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Invalid operator")
        return None

def test():
   num1 = 10
   num2 = 5
   operator = "+"
   result = apply_operator(num1, num2, operator)
   print(f"{num1} {operator} {num2} = {result}")


def check_answer(answer):
    user_answer = int(input("Enter your answer: "))
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {answer}")



if __name__ == '__main__':
    main()


 
"""-------------------------------{ CODE_ABOVE }-----------------------------

.OUTPUT 


.HOW_THE_SCRIPT_WORK


.LINK
   -> https://chat.openai.com/chat/

"""
