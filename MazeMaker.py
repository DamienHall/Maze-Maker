import numpy as Math
from random import randrange

"""
Script by https://github.com/LilZcrazyG
"""

class Grid:
    def __init__(self, window, size):
        self.window = window
        self.width, self.height = self.window.return_size()
        self.size = size
        self.rows = int(Math.floor(self.height / self.size))
        self.columns = int(Math.floor(self.width / self.size))
        self.cells = []
        self.unvisited = self.columns * self.rows
        self.visited = 1
        self.showable = True
        self.subdivide()
        self.current = self.cells[0]
        self.next = None
        self.stack = []
        self.done = False
        self.solution = []
        self.last = None
        self.x = None
        self.y = None

    def subdivide(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells.append(Cell(column, row, self.size, self))

    def remove_walls(self, cell_one, cell_two):
        x = cell_one.x / self.size - cell_two.x / self.size
        y = cell_one.y / self.size - cell_two.y / self.size

        if x == 1:
            cell_one.walls[3] = False
            cell_two.walls[1] = False
        elif x == -1:
            cell_one.walls[1] = False
            cell_two.walls[3] = False

        if y == 1:
            cell_one.walls[0] = False
            cell_two.walls[2] = False
        elif y == -1:
            cell_one.walls[2] = False
            cell_two.walls[0] = False

    def connect_stack(self, graphics):
        for cell in self.stack:
            graphics.square((cell.x,cell.y),self.size)
        graphics.square((self.current.x, self.current.y), self.size)
    def show(self, graphics):
        for cell in self.cells:
            if cell.visited:
                cell.show(graphics)

    def get_cell(self, x, y):
        if x < 0 or y < 0 or x > self.columns - 1 or y > self.rows - 1:
            return None
        else:
            return self.cells[int(x + y * self.columns)]

class Cell:
    def __init__(self, x, y, size, grid):
        self.x = x * size
        self.y = y * size
        self.size = size
        self.walls = [True, True, True, True]
        self.visited = False
        self.in_stack = False
        self.options = 0
        self.dir = None

    def show(self, graphics):
        for wall in self.walls:

            #top
            if self.walls[0]:
                graphics.line((self.x, self.y), (self.x + self.size, self.y))

            #right
            if self.walls[1]:
                graphics.line((self.x + self.size, self.y), (self.x + self.size, self.y + self.size))

            #bottom
            if self.walls[2]:
                graphics.line((self.x + self.size, self.y + self.size), (self.x, self.y + self.size))

            #left
            if self.walls[3]:
                graphics.line((self.x, self.y + self.size), (self.x, self.y))

    def highlight(self, graphics):
        graphics.square((self.x + 10, self.y + 10), self.size - 10 * 2)

    def check_neighbors(self, grid, bias_left, bias_right, bias_up, bias_down):
        neighbors = []

        top = grid.get_cell(self.x/self.size, self.y/self.size - 1)
        right = grid.get_cell(self.x/self.size + 1, self.y/self.size)
        bottom = grid.get_cell(self.x/self.size, self.y/self.size + 1)
        left = grid.get_cell(self.x/self.size - 1, self.y/self.size)

        if top != None and not top.visited:
            for bias in range(bias_up):
                neighbors.append(top)
        if right != None and not right.visited:
            for bias in range(bias_right):
                neighbors.append(right)
        if bottom != None and not bottom.visited:
            for bias in range(bias_down):
                neighbors.append(bottom)
        if left != None and not left.visited:
            for bias in range(bias_left):
                neighbors.append(left)


        if len(neighbors) > 0:
            self.options = len(neighbors)
            if len(neighbors)-1 != 0:
                dir = neighbors[randrange(len(neighbors))]
            else:
                dir = neighbors[0]

            return dir