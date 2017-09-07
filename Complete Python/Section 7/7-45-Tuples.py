# TUPLES are immutable ordered sets of data similar to lists

# t = "a", "b", "c"  # this returns a tuple
# print(t)

# print("a", "b", "c")  # this does NOT return a tuple
# print(("a", "b", "c"))  # enclosing in () returns a tuple

# right-hand side of an expression is evaluated first
# a = b = c = d = 12
# print(c)
# a, b = 12, 13
# print(a, b)

# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
bidgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imelda May", 2011
metallica = "Ride the Lightening", "Metallica", 1984

# you can access the tuple and its elements
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# tuples are immutable, so the following throws an exception
# metallica[0] = "Master of Puppets"

# however tuples support indexing and slicing to work around immutability
# imelda = imelda[0], "Imelda May", imelda[2]  # haven't changes the tuple, but the variable referencing the tuple object
# print(imelda)

# by contrast, lists are mutable objects
# metallica2 = ["Ride the Lightening", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# unpacking a tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)