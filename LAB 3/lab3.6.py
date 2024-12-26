import pandas as pd

# Đọc file stocks1.csv và stocks2.csv vào DataFrame
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
    
    # 1. Tạo Pivot Table với 'date' làm chỉ mục, 'symbol' làm cột và giá trị trung bình của 'close' làm giá trị
    pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')
    
    # 2. Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
    total_volume = stocks.groupby('symbol')['volume'].sum()
    
    # Thêm tổng volume vào Pivot Table (lặp qua các cột symbols)
    pivot_table['total_volume'] = total_volume
    
    # 3. Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp
    sorted_pivot_table = pivot_table.sort_values(by='total_volume', ascending=False, axis=1)
    
    # 4. Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
    print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
    print(sorted_pivot_table.iloc[:, :5])  # Chọn 5 cột đầu tiên có tổng volume cao nhất

except FileNotFoundError:
    print(f"Không tìm thấy file {file_path_stocks1} hoặc {file_path_stocks2}. Vui lòng kiểm tra lại đường dẫn.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
