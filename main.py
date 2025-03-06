from graphics import Window, Line

def main():
    window = Window(800, 600)
    line_1 = Line((0, 0), (400, 300))
    line_2 = Line((800, 0), (400, 300))
    window.draw_line(line_1, "black")
    window.draw_line(line_2, "red")
    window.wait_for_close()
    print("Is this thing on?")

main()