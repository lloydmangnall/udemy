# style good practices dictates <120 characters on a given line for readability
inputPrompt = "Please enter an IP address. An IP address consists of 4 numbers, " \
              "separated from each other with a full stop: "
ipAddress = input(inputPrompt)
if ipAddress[-1] != '.':
    ipAddress += '.'

# Initialize variables
segment = 1
segmentLength = 0
# character = ''

# Loop through characters
for character in ipAddress:
    if character == '.':
        print("Segment {} contains {} characters.".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1
        continue

# final character is a '.'
# if character != '.':
#     print("Segment {} contains {} characters.".format(segment, segmentLength))
