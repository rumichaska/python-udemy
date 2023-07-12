from tkinter import *

root = Tk()
root.title("Hola mundo!")

# NOTE: si l se encuentra acá, solo se ejecuta una vez independientemente de los clicks
l = Label(root, text="Hola Mundo")


def click():
    # NOTE: si l se encuentra acá, se crea la etiqueta en cada click
    # l = Label(root, text="Hola Mundo")
    l.pack()


btn = Button(root, text="Clickeame", command=click, fg="#FFFF00", bg="#FF00FF")
btn.pack()

root.mainloop()
