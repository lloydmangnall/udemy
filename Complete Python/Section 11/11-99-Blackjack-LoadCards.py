try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

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
player_card_frame.grid(row=1, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Hit the Dealer')
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Hit the Player')
player_button.grid(row=1, column=0)



mainWindow.mainloop()