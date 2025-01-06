class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
