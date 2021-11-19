from tkinter import *
from vista import *

class Controller():
   def __init__(self, windows1):
        print("HOla desde controller ------------------")
        self.root_controler = windows1
        obj = MainWindow(self.root_controler)
