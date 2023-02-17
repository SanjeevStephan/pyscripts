# Prompt the user to input a range
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Prompt the user to input the numbers in the range
numbers = []
for i in range(start, end+1):
    number = int(input("Enter a two-digit number in the range: "))
    numbers.append(number)

# Define a function to calculate the HCF of two numbers
def hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Calculate the HCF of the numbers
result = numbers[0]
for i in range(1, len(numbers)):
    result = hcf(result, numbers[i])

# Display the result
print("The HCF of the numbers in the range", start, "to", end, "is", result)

