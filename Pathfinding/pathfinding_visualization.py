from pathfinding_constant import *
import pygame

class Node:

    def __init__(self, row, col, width, total_rows):
        self.row = row 
        self.col = col
        self.x = row * width
        self.y = col * width 
        self.color = BLACK
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows


    def get_position(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == CYAN

    def is_open(self):
        return self.color == GOLD

    def is_wall(self):
        return self.color == WHITE

    def is_starting_node(self):
        return self.color == DARK_ORCHID

    def is_end_node(self):
        return self.color == DEEP_SKY_BLUE

    def reset(self):
        self.color = BLACK

    def create_open(self):
        self.color = GOLD
        
    def create_close(self):
        self.color = CYAN

    def create_wall(self):
        self.color = WHITE

    def create_start(self):
        self.color = DARK_ORCHID
        
    def create_end(self):
        self.color = DEEP_SKY_BLUE

    def create_path(self):
        self.color = YELLOW

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []

        # Down
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])
        # Up    
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbors.append(grid[self.row - 1][self.col])
        # Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])
        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbors.append(grid[self.row][self.col - 1])    


    def __it__ (self, other):
        return False




