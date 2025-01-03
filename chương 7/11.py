import tkinter as tk
from tkinter import messagebox

def convert_year():
    year = int(entry.get())
    can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    result = f"Năm Âm lịch: {can[year % 10]} {chi[year % 12]}"
    messagebox.showinfo("Kết quả", result)

root = tk.Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")

tk.Label(root, text="Nhập năm Dương lịch:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=5)

tk.Button(root, text="Chuyển đổi", command=convert_year).grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
