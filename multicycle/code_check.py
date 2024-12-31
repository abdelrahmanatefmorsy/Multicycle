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
    print(instruction)
    if len(instruction) != 4:
        messagebox.showerror("Error", "Instruction  Not Found")
        return
    
    for i in range(1, len(instruction)):
        if instruction[i] not in Registers:
            messagebox.showerror("Error", "Instruction  Not Found")
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
        messagebox.showerror("Error", "Instruction  Not Found")
        return
    
    for i in range(1, len(instruction) - 1):
        if instruction[i] not in Registers:
            messagebox.showerror("Error", "Instruction  Not Found")

            return
    if(instruction[-1].isdecimal()==False):
            print(instruction[-1])
            messagebox.showerror("Error", "Instruction  Not Found")
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
def conditionsOr(instruction):
    print("hello")
    if len(instruction) != 4:
        messagebox.showerror("Error", "Instruction  Not Found")
  # Add error message
        return
    
    for i in range(1, len(instruction) - 1):
        if instruction[i] not in Registers:
            messagebox.showerror("Error", "Instruction  Not Found")
            return
        if(instruction[-1].isdecimal()==True):
            messagebox.showerror("Error", "Instruction  Not Found")
            return
    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(BEQ)
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
def jumbOr(instruction):
    if len(instruction) != 2:
        messagebox.showerror("Error", "Instruction  Not Found")
  # Add error message
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
        messagebox.showerror("Error", "Instruction  Not Found")
 # Add error message
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
        messagebox.showerror("Error", "Instruction  Not Found")
# Add error message
        return

    if(instruction[-1]not in Registers):
                messagebox.showerror("Error", "Instruction  Not Found")

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
def lwOr(instruction):
    print(instruction[1],len(instruction))
    if len(instruction) != 3 or instruction[1] not in Registers:
        messagebox.showerror("Error", "Instruction  Not Found")
        return
    s = instruction[2]
    num = ""
    regg = ""
    flag = 0
    for i in s:
         if(i != "("):
              num+=i
         else:
            break
         flag+=1
    print(s[flag+1:-1])
    if(num.isdecimal()==False or s[flag+1 :-1] not in Registers or s[-1] != ')'):
        messagebox.showerror("Error", "Instruction  Not Found")
        return
       

    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(i_type1)
    actives.append(Lw1)
    actives.append(Lw2)
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
def SwOr(instruction):
    print(instruction[1],len(instruction))
    if len(instruction) != 3 or instruction[1] not in Registers:
        messagebox.showerror("Error", "Instruction  Not Found")

        return

    s = instruction[2]
    num = ""
    regg = ""
    flag = 0
    for i in s:
         if(i != "("):
              num+=i
         else:
            break
         flag+=1
    print(s[flag+1:-1])
    if(num.isdecimal()==False or s[flag+1 :-1] not in Registers or s[-1] != ')'):
        messagebox.showerror("Error", "Instruction  Not Found")

        return
       

    actives = []
    actives.append(fetch)
    actives.append(decode)
    actives.append(i_type1)
    actives.append(sw)
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
    "jr":lambda *args:jumbregOr(*args),
    ("lw","lb"):lambda *args:lwOr(*args),
    ("sw","sb"):lambda *args:SwOr(*args),
}

def check_code(instruction):
    instruction = instruction.replace('\xa0', ' ')
    instruction = re.split(r'[ ,]+', instruction)
    print(instruction)
    # Iterate through code_methods and invoke the appropriate function
    for x in code_methods:
        print(instruction[0],x)
        if instruction[0] in x:
            # Pass the instruction and canvas explicitly
            code_methods[x](instruction)
            break
    else:
        messagebox.showerror("Error", "Instruction  Not Found")
