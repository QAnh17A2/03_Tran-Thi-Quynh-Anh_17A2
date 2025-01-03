import tkinter as tk
from tkinter import messagebox

def check_age():
    name = entry_name.get()
    age = int(entry_age.get())
    if age >= 18:
        messagebox.showinfo("Result", f"Xin chào {name}, bạn đã trưởng thành!")
    else:
        messagebox.showinfo("Result", f"Xin chào {name}, bạn còn nhỏ tuổi!")

root = tk.Tk()
root.title("Kiểm tra tuổi")

tk.Label(root, text="Tên của bạn:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tuổi của bạn:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Kiểm tra", command=check_age).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
