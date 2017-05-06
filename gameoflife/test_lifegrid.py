# Program for playing the game of Life.
from lifegrid import LifeGrid
import time
import os

os.system('color 3')

# Define the initial configuration of live cells.
# INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]
INIT_CONFIG = [(0, 1), (1, 2), (2, 0), (2, 1), (2,2)]


def main():
    # Set the size of the grid.
    GRID_WIDTH, GRID_HEIGHT = None, None
    while not GRID_WIDTH and not GRID_HEIGHT:
        try:
            GRID_WIDTH, GRID_HEIGHT = [int(x) for x in input(
                "Enter width and height of the grid: ").split()]
        except:
            print("Something went wrong - make sure you entered\
                  two positive numbers")

    # Indicate the number of generations.
    NUM_GENS = None
    while not NUM_GENS:
        try:
            NUM_GENS = int(input("Enter the number of generations: "))
        except:
            print("Something went wrong - make sure you entered\
                  one positive number")

    # Constructs the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG, list())

    # Plays the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)


# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    live_cells = []
    dead_cells = []

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

            # Add the (i,j) tuple to deadCells if this cell contains
            # a dead organism in the next generation.
            if (neighbors >= 4 and grid.is_live_cell(i, j) or (neighbors <= 1)):
                dead_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells, dead_cells)


# Prints a text based representation of the game grid.
def draw(grid):
    time.sleep(0.5)
    os.system('cls')
    print("NEW GENERATION")
    for i in range(grid.num_rows()):
        print("                                     ", end="")
        for j in range(grid.num_cols()):
            if grid.is_live_cell(i, j):
                print(" O |", end="")
            else:
                print("   |", end="")
        print("\n")
        # print("----------------------------------------------------------")

# Executes the main routine.
main()
