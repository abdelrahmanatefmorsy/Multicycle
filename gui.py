import tkinter as tk
root = tk.Tk()
root.title("TEAM")
instruction = 0
root.config(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")  
frame.pack(pady=10, padx=10, fill="x")

def add_entry_and_button():
    sub_frame = tk.Frame(frame, bg="#f0f0f0") 
    sub_frame.pack(fill="x", pady=2)  
    entry = tk.Entry(sub_frame, justify="right", width=20)
    entry.pack(side="right", padx=3, pady=3) 
    button = tk.Button(sub_frame, text="Cycle", command=lambda: print(entry.get()), bg="#4CAF50", fg="white", relief="solid", padx=10, pady=5)
    button.pack(side="right", padx=3)

add_button = tk.Button(root, text="Add", command=add_entry_and_button, bg="#008CBA", fg="white", relief="solid", padx=10, pady=5)
add_button.pack(pady=5, anchor="e")  
root.mainloop()
