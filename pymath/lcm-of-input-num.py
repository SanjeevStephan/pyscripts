import math
import os

os.system('python ./../figlet.py --message "LCM [user-input]"')

#Number of Questions to ask
ques_num=10

# Prompt the user to enter range of items
total_range_num = int(input("Enter the Range Number of Items :-"))

def calc_lcm():
    # Prompt the user to enter 4 two-digit numbers
    numbers = []
    for i in range(total_range_num):
        while True:
            number = input("Enter two-digit number {}: ".format(i+1))
            if len(number) == 2 and number.isdigit():
                numbers.append(int(number))
                break
            else:
                print("Invalid input, please enter a two-digit number.")

    # Find the LCM of the numbers
    lcm = math.lcm(*numbers)

    # Display the LCM of the numbers
    print("LCM of the numbers", numbers, "is:", lcm)


for i in range(ques_num):
    print("[{}/{}] Exercise".format(i,ques_num))
    calc_lcm() 