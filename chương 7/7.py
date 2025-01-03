import tkinter as tk

def calculate_sum():
    n = int(entry.get())
    result = sum(range(1, n + 1))
    result_label.config(text=f"The sum is 1 + 2 + ... + {n} = {result}")

root = tk.Tk()
root.title("Tính tổng từ 1 đến N")

tk.Label(root, text="Enter value of integer N:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(root, text="Validate", command=calculate_sum).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
