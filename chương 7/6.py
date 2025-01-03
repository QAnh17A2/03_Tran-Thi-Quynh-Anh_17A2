import tkinter as tk

def reverse_text():
    input_text = entry.get()  # Lấy nội dung người dùng nhập
    reversed_text = input_text[::-1]  # Đảo ngược chuỗi
    result_label.config(text=reversed_text)  # Hiển thị kết quả

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chương trình đảo ngược chuỗi")

# Thêm ô nhập liệu và nút Validate
tk.Label(root, text="Enter a word:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=2, pady=10)

validate_button = tk.Button(root, text="Validate", command=reverse_text)
validate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Hiển thị cửa sổ
root.mainloop()
