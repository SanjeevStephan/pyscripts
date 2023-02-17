# Prompt the user to input four two-digit numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

# Define a function to calculate the HCF of two numbers
def hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Calculate the HCF of the four numbers
result = hcf(hcf(a, b), hcf(c, d))

# Display the result
print("The HCF of", a, ",", b, ",", c, ", and", d, "is", result)
