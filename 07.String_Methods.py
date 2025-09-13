course = 'Python for Beginners'

# len() => Counts the number of characters in a string (including spaces).
#          This is a general-purpose function built into Python.
#print(len(course))

# upper() => Converts all characters in the string to uppercase.
print(course.upper())

# lower() => Converts all characters in the string to lowercase.
print(course.lower())

# find() => Returns the index of the first occurrence of the specified substring.
#           It is case-sensitive. If the substring is not found, it returns -1.
print(course.find('o'))  # Finds the first occurrence of 'o'.
print(course.find('Beginners'))  # Finds the starting index of 'Beginners'.

# replace() => Replaces occurrences of a specified substring with another substring.
print(course.replace('Beginners', 'Absolute Beginners'))
# If 'beginners' (lowercase) is used instead of 'Beginners', no replacement occurs.

print(course.replace('P', 'J'))  # Replaces 'P' with 'J', making it 'Jython for Beginners'.

# '...' in course => Checks if a substring exists in the string.
#                    Returns True if found, otherwise False.
print('Python' in course)  # Boolean expression: True if 'Python' exists in course.

