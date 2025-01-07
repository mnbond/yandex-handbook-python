# Решение задач из хэндбука Яндекс «Основы Python», глава 5

## Параграф 5.1. Объектная модель Python. Классы, поля и методы

A. Классная точка
```python
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

B. Классная точка 2.0
```python
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
```

C. Не нажимай красную кнопку!
```python
class RedButton:
    
    def __init__(self):
        self.counter = 0
    
    def click(self):
        self.counter += 1
        print("Тревога!")
    
    def count(self):
        return self.counter
```

D. Работа не волк
```python
class Programmer:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.rise_counter = 0
        self.salary = 0
        self.time = 0

    def info(self):
        return f"{self.name} {self.time}ч. {self.salary}тгр."
    
    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        elif self.position == "Senior":
            self.rise_counter += 1
    
    def work(self, time):
        salaries = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.time += time
        self.salary += time * (salaries[self.position] + self.rise_counter)
```

E. Классный прямоугольник
```python
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
```

F. Классный прямоугольник 2.0
```python
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
```

G. Классный прямоугольник 3.0
```python
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
        
    def scale(self, factor):
        self.move(self.width * (1 - factor) / 2, -self.height * (1 - factor) / 2)
        self.resize(round(self.width * factor, 2), round(self.height * factor, 2))
        
    def turn(self):
        self.move((self.width - self.height) / 2, (self.width - self.height) / 2)
        self.resize(self.height, self.width)
```

H. Шашки
```python
class Cell:

    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:
    
    def __init__(self):
        self.cells = {}
        for row in "87654321":
            for col in "ABCDEFGH":
                p = col + row
                if (row in "86" and col in "BDFH") or (row == "7" and col in "ACEG"):
                    self.cells[p] = Cell("B")
                elif (row in "31" and col in "ACEG") or (row == "2" and col in "BDFH"):
                    self.cells[p] = Cell("W")
                else:
                    self.cells[p] = Cell("X")

    def get_cell(self, p):
        return self.cells[p]
    
    def move(self, f, t):
        self.cells[t].state = self.cells[f].state
        self.cells[f].state = "X"
```

I. Очередь
```python
class Queue:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        return self.items.pop(0)
    
    def push(self, item):
        self.items.append(item)
```

J. Стек
```python
class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
```