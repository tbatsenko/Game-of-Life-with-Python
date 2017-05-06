from arrays import Array2D


class GrayscaleImage:
    """
    Implements the GrayscaleImage ADT.
    """

    def __init__(self, nrows, ncols):
        """
        Creates the GrayscaleImage grid and initializes the cells to 0 value.

        :param nrows: the number of rows.
        :param ncols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(nrows, ncols)
        self.rows = nrows
        self.cols = ncols
        # Clears the grid and set all cells to dead.
        self.clear(0)

    def width(self):
        """
        Returns width of the image.

        :return: width of the image.
        """
        return self.rows

    def heigth(self):
        """
        Returns heigth of the image.

        :return: heigth of the image.
        """
        return self.cols

    def clear(self, value):
        """
        Clears the image by setting its cells to the same value.

        :param value: int in range(0, 256)
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self._grid.__setitem__((i, j), value)

    def __getitem__(self, row, col):
        """
        Returns the indicated cell value.

        :param row: row of the cell.
        :param col: column of the cell.
        :param value: cell's value. (int) in range(256)
        :return: cell with index [row][col]
        """
        if row in range(self.rows) and col in range(self.cols):
            return self._grid.__getitem__((row, col))
        return "Incorrect index"

    def __setitem__(self, row, col, value):
        """
        Sets the indicated cell to the given value.

        :param row: row of the cell.
        :param col: column of the cell.
        :param value: cell's value. (int) in range(256)
        """
        if row in range(self.rows) and col in range(self.cols
                                                    ) and value in range(256):
            return self._grid.__setitem__((row, col), value)
        return "Incorrect index or Invalid value (valid: 0 to 255)"

# Testing
myimg = GrayscaleImage(10, 10)

print(myimg.heigth())
print(myimg.width())

myimg.__setitem__(1, 1, 255)
print(myimg.__getitem__(1, 1))
