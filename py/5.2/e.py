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
