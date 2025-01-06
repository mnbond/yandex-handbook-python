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
