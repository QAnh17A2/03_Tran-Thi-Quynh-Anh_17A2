import threading

def chan(so_gioi_han):
    for i in range(2, so_gioi_han + 1, 2):
        print(f"chẵn: {i}")

def le(so_gioi_han):
    for i in range(1, so_gioi_han + 1, 2):
        print(f"lẻ: {i}")

so_gioi_han = 20  # Ngưỡng tối đa
thread1 = threading.Thread(target=chan, args=(so_gioi_han,))
thread2 = threading.Thread(target=le, args=(so_gioi_han,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
