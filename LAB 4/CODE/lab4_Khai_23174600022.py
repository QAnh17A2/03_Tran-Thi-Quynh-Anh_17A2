import sqlite3

# Kết nối tới cơ sở dữ liệu và tạo bảng nếu chưa tồn tại
def connect_database():
    conn = sqlite3.connect(r'C:\Users\Admin\OneDrive\Máy tính\25.PHAM_-DUY_KHAI_DHKL17A2HN_23174600022\LABS\lab4\DATA\product.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    conn.commit()
    return conn

# Hiển thị danh sách sản phẩm
def show_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    print("\nDanh sách sản phẩm:")
    print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Tên", "Giá", "Số lượng"))
    print("-" * 50)
    for product in products:
        print("{:<5} {:<20} {:<10} {:<10}".format(product[0], product[1], product[2], product[3]))
    print()

# Thêm sản phẩm mới
def add_product(conn):
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    print("Đã thêm sản phẩm mới.\n")

# Tìm kiếm sản phẩm theo tên
def search_product(conn):
    name = input("Nhập tên sản phẩm cần tìm: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + name + '%',))
    products = cursor.fetchall()
    print("\nKết quả tìm kiếm:")
    print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Tên", "Giá", "Số lượng"))
    print("-" * 50)
    for product in products:
        print("{:<5} {:<20} {:<10} {:<10}".format(product[0], product[1], product[2], product[3]))
    print()

# Cập nhật thông tin sản phẩm
def update_product(conn):
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    conn.commit()
    print("Đã cập nhật thông tin sản phẩm.\n")

# Xóa sản phẩm
def delete_product(conn):
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    print("Đã xóa sản phẩm.\n")

# Menu chính
def main():
    conn = connect_database()
    while True:
        print("Quản Lý Sản Phẩm")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ")
        
        if choice == "1":
            show_products(conn)
        elif choice == "2":
            add_product(conn)
        elif choice == "3":
            search_product(conn)
        elif choice == "4":
            update_product(conn)
        elif choice == "5":
            delete_product(conn)
        elif choice == "6":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")

    conn.close()

if __name__ == "__main__":
    main()
