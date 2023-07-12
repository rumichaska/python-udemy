""" Ejemplo para abrir ventanas
"""
from tkinter import Tk, Button, Label, Toplevel
from PIL import ImageTk, Image

root = Tk()
root.title("Hola mundo")


# def open_img():
#     """Solucion1: Función para abrir imágen, con mainloop"""
#     img = ImageTk.PhotoImage(Image.open("./images/cascada.png"))
#     top = Toplevel()
#     top.title("Hola mundo, nueva ventana")
#     l_txt = Label(top, text="Soy un texto en una segunda ventana")
#     l_txt.pack()
#     l_img = Label(top, image=img)
#     l_img.pack()
#     top.mainloop()


# def open_img():
#     """Solucion2: Función para abrir imágen, con global"""
#     global img
#     img = ImageTk.PhotoImage(Image.open("./images/cascada.png"))
#     top = Toplevel()
#     top.title("Hola mundo, nueva ventana")
#     l_txt = Label(top, text="Soy un texto en una segunda ventana")
#     l_txt.pack()
#     l_img = Label(top, image=img)
#     l_img.pack()


# Button(root, text="Click", command=open_img).pack()


def open_img(img):
    """Solucion3: Función para abrir imágen, con variable"""
    top = Toplevel()
    top.title("Hola mundo, nueva ventana")
    l_txt = Label(top, text="Soy un texto en una segunda ventana")
    l_txt.pack()
    l_img = Label(top, image=img)
    l_img.pack()


img = ImageTk.PhotoImage(Image.open("./images/cascada.png"))
Button(root, text="Click", command=lambda: open_img(img)).pack()

root.mainloop()
