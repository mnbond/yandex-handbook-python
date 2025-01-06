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


class PatchedPoint(Point):
    
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(*args[0])
        elif len(args) == 2:
            super().__init__(*args)
