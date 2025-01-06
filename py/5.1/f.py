class Rectangle:
    
    def __init__(self, corner, opposite_corner):
        self.width, self.height = abs(corner[0] - opposite_corner[0]), \
            abs(corner[1] - opposite_corner[1])
        self.x, self.y = min(corner[0], opposite_corner[0]), \
            max(corner[1], opposite_corner[1])
    
    def area(self):
        result = self.width * self.height
        return round(result, 2)
    
    def get_pos(self):
        return round(self.x, 2), round(self.y, 2)
        
    def get_size(self):
        return round(self.width, 2), round(self.height, 2)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def perimeter(self):
        result = (self.width + self.height) * 2
        return round(result, 2)
    
    def resize(self, width, height):
        self.width, self.height = width, height