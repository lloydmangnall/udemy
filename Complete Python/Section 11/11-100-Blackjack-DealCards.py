import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()


# function to load the cards
def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


# functions to deal cards from the deck
def deal_card(frame):
    # pop the next card off of the top of the deck
    next_card = deck.pop()
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def deal_dealer():
    deal_card(dealer_card_frame)


def deal_player():
    deal_card(player_card_frame)

# Set up the screen and frames for the dealer and player
mainWindow.title('Blackjack')
mainWindow.geometry('1024x768')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, text=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame to hold the dealer cards
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, text=player_score_label, background='green', fg='white').grid(row=3, column=0)
# embedded frame to hold the player cards
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
print(cards)

# create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

mainWindow.mainloop()
