import tkinter as tk

def list_divisors():
    n = int(entry.get())
    divisors = [str(i) for i in range(1, n + 1) if n % i == 0]
    result_label.config(text=f"The divisors of {n}: " + " ".join(divisors))

root = tk.Tk()
root.title("Liệt kê các ước của N")

tk.Label(root, text="Enter the value of N:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(root, text="Validate", command=list_divisors).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
