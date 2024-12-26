import inspect
Line = 0
Labels = {}
tmp = {}
import globalVar
from tkinter import messagebox
    
def add(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in globalVar.register_vars:
        print("Invalid register")
        return 0
    print(x,y,z)
    tmp[x]  = str(int(tmp[y]) + int(tmp[z]))
    return 1
def sub(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in globalVar.register_vars:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) - int(tmp[z]))
    return 1
def orr(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in globalVar.register_vars:  
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) | int(tmp[z]))
    return 1
def andd(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in globalVar.register_vars:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) & int(tmp[z]))
def sll(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) << int(z))
    return 1
def srl(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) >> int(z))
def addi(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) + int(z))
    return 1
def subi(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) - int(z))
    return 1
def ori(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) | int(z))
    return 1
def andi(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) & int(z))
    return 1
def j(x):
    print("valid")
    global Labels
    global Line
    if x not in Labels:
        print("Invalid label")
        return 0
    Line = Labels[x]
    return 1
def beq(x,y,z):
    global Line
    global Labels

    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in Labels:
        print(x,y,z)
        print("Invalid register")
        return 0
    if tmp[x] == tmp[y]:
        Line = Labels[z]
    return 1
def bneq(x,y,z):
    global Line
    global Labels

    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in Labels:
        print("Invalid register")
        return 0
    if tmp[x] != tmp[y]:
        Line = Labels[z]
    return
def bge(x,y,z):
    global Line
    global Labels

    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in Labels:
        print("Invalid register")
        return 0
    if int(tmp[x]) >= int(tmp[y]):
        Line = Labels[z]
    return 1
def ble(x,y,z):
    global Line
    global Labels

    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in Labels:
        print("Invalid register")
        return 0
    if int(tmp[x]) <= int(tmp[y]):
        Line = Labels[z]
    return 1
def bgt(x,y,z):
    global Line
    global Labels

    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in Labels:
        print("Invalid register")
        return 0
    if int(tmp[x]) > int(tmp[y]):
        Line = Labels[z]
    return 1
def blt(x,y,z):
    global Line
    global Labels

    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in Labels:
        print("Invalid register")
        return 0
    if int(tmp[x]) < int(tmp[y]):
        Line = Labels[z]
    return 1
def xorr(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z not in globalVar.register_vars:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) ^ int(tmp[z]))
    return 1
def xori(x,y,z):
    if x not in globalVar.register_vars or y not in globalVar.register_vars or z.isdecimal() == False:
        print("Invalid register")
        return 0
    tmp[x] = str(int(tmp[y]) ^ int(z))
ops = {
    "add": lambda x, y,z: add(x, y,z),
    "sub": lambda x, y,z: sub(x, y,z),
    "or": lambda x, y,z: orr(x, y,z),
    "and": lambda x, y,z: andd(x, y,z),
    "sll": lambda x, y,z: sll(x, y,z),
    "srl": lambda x, y,z: srl(x, y,z),
    "addi": lambda x, y,z: addi(x, y,z),
    "subi": lambda x, y,z: subi(x, y,z),
    "ori": lambda x, y,z: ori(x, y,z),
    "andi": lambda x, y,z: andi(x, y,z),
    "j": lambda x: j(x),
    "beq": lambda x, y,z: beq(x, y,z),
    "bneq": lambda x, y,z: bneq(x, y,z),
    "bge": lambda x, y,z: bge(x, y,z),
    "xori": lambda x, y,z: xori(x, y,z),
    "blt": lambda x, y,z: blt(x, y,z),
    "bgt": lambda x, y,z: bgt(x, y,z),
    "ble": lambda x, y,z: ble(x, y,z),
    "bge": lambda x, y,z: bge(x, y,z)
}
def check_code(code):
    code = code.split()
    if code[0][-1]==':':
        return 1
    if code[0] not in ops and code[0][-1] != ':':
        print(code[0])
        print("Invalid instruction")
        return 0
    if code[0][-1] == ':':
        if len(code) != 1:
            print("Invalid label")
            return 0
        Labels[code[0][:-1]] = Line
        return 1
    param_count = len(inspect.signature(ops[code[0]]).parameters)
    if(len(code) != param_count + 1):
        print(param_count,len(code))
        print("syntax error")
        return 0
    ops[code[0]](*code[1:])
    return 1
def run_code(code):
    global Line
    Line  = 0
    Labels.clear()
    tmp.clear()
    for i in globalVar.register_vars:
        tmp[i] = str(globalVar.register_vars[i].get())
        # print(i,tmp[i])
    code = list(code.split('\n'))
    for i in range(len(code)):
            x = code[i].split()
            if x[0][-1] == ':':
                if len(x) != 1:
                    print("Invalid label")
                    return 0
                Labels[x[0][:-1]] = i
    while Line < len(code):
        if not check_code(code[Line]):
            break
        Line += 1
    for i in globalVar.register_vars:
        globalVar.register_vars[i].set(str(tmp[i]))
    messagebox.showinfo("Successful", "Code Run completed successfully")
    # for i in globalVar.register_vars:
    #     print(globalVar.register_vars[i].get())


# Example usage
