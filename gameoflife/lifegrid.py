import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
    inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        self.rows = num_rows
        self.cols = num_cols
        # Clears the grid and set all cells to dead.
        self.configure(list(), list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self.rows

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid.
        """
        return self.cols

    def configure(self, live_coords_list, dead_coords_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for cell in live_coords_list:
            self.set_cell(cell[0], cell[1])
        for cell in dead_coords_list:
            self.clear_cell(cell[0], cell[1])

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return True if self._grid.__getitem__((row, col)) else False

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row, col), LifeGrid.DEAD_CELL)

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row, col), LifeGrid.LIVE_CELL)

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        # lst of possible neighbors
        lst = [(-1, 0), (-1, 1), (0, 1), (1, 1),
               (1, 0), (1, -1), (0, -1), (-1, -1)]
        counter = 0
        for i, j in lst:
            try:
                if self._grid.__getitem__((row+i, col+j)) == self.LIVE_CELL:
                    counter += 1
            except:
                pass
        return counter
