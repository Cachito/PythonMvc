import tkinter as tk
from model import *
from view import *
from controller import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
