from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Carrusel de las américas")

img1 = ImageTk.PhotoImage(Image.open("./images/img2.png"))
img2 = ImageTk.PhotoImage(Image.open("./images/img3.png"))
img3 = ImageTk.PhotoImage(Image.open("./images/img4.png"))
img4 = ImageTk.PhotoImage(Image.open("./images/img5.png"))

lista = [img1, img2, img3, img4]

# UI
l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)


def adelante(img_num):
    """
    Función para pasar imágenes
    """
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text="<-", command=lambda: atras(img_num - 1))
    btn_adelante = Button(
        root, text="->", command=lambda: adelante(img_num + 1))

    if img_num == 3:
        btn_adelante = Button(root, text="N/A", state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)


def atras(img_num):
    """
    Función para pasar imágenes
    """
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text="<-", command=lambda: atras(img_num - 1))
    btn_adelante = Button(
        root, text="->", command=lambda: adelante(img_num + 1))

    if img_num == 0:
        btn_atras = Button(root, text="N/A", state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)


btn_atras = Button(root, text="N/A", state=DISABLED)
btn_adelante = Button(root, text="->", command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()
