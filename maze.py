from cell import Cell
from time import sleep

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        cell_matrix = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                cell = Cell(self._win)
                self._draw_cell(i, j, cell)
                col.append(cell)
            cell_matrix.append(col)
        self._cells = cell_matrix
    
    def _draw_cell(self, i, j, cell):
        x1 = self.x1 + self.cell_size_x * i
        x2 = self.x1 + self.cell_size_x * (i + 1)
        y1 = self.y1 + self.cell_size_y * j
        y2 = self.y1 + self.cell_size_y * (j + 1)
        cell.draw(x1, x2, y1, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        sleep(0.05)

