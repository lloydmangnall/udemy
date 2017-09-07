# options for importing other modules
# option 1: import turtle
# option 2: from turtle import forward, right, done  # can be useful if you want to avoid referencing turtle.method
# option 3: from turtle import * # should generally avoid this import approach

import webbrowser
# help(webbrowser)

# webbrowser.open("http://www.python.org/", new=1)

chrome = webbrowser.get(using='windows-default')
chrome.open_new_tab("http://www.python.org/")

