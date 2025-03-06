from graphics import Window
from cell import Cell

def main():
    window = Window(800, 600)
    cell_1 = Cell(window, 40, 60, 60, 70)
    cell_2 = Cell(window, 60, 80, 70, 80)
    cell_1.draw()
    cell_2.draw()
    window.wait_for_close()
    print("Is this thing on?")

main()