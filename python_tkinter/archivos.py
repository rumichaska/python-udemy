""" Ejemplo para seleccionar archivos
"""
from tkinter import Tk, Label, Button, filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Hola mundo")

# # SOLUCION 1
# root.filename = filedialog.askopenfilename(title="Elige una foto",
#                                            filetypes=(("Archivos PNG", "*.png"),
#                                                       ("Todos", "*")))
# l = Label(root, text=root.filename)
# l.pack()
# img = Image.open(root.filename)
# imgTK = ImageTk.PhotoImage(img)
# l2 = Label(root, image=imgTK)
# l2.pack()


def open_img():
    """Función para seleccionar archivos"""
    global imgTK
    root.filename = filedialog.askopenfilename(title="Elige una foto",
                                               filetypes=(("Archivos PNG", "*.png"),
                                                          ("Todos", "*")))
    l = Label(root, text=root.filename)
    l.pack()
    img = Image.open(root.filename)
    imgTK = ImageTk.PhotoImage(img)
    l2 = Label(root, image=imgTK)
    l2.pack()


btn = Button(root, text="Cargar imagen", command=open_img)
btn.pack()

root.mainloop()
