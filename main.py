from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title("Labyrinth")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()

    def close(self):
        self.__isRunning = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

def main():
    win = Window(800, 600)
    p1 = Point(150, 20)
    p2 = Point(20, 50)
    l1= Line(p1, p2)
    win.draw_line(l1, "red")
    win.wait_for_close()


main()