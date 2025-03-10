from graphics import Line

class Cell():
    def __init__(self, window=None):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False
    
    def draw(self, x1, x2, y1, y2, color):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line((self._x1, self._y1), (self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(line, color)
        else:
            self._win.draw_line(line, "white")
        line = Line((self._x2, self._y1), (self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(line, color)
        else:
            self._win.draw_line(line, "white")
        line = Line((self._x1, self._y2), (self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(line, color)
        else:
            self._win.draw_line(line, "white")
        line = Line((self._x1, self._y1), (self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(line, color)
        else:
            self._win.draw_line(line, "white")
    
    def get_center(self):
        return (
            self._x1 + int((self._x2 - self._x1) / 2),
            self._y1 + int((self._y2 - self._y1) / 2)
        )
    
    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center(), to_cell.get_center())
        if not undo:
            self._win.draw_line(line, "grey")
        else:
            self._win.draw_line(line, "red")
    