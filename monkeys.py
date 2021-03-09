import tkinter as tk
import tkinter.ttk as tkk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500


class MonkeyGame(tkk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.grid(sticky="news")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.grid(sticky="news")

        self.banana_image = tk.PhotoImage(file='banana.png')
        self.banana = self.canvas.create_image(10, 10, image=self.banana_image)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Monkey Game")

    # do not allow window resizing
    root.resizable(False, False)
    app = MonkeyGame(root)
    root.mainloop()
