# Решение задач из хэндбука Яндекс «Основы Python», глава 5

## Параграф 5.2. Волшебные методы, переопределение методов. Наследование

A. Классная точка 3.0
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


class PatchedPoint(Point):
    
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(*args[0])
        elif len(args) == 2:
            super().__init__(*args)
```

B. Классная точка 4.0
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


class PatchedPoint(Point):
    
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(*args[0])
        elif len(args) == 2:
            super().__init__(*args)
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
```

C. Классная точка 5.0
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


class PatchedPoint(Point):
    
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(*args[0])
        elif len(args) == 2:
            super().__init__(*args)
    
    def __add__(self, other):
        new_point = PatchedPoint(self.x, self.y)
        new_point.move(*other)
        return new_point
    
    def __iadd__(self, other):
        self.move(*other)
        return self
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
```

D. Дроби v0.1
```python
class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            self.__numerator, self.__denominator = map(int, args[0].split("/"))
        else:
            self.__numerator, self.__denominator = args
        self.__simplify()
    
    def __repr__(self):
        return f"Fraction({self.__numerator}, {self.__denominator})"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        self.__simplify()
            
    def numerator(self, value=None):
        if value is None:
            return self.__numerator
        self.__numerator = value
        self.__simplify()
```

E. Дроби v0.
```python
class Fraction:

    def __init__(self, *args):
        self.__numerator, self.__denominator = 1, 1
        if len(args) == 1:
            a, b = map(int, args[0].split("/"))
        else:
            a, b = args
        self.numerator(a)
        self.denominator(b)
        
    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def __repr__(self):
        return f"Fraction('{self}')"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
        self.__simplify()
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.__numerator)
        if self.__numerator < 0:
            self.__numerator = -value
        else:
            self.__numerator = value
        self.__simplify()
```

F. Дроби v0.3
```python
class Fraction:

    def __init__(self, *args):
        self.__numerator, self.__denominator = 1, 1
        if len(args) == 1:
            a, b = map(int, args[0].split("/"))
        else:
            a, b = args
        self.numerator(a)
        self.denominator(b)
        
    def __add__(self, other):
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator, 
                        self.__denominator * other.__denominator)

    def __iadd__(self, other):
        self.__copy(self + other)
        return self
    
    def __isub__(self, other):
        self.__copy(self - other)
        return self
    
    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def __repr__(self):
        return f"Fraction('{self}')"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __sub__(self, other):
        return self + -other
    
    def __copy(self, other):
        self.__numerator, self.__denominator = other.__numerator, other.__denominator
        
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
        self.__simplify()
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.__numerator)
        if self.__numerator < 0:
            self.__numerator = -value
        else:
            self.__numerator = value
        self.__simplify()
```

G. Дроби v0.4
```python
class Fraction:

    def __init__(self, *args):
        self.__numerator, self.__denominator = 1, 1
        if len(args) == 1:
            a, b = map(int, args[0].split("/"))
        else:
            a, b = args
        self.numerator(a)
        self.denominator(b)
        
    def __add__(self, other):
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator, 
                        self.__denominator * other.__denominator)

    def __iadd__(self, other):
        self.__copy(self + other)
        return self
    
    def __imul__(self, other):
        self.__copy(self * other)
        return self
    
    def __isub__(self, other):
        self.__copy(self - other)
        return self
    
    def __itruediv__(self, other):
        self.__copy(self / other)
        return self
    
    def __mul__(self, other):
        return Fraction(self.__numerator * other.__numerator, 
                        self.__denominator * other.__denominator)
    
    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def __repr__(self):
        return f"Fraction('{self}')"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __sub__(self, other):
        return self + -other
    
    def __truediv__(self, other):
        return self * other.reverse()
    
    def __copy(self, other):
        self.__numerator, self.__denominator = other.__numerator, other.__denominator
        
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
        self.__simplify()
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.__numerator)
        if self.__numerator < 0:
            self.__numerator = -value
        else:
            self.__numerator = value
        self.__simplify()
        
    def reverse(self):
        return Fraction(self.__denominator, self.__numerator)
```

H. Дроби v0.5
```python
class Fraction:

    def __init__(self, *args):
        self.__numerator, self.__denominator = 1, 1
        if len(args) == 1:
            a, b = map(int, args[0].split("/"))
        else:
            a, b = args
        self.numerator(a)
        self.denominator(b)
        
    def __add__(self, other):
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator, 
                        self.__denominator * other.__denominator)
    
    def __eq__(self, other):
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __gt__(self, other):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __iadd__(self, other):
        self.__copy(self + other)
        return self
    
    def __imul__(self, other):
        self.__copy(self * other)
        return self
    
    def __isub__(self, other):
        self.__copy(self - other)
        return self
    
    def __itruediv__(self, other):
        self.__copy(self / other)
        return self
    
    def __le__(self, other):
        return self < other or self == other
    
    def __lt__(self, other):
        return not self >= other
    
    def __mul__(self, other):
        return Fraction(self.__numerator * other.__numerator, 
                        self.__denominator * other.__denominator)
    
    def __ne__(self, other):
        return not self == other
    
    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def __repr__(self):
        return f"Fraction('{self}')"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __sub__(self, other):
        return self + -other
    
    def __truediv__(self, other):
        return self * other.reverse()
    
    def __copy(self, other):
        self.__numerator, self.__denominator = other.__numerator, other.__denominator
        
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
        self.__simplify()
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.__numerator)
        if self.__numerator < 0:
            self.__numerator = -value
        else:
            self.__numerator = value
        self.__simplify()
        
    def reverse(self):
        return Fraction(self.__denominator, self.__numerator)
```

I. Дроби v0.6
```python
class Fraction:

    def __init__(self, *args):
        self.__numerator, self.__denominator = 1, 1
        if len(args) == 1:
            if "/" in str(args[0]):
                a, b = map(int, args[0].split("/"))
            else:
                a, b = int(args[0]), 1
        else:
            a, b = args
        self.numerator(a)
        self.denominator(b)
        
    def __add__(self, other):
        other = Fraction(str(other))
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator, 
                        self.__denominator * other.__denominator)
    
    def __eq__(self, other):
        other = Fraction(str(other))
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __gt__(self, other):
        other = Fraction(str(other))
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __iadd__(self, other):
        self.__copy(self + other)
        return self
    
    def __imul__(self, other):
        self.__copy(self * other)
        return self
    
    def __isub__(self, other):
        self.__copy(self - other)
        return self
    
    def __itruediv__(self, other):
        self.__copy(self / other)
        return self
    
    def __le__(self, other):
        return self < other or self == other
    
    def __lt__(self, other):
        return not self >= other
    
    def __mul__(self, other):
        other = Fraction(str(other))
        return Fraction(self.__numerator * other.__numerator, 
                        self.__denominator * other.__denominator)
    
    def __ne__(self, other):
        return not self == other
    
    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def __repr__(self):
        return f"Fraction('{self}')"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __sub__(self, other):
        return self + -other
    
    def __truediv__(self, other):
        other = Fraction(str(other))
        return self * other.reverse()
    
    def __copy(self, other):
        self.__numerator, self.__denominator = other.__numerator, other.__denominator
        
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
        self.__simplify()
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.__numerator)
        if self.__numerator < 0:
            self.__numerator = -value
        else:
            self.__numerator = value
        self.__simplify()
        
    def reverse(self):
        return Fraction(self.__denominator, self.__numerator)
```

J. Дроби v0.7
```python
class Fraction:

    def __init__(self, *args):
        self.__numerator, self.__denominator = 1, 1
        if len(args) == 1:
            if "/" in str(args[0]):
                a, b = map(int, args[0].split("/"))
            else:
                a, b = int(args[0]), 1
        else:
            a, b = args
        self.numerator(a)
        self.denominator(b)
        
    def __add__(self, other):
        other = Fraction(str(other))
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator, 
                        self.__denominator * other.__denominator)
    
    def __eq__(self, other):
        other = Fraction(str(other))
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __gt__(self, other):
        other = Fraction(str(other))
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __iadd__(self, other):
        self.__copy(self + other)
        return self
    
    def __imul__(self, other):
        self.__copy(self * other)
        return self
    
    def __isub__(self, other):
        self.__copy(self - other)
        return self
    
    def __itruediv__(self, other):
        self.__copy(self / other)
        return self
    
    def __le__(self, other):
        return self < other or self == other
    
    def __lt__(self, other):
        return not self >= other
    
    def __mul__(self, other):
        other = Fraction(str(other))
        return Fraction(self.__numerator * other.__numerator, 
                        self.__denominator * other.__denominator)
    
    def __ne__(self, other):
        return not self == other
    
    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def __radd__(self, other):
        return self + other
    
    def __repr__(self):
        return f"Fraction('{self}')"
    
    def __rmul__(self, other):
        return self * other
    
    def __rsub__(self, other):
        return -self + other
    
    def __rtruediv__(self, other):
        return self.reverse() * other
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __sub__(self, other):
        return self + -other
    
    def __truediv__(self, other):
        other = Fraction(str(other))
        return self * other.reverse()
    
    def __copy(self, other):
        self.__numerator, self.__denominator = other.__numerator, other.__denominator
        
    def __simplify(self):
        a, b = self.__numerator, self.__denominator
        while b:
            a, b = b, a % b
        self.__numerator //= a
        self.__denominator //= a
    
    def denominator(self, value=None):
        if value is None:
            return self.__denominator
        self.__denominator = value
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
        self.__simplify()
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.__numerator)
        if self.__numerator < 0:
            self.__numerator = -value
        else:
            self.__numerator = value
        self.__simplify()
        
    def reverse(self):
        return Fraction(self.__denominator, self.__numerator)
```