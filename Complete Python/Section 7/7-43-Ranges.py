# RANGES are a built in type in python3
# myList = list(range(10))
# print(myList)

# creating list using ranges
even = list(range(0, 10000, 2))
odd = list(range(1, 10000, 2))

# print(even)
# print(odd)

# these both use the same memory
# range(0, 10)
# range(0, 10000000)

# range index
# myString = "abcdefghijklmnopqrstuvwxyz"
# print(myString.index('e'))
# print(myString[4])

# smallDecimals = range(0, 10)
# # print(smallDecimals)
# # print(smallDecimals.index(3))
#
# print(odd)
# print(odd[985])
#
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
#
# print(smallDecimals)
#
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(4))

decimals = range(0, 100)
print(decimals)

# take a slice of 'decimals' to create a new range
myRange = decimals[3:40:3]
print(myRange)

# these are equivalent
for i in myRange:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

# show the ranges are equal
print(myRange == range(3, 40, 3))