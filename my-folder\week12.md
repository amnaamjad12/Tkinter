import tkinter as tk

root = tk.Tk()
root.title("Simple Counter")
root.geometry("250x200")

count = tk.IntVar(value=0)

def increase():
    count.set(count.get() + 1)

def decrease():
        count.set(count.get() - 1)

def reset():
    count.set(0)

tk.Label(root, text="Counter", font=("Arial", 14)).pack(pady=10)
tk.Label(root, textvariable=count, font=("Arial", 24)).pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="+", width=8, command=increase).pack(side="left", padx=5)
tk.Button(button_frame, text="-", width=8, command=decrease).pack(side="left", padx=5)

tk.Button(root, text="Reset", width=20, command=reset).pack(pady=10)

root.mainloop()
