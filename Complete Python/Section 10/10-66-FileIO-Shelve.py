# using the SHELVE module
# shelve builds on top of pickle and implements a serialization dictionary where objects are pickled
# but associated with a key (some string), so you can load your shelved data file and access your pickled
# objects via keys. Shelve is more convenient were you to be serializing many objects.
import shelve

with shelve.open("ShelfTest") as fruit:  # using the WITH statement automatically closes the file when the block closes
    fruit["orange"] = "a sweet, orange citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, gree citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

with shelve.open("bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["color"] = "red"
    # bike["engin_size"] = "250"

    del bike["engin_size"]

    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["color"])
