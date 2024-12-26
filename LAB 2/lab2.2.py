import numpy as np
import csv
# Đọc dữ liệu fle csv
filename = "D:/17A2KHDL/Lab2/data/diem_hoc_phan.csv"
data = []
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        data.append(row)
# Chuyển sang mảng NumPy
data_array = np.array(data)
print(data_array)
def quy_doi_diem(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 8.0 <= diem < 8.5:
        return 'B+'
    elif 7.0 <= diem < 8.0:
        return 'B'
    elif 6.5 <= diem < 7.0:
        return 'C+'
    elif 5.5 <= diem < 6.5:
        return 'C'
    elif 5.0 <= diem < 5.5:
        return 'D+'
    elif 4.0 <= diem < 5.0:
        return 'D'
    else:
        return 'F'
# Lấy cột điểm học phần và chuyển đổi
diem_hoc_phan = data_array[:, 2:].astype(float)
diem_tin_chi = np.vectorize(quy_doi_diem)(diem_hoc_phan)
print(diem_tin_chi)
hp1 = diem_hoc_phan[:, 0]
hp2 = diem_hoc_phan[:, 1]
hp3 = diem_hoc_phan[:, 2]

print("Điểm HP1:", hp1)
print("Điểm HP2:", hp2)
print("Điểm HP3:", hp3)
def phan_tich_diem(hoc_phan, ten_hp):
    tong = np.sum(hoc_phan)
    trung_binh = np.mean(hoc_phan)
    do_lech_chuan = np.std(hoc_phan)
    print(f"{ten_hp}: Tổng = {tong}, Trung bình = {trung_binh:.2f}, Độ lệch chuẩn = {do_lech_chuan:.2f}")

phan_tich_diem(hp1, "HP1")
phan_tich_diem(hp2, "HP2")
phan_tich_diem(hp3, "HP3")
# Gộp tất cả điểm học phần
diem_tong_hop = diem_tin_chi.flatten()

# Đếm số lượng từng loại điểm
loai_diem, so_luong = np.unique(diem_tong_hop, return_counts=True)

print("Phân tích điểm tổng hợp:")
for diem, sl in zip(loai_diem, so_luong):
    print(f"Điểm {diem}: {sl} sinh viên")




