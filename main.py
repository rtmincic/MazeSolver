from Window import Window
from Point import Line, Point

win = Window(2000, 1500)

point1 = Point(10, 10)
point2 = Point(100, 100)
line = Line(point1, point2)
win.draw_line(line, "black")

win.wait_for_close()