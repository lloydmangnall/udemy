import math
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)

# challenge: modify the circle function so that it allows the color of the circle to be specified
# and defaults to red if a color is not given.  You may want to review the previous lectures
# about named parameters and default values.
def circle(page, radius, g, h, color='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)

    # a circle can also be plotted with the following algebra, but it renders very slowly
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("1024x768")

canvas = tkinter.Canvas(mainWindow, width=1024, height=768)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, 'green')
circle(canvas, 100, 100, -100, 'orange')
circle(canvas, 100, -100, 100, 'purple')
circle(canvas, 100, -100, -100, 'blue')
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
