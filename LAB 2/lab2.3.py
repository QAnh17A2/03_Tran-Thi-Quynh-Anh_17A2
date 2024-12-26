#1 Đọc dữ liệu
import numpy as np
path_1="D:/17A2KHDL/Lab2/data/efficiency.txt"
efficiency=[]
with open (path_1,encoding='utf-8') as file:
    efficiency=np.loadtxt(file,dtype=float)  
print("danh sách đọc từ file efficiency.txt:")
efficiency.tolist()
path_2="D:/17A2KHDL/Lab2/data/shifts.txt"
shifts=[]
with open (path_2,'r',encoding='utf-8') as txtfile:
    shifts=np.loadtxt(txtfile,dtype=str)  
print("danh sách đọc từ file shifts.txt:")
shifts.tolist()
#2 
np_shifts=np.array(shifts)
print("mảng numpy tạo từ list shifts:")
print(np_shifts)
print("Kiểu dữ liệu của np_shifts là:",np_shifts.dtype)
np_shifts=np.array(shifts)
print("mảng numpy tạo từ list shifts:")
print(np_shifts)
print("Kiểu dữ liệu của np_shifts là:",np_shifts.dtype)
#3
np_efficiency=np.array(efficiency)
print("Mảng được tạo list efficiency :")
print(np_efficiency)
print("Kiểu dữ liệu của np_efficiency:",np_efficiency.dtype)
#4
morning_indices=np_shifts=='Morning'
morning_efficiency=np_efficiency[morning_indices]
average_1=np.mean(morning_efficiency)
print("Hiệu suất trung bình ca 'Morning':",average_1)
#5
other_indicies=np_shifts!='Morning'
other_efficiency=np_efficiency[other_indicies]
average_2=np.mean(other_efficiency)
print("Hiệu suất trung bình của ca không phải 'Morning':",average_2)
#6
workers = np.zeros(len(np_shifts), dtype={'names': ('shift', 'efficiency'),
                                          'formats': ('<U10', 'float')})
workers['shift'] = np_shifts
workers['efficiency'] = np_efficiency
print("Mảng dữ liệu workers:")
print(workers)
#7
sorted_workers = np.sort(workers, order='efficiency')
print("Mảng workers sắp xếp theo efficiency:")
print(sorted_workers)
highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']
print("\nCa làm việc có hiệu suất cao nhất:", highest_efficiency_shift)
print("Ca làm việc có hiệu suất thấp nhất:", lowest_efficiency_shift)