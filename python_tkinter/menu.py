""" Ejemplo de Dropdown Menu
"""
from tkinter import Tk, StringVar, OptionMenu, Button, Label

root = Tk()
root.title("Hola mundo: Option menu")
root.geometry("500x500")

lista = [
    "Chanhito feliz",
    "Chanchito triste",
    "Chanchito emocionado"
]

value = StringVar()
value.set(lista[0])

drop = OptionMenu(root, value, *lista)
drop.pack()


def enviar():
    """Mostrar texto del menu"""
    Label(root, text=value.get()).pack()


btn = Button(root, text="Enviar", command=enviar)
btn.pack()

root.mainloop()
