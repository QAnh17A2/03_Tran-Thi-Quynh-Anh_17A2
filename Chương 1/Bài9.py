class Da_giac:
    def __init__(self, sides):
        self.sides = sides

    def chu_vi(self):
        return sum(self.sides)

    def display_sides(self):
        for i, side in enumerate(self.sides, 1):
            print(f"Side {i}: {side}")

class Binh_hanh(Da_giac):
    def __init__(self, base, side, height):
        super().__init__([base, side, base, side])
        self.base = base
        self.side = side
        self.height = height

    def dien_tich(self):
        return self.base * self.height

class Chu_nhat(Binh_hanh):
    def __init__(self, width, height):
        super().__init__(width, width, height)
        self.width = width
        self.height = height
    def dien_tich(self):
        return self.width * self.height

class Vuong(Chu_nhat):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def dien_tich(self):
        return self.side * self.side
# Tạo đối tượng Da_giac
da_giac = Da_giac([5, 7, 8, 9])
print("Đa giác:")
da_giac.display_sides()
print(f"Đa giác:\nChu vi: {da_giac.chu_vi()}\n")

binh_hanh = Binh_hanh(5, 7, 8)
print(f"Hình bình hành:\nChu vi: {binh_hanh.chu_vi()}\n{binh_hanh.dien_tich()}\n")

chu_nhat = Chu_nhat(5, 10)
print(f"Hình chữ nhật:\nChu vi: {chu_nhat.chu_vi()}\nDiện tích: {chu_nhat.dien_tich()}\n")

vuong = Vuong(5)
print(f"Hình vuông:\nChu vi: {vuong.chu_vi()}\nDiện tích: {vuong.dien_tich()}")
