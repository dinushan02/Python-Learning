"""
This script demonstrates operator precedence in Python.
Operator precedence determines the order in which operations are performed.
Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).
"""

# Example 1: Operator precedence without parentheses
x = 10 + 3 * 2 ** 2  # Exponentiation first, then multiplication, then addition
print("Result of 10 + 3 * 2 ** 2:", x)  # Output: 22

# Example 2: Using parentheses to change order of operations
x = (10 + 3) * 2 ** 2  # Parentheses first, then exponentiation, then multiplication
print("Result of (10 + 3) * 2 ** 2:", x)  # Output: 52

# Example 3: Another expression with parentheses
x = (2 + 3) * 10 - 3  # Parentheses first, then multiplication, then subtraction
print("Result of (2 + 3) * 10 - 3:", x)  # Output: 47

"""
Operator Precedence in Python:
1. Parentheses: ()
2. Exponentiation: **
3. Multiplication *, Division /, Floor Division //, Modulus % (evaluated left to right)
4. Addition + and Subtraction - (evaluated left to right)
"""
