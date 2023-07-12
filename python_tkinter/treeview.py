"""Proyecto de gestor de clientes"""
from tkinter import Tk, ttk

root = Tk()
root.title("Hola mundo: Treeview")

# Definición de las columnas
tree = ttk.Treeview(root)
tree["columns"] = ("Nombre", "Teléfono", "Empresa")

# Definición de los índices
# tree.column("#0")
tree.column("#0", width=0, stretch=False)
tree.column("Nombre")
tree.column("Teléfono")
tree.column("Empresa")

# Definición de los encabezados
# tree.heading("#0", text="id")
tree.heading("#0")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Empresa", text="Empresa")

tree.grid(row=0, column=0)

tree.insert("", "end", "lala", values=("Uno", "Dos", "Tres"),
            text="Chanchito Feliz")
tree.insert("", "end", "lele", values=("Cuatro", "Cinco", "Seis"),
            text="Chanchito Triste")
tree.insert("lele", "end", "lili", values=("4", "5", "6"),
            text="Chanchito Hijo")

root.mainloop()
