from functools import partial
import tkinter as tk
global root
mx_element = 2 ** 31 - 1
mn_element = -2 ** 31
class TextWithLineNumbers(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.text = tk.Text(self, height=17, width=40, font=("Arial", 14))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.line_numbers = tk.Canvas(self, width=30, bg="#dcdcdc")
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        self.text.bind("<KeyRelease>", self.update_line_numbers)
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.delete("all")
        i = self.text.index("@0,0")
        while True:
            dline = self.text.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.line_numbers.create_text(2, y, anchor="nw", text=linenum, font=("Arial", 14))
            i = self.text.index(f"{i}+1line")

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
        self.canvas.tag_bind(self.line, "<Button-1>", self.on_click)

    def on_click(self, event):
        print(self.id)

    
    def make_active(self):

        new_color = "#7CFC00"
        self.canvas.itemconfig(self.line, fill=new_color)  
    def reactive(self):
        new_color = "black"
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

class MUX:
    def __init__(self, canvas, center, radius, text="", fill_color="white", outline_color="black",radz = 8):
        x, y = center
        radius_x = radius  
        radius_y = radius 
        
        self.mux = canvas.create_oval(
            x - radius_x, y - radius_y, x + radius_x, y + radius_y,
            fill=fill_color, outline=outline_color, width=2
        )
        if text:
            canvas.create_text(
                x, y, text=text, font=("Arial", 10)
            )
class ALU:
    def __init__(self, canvas, points, text="", fill_color="white", outline_color="black"):
        self.alu = canvas.create_polygon(
            points, fill=fill_color, outline=outline_color, width=2
        )
        if text:
            x_center = sum(p[0] for p in points) / len(points)
            y_center = sum(p[1] for p in points) / len(points)
            canvas.create_text(
                x_center, y_center, text=text, font=("Arial", 10)
            )

def on_line_click():
    print("Line clicked!")
Fetch = {71, 0, 6, 7, 101, 101, 7, 8, 55, 58, 59, 59, 61, 80, 63, 82, 82, 83, 83, 84, 84, 84, 85, 85, 85, 9,81,1,15,16,17,73,86}
Decode = {8, 39, 7, 28, 29, 61, 6, 37, 9,  27, 25, 24, 59,58,49,50,34,35}
R_type1 = {52, 54, 51,  58, 59, 56, 53, 61,50,49,57}
R_type2 = {44,43,60,23,22,14,65,46,21,70}
I_type = {49,51,57,56,58,24,25,30,31,32,33,59,61}
I_type_2 =[60,42,41,37,22,14,65,181,125,123,172,148,23,21,46,70,23,22,22,21,46,60]

lw1 = {63,64,13,12,10,15,65,14,11,10}
lw2 = {17,18,19,20,41,42,46,70,37,60}
Sw = {13,12,52,53,69,68,67,66,14,10,11,15,63,64,65}
Beq ={51,57,58,56,61, 62, 59, 52, 53, 54, 74, 63, 65, 76, 77, 78,75,79,64 ,83 ,84 ,85 , 86, 82, 71,72,73, 379,378}
J ={91, 89, 88, 82, 83, 84, 86, 73,90,92,34,85,71}
Jal =  {34, 92, 91, 89, 73, 0, 2, 4, 5, 70, 47, 48,88,90,3,46,82,83,84,85,86,71,34}
Jr ={51, 56, 96, 95, 94, 93, 82, 83, 84 ,85,86,73,71}

def fetch():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Fetch:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def decode():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Decode:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def r_type1():
    for j in Line.Lines_lst:
        j.reactive()
    for i in R_type1:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def r_type2():
    for j in Line.Lines_lst:
        j.reactive()
    for i in R_type2:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def i_type1():
    for j in Line.Lines_lst:
        j.reactive()
    for i in I_type:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def i_type2():
    for j in Line.Lines_lst:
        j.reactive()
    for i in I_type_2:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def Lw1():
    for j in Line.Lines_lst:
        j.reactive()
    for i in lw1:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def Lw2():
    for j in Line.Lines_lst:
        j.reactive()
    for i in lw2:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def sw():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Sw:
         if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def BEQ():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Beq:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def jumb():
    for j in Line.Lines_lst:
        j.reactive()
    for i in J:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def jumbreg():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Jr:
        if(i <len(Line.Lines_lst)):
            Line.Lines_lst[i].make_active()
def jumbal():
    for j in Line.Lines_lst:
        j.reactive()
    for i in Jal:
          if(i <len(Line.Lines_lst)):
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
