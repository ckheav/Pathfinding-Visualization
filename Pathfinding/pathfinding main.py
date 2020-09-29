from queue import PriorityQueue
from pathfinding_visualization import *
import numpy as np
import pygame
import random
import math



def h(p1, p2):
       x1, y1 = p1
       x2, y2 = p2
       return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.create_path()
        draw()


def a_path_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g = {node: float('inf') for row in grid for node in row}
    g[start] = 0
    f = {node: float('inf') for row in grid for node in row}
    f[start] = h(start.get_position(), end.get_position())

    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.create_end()
            return True

        for neighbor in current.neighbors:
            temp_g = g[current] + 1
            
            if temp_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = temp_g + h(neighbor.get_position(), end.get_position())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.create_open()

        draw()
        if current != start:
            current.create_close()

    return False

def create_maze(draw, grid, rows, width):
    pass

def create_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid


def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j *gap, width))


def draw(win, grid, rows, width):
    win.fill(BLACK)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_position(pos, rows, width):
    gap = width // rows
    x, y = pos
    row = x // gap
    col = y // gap
    return row, col


def main(win, width):
    ROWS = 60
    grid = create_grid(ROWS, width)

    start = None
    end = None
    run = True
    
    while run:

        draw(win, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # Left
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.create_start()
                elif not end and node != start:
                    end = node
                    end.create_end()
                elif node != start and node != end:
                    node.create_wall()    
                    
            elif pygame.mouse.get_pressed()[2]: # Right
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.K_m:
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:       
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    a_path_algorithm(lambda: draw(win,grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = create_grid(ROWS, width)
                
    pygame.quit()


main(WIN, WIDTH)