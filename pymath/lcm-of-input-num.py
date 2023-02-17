import math

# Prompt the user to enter range of items
total_range_num = int(input("Enter the Range Number of Items :-"))

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
