fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)

# dynamic view objects
# fruitKeys = fruit.keys()
# print(fruitKeys)
#
# fruit["tomato"] = "not nice with ice cream" # can add items to a dictionary
# print(fruitKeys)
#
# print(fruit.items())                        # creates a tuple out of each dict_value
#
# f_tuple = tuple(fruit.items())
# print(f_tuple)                              # creates a tuple out of the entire dictionary
#
# for snack in f_tuple:                       # unpack the tuple like normal
#     item, description = snack
#     print(item + ' is ' + description)
#
# print(dict(f_tuple))                        # can also create a dictionary from a tuple

# using .join method for string concatenation
myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

newString = ''
for c in myList:
    # newString += c + ", "                   # very inefficient
    # newString = ", ".join(myList)           # use .join method to concatenate strings
    newString = " mississippi ".join(numbers)
print(newString)
