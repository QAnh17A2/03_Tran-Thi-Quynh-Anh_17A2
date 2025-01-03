import threading
import requests

def fetch_url(lien_ket):
    try:
        response = requests.get(lien_ket)
        if response.status_code == 200:
            print(f"đường dẫn: {lien_ket} truy cập thành công")
        elif response.status_code == 404:
            print(f"đường dẫn: {lien_ket} không tìm thấy")
        elif response.status_code == 500:
            print(f"đường dẫn: {lien_ket} lỗi máy chủ nội bộ")
        else:
            print(f"đường dẫn: {lien_ket} trạng thái không xác định: {response.status_code}")
    except Exception as e:
        print(f"có lỗi {lien_ket}: {e}")

lien_ket = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]

luong = []
for lien_ket in lien_ket:
    thread = threading.Thread(target=fetch_url, args=(lien_ket,))
    luong.append(thread)
    thread.start()

for thread in luong:
    thread.join()
