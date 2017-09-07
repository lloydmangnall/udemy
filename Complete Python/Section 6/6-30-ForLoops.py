# for i in range(1,20): # range = 1-19
#     print("i is now {}".format(i))

# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i]) # print the character at position i

number = "9,223,372,036,854,775,807"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789': # strip the commas
        print(number[i], end='')  # print the character at position i without /n
        cleanedNumber = cleanedNumber + number[i] # store the number in a new string variable
newNumber = int(cleanedNumber) # convert the string to an int
print()
print("The number stored in the variable is {} ".format(newNumber)) # print the new number


