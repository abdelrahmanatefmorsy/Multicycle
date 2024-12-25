from functools import partial
import tkinter as tk
global root 
class Line:
    count = 0
    Lines_lst = []
    def __init__(self, canvas, pos1, pos2, color="black", width=2):
        self.id = Line.count
        Line.count+=1
        Line.Lines_lst.append(self)
        self.canvas = canvas
        self.line = canvas.create_line(
            pos1[0], pos1[1], pos2[0], pos2[1],
            fill=color, width=width
        )
        # Bind the line to an event
        self.canvas.tag_bind(self.line, "<Button-1>", self.on_click)

    def on_click(self, event):
        print(self.id)

    
    def make_active(self):
        # Get the current color of the line
        
        # Toggle the color
        new_color = "#00ff00"
        self.canvas.itemconfig(self.line, fill=new_color)  
    def reactive(self):
        # Get the current color of the line
        
        # Toggle the color
        new_color = "black"
        self.canvas.itemconfig(self.line, fill=new_color)  

# Example function that takes an integer parameter
def on_line_click(arg):
        print(f"Line clicked with argument: {arg}")
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
    def __init__(self, canvas, center, radius, text="", fill_color="white", outline_color="black",radz = 8):
        x, y = center
        # تعديل لعمل شكل بيضاوي بدل دائرة
        radius_x = radius  # العرض الأفقي (يمكنك تعديله)
        radius_y = radius # الارتفاع الرأسي (يمكنك تعديله)
        
        self.mux = canvas.create_oval(
            x - radius_x, y - radius_y, x + radius_x, y + radius_y,
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
Fetch = [84, 84, 90, 91, 99, 99, 27, 68, 12, 13]
Decode = [4,2,1]
R_type1 = [5,6,10]
R_type2 = [9,10,11]
I_type = [12,13,14]
lw1 = []
lw2 = []
Sw = []
I_type_2 = [60,11,13]
Beq = []
J =[]
Jal = []
Jr =[]

def fetch():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Fetch:
        Line.Lines_lst[i].make_active()
def decode():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Decode:
        Line.Lines_lst[i].make_active()
def r_type1():
    for j in Line.Lines_lst:
        j.reactive()
    for i in R_type1:
        Line.Lines_lst[i].make_active()
def r_type2():
    for j in Line.Lines_lst:
        j.reactive()
    for i in R_type2:
        Line.Lines_lst[i].make_active()
def i_type1():
    for j in Line.Lines_lst:
        j.reactive()
    for i in I_type:
        Line.Lines_lst[i].make_active()
def i_type2():
    for j in Line.Lines_lst:
        j.reactive()
    for i in I_type_2:
        Line.Lines_lst[i].make_active()
def Lw1():
    for j in Line.Lines_lst:
        j.reactive()
    for i in lw1:
        Line.Lines_lst[i].make_active()
def Lw2():
    for j in Line.Lines_lst:
        j.reactive()
    for i in lw2:
        Line.Lines_lst[i].make_active()
def sw():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Sw:
        Line.Lines_lst[i].make_active()
def BEQ():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Beq:
        Line.Lines_lst[i].make_active()
def jumb():
    for j in Line.Lines_lst:
        j.reactive()
    for i in J:
        Line.Lines_lst[i].make_active()
def jumbreg():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Jr:
        Line.Lines_lst[i].make_active()
def jumbal():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Jal:
        Line.Lines_lst[i].make_active()

Registers = [
    "$zero",
    "$v0", "$v1",
    "$a0", "$a1", "$a2", "$a3",
    "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7",
    "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7",
    "$t8", "$t9"
]
instructions = ["add","sub","or","and","sll","srl","addi","subi","ori","andi","j","jal","jal","jr","swap","beq","bneq","bge","b","xor","xori","blt","bgt","ble","bge"]
