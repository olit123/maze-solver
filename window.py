from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "root"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()