# ONLY UNPICKLE DATA THAT YOU TRUST!!!!

import pickle

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", 'rb') as pickled_file:
#     imelda2 = pickle.load(pickled_file)

# print(imelda2)

# album, artist, year, track_list = imelda2

# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     trackNumber, trackTitle = track
#     print(trackNumber, trackTitle)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=4)
    pickle.dump(even, pickle_file, protocol=4)
    pickle.dump(odd, pickle_file, protocol=4)
    pickle.dump(2998302, pickle_file, protocol=4)

with open("imelda.pickle", 'rb') as pickled_file:   # objects must be read in same order they were written
    imelda_list = pickle.load(pickled_file)
    even_list = pickle.load(pickled_file)
    odd_list = pickle.load(pickled_file)
    x = pickle.load(pickled_file)

print(imelda_list)

album, artist, year, track_list = imelda_list

print(album)
print(artist)
print(year)
for track in track_list:
    trackNumber, trackTitle = track
    print(trackNumber, trackTitle)

print("-" * 40)

for i in even_list:
    print(i)

print("-" * 40)

for i in odd_list:
    print(i)

print("-" * 40)

print(x)

print("-" * 40)

# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR")       # injects malicious code into the process
