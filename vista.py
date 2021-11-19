from tkinter import StringVar
from tkinter import Entry
from tkinter import Frame
from tkinter import Button
from tkinter import ttk
from tkinter import Label
from modelo import *

class MainWindow():
    def __init__(self, window):
        self.root = window
        self.root.title("Ejemplo MVC")
        self.nombre = StringVar()
        self.entrada = Entry(self.root, textvariable=self.nombre)
        self.entrada.grid(row=1, column=1)

        self.mi_boton = Button(self.root, text="Sumar", command=lambda: sumar(self.nombre.get(), 3))
        self.mi_boton.grid(row=2, column=1)

print("Desde Ventanita:  ", __name__)

if __name__ == "__main__":
    print("Esto se ejecuta si estamos en vista.p ")
