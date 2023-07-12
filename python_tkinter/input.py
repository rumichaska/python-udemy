from tkinter import *

root = Tk()
root.title("Hola mundo!")
root.geometry("500x500")

# ACTUALIZAR TEXTO
e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto")


def click():
    """
    Función para recuperar y actualizar un Label
    """
    texto = e.get()
    l.configure(text=texto)


btn = Button(root, text="Click", command=click)
btn.pack()

l = Label(root, text="Texto de la etiqueta")
l.pack()

# AÑADIR TEXTOS
e_list = Entry(root, width=40)
e_list.pack()
e_list.insert(0, "Ingresa textos")


def click_list():
    """
    Función para recuperar y agrear Label's
    """
    texto = e_list.get()
    l_list = Label(root, text=texto)
    l_list.pack()
    e_list.delete(0, END)


btn_list = Button(root, text="Añadir", command=click_list)
btn_list.pack()

# VARIABLES
e_var = Entry(root, width=40)
e_var.pack()
e_var.insert(0, "Ingresa texto")


def click_var():
    """
    Función para actualizar Label usando variables
    """
    texto = e_var.get()
    text_variable.set(texto)
    valor = text_variable.get()
    print(valor)
    e_var.delete(0, END)


text_variable = StringVar()

label = Label(root, textvariable=text_variable)
label.pack()


btn_var = Button(root, text="Añadir", command=click_var)
btn_var.pack()

root.mainloop()
