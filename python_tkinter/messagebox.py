from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hola mundo")


# def click():
#     messagebox.showwarning("Popup", "Hola Mundo")


# def click():
#     messagebox.showinfo("Popup", "Hola Mundo")


# def click():
#     messagebox.showerror("Popup", "Hola Mundo")


# def click():
#     """
#     Devuelve string
#     """
#     respuesta = messagebox.askquestion("Popup", "Hola Mundo")
#     if respuesta == "yes":
#         messagebox.showinfo("Respuesta", "la respuesta fue " + respuesta)
#     else:
#         messagebox.showinfo("Respuesta", ":( la respuesta fue " + respuesta)


# def click():
#     """
#     Devuelve boolean
#     """
#     respuesta = messagebox.askokcancel("Hola Mundo", "Desea realizar acción?")
#     if respuesta:
#         messagebox.showinfo("Respuesta", "La respuesta fue OK")
#     else:
#         messagebox.showinfo("Respuesta", "La respuesta fue Cancelar")


def click():
    """
    Devuelve boolean
    """
    respuesta = messagebox.askyesno("Hola Mundo", "Desea realizar acción?")
    if respuesta:
        messagebox.showinfo("Respuesta", "La respuesta fue Yes")
    else:
        messagebox.showinfo("Respuesta", "La respuesta fue No")


button = Button(root, text="Presióname", command=click)
button.pack()

root.mainloop()
