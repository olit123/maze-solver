from graphics import Window
from cell import Cell

def main():
    window = Window(800, 600)
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell1.draw(100, 200, 100, 150)
    cell2.draw(200, 300, 150, 200)
    cell1.draw_move(cell2, True)
    window.wait_for_close()

main()