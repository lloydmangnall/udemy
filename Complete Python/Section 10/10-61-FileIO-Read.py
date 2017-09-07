# File Input/Output

# Basics of reading text files:
# jabber = open("sample.txt","r")     # 1) Open the file (read only)
# for line in jabber:                 # 2) Read data
#     print(line)
# jabber.close()                      # 3) Close the file

# common mode of reading text files using the WITH-AS notation
# with open("sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()          # reads a single line
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()          # reads the entire file and puts each LINE into a list
# print(lines)

# for line in lines:                      # print each line in list of 'lines'
#     print(line, end='')

with open("sample.txt", "r") as jabber:
    lines = jabber.read()          # reads the entire file and puts each CHARACTER into a list

for line in lines[::-1]:                # print each letter in list of 'lines' in reverse order
    print(line, end='')
