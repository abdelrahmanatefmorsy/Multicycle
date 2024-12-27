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
def execute_code(text_widget):
    code = text_widget.get("1.0", tk.END).strip('\n')
    run_code(code)
def reset():
    for i in globalVar.register_vars:
        globalVar.register_vars[i].set("0")
def add_entry_and_button():
    var = tk.StringVar()
    sub_frame = tk.Frame(dynamic_frame, bg="#f0f0f0")
    sub_frame.pack(fill="x", pady=2)
    
    entry = tk.Entry(sub_frame, textvariable=var, justify="right", width=20, font=("Arial", 12))
    entry.pack(side="right", padx=3, pady=3)
    
    cycle_button = tk.Button(sub_frame, text="Cycle", command=lambda: check_code(var.get()), bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
    cycle_button.pack(side="right", padx=3)
    
    delete_button = tk.Button(sub_frame, text="Delete", command=sub_frame.destroy, bg="#FF0000", fg="white", relief="solid", padx=10, pady=5)
    delete_button.pack(side="right", padx=3)
# table of registers
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

table_frame = tk.Frame(main_frame, bg="#f0f0f0", bd=2, relief="solid")
table_frame.pack(side="left", padx=10, pady=10, fill="y")
tk.Label(table_frame, text="Register", bg="#f0f0f0", fg="black", font=("Arial", 10, "bold"), width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
tk.Label(table_frame, text="Value", bg="#f0f0f0", fg="black", font=("Arial", 10, "bold"), width=10, anchor="w").grid(row=0, column=1, padx=5, pady=5)

# make the text field for each register
for i, reg in enumerate(Registers):
    tk.Label(table_frame, text=reg, bg="#f0f0f0", fg="black", font=("Arial", 10), anchor="w").grid(row=i + 1, column=0, padx=5, pady=2)
    globalVar.register_vars[reg] = tk.StringVar(value="0")
    tk.Entry(table_frame, textvariable=globalVar.register_vars[reg], width=10,font=12).grid(row=i + 1, column=1, padx=5, pady=2)

dynamic_frame = tk.Frame(main_frame, bg="#f0f0f0")
dynamic_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)
top_fr = tk.Frame(dynamic_frame, bg="#f0f0f0")
top_fr.pack(fill="x", pady=2)
add_button = tk.Button(top_fr, text="Add", command=add_entry_and_button, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
add_button.pack(pady=5, anchor="e")


# make the compiler frame
code_frame = tk.Frame(root, bg="#dcdcdc", bd=2, relief="solid")
code_frame.place(relx=0.5, rely=0.5, anchor="center")

code_label = tk.Label(code_frame, text="Enter Assembly Code:", bg="#dcdcdc", font=("Arial", 10, "bold"))
code_label.pack(pady=5)

text_with_line_numbers = TextWithLineNumbers(code_frame)
text_with_line_numbers.pack(pady=5)

run_button = tk.Button(code_frame, text="Run Code", command=lambda: execute_code(text_with_line_numbers.text), bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
run_button.pack(pady=5)

run_button2 = tk.Button(code_frame, text="Reset", command=reset, bg="#4CAF50", fg="white", relief="solid", padx=15, pady=5)
run_button2.pack(padx=15)


root.mainloop()
