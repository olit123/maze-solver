from cell import Cell
from time import sleep
import random

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
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        cell_matrix = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                cell = Cell(self._win)
                col.append(cell)
            cell_matrix.append(col)
        self._cells = cell_matrix

    
    def _draw_cell(self, i, j, cell, color="black"):
        x1 = self.x1 + self.cell_size_x * i
        x2 = self.x1 + self.cell_size_x * (i + 1)
        y1 = self.y1 + self.cell_size_y * j
        y2 = self.y1 + self.cell_size_y * (j + 1)
        cell.draw(x1, x2, y1, y2, color)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        sleep(0.02)
    
    def _break_entrance_and_exit(self):
        cell = self._cells[0][0]
        cell.has_left_wall = False
        self._draw_cell(0, 0, cell, "black")
        i = self.num_cols - 1
        j = self.num_rows - 1
        cell = self._cells[i][j]
        cell.has_bottom_wall = False
        self._draw_cell(i, j, cell, "black")

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            direction_indexes = self._get_direction_indexes(i, j)
            if not direction_indexes:
                self._draw_cell(i, j, self._cells[i][j])
                return
            random_index = random.randrange(0, len(direction_indexes), 1)
            next_direction_index = direction_indexes[random_index]

            # up
            if next_direction_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # right
            if next_direction_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # down
            if next_direction_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # left
            if next_direction_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_direction_index[0], next_direction_index[1])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r()
    
    def _solve_r(self, i=0, j=0):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        directions = self._get_direction_indexes(i, j)
        random.shuffle(directions)
        for direction in directions:
            i_to, j_to, text = direction

            blocked = False
            if (
                (text == "up") and 
                (self._cells[i][j].has_top_wall or self._cells[i_to][j_to].has_bottom_wall)
            ) or (
                (text == "right") and 
                (self._cells[i][j].has_right_wall or self._cells[i_to][j_to].has_left_wall)
            ) or (
                (text == "down") and 
                (self._cells[i][j].has_bottom_wall or self._cells[i_to][j_to].has_top_wall)
            ) or (
                (text == "left") and 
                (self._cells[i][j].has_left_wall or self._cells[i_to][j_to].has_right_wall)
            ):
                blocked = True
            
            if not blocked:
                self._cells[i][j].draw_move(self._cells[i_to][j_to])
                solved = self._solve_r(i_to, j_to)
                if solved:
                    return True
                else:
                    self._cells[i_to][j_to].draw_move(
                        self._cells[i][j],
                        True
                    )
        return False
    
    def _get_direction_indexes(self, i, j):
        direction_indexes = []
        if j > 0: # above
            cell = self._cells[i][j-1]
            if not cell.visited:
                direction_indexes.append((i, j-1, "up"))
        # Check cell to right
        if i + 1 < self.num_cols: # right
            cell = self._cells[i+1][j]
            if not cell.visited:
                direction_indexes.append((i+1, j, "right"))
        # Check cell below
        if j + 1 < self.num_rows: # below
            cell = self._cells[i][j+1]
            if not cell.visited:
                direction_indexes.append((i, j+1, "down"))
        # Check cell to left
        if i > 0: # left
            cell = self._cells[i-1][j]
            if not cell.visited:
                direction_indexes.append((i-1, j, "left"))
        return direction_indexes

