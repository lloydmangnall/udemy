try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# Simple method to test tkinter
# tkinter._test()

# Alternative method to create a simple window
mainWindow = tkinter.Tk()
mainWindow.title('Hello World')
mainWindow.geometry('640x480+300+400')
mainWindow.mainloop()

# everything in Tk is a window and objects are placed in a hierarchy
