# unordered collections
fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "round and crunchy"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"   # dictionaries are mutable
# print(fruit)
# fruit["lime"] = "great with tequila"    # values can be overridden
# print(fruit)
# del fruit["lemon"]                      # values can also be deleted
# print(fruit)
# fruit.clear()                           # deletes ALL values without deleting the dictionary
# print(fruit)
# del fruit                               # deletes the dictionary

print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)      # retrieve the value of the key from the dictionary
        print(description)
    else:
        print("We don't have {}".format(dict_key))

# bike = {"make": "honda", "model": "250 dream", "color": "red", "engine size": 250}
# print(bike["engine size"])
# print(bike["color"])