"""names = ["John", "Bob", "Mosh","Ram","Sam"]
print(names)
print(names[1])
print(names[-1])
print(names[2:4])
names[0] = "Arutperunjothi Andavar"
print(names)"""

#Write a program to find the largest number in a list
# Find the maximum number in a list without using built-in functions
numbers = [4, 9, 15, 5, 85, 34, 10]
max_num = numbers[0]  # Assume first number is largest

for number in numbers:
    if number > max_num:
        max_num = number  # Update if a larger number is found

print(max_num)  # Output: 85

# Finds and prints the largest number in the list.



