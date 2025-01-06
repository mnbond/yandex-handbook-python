class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
