try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
import os

mainWindow = tkinter.Tk()

# size & positioning of the window on the screen
mainWindow.title('Grid Demo')
mainWindow.geometry('640x480+600+400')
mainWindow['padx'] = 8

# the top window label
label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

# configuring the overall grid layout
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=3)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# scrolling list box view of my OneDrive directory
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Users/lloyd/OneDrive'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# frame for radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')
rbValue= tkinter.IntVar()
rbValue.set(3)
# radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
# optionFrame['padx'] = 10

# widget to display the result
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(2, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to_=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to_=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# frame for the date spinners
# dateFrame = tkinter.LabelFrame(mainWindow, text='Date')
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# date spinners
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to_=31)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpinner = tkinter.Spinbox(dateFrame, width=5, from_=2000, to_=2025)
daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)
# dateFrame['padx'] = 36

# program buttons
okButton = tkinter.Button(mainWindow, text='OK')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)  # omit the parentheses on the .destroy function
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

# print(rbValue.get())