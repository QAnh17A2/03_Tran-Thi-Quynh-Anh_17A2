import pandas as pd

# Đường dẫn tới các file CSV
file_path_stocks1 = 'D:/17A2KHDL/Lab3/data/stocks1.csv'
file_path_stocks2 = 'D:/17A2KHDL/Lab3/data/stocks2.csv'
file_path_companies = 'D:/17A2KHDL/lab3/data/companies.csv'  

# 1. Đọc các file CSV vào DataFrame
try:
    # Đọc dữ liệu từ stocks1.csv và stocks2.csv
    stocks1 = pd.read_csv(file_path_stocks1)
    stocks2 = pd.read_csv(file_path_stocks2)
    
    # Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
    stocks = pd.concat([stocks1, stocks2], ignore_index=True)
    
    # Đọc dữ liệu từ companies.csv vào DataFrame companies
    companies = pd.read_csv(file_path_companies)
    
    # 2. Hiển thị 5 dòng đầu tiên của companies
    print("5 dòng đầu tiên của DataFrame companies:")
    print(companies.head())
    
    # 3. Kết hợp stocks và companies dựa trên cột chung là 'symbol'
    merged_data = pd.merge(stocks, companies, on='symbol', how='inner')
    
    # 4. Tính giá đóng cửa (close) trung bình cho mỗi công ty
    avg_close_per_company = merged_data.groupby('name')['close'].mean().reset_index()
    
    # 5. Hiển thị kết quả cho 5 công ty đầu tiên
    print("\nGiá đóng cửa trung bình cho mỗi công ty:")
    print(avg_close_per_company.head())
    
except FileNotFoundError as e:
    print(f"Không tìm thấy file: {e.filename}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
