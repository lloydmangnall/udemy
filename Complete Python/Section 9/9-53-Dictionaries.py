fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a {}".format(dict_key))
#     if dict_key in fruit:
#         description = fruit.get(dict_key)      # retrieve the value of the key from the dictionary
#         print(description)
#     else:
#         print("We don't have {}".format(dict_key))

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# orderedKeys = list(fruit.keys())                # sorting dictionary keys
# orderedKeys.sort()
orderedKeys = sorted(list(fruit.keys()))          # sorting keys with one line of code w/ .keys method
# for f in orderedKeys:
# for f in sorted(fruit.keys()):                  # sorting key directly in the FOR LOOP w/ .keys method
#     print(f + ' - ' + fruit[f])

# for val in fruit.values():                      # you can also use the .values method, but...
#     print(val)
# print('-' * 40)
# for key in fruit:                               # ...not as optimized as the key method
#     print(fruit[key])

# print(fruit.keys())                             # returns the dictionary keys (dict_keys) object
# print(fruit.values())                           # returns the dictionary values (dict_values) object

fruitKeys = fruit.keys()
print(fruitKeys)

fruit["tomato"] = "not nice with ice cream"
print(fruitKeys)