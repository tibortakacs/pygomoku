# Defines the board class
class Board:
    def __init__(self, size):
        self.__board = [[0 for x in range(size)] for y in range(size)]
        self.__size = size

    def __index(self, i):
        if i < 0:
            raise IndexError("Negative __index is not allowed")
        return i

    def get_size(self):
        return self.__size

    def get_element(self, x, y):
        return self.__board[self.__index(x)][self.__index(y)]

    def set_element(self, x, y, value):
        self.__board[self.__index(x)][self.__index(y)] = value

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

        return [self.__board[self.__index(x + i * dx)][self.__index(y + i * dy)] for i in range(n)]
