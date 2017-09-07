# shelve allows you to persist (pickle) application data to disk w/o having to resort to SQL
import shelve

# with shelve.open("ShelfTest") as fruit:  # WITH statement automatically closes the file when the block closes
fruit = shelve.open("ShelfTest")
fruit["orange"] = "a sweet, orange citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow citrus fruit"
fruit["grape"] = "a small, sweet fruit growing in bunches"
fruit["lime"] = "a sour, gree citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# interact with a shelve the same as a dictionary
# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "we don't have a " + shelf_key)
#     print(description)
#
#     print("-" * 40)
#
#     # an alternative to the above
#     if shelf_key in fruit:
#         description = fruit[shelf_key]
#         print(description)
#     else:
#         print("We don't have a " + shelf_key)

# sorting and ordering shelve items
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# values and items views
for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():  # returns a list of tuples
    print(f)

print(fruit.items())

fruit.close()

# print(fruit)
