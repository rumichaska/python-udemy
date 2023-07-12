from tkinter import *


root = Tk()
root.title("Hola mundo")

btn = Button(root, text="Salir", command=root.quit)
btn.pack()

root.mainloop()
