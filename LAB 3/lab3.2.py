# 1. Kiểm tra xem trong stocks1 có dữ liệu Null nào không
import pandas as pd
stocks1 = pd.read_csv('D:/17A2KHDL/Lab3/data/stocks1.csv')
print(stocks1.isnull().sum())

# 2. Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột
stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)

# 3. Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print(stocks1.info())
