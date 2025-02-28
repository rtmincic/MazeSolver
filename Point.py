from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def draw(self, canvas, color):
        canvas.create_line(self.input1.x, self.input1.y, self.input2.x , self.input2.y, fill=color, width=2)

    