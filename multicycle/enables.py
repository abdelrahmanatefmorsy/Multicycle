from classes import *

# Function to draw a grid on the canvas
def draw_grid(canvas, width, height, grid_size=20, color="#e0e0e0"):
    for x in range(0, width, grid_size):
        canvas.create_line(x, 0, x, height, fill=color)
    for y in range(0, height, grid_size):
        canvas.create_line(0, y, width, y, fill=color)

# Initialize the Tkinter window
window = tk.Tk()
window.title("Multi-Cycle Microprocessor Diagram")
window.geometry("1600x900")  # Window size
window.configure(bg="white")  # Set the background color of the window

# Create a canvas and pack it
canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Draw the grid
canvas_width = 1600
canvas_height = 900
draw_grid(canvas, canvas_width, canvas_height, grid_size=20)
x_offset = 50
y_offset =100 

# PC (Program Counter)
pc = Rectangle(canvas, [x_offset + 50, y_offset + 100], [x_offset + 150, y_offset + 200], text="PC")
Fetch.append(Line(canvas, [x_offset + 150, y_offset + 150], [x_offset + 200, y_offset + 150]))
 
# IorD Multiplexer (كدائرة)
IorD = MUX(canvas, center=[x_offset + 225, y_offset + 150], radius=25, text="IorD")
Fetch.append(Line(canvas, [x_offset + 250, y_offset + 150], [x_offset + 300, y_offset + 150]))
Decode.extend(Fetch)
# Memory
memory = Rectangle(canvas, [x_offset + 300, y_offset + 100], [x_offset + 400, y_offset + 500], text="Memory")
Fetch.append(Line(canvas, [x_offset + 400, y_offset + 150], [x_offset + 450, y_offset + 150]))
Line(canvas, [x_offset + 425, y_offset + 150], [x_offset + 425, y_offset + 280])
Line(canvas, [x_offset + 425, y_offset + 280], [x_offset + 450, y_offset + 280])
MUX(canvas, center=[x_offset + 425, y_offset + 150], radius=6, text="",fill_color="black")


# Instruction Register
instruction_register = Rectangle(canvas, [x_offset + 450, y_offset + 100], [x_offset + 550, y_offset + 200], text="Instruction\nRegister")


# Memory Data Register
memory_data_register = Rectangle(canvas, [x_offset + 450, y_offset + 250], [x_offset + 550, y_offset + 350], text="Memory\nData Register")

# Sign Extend
Line(canvas, [x_offset + 500, y_offset + 350], [x_offset + 500, y_offset + 400])
sign_extend = Rectangle(canvas, [x_offset + 450, y_offset + 400], [x_offset + 550, y_offset + 450], text="Sign Extend")

# Register File
Line(canvas, [x_offset + 550, y_offset + 150], [x_offset + 750, y_offset + 150])
MUX(canvas, center=[x_offset + 650, y_offset + 150], radius=8, text="",fill_color="black")
Line(canvas, [x_offset + 655, y_offset + 150], [x_offset + 655, y_offset + 170],color="#FFA500")
Line(canvas, [x_offset + 655, y_offset + 170], [x_offset + 660, y_offset + 170],color="#FFA500")
MUX(canvas, center=[x_offset + 660, y_offset + 170], radius=3, text="",fill_color="#FFA500",outline_color="#FFA500")
Line(canvas, [x_offset + 660, y_offset + 170], [x_offset + 710, y_offset + 170],color="#FFA500")
MUX(canvas, center=[x_offset + 710, y_offset + 180], radius=25, text="Read\nReg",fill_color="white")
Line(canvas, [x_offset + 735, y_offset + 180], [x_offset + 750, y_offset + 180])
Line(canvas, [x_offset + 660, y_offset + 170], [x_offset + 660, y_offset + 240],color="#FFA500")
Line(canvas, [x_offset + 660, y_offset + 240], [x_offset + 680, y_offset + 240],color="#FFA500")
Line(canvas, [x_offset + 650, y_offset + 150], [x_offset + 650, y_offset + 250],color="blue")
Line(canvas, [x_offset + 650, y_offset + 250], [x_offset + 700, y_offset + 250],color="blue")
Line(canvas, [x_offset + 650, y_offset + 200], [x_offset + 695, y_offset + 200],color="blue")
MUX(canvas, center=[x_offset + 700, y_offset + 250], radius=25, text="write")
Line(canvas, [x_offset + 725, y_offset + 250], [x_offset + 750, y_offset + 250])
MUX(canvas, center=[x_offset + 670, y_offset + 150], radius=5, text="",fill_color="red",outline_color="red")
Line(canvas, [x_offset + 670, y_offset + 150], [x_offset + 670, y_offset + 270],color="red")
Line(canvas, [x_offset + 670, y_offset + 270], [x_offset + 687, y_offset + 270],color="red")

register_file = Rectangle(canvas, [x_offset + 750, y_offset + 100], [x_offset + 850, y_offset + 350], text="Register\nFile")

# # ALU (كمثلث)
# Line(canvas, [x_offset + 750, y_offset + 150], [x_offset + 850, y_offset + 150])
# alu_points = [
#     [x_offset + 850, y_offset + 100],  # النقطة العلوية
#     [x_offset + 950, y_offset + 150],  # النقطة اليمنى
#     [x_offset + 850, y_offset + 200],  # النقطة السفلية
# ]
# alu = ALU(canvas, alu_points, text="ALU")

# # ALU Control
# alu_control = Rectangle(canvas, [x_offset + 850, y_offset + 250], [x_offset + 950, y_offset + 350], text="ALU Control")

# # PC Source Multiplexer (كدائرة)
# Line(canvas, [x_offset + 950, y_offset + 150], [x_offset + 1000, y_offset + 150])
# pc_source = MUX(canvas, center=[x_offset + 1025, y_offset + 150], radius=25, text="PC\nSRC")

# # 2SL Unit
# l1 = Line(canvas, [x_offset + 550, y_offset + 425], [x_offset + 600, y_offset + 425])
# lst = []
# lst.append(l1)
# lst[0].make_active()
# two_sl = Rectangle(canvas, [x_offset + 600, y_offset + 400], [x_offset + 700, y_offset + 450], text="2SL")
# Line(canvas, [x_offset + 700, y_offset + 425], [x_offset + 850, y_offset + 300])

# تشغيل النافذة
from classes import *
import re
s = "add  $t0 , $t1 , $t2"
Registers = [
    "$zero",
    "$v0", "$v1", 
    "$a0", "$a1", "$a2", "$a3",
    "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7",
    "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7",
    "$t8", "$t9"
]
# def r_type(instruction):
#     if(len(instruction) != 4):
#         print("invalid instruction")
#     if(instruction[0] in ["sll","srl"]):
#         pass
#     else:
#         if (instruction[1] in Registers and instruction[2] in Registers and instruction[3] in Registers):
#             for j in Fetch:
#                 j.make_active()
#         else:
#             print(instruction[1:])
    


# code = [(["add,sub,and,or,sll,srl", lambda instruction: r_type(instruction)])]
# lst = re.split(r'[ ,]+', s)
# for i in code:
#     if lst[0] in i[0]:
#         i[1](lst)

window.mainloop()
