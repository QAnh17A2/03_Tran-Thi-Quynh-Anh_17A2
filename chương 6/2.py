import threading
import time

def download_file(file_name):
    print(f"đang tải filefile {file_name}...")
    time.sleep(2)  # Giả lập thời gian tải xuống
    print(f"file {file_name} đã được tải xuống")

files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]

threads = []
for file in files:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
