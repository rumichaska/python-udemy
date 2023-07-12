from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hola mundo")

# METODO 1
# imagen = Image.open("./cascada.png")
# imagen.show()

# METODO 2
img = ImageTk.PhotoImage(Image.open("./cascada.png"))
l = Label(image=img)
l.pack()

root.mainloop()
