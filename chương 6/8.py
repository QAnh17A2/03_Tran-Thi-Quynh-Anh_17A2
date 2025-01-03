import threading
import random

# Hàm tính tổng các phần tử trong một phần của list
def tinh_tong(mang_con, ket_qua, index):
    tong = sum(mang_con)
    print(f"Thread {index} tính tổng: {tong}")
    ket_qua[index] = tong

# Chương trình chính
n = int(input("Nhập số phần tử: "))
so_thread = int(input("Nhập vào số thread: "))

# Tạo list ngẫu nhiên với giá trị từ 0 đến 10
mang = [random.randint(0, 10) for _ in range(n)]
print(f"List: {mang}")

# Chia list thành các phần nhỏ
khoang_cach = n // so_thread
cac_mang_con = [mang[i * khoang_cach:(i + 1) * khoang_cach] for i in range(so_thread)]
# Nếu còn dư phần tử, thêm vào list cuối
if n % so_thread != 0:
    cac_mang_con[-1].extend(mang[so_thread * khoang_cach:])

# Lưu kết quả tính tổng của từng thread
ket_qua = [0] * so_thread
threads = []

# Tạo và bắt đầu các thread
for i, mang_con in enumerate(cac_mang_con):
    thread = threading.Thread(target=tinh_tong, args=(mang_con, ket_qua, i + 1))
    threads.append(thread)
    thread.start()

# Chờ tất cả các thread hoàn thành
for thread in threads:
    thread.join()

# Tính tổng cuối cùng
tong_cuoi = sum(ket_qua)
print(f"Tổng list = {tong_cuoi}")
