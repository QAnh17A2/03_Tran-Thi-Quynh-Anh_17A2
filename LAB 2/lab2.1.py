#1. Tạo dữ liệu mô phỏng
import numpy as np
nhiet_do = np.round(np.random.uniform(10.0,30.0 ,size=30),2)
print("Trung bình nhiệt độ trong tháng là :", np.mean(nhiet_do))
#2.phân tích xu hướng nhiệt độ
max_temp=np.max(nhiet_do)
min_temp=np.min(nhiet_do)
day_max_temp=np.argmax(nhiet_do)+1
day_min_temp=np.argmin(nhiet_do)+1
print(f"Nhiệt độ ngày cao nhất trong tháng là :",max_temp)
print(f"Ngày có nhiệt độ cao nhất là ngày thứ :", day_max_temp)
print(f"Ngày có nhiệt độ thấp nhất là ngày thứ :",day_min_temp)
temp_diff = np.abs(np.diff(nhiet_do))
max_temp_diff = np.max(temp_diff)
day_max_temp_diff = np.argmax(temp_diff) + 1 
print(f"Sự chênh lệch nhiệt độ lớn nhất: {max_temp_diff}°C")
print(f"Ngày xảy ra sự biến đổi cao nhất: Giữa ngày {day_max_temp_diff} và ngày {day_max_temp_diff + 1}")
trung_binh = np.mean(nhiet_do)
days_above_20 = nhiet_do[nhiet_do > 20]
# 2. Nhiệt độ của ngày 5, 10, 15, 20, và 25
specific_days_temps = nhiet_do[[4, 9, 14, 19, 24]]
# 3. Nhiệt độ của các ngày có nhiệt độ trên trung bình
temps_above_avg = nhiet_do[nhiet_do > trung_binh]
# 4. Lấy nhiệt độ của các ngày chẵn và lẻ trong tháng
even_days_temps = nhiet_do[1::2]  # Ngày chẵn (chỉ số lẻ trong mảng 0-based)
odd_days_temps = nhiet_do[0::2]   # Ngày lẻ (chỉ số chẵn trong mảng 0-based)
days_above_20, specific_days_temps, temps_above_avg, even_days_temps, odd_days_temps