class Rectangle:
    
    def __init__(self, corner, opposite_corner):
        self.width, self.height = abs(corner[0] - opposite_corner[0]), \
                                  abs(corner[1] - opposite_corner[1])
    
    def area(self):
        result = self.width * self.height
        return round(result, 2)
    
    def perimeter(self):
        result = (self.width + self.height) * 2
        return round(result, 2)
