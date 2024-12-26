import pandas as pd

#1. Đọc file stocks1.csv 
stocks1 = pd.read_csv('D:/17A2KHDL/Lab3/data/stocks1.csv')

#2. Hiển thị 5 dòng đầu tiên của DataFrame
print(stocks1.head())

#3. Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1
print(stocks1.dtypes)

#4. Xem thông tin tổng quan (info) của stocks1
print(stocks1.info())


