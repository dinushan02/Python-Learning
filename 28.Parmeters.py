# These parameters are placeholders for receiving information.
# When a function is called, we pass the actual values (arguments) to these parameters.
# Parameters allow us to customize the behavior of functions based on the input provided.
# Example:
# Here, 'name' is a parameter that the function 'greet_user' uses to receive a value when called.
# When we call the function, we provide an argument (e.g., "John" or "Mary") that gets assigned to the parameter 'name'.
# 😁😁😁Difference between parameters and arguments:
# Parameters are defined within the parentheses in the function definition.
# Arguments are the actual values we pass to the function when we call it.

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")
print("Finish")