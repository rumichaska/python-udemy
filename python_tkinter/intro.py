from tkinter import *

# Inicializar Tk
root = Tk()

# Titulo de la ventaja
root.title("Hola mundo")
# Dimensiones de la vnetana
root.geometry("500x500")

# METODO 1
# Crear (instancia) etiqueta dentro de root
# label = Label(root, text="Hola mundo, mi primera etiqueta")
# LLamar a la instancia dentro de la UI
# label.pack()
# METODO 2
# Label(root, text="Hola mundo, mi primera etiqueta").pack()

l1 = Label(root, text="Hola mundo, primera etiqueta")
l2 = Label(root, text="Chao mundo, segunda etiqueta")
l3 = Label(root, text="                            ")

l1.grid(row=0, column=0)
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)

# Mantener ejecución/actualización
root.mainloop()
