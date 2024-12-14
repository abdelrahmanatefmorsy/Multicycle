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
y_offset =120 
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
MUX(canvas, center=[x_offset + 425, y_offset + 150], radius=6, text="",fill_color="black",radz=0)


# Instruction Register
instruction_register = Rectangle(canvas, [x_offset + 450, y_offset + 100], [x_offset + 550, y_offset + 200], text="Instruction\nRegister")


# Memory Data Register
memory_data_register = Rectangle(canvas, [x_offset + 450, y_offset + 250], [x_offset + 550, y_offset + 350], text="Memory\nData Register")

# Sign Extend
Line(canvas, [x_offset + 500, y_offset + 350], [x_offset + 500, y_offset + 400])
sign_extend = Rectangle(canvas, [x_offset + 450, y_offset + 400], [x_offset + 550, y_offset + 450], text="Sign Extend")

# Register File
Line(canvas, [x_offset + 550, y_offset + 150], [x_offset + 750, y_offset + 150])
MUX(canvas, center=[x_offset + 650, y_offset + 150], radius=8, text="",fill_color="black",radz=0)
Line(canvas, [x_offset + 655, y_offset + 150], [x_offset + 655, y_offset + 170],color="#FFA500")
Line(canvas, [x_offset + 655, y_offset + 170], [x_offset + 660, y_offset + 170],color="#FFA500")
MUX(canvas, center=[x_offset + 660, y_offset + 170], radius=3, text="",fill_color="#FFA500",outline_color="#FFA500",radz=0)
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
MUX(canvas, center=[x_offset + 670, y_offset + 150], radius=5, text="",fill_color="red",outline_color="red",radz=0)
Line(canvas, [x_offset + 670, y_offset + 150], [x_offset + 670, y_offset + 270],color="red")
Line(canvas, [x_offset + 670, y_offset + 270], [x_offset + 687, y_offset + 270],color="red")

register_file = Rectangle(canvas, [x_offset + 750, y_offset + 100], [x_offset + 850, y_offset + 350], text="Register\nFile")
Line(canvas, [x_offset + 850, y_offset + 150], [x_offset + 900, y_offset + 150])
A = Rectangle(canvas, [x_offset + 900, y_offset + 140], [x_offset + 950, y_offset + 160], text="A",bg_color="#ffe6cc", outline_color="#e9cc83")
Line(canvas, [x_offset + 850, y_offset + 300], [x_offset + 900, y_offset + 300])
B = Rectangle(canvas, [x_offset + 900, y_offset + 290], [x_offset + 950, y_offset + 310], text="B",bg_color="#ffe6cc", outline_color="#e9cc83")
Line(canvas, [x_offset + 950, y_offset + 150], [x_offset + 970, y_offset + 150])
MUX(canvas, center=[x_offset + 970, y_offset + 150], radius=3, text="",fill_color="black",outline_color="black",radz=0)
Line(canvas, [x_offset + 950, y_offset + 300], [x_offset + 970, y_offset + 300])
MUX(canvas, center=[x_offset + 970, y_offset + 300], radius=3, text="",fill_color="black",outline_color="black",radz=0)
Line(canvas, [x_offset + 973, y_offset + 300], [x_offset + 990, y_offset + 300])
MUX(canvas, center=[x_offset + 990, y_offset + 300], radius=3, text="",fill_color="black",outline_color="black",radz=0)
Line(canvas, [x_offset + 993, y_offset + 300], [x_offset + 1050, y_offset + 300])

MUX(canvas, center=[x_offset + 1050, y_offset + 310], radius=30, text="ALU \nSrc B")
MUX(canvas, center=[x_offset + 990, y_offset + 285], radius=8, text="4",outline_color="white",radz=0)
Line(canvas, [x_offset + 1000, y_offset + 285], [x_offset + 1038, y_offset + 285])
Line(canvas, [x_offset + 973, y_offset + 150], [x_offset + 990, y_offset + 150])
MUX(canvas, center=[x_offset + 990, y_offset + 150], radius=3, text="",fill_color="black",outline_color="black",radz=0)
Line(canvas, [x_offset + 993, y_offset + 150], [x_offset + 1050, y_offset + 150])
MUX(canvas, center=[x_offset + 1050, y_offset + 140], radius=30, text="ALU \nSrc A")
Line(canvas, [x_offset + 1080, y_offset + 140], [x_offset + 1100, y_offset + 140])
Line(canvas, [x_offset + 1080, y_offset + 310], [x_offset + 1100, y_offset + 310])


# # ALU (كمثلث)
alu_points = [
    [x_offset + 1100, y_offset + 100],  # النقطة العلوية
    [x_offset + 1250, y_offset + 230],  # النقطة اليمنى
    [x_offset + 1100, y_offset + 320],  # النقطة السفلية
]
alu = ALU(canvas, alu_points, text="ALU")
Line(canvas, [x_offset + 1200, y_offset + 260], [x_offset + 1200, y_offset + 320])
Line(canvas, [x_offset + 1200, y_offset +190], [x_offset + 1200, y_offset + 120])
Rectangle(canvas, [x_offset + 1180, y_offset + 100], [x_offset + 1220, y_offset + 120], text="Z",bg_color="white", outline_color="white")
Rectangle(canvas, [x_offset + 1180, y_offset + 320], [x_offset + 1220, y_offset + 340], text="ALU OP",bg_color="white", outline_color="white")
ANDGate(canvas,1220,320)
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
window.mainloop()
