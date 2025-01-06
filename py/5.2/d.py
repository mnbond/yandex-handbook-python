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
