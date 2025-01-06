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
