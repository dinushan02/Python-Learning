message = input(">")
words = message.split(' ') # split the message into words
emojis = {
    ":)": "😁",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)