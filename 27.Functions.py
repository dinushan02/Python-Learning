# We need to break up our code into smaller, more manageable, and 
# more maintainable chunks which we call functions.
#
# Function is a container for a few lines of code that perform a specific task.
# We can call this function whenever we want to perform that task.
# This helps us avoid code duplication and makes our code more organized.
# To define a function, we use the 'def' keyword followed by the function name
# and parentheses. The code block within every function starts with a colon (:)
# and is indented.
# By convention, function names are written in lowercase letters and words are
# separated by underscores (_).
# A function can take inputs (parameters) and can return an output (return value).
# Here, we will define a simple function that greets the user.
# Note: A function must be defined before it is called.
# Let's see an example: 

# If we don't call this function, it will not execute

def greet_user():
    print("Hi there")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")
