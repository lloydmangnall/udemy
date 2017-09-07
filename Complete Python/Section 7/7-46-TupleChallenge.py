# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
#
# title, artist, year, tracks = imelda  # unpack tracks tuple
# print(title)
# print(artist)
# print(year)
# for song in tracks:                   # loop through songs
#     track, title = song               # unpack song tuple(s)
#     print("\tTrack {}: {}".format(track, title))


# follow on question: if a tuple is immutable, what about a list IN a tuple??
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])  # list of 4 tuples within a tuple

print(imelda)

imelda[3].append((5, "All For You"))    # add another track tuple to the tracks list

title, artist, year, tracks = imelda    # unpack tracks tuple
tracks.append((6, "Eternity"))          # add another track tuple to the mutable tracks list
print(title)
print(artist)
print(year)
for song in tracks:                     # loop through songs
    track, title = song                 # unpack song tuple(s)
    print("\tTrack {}: {}".format(track, title))
