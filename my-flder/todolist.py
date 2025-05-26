import tkinter as tk

def add_item():
    item = item_input.get()
    level = level_var.get()
    if item:
        item_box.insert(tk.END, "Task: " + item + " | Priority: " + level)
    

window = tk.Tk()
window.title("My To-Do List")

tk.Label(window, text="Enter Task:").pack()
item_input = tk.Entry(window, width=40)
item_input.pack(pady=5)

tk.Label(window, text="Priority Level:").pack()
level_var = tk.StringVar()
level_var.set("Medium")  # Default priority

tk.OptionMenu(window, level_var, "Low", "Medium", "High").pack(pady=5)

tk.Button(window, text="Add Task", command=add_item).pack(pady=5)
     
item_box = tk.Listbox(window, width=50)
item_box.pack(pady=10)

window.mainloop()
