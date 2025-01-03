import threading

def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"chẵn: {i}")

def print_odd_numbers():
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"lẻ: {i}")

thread1 = threading.Thread(target=print_even_numbers)
thread2 = threading.Thread(target=print_odd_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
