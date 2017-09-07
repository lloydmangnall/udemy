name = input("What is your name? ")
age = int(input("Hello {0}, how old are you? ".format(name)))

if 18 <= age <= 30:
    print("Please enjoy your time on holiday, {0}".format(name))
else:
    print("Sorry {0}, but you're not able to go on an 18-30 holiday".format(name))
