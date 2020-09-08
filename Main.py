from GameEngine import Window, Graphics
from MazeMaker import Grid
import numpy as np
import pygame

"""
Script by https://github.com/LilZcrazyG
"""

window = Window(8001,8001,"Maze Generator")
graphics = Graphics(window.return_self())
grid = Grid(window,5)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(np.round(100 * (iteration / float(total))))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent[0]+percent[1]+percent[2]}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def main():
    window.return_self().fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if grid.showable:
                    grid.showable = False
                else:
                    grid.showable = True
    if not grid.done:
        if grid.current.x == grid.cells[-1].x and grid.current.y == grid.cells[-1].y:
            for cell in grid.stack:
                grid.solution.append(cell)
        grid.current.visited = True
        grid.next = grid.current.check_neighbors(grid,1,1,1,1)

        if grid.next:
            grid.next.visited = True
            grid.visited += 1

            grid.stack.append(grid.current)
            grid.stack[len(grid.stack)-1].in_stack = True

            grid.remove_walls(grid.current, grid.next)

            grid.current = grid.next
        elif len(grid.stack) > 0:
            grid.current = grid.stack.pop()
            if np.round((grid.visited/grid.unvisited)*100) != grid.last:
                printProgressBar(grid.visited, grid.unvisited, 'Progress:', 'Complete', 50)
            grid.last = np.round((grid.visited/grid.unvisited)*100)
        else:
            grid.done = True
            grid.current = grid.cells[-1]
            grid.stack = grid.solution
            graphics.set_color((100, 100, 255))
            grid.connect_stack(graphics)
            graphics.set_color((255, 255, 255))
            grid.show(graphics)
            pygame.image.save(window.return_self(), "Maze ["+str(window.width)+","+str(window.height)+"].jpeg")
    else:
        graphics.set_color((100, 100, 255))
        grid.connect_stack(graphics)
        graphics.set_color((255, 255, 255))
        grid.show(graphics)

window.game_loop(main)
