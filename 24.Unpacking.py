# In this tutorial, I'm going to show you a powerful feature we
# have in Python called unpacking.
"""x = coordinates[0]
y = coordinates[1]
z = coordinates[2]"""

coordinates = (1, 2, 3) # Define a tuple
#coordinates = [1, 2, 3]
x, y, z = coordinates # Unpack the tuple into variables
print(x)
print(y)
print(z)