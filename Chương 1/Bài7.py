class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
    
    #hàm nhập ngày tháng năm
    def creat(self):
        self.day = int(input('nhập ngày:'))
        self.month = int(input('nhập tháng:'))
        self.year = int(input('nhập năm:'))
    
    def display(self):
        print(f"Ngày: {self.day:02d}/{self.month:02d}/{self.year}")
    
    def next(self):
        # Kiểm tra ngày cuối cùng của tháng
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
    
    def days_in_month(self):
        # Kiểm tra tháng có bao nhiêu ngày
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
    
    def is_leap_year(self):
        # Kiểm tra năm nhuận
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        else:
            return False

# Ví dụ sử dụng lớp Date
date1 = Date()
date1.creat()
date1.display()
date1.next()
date1.display()
date1.next()
date1.display()
