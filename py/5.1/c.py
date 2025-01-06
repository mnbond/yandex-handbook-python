class RedButton:
    
    def __init__(self):
        self.counter = 0
    
    def click(self):
        self.counter += 1
        print("Тревога!")
    
    def count(self):
        return self.counter
