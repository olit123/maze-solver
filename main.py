from graphics import Window
from maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(10, 100, 7, 7, 100, 100, window)
    window.wait_for_close()

main()