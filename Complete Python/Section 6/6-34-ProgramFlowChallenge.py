address = input("Please enter an IP address: ")

# Initialize variables
segment = 1
segmentLength = 0
character = ''

# Loop through characters
for character in address:
    if character == '.':
        print("Segment {} contains {} characters.".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1
        continue

# final character is a '.'
if character != '.':
    print("Segment {} contains {} characters.".format(segment, segmentLength))
