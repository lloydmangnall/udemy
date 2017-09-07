# what is a LIST in python?
#

# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count('.'))

# parrotList = ["not pinin'", "no more", "a stiff", "bereft of life"]
#
# parrotList.append("A Norwegian Blue")
#
# for state in parrotList:
#     print("This parrot is " + state)


# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# # numbers = even + odd
# orderedNumbers = sorted(numbers)

# numbers.sort() will sort 'numbers'
# print(numbers)
# print(sorted(numbers))  # sorted with also sort 'numbers'
#
# # list can be compared to one another
# if numbers == orderedNumbers:
#     print("Lists equal")
# else:
#     print("Lists not equal")
# if sorted(numbers) == orderedNumbers:
#     print("Lists equal")
# else:
#     print("Lists not equal")
#
# # list with no parameters
# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

#  comparing lists can be confusing as it could be looking at same list verses two different equal lists
# even = [2, 4, 6, 8]
# another_even = even  # set another list pointing to the SAME list
#
# another_even.sort(reverse=True)  # reverses the 'another_even' list
# print(even)  # returns the reverse of the 'even' list
# print(another_even is even)
# print(another_even == even)

# list of lists
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

print(numbers)

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)