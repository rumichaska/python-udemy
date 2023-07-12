""" Ejemplo de slider
"""
from tkinter import Tk, Scale, Button

root = Tk()
root.title("Hola mundo: sliders")

vertical = Scale(root, from_=0, to=200, command=lambda x: enviar())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient="horizontal")
horizontal.pack()


def enviar():
    """Valores de los slider"""
    hor = horizontal.get()
    ver = vertical.get()
    print(str(hor) + " " + str(ver))


btn = Button(root, text="Enviar", command=enviar)
btn.pack()

root.mainloop()
