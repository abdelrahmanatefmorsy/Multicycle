import tkinter as tk
from classes import *
from code_check import *
import globalVar
import re
# Reg_index ={
# }
# for i in range(len(Registers)):
#     Reg_index[Registers[i]]= i
root = tk.Tk()
globalVar.TKROOT = root
root.title("TEAM")
root.geometry("1500x800")
root.config(bg="#f0f0f0")

# جدول الرجسترات
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(pady=10, padx=10, fill="both", expand=True)
table_frame = tk.Frame(main_frame, bg="#f0f0f0", bd=2, relief="solid")
table_frame.pack(side="left", padx=10, pady=10, fill="y")
tk.Label(table_frame, text="Register", bg="#f0f0f0", fg="black", font=("Arial", 10, "bold"), width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
tk.Label(table_frame, text="Value", bg="#f0f0f0", fg="black", font=("Arial", 10, "bold"), width=10, anchor="w").grid(row=0, column=1, padx=5, pady=5)
register_vars = {}  # لتخزين قيم كل رجستر
for i, reg in enumerate(Registers):
    tk.Label(table_frame, text=reg, bg="#f0f0f0", fg="black", font=("Arial", 10), anchor="w").grid(row=i + 1, column=0, padx=5, pady=2)
    register_vars[reg] =  tk.StringVar(value="null")
     #قيمة الرجستر 
    print(register_vars[reg])
    tk.Entry(table_frame, textvariable=register_vars[reg], width=10).grid(row=i + 1, column=1, padx=5, pady=2)

dynamic_frame = tk.Frame(main_frame, bg="#f0f0f0")
dynamic_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

variables = []  # لتخزين قيمه cycle
def add_entry_and_button():
    var = tk.StringVar()
    variables.append(var)  # حفظ المتغير في القائمة
    
    sub_frame = tk.Frame(dynamic_frame, bg="#f0f0f0")
    sub_frame.pack(fill="x", pady=2)
    entry = tk.Entry(sub_frame, textvariable=var, justify="right", width=20)
    entry.pack(side="right", padx=3, pady=3)
    
    button = tk.Button(sub_frame, text="Cycle", command=lambda:check_code(var.get()), bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
    button.pack(side="right", padx=3)
register_vars["$v1"] = tk.StringVar(value="2")
def print_rg():
    print(len(variables))
    for i in register_vars:
        print(i,register_vars[i].get())
add_button = tk.Button(root, text="Add", command=add_entry_and_button, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
simmulate = tk.Button(root, text="simmulate", command=print_rg, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
add_button.pack(pady=5, anchor="e")
simmulate.pack(pady=10, anchor="e")

def change_reg(reg,x):
    register_vars[reg].set(str(x))

root.mainloop()
