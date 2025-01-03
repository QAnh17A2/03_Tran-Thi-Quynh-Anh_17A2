import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

#1
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chương trình xem ảnh")

# Đọc và hiển thị hình ảnh
image_path = "Otto.png"  # Đường dẫn tới file hình ảnh
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo)
label.pack()

# Hiển thị cửa sổ
root.mainloop()

#2
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chương trình xem ảnh từ URL")

# Tải và hiển thị ảnh từ URL
url = "https://example.com/image.png"  # URL của ảnh
response = requests.get(url)
img = Image.open(BytesIO(response.content))
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo)
label.pack()

# Hiển thị cửa sổ
root.mainloop()