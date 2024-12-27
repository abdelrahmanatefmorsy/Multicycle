from classes import *
from globalVar import *
def Multi_cycle(canvas,window,actives):
    def toggle_fullscreen(event=None):
        current_state = window.attributes('-fullscreen')
        window.attributes('-fullscreen', not current_state)
    window.attributes('-fullscreen', True)
    window.bind("<Escape>", toggle_fullscreen)
    def draw_grid(canvas, width, height, grid_size=20, color="#e0e0e0"):
        for x in range(0, width, grid_size):
            canvas.create_line(x, 0, x, height, fill=color)
        for y in range(0, height, grid_size):
            canvas.create_line(0, y, width, y, fill=color)

    canvas = tk.Canvas(window, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas_width = 1600
    canvas_height = 900
    draw_grid(canvas, canvas_width, canvas_height, grid_size=20)
    x_offset = -10
    y_offset =120 
    # PC (Program Counter)
    pc = Rectangle(canvas, [x_offset + 50, y_offset + 100], [x_offset + 150, y_offset + 200], text="PC")
    Line(canvas, [x_offset + 150, y_offset + 150], [x_offset + 175, y_offset + 150],color="black")
    MUX(canvas, center=[x_offset + 175, y_offset + 150], radius=5, text="",fill_color="black")
    Line(canvas, [x_offset + 180, y_offset + 150], [x_offset + 200, y_offset + 150],color="black")
    Line(canvas, [x_offset + 175, y_offset + 150], [x_offset + 175, y_offset + 550])
    Line(canvas, [x_offset + 175, y_offset + 550], [x_offset + 650, y_offset + 550])
    Line(canvas, [x_offset + 650, y_offset + 550], [x_offset + 650, y_offset + 350])
    Line(canvas, [x_offset + 650, y_offset + 350], [x_offset + 680, y_offset + 350])
    Line(canvas, [x_offset + 175, y_offset + 150], [x_offset + 175, y_offset + 30])
    Line(canvas, [x_offset + 175, y_offset + 30], [x_offset + 990, y_offset + 30])
    Line(canvas, [x_offset + 990, y_offset + 30], [x_offset + 990, y_offset + 130])
    Line(canvas, [x_offset + 990, y_offset + 130], [x_offset + 1030, y_offset + 130])
    Rectangle(canvas, [x_offset + 1040, y_offset + 140], [x_offset + 1040, y_offset + 235], text="ALU SOURCE 'A'",bg_color="white", outline_color="white")
    Line(canvas, [x_offset + 190, y_offset + 170], [x_offset + 190, y_offset+ 650])
    Line(canvas, [x_offset + 190, y_offset + 170], [x_offset + 220, y_offset+ 170])
    Line(canvas, [x_offset + 190, y_offset+ 650], [x_offset + 1500, y_offset+ 650])
    Line(canvas, [x_offset + 1500, y_offset+ 430], [x_offset + 1500, y_offset+650] ,color="black")
    Line(canvas, [x_offset + 1500, y_offset+ 430], [x_offset + 1500, y_offset+ 230],color="black")
    # IorD Multiplexer
    IorD = MUX(canvas, center=[x_offset + 225, y_offset + 160], radius=27, text= "0 \n1" ,fill_color="#d9e7fb",outline_color="#6b8ebe")
    Rectangle(canvas, [x_offset + 220, y_offset + 120], [x_offset + 240, y_offset + 130], text="I or D",bg_color="white", outline_color="white")
    Line(canvas, [x_offset + 250, y_offset + 150], [x_offset + 300, y_offset + 150])
    # Memory
    memory = Rectangle(canvas, [x_offset + 300, y_offset + 100], [x_offset + 400, y_offset + 500], text="Address\n\n\n\n\n\n\n\n\n\n Memory \n\n\n\n\n\n\n\n\nwrite data")
    Line(canvas, [x_offset + 427, y_offset + 150], [x_offset + 480, y_offset + 150],color="black")
    Line(canvas, [x_offset + 400, y_offset + 150], [x_offset + 425, y_offset + 150],color="black")
    Line(canvas, [x_offset + 425, y_offset + 150], [x_offset + 425, y_offset + 280])
    Line(canvas, [x_offset + 425, y_offset + 280], [x_offset + 450, y_offset + 280])
    MUX(canvas, center=[x_offset + 425, y_offset + 150], radius=4, text="",fill_color="black")


    # Instruction Register
    instruction_register = Rectangle(canvas, [x_offset + 450, y_offset + 100], [x_offset + 550, y_offset + 200], text="Instruction\nRegister",bg_color="#ffe6cc", outline_color="#e9cc83")
    MUX(canvas, center=[x_offset + 580, y_offset + 150], radius=4, text="",fill_color="black")


    # Memory Data Register
    memory_data_register = Rectangle(canvas, [x_offset + 450, y_offset + 250], [x_offset + 550, y_offset + 350], text="Memory\nData Register",bg_color="#ffe6cc", outline_color="#e9cc83")
    Line(canvas, [x_offset + 550, y_offset + 317], [x_offset + 680, y_offset + 317])
    Line(canvas, [x_offset + 630, y_offset + 335], [x_offset + 680, y_offset + 335])
    Line(canvas, [x_offset + 630, y_offset + 335], [x_offset + 630, y_offset + 430])
    Line(canvas, [x_offset + 630, y_offset + 430], [x_offset + 1500, y_offset + 430])
    MUX(canvas, center=[x_offset + 1500, y_offset + 430], radius=4, text="",fill_color="black")


    # Sign Extend
    Line(canvas, [x_offset + 580, y_offset + 150], [x_offset + 580, y_offset + 500])
    sign_extend = Rectangle(canvas, [x_offset + 540, y_offset + 450], [x_offset + 620, y_offset + 500], text="Sign Extend " ,bg_color="#DED2E4" , outline_color="#9573A6")
    Line(canvas, [x_offset + 620, y_offset + 475], [x_offset + 750, y_offset + 475],color="black")
    Line(canvas, [x_offset + 750, y_offset + 475], [x_offset + 780, y_offset + 475],color="black")
    sign_extend = Rectangle(canvas, [x_offset + 780, y_offset + 450], [x_offset + 820, y_offset + 490], text="2SL",bg_color="#d5e7d4",outline_color="#81b366")
    Line(canvas, [x_offset + 820, y_offset + 475], [x_offset + 1010, y_offset + 475])
    Line(canvas, [x_offset + 1010, y_offset + 475], [x_offset + 1010, y_offset + 340])
    Line(canvas, [x_offset + 1010, y_offset + 340], [x_offset + 1043, y_offset + 340])
    MUX(canvas, center=[x_offset + 750, y_offset + 475], radius=4, text="",fill_color="black")
    Line(canvas, [x_offset + 750, y_offset + 475], [x_offset + 750, y_offset + 370])
    Line(canvas, [x_offset + 750, y_offset + 370], [x_offset + 920, y_offset + 370])
    Line(canvas, [x_offset + 920, y_offset + 370], [x_offset + 920, y_offset + 320])
    Line(canvas, [x_offset + 920, y_offset + 320], [x_offset + 1021, y_offset + 320])


    # Register File
    Line(canvas, [x_offset + 550, y_offset + 150], [x_offset + 580, y_offset + 150],color="black")
    Line(canvas, [x_offset + 580, y_offset + 150], [x_offset + 650, y_offset + 150],color="black")
    Line(canvas, [x_offset + 650, y_offset + 150], [x_offset + 750, y_offset + 150],color="red")
    MUX(canvas, center=[x_offset + 650, y_offset + 150], radius=8, text="",fill_color="black")
    Line(canvas, [x_offset + 655, y_offset + 150], [x_offset + 655, y_offset + 170],color="#FFA500")
    Line(canvas, [x_offset + 655, y_offset + 170], [x_offset + 660, y_offset + 170],color="#FFA500")
    MUX(canvas, center=[x_offset + 660, y_offset + 170], radius=3, text="",fill_color="#FFA500",outline_color="#FFA500")
    Line(canvas, [x_offset + 660, y_offset + 170], [x_offset + 710, y_offset + 170],color="#FFA500")
    MUX(canvas, center=[x_offset + 710, y_offset + 180], radius=25, text="0\n1",fill_color="#d9e7fb",outline_color="#6b8ebe")
    Line(canvas, [x_offset + 735, y_offset + 180], [x_offset + 750, y_offset + 180])
    Line(canvas, [x_offset + 660, y_offset + 170], [x_offset + 660, y_offset + 240],color="#FFA500")
    Line(canvas, [x_offset + 660, y_offset + 240], [x_offset + 680, y_offset + 240],color="#FFA500")
    Line(canvas, [x_offset + 650, y_offset + 150], [x_offset + 650, y_offset + 250],color="blue")
    Line(canvas, [x_offset + 650, y_offset + 250], [x_offset + 700, y_offset + 250],color="blue")
    Line(canvas, [x_offset + 650, y_offset + 200], [x_offset + 695, y_offset + 200],color="blue")
    MUX(canvas, center=[x_offset + 700, y_offset + 250], radius=25, text="0\n1\n2",fill_color="#d9e7fb",outline_color="#6b8ebe")
    Line(canvas, [x_offset + 725, y_offset + 250], [x_offset + 750, y_offset + 250])
    MUX(canvas, center=[x_offset + 670, y_offset + 150], radius=5, text="",fill_color="red",outline_color="red")
    Line(canvas, [x_offset + 670, y_offset + 150], [x_offset + 670, y_offset + 270],color="red")
    Line(canvas, [x_offset + 670, y_offset + 270], [x_offset + 687, y_offset + 270],color="red")

    register_file = Rectangle(canvas, [x_offset + 750, y_offset + 100], [x_offset + 850, y_offset + 350], text="ReadReg1\n\nReadReg2\n\n\n\nwriteReg\n\n\n\nRegister\n File")
    Line(canvas, [x_offset + 850, y_offset + 150], [x_offset + 900, y_offset + 150],color="black")
    Rectangle(canvas, [x_offset + 855, y_offset + 110], [x_offset + 910, y_offset + 140], text="rs value",bg_color="white", outline_color="white")

    A = Rectangle(canvas, [x_offset + 900, y_offset + 140], [x_offset + 950, y_offset + 160], text="A",bg_color="#ffe6cc", outline_color="#e9cc83")
    Line(canvas, [x_offset + 850, y_offset + 300], [x_offset + 900, y_offset + 300],color="black")
    Rectangle(canvas, [x_offset + 865, y_offset + 260], [x_offset + 895, y_offset + 290], text="rt value",bg_color="white", outline_color="white")

    B = Rectangle(canvas, [x_offset + 900, y_offset + 290], [x_offset + 950, y_offset + 310], text="B",bg_color="#ffe6cc", outline_color="#e9cc83")
    Line(canvas, [x_offset + 950, y_offset + 150], [x_offset + 970, y_offset + 150])
    MUX(canvas, center=[x_offset + 970, y_offset + 150], radius=3, text="",fill_color="black",outline_color="black")
    Line(canvas, [x_offset + 950, y_offset + 300], [x_offset + 970, y_offset + 300])
    MUX(canvas, center=[x_offset + 970, y_offset + 300], radius=3, text="",fill_color="black",outline_color="black")
    Line(canvas, [x_offset + 973, y_offset + 300], [x_offset + 990, y_offset + 300])
    MUX(canvas, center=[x_offset + 990, y_offset + 300], radius=3, text="",fill_color="black",outline_color="black")
    Line(canvas, [x_offset + 993, y_offset + 300], [x_offset + 1050, y_offset + 300])

    MUX(canvas, center=[x_offset + 1050, y_offset + 310], radius=30, text="0 \n1 \n2 \n3",fill_color="#d9e7fb",outline_color="#6b8ebe")
    Rectangle(canvas, [x_offset + 1040, y_offset + 280], [x_offset + 1040, y_offset + 250], text="ALU SOURCE 'B'",bg_color="white", outline_color="white")

    MUX(canvas, center=[x_offset + 990, y_offset + 285], radius=8, text="4")
    Line(canvas, [x_offset + 1000, y_offset + 285], [x_offset + 1038, y_offset + 285])
    Line(canvas, [x_offset + 973, y_offset + 150], [x_offset + 1006, y_offset + 150])
    MUX(canvas, center=[x_offset + 1008, y_offset + 150], radius=5, text="",fill_color="black",outline_color="black")
    Line(canvas, [x_offset + 1010, y_offset + 150], [x_offset + 1050, y_offset + 150])
    MUX(canvas, center=[x_offset + 1050, y_offset + 140], radius=30, text="0 \n1",fill_color="#d9e7fb",outline_color="#6b8ebe")
    Line(canvas, [x_offset + 1080, y_offset + 140], [x_offset + 1100, y_offset + 140])
    Line(canvas, [x_offset + 1080, y_offset + 310], [x_offset + 1100, y_offset + 310])

    Rectangle(canvas, [x_offset + 780, y_offset+ 80], [x_offset + 820, y_offset+ 70], text="RG WR",bg_color="white", outline_color="white")
    Line(canvas, [x_offset + 800, y_offset + 100], [x_offset + 800, y_offset + 84],color="black")
    sign_extend
    
    alu_points = [
        [x_offset + 1100, y_offset + 100],  # top point
        [x_offset + 1200, y_offset + 230],  # middle point
        [x_offset + 1100, y_offset + 320],  # bottom point
    ]
    alu = ALU(canvas, alu_points, text="ALU")
    Line(canvas, [x_offset + 1170, y_offset + 260], [x_offset + 1170, y_offset + 320])
    Line(canvas, [x_offset + 1170, y_offset +190], [x_offset + 1170, y_offset + 120])
    Rectangle(canvas, [x_offset + 1165, y_offset + 120], [x_offset + 1165, y_offset + 80], text="Z",bg_color="white", outline_color="white")
    Rectangle(canvas, [x_offset + 1165, y_offset + 320], [x_offset + 1165, y_offset + 340], text="ALU OP",bg_color="white", outline_color="white")
    Line(canvas, [x_offset + 1200, y_offset + 230], [x_offset + 1270, y_offset + 230],color="black")
    Line(canvas, [x_offset + 1270, y_offset + 230], [x_offset + 1340, y_offset + 230],color="black")




    Rectangle(canvas, [x_offset +1340, y_offset + 220], [x_offset + 1450, y_offset + 250], text="ALU Temp",bg_color="#ffe6cc", outline_color="#e9cc83")
    Line(canvas, [x_offset + 1450, y_offset + 230], [x_offset + 1500, y_offset + 230])
    MUX(canvas, center=[x_offset + 1500, y_offset + 230], radius=4, text="",fill_color="black",outline_color="black")
    Line(canvas, [x_offset + 300, y_offset + 450], [x_offset +220, y_offset + 450])
    Line(canvas, [x_offset +220, y_offset + 450], [x_offset +220, y_offset + 600])
    Line(canvas, [x_offset +220, y_offset + 600], [x_offset + 990, y_offset + 600])
    Line(canvas, [x_offset + 990, y_offset + 600], [x_offset + 990, y_offset + 300])
    MUX(canvas, center=[x_offset + 700, y_offset + 350], radius=40, text=" 0 \n 1 \n 2 \n 3\n 4",fill_color="#d9e7fb",outline_color="#6b8ebe")
    Line(canvas, [x_offset + 738, y_offset + 350], [x_offset + 750, y_offset + 350])

    #or
    Line(canvas, [x_offset + 100, y_offset + 250], [x_offset + 100, y_offset + 200])
    Rectangle(canvas, [x_offset +55, y_offset + 250], [x_offset + 145, y_offset + 270], text="OR Gate",bg_color="white", outline_color="black")
    Line(canvas, [x_offset + 120, y_offset + 270], [x_offset + 120, y_offset + 350])
    Line(canvas, [x_offset + 80, y_offset + 270], [x_offset + 80, y_offset + 300])

    #and
    Rectangle(canvas, [x_offset +80, y_offset + 350], [x_offset + 160, y_offset + 380], text="AND Gate",bg_color="white", outline_color="black")
    Line(canvas, [x_offset + 140, y_offset + 380], [x_offset + 140, y_offset + 450])
    Rectangle(canvas, [x_offset + 130, y_offset + 430], [x_offset + 150, y_offset +470], text="PC COUNT ",bg_color="white", outline_color="white")
    Line(canvas, [x_offset + 90, y_offset + 380], [x_offset + 90, y_offset + 450])
    Rectangle(canvas, [x_offset + 80, y_offset + 410], [x_offset + 90, y_offset +480], text="Z",bg_color="white", outline_color="white")
    Rectangle(canvas, [x_offset + 60, y_offset + 330], [x_offset + 100, y_offset +300], text="PC COUNT ",bg_color="white", outline_color="white")



    Line(canvas, [x_offset + 1500, y_offset + 230], [x_offset + 1500, y_offset + 160])
    Line(canvas, [x_offset + 1500, y_offset + 160], [x_offset + 1410, y_offset + 160])
    Line(canvas, [x_offset + 1410, y_offset + 160], [x_offset + 1410, y_offset + 81])
    Line(canvas, [x_offset + 1410, y_offset + 81], [x_offset + 1440, y_offset + 81])
    MUX(canvas, center=[x_offset + 1460, y_offset + 90], radius=35, text="0 \n1 \n2 \n3" ,fill_color="#d9e7fb",outline_color="#6b8ebe")
    Line(canvas, [x_offset + 1270, y_offset + 230], [x_offset + 1270, y_offset + 68])
    Line(canvas, [x_offset + 1270, y_offset + 68], [x_offset + 1433, y_offset + 68])
    MUX(canvas, center=[x_offset + 1270, y_offset + 230], radius=4, text="",fill_color="black",outline_color="black")
    Line(canvas, [x_offset + 1495, y_offset + 81], [x_offset + 1520, y_offset + 81])

    Line(canvas, [x_offset + 1520, y_offset + 81], [x_offset + 1520, y_offset + -8])
    Line(canvas, [x_offset + 1520, y_offset +-8], [x_offset + 30, y_offset + -8])
    Line(canvas, [x_offset + 30, y_offset +-8], [x_offset + 30, y_offset + 150])
    Line(canvas, [x_offset + 30, y_offset +150], [x_offset + 50, y_offset + 150])

    Rectangle(canvas, [x_offset + 1460, y_offset + 50], [x_offset + 1480, y_offset + 40], text="PC-SRC",bg_color="white", outline_color="white")
    Line(canvas, [ x_offset + 1430, y_offset +98], [x_offset +1180, y_offset + 98])
    Line(canvas, [ x_offset + 1430, y_offset +98], [x_offset +1180, y_offset + 98])
    Line(canvas, [ x_offset + 1180, y_offset +98], [x_offset +1180, y_offset + -70])
    Line(canvas, [ x_offset + 1180, y_offset -70], [x_offset +1110, y_offset + -70])

    Rectangle(canvas, [x_offset + 1110, y_offset +-90], [x_offset + 1010, y_offset + -50], text="2SL",bg_color="#d5e7d4",outline_color="#81b366")
    Line(canvas, [ x_offset + 1010, y_offset -70], [x_offset +580, y_offset + -70])
    Line(canvas, [ x_offset + 580, y_offset -70], [x_offset +580, y_offset + 150])
    MUX(canvas, center=[x_offset + 580 ,y_offset + 150], radius=6, text="",fill_color="black",outline_color="black")

    Line(canvas,[ x_offset + 1440, y_offset +120],[x_offset+1210 ,y_offset + 120])


    Line(canvas,[ x_offset +1210, y_offset +120],[x_offset+1210 ,y_offset + 60])


    Line(canvas,[ x_offset +1210, y_offset +60],[x_offset+1010 ,y_offset + 60])


    Line(canvas,[ x_offset+1010 ,y_offset + 60],[x_offset + 1010, y_offset + 150])

    Line(canvas,[x_offset + 970, y_offset + 150],[x_offset+970 ,y_offset + 60])

    Line(canvas,[x_offset + 970, y_offset + 60],[x_offset+610 ,y_offset + 60])
    Line(canvas,[x_offset + 610, y_offset + 60],[x_offset+610 ,y_offset + 387])
    Line(canvas,[x_offset + 610, y_offset + 387],[x_offset+680 ,y_offset + 387])
    Line(canvas, [x_offset +500, y_offset + 100], [x_offset + 500, y_offset + 70])
    Rectangle(canvas, [x_offset + 480, y_offset+ 50], [x_offset + 520, y_offset+ 60], text="IR Write",bg_color="white", outline_color="white")
    Rectangle(canvas, [x_offset + 705, y_offset+ 212], [x_offset + 715, y_offset+ 213], text="Read Src",bg_color="white", outline_color="white")
    Rectangle(canvas, [x_offset + 690, y_offset+ 280], [x_offset + 700, y_offset+ 290], text="Write Dst",bg_color="white", outline_color="white")

    Rectangle(canvas, [x_offset +685, y_offset + 400], [x_offset + 710 ,y_offset + 410], text=" Memory to Reg",bg_color="white", outline_color="white")


    Rectangle(canvas, [ x_offset+680,y_offset + 140], [x_offset + 730, y_offset + 130], text="Rs",bg_color="red")
    Rectangle(canvas, [ x_offset+620,y_offset + 180], [x_offset + 640, y_offset + 160], text="Rt",bg_color="#FFA500")
    Rectangle(canvas, [ x_offset+620,y_offset + 200], [x_offset + 640, y_offset + 220], text="Rd",bg_color="blue")
    for i, func in enumerate(actives):
        btn = tk.Button(canvas, text=f"cycle {i+1}", command=lambda f=func: f(), bg="#d5e7d4")        
        btn.place(x=window.winfo_screenwidth() - 150, y=10 + i * 50)
    def on_close():
        Line.Lines_lst.clear()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
