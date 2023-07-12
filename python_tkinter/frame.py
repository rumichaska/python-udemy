from tkinter import *

root = Tk()
root.title("Hola mundo")

# frame = LabelFrame(root, text="Login", padx=10, pady=10, borderwidth=10)
frame = Frame(root, padx=10, pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)

l = Label(frame, text="Estoy dentro de un frame")
b = Button(frame, text="Salir", command=root.quit)
l.pack()
b.pack()

root.mainloop()
