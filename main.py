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


def main():
    win = Window(800, 600)
    win.wait_for_close()


main()