""" Ejemplo para generar 'radiobuttons'
"""
from tkinter import Tk, IntVar, Radiobutton, Label, StringVar

root = Tk()
root.title("Hola mundo")

r = IntVar()
r.set(2)

# Radiobutton(root, text="Opción 1", variable=r, value=1).pack()
# Radiobutton(root, text="Opción 2", variable=r, value=2).pack()

CHANCHITOS = [
    ("Feliz", "Feliz"),
    ("Triste", "Triste"),
    ("Amargado", "Amargado"),
    ("Wolfgang", "Wolfgang")
]

chanchito = StringVar()
chanchito.set("Wolfgang")

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()
