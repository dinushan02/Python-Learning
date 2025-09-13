# When we run the program, we can see.
# When we print this list, you can see.
# Let me show you
# We can also...
# I want to show you here

# Add any numbers at the end of this list, we use append() method
"""numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)"""

# If you want to add a number somewhere in the middle or
# at the begining of this list, we use insert() method
# This method takes 2 values
# We want to add an item at the beginning of our list, so we passed our index position
# and then second value is the actual object
"""numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)"""

# Remove
"""numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)"""

# If you want to remove all the item in the list, you can call the clear() method
"""numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)"""  # All the item are removed.

# pop() method => We can remove the last item in a list.
"""numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)"""

# You can call the index() method
"""numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))"""  # This returns the index of the first occurrence of this item.

# There is also another way to check for the existence of an item,
# we can use the "in" operator.
"""numbers = [5, 2, 1, 7, 4]
print(50 in numbers)"""  # it doesn't make an error

# Count
"""numbers = [5, 2, 1, 7, 5, 4]
print(numbers.count(5))"""

# If you want to sort lists, you can call sort method
"""numbers = [5, 2, 1, 7, 5, 4]
numbers.sort()
print(numbers)"""  # 1,2,3,4,5 => Ascending order

# Descending order
"""numbers = [5, 2, 1, 7, 5, 4]
numbers.sort()
numbers.reverse()
print(numbers)"""

# Copy() method
"""numbers = [5, 2, 1, 7, 5, 4]
numbers2 = numbers.copy()
numbers.append(10)

print(numbers2)""" # We do not have 10 here

# Write a program to remove the duplicates in a list
numbers = [2, 2, 2, 4, 6, 3, 4, 6, 1]  # முதலில் duplicate values உள்ள பட்டியல்
uniques = []  # காலியான பட்டியல் - இதில் unique values மட்டும் சேகரிக்கப்படும்

for number in numbers:  # numbers பட்டியலின் ஒவ்வொரு எண்ணையும் எடுக்கிறது
    if number not in uniques:  # அந்த எண் uniques பட்டியலில் ஏற்கனவே இல்லையெனில்
        uniques.append(number)  # அந்த எண்ணை uniques பட்டியலில் சேர்க்கிறது

print(uniques)  # uniques பட்டியலை அச்சிடுகிறது




