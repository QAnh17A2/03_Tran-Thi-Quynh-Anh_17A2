import threading
import random

def tim_max(mang_con, ket_qua, i):
    ket_qua[i] = max(mang_con)
    print(f"Thread {i + 1} tìm max: {ket_qua[i]}")

# Nhập số phần tử và số thread
n = int(input("Nhập số phần tử: "))
so_thread = int(input("Nhập vào số thread: "))

# Tạo danh sách ngẫu nhiên từ 0-100
mang = [random.randint(0, 100) for _ in range(n)]
print(f"List: {mang}")

# Khởi tạo danh sách kết quả với kích thước bằng số thread
ket_qua = [0] * so_thread

# Chia danh sách lớn thành các phần nhỏ cho từng thread
cac_mang_con = [mang[i::so_thread] for i in range(so_thread)]

# Tạo và chạy các thread
threads = []
for i in range(so_thread):
    t = threading.Thread(target=tim_max, args=(cac_mang_con[i], ket_qua, i))
    threads.append(t)
    t.start()

# Chờ các thread hoàn thành
for t in threads:
    t.join()

# Tìm giá trị lớn nhất từ các phần
max_cuoi = max(ket_qua)
print(f"Giá trị lớn nhất trong list = {max_cuoi}")
