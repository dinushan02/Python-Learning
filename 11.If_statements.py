"""is_hot = False  # Boolean value representing if it's hot
is_cold = False  # Boolean value representing if it's cold

if is_hot:  # If is_hot is True, this block will execute
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:  # If is_hot is False and is_cold is True, this block will execute
    print("It's a cold day")
    print("Wear warm clothes")
else:  # If both is_hot and is_cold are False, this block will execute
    print("It's a lovely day")

print("Enjoy your day")  # This will always be printed as it's outside the if-else block"""

price = 1000000  # The total price of the item
has_credit_good = True  # Boolean indicating if the user has good credit

if has_credit_good:  # If the user has good credit, down payment is 10% of the price
    down_payment = 0.1 * price
else:  # If the user doesn't have good credit, down payment is 20% of the price
    down_payment = 0.2 * price

# Print the down payment amount using formatted string
print(f"Down payment: ${down_payment}")

