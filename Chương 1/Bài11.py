import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        # Sử dụng công thức Heron để tính diện tích tam giác
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def display(self):
        print(f"Cạnh a: {self.a}, cạnh b: {self.b}, cạnh c: {self.c}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")
class RightTriangle(Triangle):
    def __init__(self, a, b):
        c = math.sqrt(a ** 2 + b ** 2)  # Tính cạnh huyền
        super().__init__(a, b, c)
    
    def display(self):
        print("Tam giác vuông:")
        super().display()
class IsoscelesTriangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a, a, b)
    
    def display(self):
        print("Tam giác cân:")
        super().display()
class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, a):
        super().__init__(a, a)
    
    def display(self):
        print("Tam giác đều:")
        super().display()
# Tạo đối tượng Tam giác
triangle = Triangle(3, 4, 5)
print("Tam giác:")
triangle.display()
print()

# Tạo đối tượng Tam giác vuông
right_triangle = RightTriangle(3, 4)
right_triangle.display()
print()

# Tạo đối tượng Tam giác cân
isosceles_triangle = IsoscelesTriangle(3, 4)
isosceles_triangle.display()
print()

# Tạo đối tượng Tam giác đều
equilateral_triangle = EquilateralTriangle(3)
equilateral_triangle.display()
