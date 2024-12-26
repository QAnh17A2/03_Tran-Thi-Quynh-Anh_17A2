import pandas as pd


# Đường dẫn tới các file CSV
file_path_stocks1 = 'D:/17A2KHDL/Lab3/data/stocks1.csv'  # Thay đổi thành đường dẫn chính xác của stocks1.csv
file_path_stocks2 = 'D:/17A2KHDL/Lab3/data/stocks2.csv'  # Thay đổi thành đường dẫn chính xác của stocks2.csv
file_path_companies = 'D:/17A2KHDL/lab3/data/companies.csv'  # Thay đổi thành đường dẫn chính xác của companies.csv

try:
    # Đọc dữ liệu từ stocks1.csv và stocks2.csv
    stocks1 = pd.read_csv(file_path_stocks1)
    stocks2 = pd.read_csv(file_path_stocks2)
    companies=pd.read_csv(file_path_companies)
    # Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
    stocks = pd.concat([stocks1, stocks2,companies ], ignore_index=True)
    
    # 2. Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột 'date' và 'symbol' làm chỉ mục
    stocks.set_index(['date', 'symbol'], inplace=True)
    
    # 3. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, mỗi mã chứng khoán
    grouped = stocks.groupby(['date', 'symbol'])[['open', 'high', 'low', 'close', 'volume']].mean()
    
    # 4. Sắp xếp dữ liệu theo ngày và mã chứng khoán
    sorted_grouped = grouped.sort_index()
    
    # 5. Hiển thị kết quả cho 5 ngày đầu tiên
    print("5 ngày đầu tiên trong dữ liệu đã sắp xếp:")
    print(sorted_grouped.head())
    
except FileNotFoundError as e:
    print(f"Không tìm thấy file: {e.filename}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
