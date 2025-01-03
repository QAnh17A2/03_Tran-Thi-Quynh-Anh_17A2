import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            result = "Gầy"
        elif 18.5 <= bmi < 24.9:
            result = "Bình thường"
        elif 25 <= bmi < 29.9:
            result = "Thừa cân"
        else:
            result = "Béo phì"
        result_label.config(text=f"BMI: {bmi:.2f}")
        conclusion_label.config(text=f"Kết luận: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")

root = tk.Tk()
root.title("Tính chỉ số BMI")

tk.Label(root, text="Cân nặng (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Chiều cao (m):").grid(row=1, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Tính BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=3, column=0, columnspan=2)

conclusion_label = tk.Label(root, text="Kết luận: ")
conclusion_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
