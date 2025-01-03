import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Cửa sổ Tkinter với Label")

# Thêm một nhãn
label = tk.Label(root, text="Chào mừng bạn đến với Tkinter!")
label.pack()

# Hiển thị cửa sổ
root.mainloop()
