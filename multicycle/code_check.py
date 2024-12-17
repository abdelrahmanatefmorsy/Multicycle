from classes import *
from enables import *
import re
from tkinter import messagebox
import globalVar
canvas = None
window = None
instructions = ["add","sub","or","and","sll","srl","addi","subi","ori","andi","j","jal","jal","jr","swap","beq","bneq","bge","xor","xori","blt","bgt","ble","bge"]
def R_typeOr(instruction):
    print("hello")
    if len(instruction) != 4:
        print("Error: Incorrect instruction format!")  # Add error message
        return
    
    for i in range(1, len(instruction)):
        if instruction[i] not in Registers:
            print("Error: Invalid register!")
            return
    
    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(r_type1)
    actives.append(r_type2)
    print("Instruction:", instruction)
    if(len(Line.Lines_lst)):
        messagebox.showerror("Error", "There is an already cycle you do close it and try again")
        print("invalid")
        return
    window = tk.Toplevel(globalVar.TKROOT)
    window.title("Multi-Cycle Microprocessor Diagram")
    window.geometry("1600x900")  # Window size
    window.configure(bg="white") 
    canvas = tk.Canvas(window, bg="white")
    Multi_cycle(canvas, window,actives)


def I_typeOr(instruction):
    print("hello")
    if len(instruction) != 4:
        print("Error: Incorrect instruction format!")  # Add error message
        return
    
    for i in range(1, len(instruction) - 1):
        if instruction[i] not in Registers:
            print("Error: Invalid register!")
            return
    if(instruction[-1].isdecimal()==False):
            print("Error: Invalid register!")
            return
    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(i_type1)
    actives.append(i_type2)
    print("Instruction:", instruction)
    if(len(Line.Lines_lst)):
        messagebox.showerror("Error", "There is an already cycle you do close it and try again")
        print("invalid")
        return
    window = tk.Toplevel(globalVar.TKROOT)
    window.title("Multi-Cycle Microprocessor Diagram")
    window.geometry("1600x900")  # Window size
    window.configure(bg="white") 
    canvas = tk.Canvas(window, bg="white")
    Multi_cycle(canvas, window,actives)
def conditionsOr(instructions):
    pass
def jumbOr(instruction):
    if len(instruction) != 2:
        print("Error: Incorrect instruction format!")  # Add error message
        return

    if(instruction[-1].isdecimal()==False):
                print("Error: Invalid register!")
                return
    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(jumb)
    print("Instruction:", instruction)
    if(len(Line.Lines_lst)):
        messagebox.showerror("Error", "There is an already cycle you do close it and try again")
        print("invalid")
        return
    window = tk.Toplevel(globalVar.TKROOT)
    window.title("Multi-Cycle Microprocessor Diagram")
    window.geometry("1600x900")  # Window size
    window.configure(bg="white") 
    canvas = tk.Canvas(window, bg="white")
    Multi_cycle(canvas, window,actives)
def jumbalOr(instruction):
    if len(instruction) != 2:
        print("Error: Incorrect instruction format!")  # Add error message
        return

    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(jumbal)
    print("Instruction:", instruction)
    if(len(Line.Lines_lst)):
        messagebox.showerror("Error", "There is an already cycle you do close it and try again")
        print("invalid")
        return
    window = tk.Toplevel(globalVar.TKROOT)
    window.title("Multi-Cycle Microprocessor Diagram")
    window.geometry("1600x900")  # Window size
    window.configure(bg="white") 
    canvas = tk.Canvas(window, bg="white")
    Multi_cycle(canvas, window,actives)
def jumbregOr(instruction):
    if len(instruction) != 2:
        print("Error: Incorrect instruction format!")  # Add error message
        return

    if(instruction[-1]not in Registers):
                print("Error: Invalid register!")
                return
    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(jumbreg)
    print("Instruction:", instruction)
    if(len(Line.Lines_lst)):
        messagebox.showerror("Error", "There is an already cycle you do close it and try again")
        print("invalid")
        return
    window = tk.Toplevel(globalVar.TKROOT)
    window.title("Multi-Cycle Microprocessor Diagram")
    window.geometry("1600x900")  # Window size
    window.configure(bg="white") 
    canvas = tk.Canvas(window, bg="white")
    Multi_cycle(canvas, window,actives)
s = "add $s0 , $s1 , $s2"
code_methods = {
    ("add","sub","or","and","xor"): lambda *args: R_typeOr(*args),
    ("sll","srl","addi","subi","ori","andi","xori") :lambda *args:I_typeOr(*args),
    ("beq","bneq","bge","blt","bgt"): lambda *args:conditionsOr(*args),
    "j":lambda *args:jumbOr(*args),
    "jal":lambda *args:jumbalOr(*args),
    "jr":lambda *args:jumbregOr(*args)
}

def check_code(instruction):
    instruction = re.split(r'[ ,]+', instruction)

    # Iterate through code_methods and invoke the appropriate function
    for x in code_methods:
        if instruction[0] in x:
            # Pass the instruction and canvas explicitly
            code_methods[x](instruction)
            break
    else:
        print("Error: Instruction not recognized!")
