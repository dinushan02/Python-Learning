"""for x in range(4):
    for y in range(3):
        print(f"({x},{y})") #After inner loop completes ,goes back to line 1"""

"""numbers = [5,2,5,2,2]
for x_count in numbers:
    print("x" * x_count)""" # this method is not support to all language. It works in only Python.

"""numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)"""

numbers = [2, 2, 2, 6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += '*'
    print(output)

