import tkinter as tk

def submit_info():
    name = entry_name.get()
    student_id = entry_id.get()
    password = entry_password.get()
    print(f"Tên: {name}, ID: {student_id}, Mật khẩu: {password}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form thông tin sinh viên")

# Thêm các nhãn và hộp nhập liệu
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Student ID:").grid(row=1, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Thêm nút Submit
submit_button = tk.Button(root, text="Submit", command=submit_info)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Hiển thị cửa sổ
root.mainloop()
