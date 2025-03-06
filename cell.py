from graphics import Line

class Cell():
    def __init__(self, window, x1, x2, y1, y2):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
    
    def draw(self):
        if self.has_top_wall:
            line = Line((self._x1, self._y1), (self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line((self._x2, self._y1), (self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line((self._x1, self._y2), (self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_left_wall:
            line = Line((self._x1, self._y1), (self._x1, self._y2))
            self._win.draw_line(line, "black")