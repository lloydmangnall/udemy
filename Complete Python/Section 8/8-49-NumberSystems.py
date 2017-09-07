# binary is a base 2 numbering system using digits 0-1
# octal is a base 8 numbering system using digits 0-7
# hexidecimal is a base 16 numbering system using digits 0-15

# for i in range(33):
#     print("{0:>2}\tis {0:>08b} in binary and {0:>02x} in hex".format(i))

# x = 0x20
# y = 0x0a

# print(x)
# print(y)
# print(x * y)

# print(0b101010)

# number system challenge
powers = []
# for power in range(15, -1, -1):   # binary
    # powers.append(2 ** power)
for power in range(7, -1, -1):      # octal
    powers.append(8 ** power)

print(powers)

printing = False

x = int(input("Please enter a number: "))

for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
