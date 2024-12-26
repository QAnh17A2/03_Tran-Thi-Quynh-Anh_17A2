import pandas as pd
stocks1 = pd.read_csv('D:/17A2KHDL/Lab3/data/stocks1.csv')
# Đọc file stocks2.csv
stocks2 = pd.read_csv("D:/17A2KHDL/Lab3/data/stocks2.csv")
# Gộp hai DataFrame lại
stocks = pd.concat([stocks1, stocks2])
# Tính giá trị trung bình của các cột
average_prices = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()
# Hiển thị 5 dòng đầu tiên
print(average_prices.head())

