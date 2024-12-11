from functools import partial
import tkinter as tk

class Line:
    def __init__(self, canvas, pos1, pos2, color="black", width=2, command=None, command_arg=None):
        # Store the line ID and canvas reference
        self.canvas = canvas
        self.command = command  # Store the function to call on click
        self.command_arg = command_arg  # Argument to pass to the command

        # Create the line on the canvas
        self.line = canvas.create_line(
            pos1[0], pos1[1], pos2[0], pos2[1],
            fill=color, width=width
        )
        
        # Bind the click event to the line
        canvas.tag_bind(self.line, "<Button-1>", self.on_click)

    def on_click(self, event):
        """Handle the line click event."""
        if self.command:  # If a command function is provided, call it with the argument
            self.command(self.command_arg)

# Example function that takes an integer parameter
def on_line_click(arg):
    print(f"Line clicked with argument: {arg}")

    
    def make_active(self):
        # Get the current color of the line
        current_color = self.canvas.itemcget(self.line, "fill")
        
        # Toggle the color
        new_color = "#44f85c" if current_color == "black" else "black"
        self.canvas.itemconfig(self.line, fill=new_color)  

class Rectangle:
    def __init__(self, canvas, pos1, pos2, text="", bg_color="white", outline_color="black"):
        self.rectangle = canvas.create_rectangle(
            pos1[0], pos1[1], pos2[0], pos2[1],
            fill=bg_color, outline=outline_color, width=2
        )
        if text:
            canvas.create_text(
                (pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2,
                text=text, font=("Arial", 10)
            )

# تعريف الـ Multiplexer (MUX) كدائرة
class MUX:
    def __init__(self, canvas, center, radius, text="", fill_color="white", outline_color="black"):
        x, y = center
        self.mux = canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=fill_color, outline=outline_color, width=2
        )
        if text:
            canvas.create_text(
                x, y, text=text, font=("Arial", 10)
            )

# تعريف وحدة ALU كمثلث
class ALU:
    def __init__(self, canvas, points, text="", fill_color="white", outline_color="black"):
        self.alu = canvas.create_polygon(
            points, fill=fill_color, outline=outline_color, width=2
        )
        if text:
            # حساب مركز المثلث لوضع النص
            x_center = sum(p[0] for p in points) / len(points)
            y_center = sum(p[1] for p in points) / len(points)
            canvas.create_text(
                x_center, y_center, text=text, font=("Arial", 10)
            )
def on_line_click():
    print("Line clicked!")
Fetch = []
Decode = []
Lines =list(range(1,300))
