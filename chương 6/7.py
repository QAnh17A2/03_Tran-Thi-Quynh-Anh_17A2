import threading
import time
from datetime import datetime

def task(ten_luong, so_lan):
    print(f"Bắt đầu {ten_luong}")
    for i in range(so_lan):
        now = datetime.now().strftime("%H:%M:%S %Y")
        print(f"{ten_luong}: Web {now}")
        time.sleep(1)  # Tạm dừng 1 giây giữa mỗi lần in
    print(f"Kết thúc {ten_luong}")

# Bắt đầu luồng chính
print("Bắt đầu luồng chính")

# Tạo các luồng độc lập
luong_google = threading.Thread(target=task, args=("Google", 5))
luong_yahoo = threading.Thread(target=task, args=("Yahoo", 6))
luong_facebook = threading.Thread(target=task, args=("Facebook", 7))

# Bắt đầu các luồng
luong_google.start()
luong_yahoo.start()
luong_facebook.start()

# Chờ các luồng kết thúc
luong_google.join()
luong_yahoo.join()
luong_facebook.join()

print("Kết thúc luồng chính")
