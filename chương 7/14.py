import tkinter as tk
from tkinter import messagebox

def calculate_fare():
    try:
        km = float(entry_km.get())
        time = int(entry_time.get())
        if car_type.get() == "4 chỗ":
            if km <= 30:
                fare = km * 15300
            else:
                fare = 30 * 15300 + (km - 30) * 12100
        elif car_type.get() == "7 chỗ":
            if km <= 30:
                fare = km * 16100
            else:
                fare = 30 * 16100 + (km - 30) * 13800

        if time > 5:
            fare += (time - 5) * 750

        result_label.config(text=f"Tổng cước: {fare:.0f} đồng")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")

root = tk.Tk()
root.title("Tính cước taxi")

tk.Label(root, text="Quãng đường (km):").grid(row=0, column=0, padx=10, pady=5)
entry_km = tk.Entry(root)
entry_km.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Thời gian chờ (phút):").grid(row=1, column=0, padx=10, pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Loại xe:").grid(row=2, column=0, padx=10, pady=5)
car_type = tk.StringVar(value="4 chỗ")
tk.OptionMenu(root, car_type, "4 chỗ", "7 chỗ").grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Tính cước", command=calculate_fare).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Tổng cước: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
