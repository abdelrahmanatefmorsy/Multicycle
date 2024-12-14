import tkinter as tk

# الرجسترات
Registers = [
    "$zero",
    "$v0", "$v1",
    "$a0", "$a1", "$a2", "$a3",
    "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7",
    "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7",
    "$t8", "$t9"
]

root = tk.Tk()
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
    register_vars[reg] = tk.StringVar(value="null")  #قيمة الرجستر 
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
    
    button = tk.Button(sub_frame, text="Cycle", command=lambda: print(var.get()), bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
    button.pack(side="right", padx=3)

add_button = tk.Button(root, text="Add", command=add_entry_and_button, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
add_button.pack(pady=5, anchor="e")

root.mainloop()
