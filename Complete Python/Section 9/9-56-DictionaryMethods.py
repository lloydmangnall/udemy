# fruit dictionary
fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)

# vegetable dictionary
veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}
print(veg)

# create a combined veg + fruit dictionary
# veg.update(fruit)
# print(veg)

# .update does NOT return a new object
# print(fruit.update(veg)
# print(fruit)

# create a combined dictionary without modifying the original dictionaries, use the .copy method
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)