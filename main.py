from tkinter import *
from vista import Ventanita
from controlador import *

print("Desde Main:  ", __name__)

if __name__ == "__main__":
    print("Esto se ejecuta si estamos en main.py ")
    root = Tk()
    objeto = Controller(root)
    root.mainloop()
