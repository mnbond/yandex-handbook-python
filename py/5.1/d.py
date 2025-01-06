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
