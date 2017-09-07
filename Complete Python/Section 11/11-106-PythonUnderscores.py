# the meaning of underscores (_) in python object names:
# add an underscore to the end of a name that is the same as a python standard keyword

# python doesn't have the concept of private/protected variables
# names with a single underscore (_myvar) at the beginning indicates protected/private variable

# names with double underscores (__myvar) at the beginning invokes python's name mangling rules
# used to prevent name clashes

# names if double underscores (__name__) at the start and end indicates objects that should NOT be changed

# variables named with ONLY a single underscore (_) is a throw-away variable


import blackjack
# from blackjack import *

# g = sorted(globals())
# for x in g:
#     print(x)

blackjack._deal_card(blackjack.dealer_card_frame)
blackjack.play()

