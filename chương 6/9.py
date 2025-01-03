import threading
import time
from datetime import datetime

def task(name):
    print(f"Starting {name}")
    for _ in range(5):  # Mỗi luồng thực hiện 5 lần
        now = datetime.now().strftime("%H:%M:%S %Y")
        print(f"{name}: Web {now}")
        time.sleep(1)  # Tạm dừng 1 giây
    print(f"Exiting {name}")

# In thông báo bắt đầu luồng chính
print("Starting Main Thread")

# Tạo các luồng
threads = []
for name in ["Google", "Yahoo", "Facebook"]:
    thread = threading.Thread(target=task, args=(name,))
    threads.append(thread)
    thread.start()

# Chờ các luồng hoàn tất
for thread in threads:
    thread.join()

# In thông báo kết thúc luồng chính
print("Exiting Main Thread")
