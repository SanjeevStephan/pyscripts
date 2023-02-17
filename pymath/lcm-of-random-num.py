import random
import math

# Generate 4 random two-digit numbers
numbers = [random.randint(10, 99) for i in range(4)]

# Find the LCM of the numbers
lcm = math.lcm(*numbers)

# Display the numbers and their LCM
print("Numbers generated:", numbers)
print("LCM of the numbers:", lcm)
