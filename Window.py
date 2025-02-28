from tkinter import Tk, BOTH, Canvas
from Point import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__height = height
        self.__width = width
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)
