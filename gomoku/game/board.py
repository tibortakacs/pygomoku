# Defines the board class
class Board:
    def __init__(self, size):
        self.board = [[0 for x in range(size)] for y in range(size)]

    def index(self, i):
        if i < 0:
            raise IndexError("Negative index is not allowed")
        return i

    def get_element(self, x, y):
        return self.board[self.index(x)][self.index(y)]

    def set_element(self, x, y, value):
        self.board[self.index(x)][self.index(y)] = value

    def get_element_array(self, x, y, n, dir):
        if dir == 0:
            dx = 0
            dy = 1
        if dir == 1:
            dx = -1
            dy = 1
        if dir == 2:
            dx = -1
            dy = 0
        if dir == 3:
            dx = -1
            dy = -1
        if dir == 4:
            dx = 0
            dy = -1
        if dir == 5:
            dx = 1
            dy = -1
        if dir == 6:
            dx = 1
            dy = 0
        if dir == 7:
            dx = 1
            dy = 1

        return [self.board[self.index(x + i * dx)][self.index(y + i * dy)] for i in range(n)]
