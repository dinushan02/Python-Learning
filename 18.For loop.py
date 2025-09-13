"""#for item in 'Python':
#    print(item)  #Each character in this string is printed on a new line.

#for item in ["Arutperunjothi Andava","Aruldev","Dinushan"]:  #List of names
#    print(item)

#for item in [1,2,3,4,5]:  #List of numbers
#    print(item)

#for item in range(5,10,2):
#   print(item)"""

prices = [10, 20, 30] # List of prices

total = 0 # Initialize total to 0
for price in prices: # Iterate over each price in the list
    total += price # Add the current price to the total
print(f"Total: {total}")
