import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thay đổi kiểu chữ Label")

# Thêm một nhãn với kiểu chữ thay đổi
label = tk.Label(root, text="Đây là nhãn với kiểu chữ mới!", font=("Arial", 16, "bold"))
label.pack()

# Hiển thị cửa sổ
root.mainloop()
