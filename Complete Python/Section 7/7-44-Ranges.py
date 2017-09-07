# decimals = range(0, 100)            # create a range (0-99)
# myRange = decimals[3:40:3]          # take a slice of 'decimals' to create a new range
# print(myRange == range(3, 40, 3))   # show the ranges are equal

# print(range(0, 5, 2) == range(0, 6, 2))  # these are equal as the lists are both [0, 2, 4]
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))

# r = range(0, 100)
# print(r)

# for i in r[::-2]:
#     print(i)

# print("=" * 50)
# for i in range(99, 0, -2):
#     print(i)

# print("=" * 50)
# print(range(0, 100)[::-2] == range(99, 0, -2))

# this will never work
# for i in range(0, 100, -2):
#     print(i)

# using negative step ranges is very powerful
# backString = "egaugnal lufrewop yrev a si nohtyP"
# print(backString[::-1])

# r = range(0, 10)
# for i in r[::-1]:
#     print(i)

# range challenge
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)