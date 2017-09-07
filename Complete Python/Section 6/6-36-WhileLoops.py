# for i in range(10):
#     print("i is now {}".format(i))

# this accomplishes same thing
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# WHILE LOOPS are used when the number of iterations is unknown
# availableExits = ["east", "north east", "south"]
#
# chosenExit = ''
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     if chosenExit == "quit":
#         print("Game Over")
#         break
# else:
#     print("Aren't you glad you got out of there!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly, the number was {}".format(answer))
else:
    print("Amazing, you go it on the first try")
