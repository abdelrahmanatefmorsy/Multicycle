import tkinter as tk

class Line:
    def __init__(self, pos1, pos2):
        self.x = pos1
        self.y = pos2
        self.canvas = canvas.create_line(self.x[0], self.x[1], self.y[0], self.y[1], fill="black", width=3)

    def make_active(self):
        current_color = canvas.itemcget(self.canvas, "fill") 
        new_color = "#44f85c" if current_color == "black" else "black"
        canvas.itemconfig(self.canvas, fill=new_color)      




class Rectangle:
    def __init__(self, pos1, pos2, outline_color="black", bg_color="white"):
        """
        Initialize a rectangle.
        :param pos1: Top-left corner of the rectangle [x1, y1].
        :param pos2: Bottom-right corner of the rectangle [x2, y2].
        :param outline_color: Color of the border (default is black).
        :param bg_color: Fill color of the rectangle (default is white).
        """
        self.x1, self.y1 = pos1
        self.x2, self.y2 = pos2
        self.rectangle = canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2,
            fill=bg_color, outline=outline_color, width=2
        )

    def change_color(self, outline_color=None, bg_color=None):
        """
        Change the color of the rectangle.
        :param outline_color: New color for the border (optional).
        :param bg_color: New fill color for the rectangle (optional).
        """
        if outline_color:
            canvas.itemconfig(self.rectangle, outline=outline_color)
        if bg_color:
            canvas.itemconfig(self.rectangle, fill=bg_color)
class MUX:
    def __init__(self, top_left, bottom_right, fill_color="white", outline_color="black"):
        """
        Initialize an egg shape.
        :param top_left: Top-left corner of the bounding oval [x1, y1].
        :param bottom_right: Bottom-right corner of the bounding oval [x2, y2].
        :param fill_color: Fill color of the egg (default is white).
        :param outline_color: Outline color of the egg (default is black).
        """
        self.x1, self.y1 = top_left
        self.x2, self.y2 = bottom_right
        self.egg = canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2,
            fill=fill_color, outline=outline_color, width=2
        )
        self.stretch_top()

    def stretch_top(self):
        """
        Stretch the top of the egg to create an asymmetrical shape.
        """
        canvas.scale(self.egg, (self.x1 + self.x2) / 2, self.y1, 1.2, 0.8)  # Adjust the top to make it more egg-shaped

    def change_color(self, fill_color=None, outline_color=None):
        """
        Change the color of the egg.
        :param fill_color: New fill color for the egg (optional).
        :param outline_color: New outline color for the egg (optional).
        """
        if fill_color:
            canvas.itemconfig(self.egg, fill=fill_color)
        if outline_color:
            canvas.itemconfig(self.egg, outline=outline_color)
window = tk.Tk()
window.title("Full Screen Canvas")

window.attributes('-fullscreen', True)

window.bind("<Escape>", lambda e: window.attributes('-fullscreen', False))

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True) 
import tkinter as tk

rect1 = Rectangle([50,100],[200,300])

window.mainloop()
