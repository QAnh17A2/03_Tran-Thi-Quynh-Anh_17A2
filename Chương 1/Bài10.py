class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def display(self):
        print(f"Điểm: ({self.x}, {self.y})")
class Ellipse(Point):
    def __init__(self, x=0, y=0, a=1, b=1):
        super().__init__(x, y)
        self.a = a  # Bán trục lớn
        self.b = b  # Bán trục nhỏ
    
    def area(self):
        import math
        return math.pi * self.a * self.b
    
    def display(self):
        super().display()
        print(f"Bán trục lớn: {self.a}")
        print(f"Bán trục nhỏ: {self.b}")
        print(f"Diện tích elip: {self.area()}")
class Circle(Ellipse):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y, radius, radius)
        self.radius = radius
    
    def display(self):
        super().display()
        print(f"Bán kính: {self.radius}")
# Tạo đối tượng Điểm
point = Point(2, 3)
print("Điểm:")
point.display()
print()

# Tạo đối tượng Elip
ellipse = Ellipse(2, 3, 5, 3)
print("Elip:")
ellipse.display()
print()

# Tạo đối tượng Đường tròn
circle = Circle(2, 3, 5)
print("Đường tròn:")
circle.display()
