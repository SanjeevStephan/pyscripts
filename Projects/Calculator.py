'''
    Description : This calculator performs basic arithmetic operations: addition, subtraction, multiplication, and division.
    It runs in the terminal and takes user input.
    @version (25-sep-2025)
    @author (Sanjeev Stephan Murmu)
'''

menu = {"1. Addition","2.Substraction","3.Multiplication","3.Division"}

for item in menu:
    print(item)

print("Enter Your Choice (1-4) : ")
choice = int(input())

print("You have entered : {}".format(choice))

num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))

calculate = 0

if choice == 1 :
    calculate = num1 + num2
elif choice == 2 :
    calculate = num1 - num2
elif choice == 3:
    calculate = num1 * num2
elif choice == 4:
    calculate = num1 / num2
else :
    print("Invalid Choice ")

print("Total of {}".format(calculate))