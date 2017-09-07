# SETS are used less often, but are useful for cleaning up data
# SETS are completely unordered
# farmAnimals = {"sheep", "cow", "hen"}
# print(farmAnimals)

# for animal in farmAnimals:
#     print(animal)

# print("=" * 40)

# wildAnimals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wildAnimals)

# for animal in wildAnimals:
#     print(animal)

# farmAnimals.add("horse")
# wildAnimals.add("horse")
# print(farmAnimals)
# print(wildAnimals)

# emptySet = set()    # creates an empty set
# emptySet2 = {}      # creates an empty dictionary
# emptySet.add("a")
# emptySet2.add("a")  # dictionary does not have a .add method

# even = set(range(0, 40, 2)) # must use SET when constructing sets from iterator objects (ranges, tuples, etc).
# print(even)
# print(len(even))
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squares)
# print(len(squares))

# print('-' * 40)

# SET union (|)
# print(even.union(squares))
# print(even | squares)
# print(len(even.union(squares)))

# print(squares.union(even))

# print('-' * 40)

# SET intersection (&)
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# SET .difference method
# print(sorted(even))
# squares = set(squaresTuple)
# print(sorted(squares))

# print("difference (e - s)")
# print(sorted(even.difference(squares)))         # Return a new set with elements in the set that are not in others.
# print(sorted(even - squares))

# print("difference (s - e)")
# print(sorted(squares.difference(even)))         # difference makes it clear you're working on a set
# print(squares - even)                           # whereas subtraction isn't as clear it is a set

# SET .difference_update method
# even = set(range(0, 40, 2))
# print("difference update (e - s)")              # Update the set, removing elements found in others.
# print(even.difference_update(squares))          # Update does NOT 'return' anything
# even.difference_update(squares)
# print(even)

# SET .symmetric_difference method
# even = set(range(0, 40, 2))
# print("symmetric difference (e - s)")
# print(even.symmetric_difference(squares))       # Return a new set with elements in either the set or other,
# print(even ^ squares)                           # but not both.

# SET .symmetric_difference_update method
# even = set(range(0, 40, 2))
# print("symmetric difference update (e - s)")
# print(even.symmetric_difference_update(squares))# Again, Update does NOT 'return' anything
# even.symmetric_difference_update(squares)       # Update the set, keeping only elements found in either set,
# print(even)                                     # but not in both.

# SET .discard & .remove methods
# print("remove items from a set")
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)                              # no exception, does nothing as there is no '8' in the set
# print(squares)
# try:
#     squares.remove(8)                             # throws an exception, discard is 'safer'
# except KeyError:                                  # but .remove handy when exception wanted
#     print("The item '8' is not a member of the set")

# SUBSETS and SUPERSETS
even = set(range(0, 40, 2))
squaresTuple = (4, 16, 36)
squares = set(squaresTuple)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("squares is a superset of even")


# FROZENSET, like a set, but immutable as the name implies
even = frozenset(range(0, 100, 2))
print(even)
# even.add(3)     # illegal because a frozenset is immutable