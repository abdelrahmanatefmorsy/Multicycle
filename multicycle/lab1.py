import tkinter as tk
from classes import *
from code_check import *
import globalVar
import re
from Run import run_code
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

# لتخزين قيم كل رجستر
for i, reg in enumerate(Registers):
    tk.Label(table_frame, text=reg, bg="#f0f0f0", fg="black", font=("Arial", 10), anchor="w").grid(row=i + 1, column=0, padx=5, pady=2)
    globalVar.register_vars[reg] = tk.StringVar(value="0")
    tk.Entry(table_frame, textvariable=globalVar.register_vars[reg], width=10).grid(row=i + 1, column=1, padx=5, pady=2)

dynamic_frame = tk.Frame(main_frame, bg="#f0f0f0")
dynamic_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

variables = []  # لتخزين قيمه cycle
def add_entry_and_button():
    var = tk.StringVar()
    variables.append(var)
    sub_frame = tk.Frame(dynamic_frame, bg="#f0f0f0")
    sub_frame.pack(fill="x", pady=2)
    entry = tk.Entry(sub_frame, textvariable=var, justify="right", width=20)
    entry.pack(side="right", padx=3, pady=3)
    button = tk.Button(sub_frame, text="Cycle", command=lambda: check_code(var.get()), bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
    button.pack(side="right", padx=3)


def print_rg():
    print(len(variables))
    for i in globalVar.register_vars:
        print(i, globalVar.register_vars[i].get())

add_button = tk.Button(root, text="Add", command=add_entry_and_button, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
simulate = tk.Button(root, text="Simulate", command=print_rg, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
add_button.pack(pady=5, anchor="e")
simulate.pack(pady=10, anchor="e")

# Adding the code execution widget in the center
code_frame = tk.Frame(root, bg="#dcdcdc", bd=2, relief="solid")
code_frame.place(relx=0.5, rely=0.5, anchor="center")  # Place it in the center

# Create a text field and button for code execution
code_label = tk.Label(code_frame, text="Enter Assembly Code:", bg="#dcdcdc", font=("Arial", 10, "bold"))
code_label.pack(pady=5)

code_field = tk.Text(code_frame, height=37, width=80,font=("Arial", 10))
code_field.pack(pady=5)

def execute_code():
    code = code_field.get("1.0", tk.END).strip('\n')
    run_code(code)
def reset():
    for i in globalVar.register_vars:
        globalVar.register_vars[i].set("0")
run_button = tk.Button(code_frame, text="Run Code", command=execute_code, bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
run_button.pack(pady=5)
run_button2 = tk.Button(code_frame, text="Reset", command=reset, bg="#4CAF50", fg="white", relief="solid", padx=15, pady=5)
run_button2.pack(padx=15)

def change_reg(reg, x):
    globalVar.register_vars[reg].set(str(x))

root.mainloop()
