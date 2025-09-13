# With a dictionary, we can store a bunch of key value pairs.
# Let me show you how to define a dictionary in Python
# {}=curly braces
# Back to our program, I am going to define a variable.
# 😃Each key should be unique in a dictionary.
# Key=> They can also be numbers.
# Value can be anything.
# Instead of using square brackets, we call the get() method and specify the key.
# None is an object that represents the absence of a value.
# If you try to access a key that doesn't exist in the dictionary, you'll get an error.
# To avoid this, you can use the get() method, which returns None if the key doesn't exist.
# when we use the get() method, we can also provide a default value to return if the key is not found.
# we can also update these values.
# before print statement, we can write code like this, customer["name"] = "New Name"
# we can add new key-value pairs to the dictionary.
# They are extremely important and they have a lot of applications in the real world.


"""customer = {
    "name": "Arutperunjothi Manava",
    "age": 30,
    "is_verified": True
}
# customer["name"] = "Dinushan"
customer["birthdate"] = "Jan 1 1990"
print(customer["birthdate"])"""

# Dictionary is a structure that allows us to map a key to a value.
# we can have a dictionary with keys
phone = input("Phone: ") 
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = "" # Initialize an empty string
for ch in phone: # Iterate over each character in the phone number
    output += digits_mapping.get(ch, "!") + " " # If the character is not found in the dictionary, it will return "!"
print(output)

