import tkinter as tk
from math import gcd

def calculate():
    m = int(entry_m.get())
    n = int(entry_n.get())
    if option.get() == "GCD":
        result = gcd(m, n)
    else:
        result = abs(m * n) // gcd(m, n)
    result_label.config(text=f"{option.get()}({m}, {n}) = {result}")

root = tk.Tk()
root.title("Tính GCD và LCM")

tk.Label(root, text="Enter value of m:").grid(row=0, column=0, padx=10, pady=5)
entry_m = tk.Entry(root)
entry_m.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter value of n:").grid(row=1, column=0, padx=10, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1, padx=10, pady=5)

option = tk.StringVar(value="GCD")
tk.OptionMenu(root, option, "GCD", "LCM").grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
