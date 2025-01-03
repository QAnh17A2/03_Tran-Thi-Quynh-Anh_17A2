import threading
from math import factorial

def calculate_factorial(number):
    print(f"giai thừa của số {number} là: {factorial(number)}")

so = [5, 7, 10, 12]
luong = []

for number in so:
    thread = threading.Thread(target=calculate_factorial, args=(number,))
    luong.append(thread)
    thread.start()

for thread in luong:
    thread.join()
