# last in firt out
class stack:
    
    def __init__(self, arr = [],size = 0, value = 0):
        self.arr = arr
        self.size = size
        self.value = value
    
    #hàm khởi tạo
    def creat(self):
        self.size = int(input('nhập kích thước của mảng:'))
        arr0 = [] 
        for i in range(self.size):
            b = float(input(f'nhập giá trị thứ{i}:'))
            arr0.append(b)   
        self.arr = arr0
    
    #hàm hủy
    def __del__(self):
        print('đã xóa mảng')
    
    #hàm thêm đối tượng lên đỉnh
    def push(self, value):
        if self.isFull() == False:
            self.arr.append(value)
        else:
            print('mảng đã full')
    
    #hàm lấy phần tử từ đỉnh
    def pop(self):
        if self.isEmpty() == False:
            self.arr.pop(-1)
        else:
            print('mảng trống')
    
    #hàm kiểm tra xem mảng đã trống chưa
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
    
    #hàm kiểm tra xem mảng đã đầy chưa
    def isFull(self):
        if len(self.arr) == self.size:
            return True
        else:
            return False
    
    #hàm count trả về số phần tử trên ngăn xếp
    def count(self):
        self.value = float(input('nhập phần tử muốn tìm:'))
        return self.arr.count(self.value)

    def print(self):
        print(f'nội dung ngăn xếp:{self.arr}')
arr1 = stack()
arr1.creat()
arr1.pop()
arr1.push(1.54)
arr1.isEmpty()
arr1.isFull()
print(arr1.count())
arr1.print()
