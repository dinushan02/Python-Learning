# Importing the math module to access mathematical functions
import math  # math is the module, and methods are accessed using the dot operator.

# Using math.ceil() to get the smallest integer greater than or equal to the input
print(math.ceil(2.9))  # 3

# Using math.floor() to get the largest integer less than or equal to the input
print(math.floor(2.9))  # 2

# You can also use round() function directly without the math module
x = 2.9
print(round(x))  # 3 (rounds to the nearest integer)

# abs() is a built-in function, not from the math module
print(abs(-2.6))  # 2.6 (returns the absolute value)
