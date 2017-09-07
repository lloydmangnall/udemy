# string = "1234567890"

# for char in string:  #FOR LOOPS are examples of Iterators
#     print(char)

# myIterator = iter(string)
# print(myIterator)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
#
# print(next(myIterator))  # throws an exception

# both do the same thing
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

# iterator challenge
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# myList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
myList = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# for each in myList:
#     print(each)

myIterator = iter(myList)
for n in range(0, len(myList)):
    print(next(myIterator))
