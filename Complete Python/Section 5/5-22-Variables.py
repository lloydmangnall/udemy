greeting = "Hello"
_myName = "Lloyd"
Lloyd50 = "good"
Lloyd_Was_49 = "Hello"
Greeting = "Hola"
print(Lloyd_Was_49 + ' ' + _myName)

age = 50
print(age)

# print(greeting + age) "Can't add string to number"

a = 12 #int now behaves as a long
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# for i in range(1, a/b): "using / throws an error as float cannot be interpreted as an int"
for i in range(1, a // b):
    print(i)

print(a + b / 3 - 4 * 12)
print(8 / 2 * 3)
print(8 * 3 / 2)
print((((a+b)/3)-4)*12)

# same output can be accomplished with intermediate variables
c = a + b
d = c / 3
e = d - 4
print(e * 12)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[0])
print(parrot[-1]) # start at end of string
print(parrot[0:6]) # 6 characters starting at index 0
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:2])
print(parrot[-4:-2])
print(parrot[0:6:2]) #
print(parrot[0:6:3]) #

number = "9,223,372,036,854,775,807"
print(number[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " "probably " "pining")
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)
print('fri' in today)
print('thur' in today)
print("parrot" in "fjord")

