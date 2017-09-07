#
# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", "w") as cityFile:
#     for city in cities:
#         print(city, file=cityFile, flush=True)

# cities = []

# with open("cities.txt", "r") as cityFile:
#     for city in cityFile:
#         cities.append(city.strip('\n'))     # strips the newline (\n) from ONLY the begin/end of an element

# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#      (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# with open("imelda.txt", 'w') as imeldaFile:
#     print(imelda, file=imeldaFile)

with open("imelda.txt", 'r') as imeldaFile:
    contents = imeldaFile.readline()

imelda = eval(contents)     # NOT good security practice to use 'eval' when reading files/data as it can enable injection

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
