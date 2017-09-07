# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

# Lloyd's solution
vowels = set(["a", "e", "i", "o", "u"])
text = set([])
string = input("Please enter some text: ")
for i in(string):
    text.add(i)
print(text)
print(sorted(text.difference(vowels)))

# Instructor's solution
sampleText = "qwertyuioplkjhgfdsazxcvbnm"
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)