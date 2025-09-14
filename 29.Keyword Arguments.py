def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith") # Positional argument
print("Finish")

# calc_cost(total=50, shipping=5, discount=0.1) # Can immediately tell what these values represent. 
# That is a power of keyword argument.
# For the most part, 😁use positional arguments, but if you are dealing with functiona that take
# numerical values.
# If you can improve the readability of your code by using keyword arguments.
# If we are mixing, these keyword arguments should always come after positional arguments.