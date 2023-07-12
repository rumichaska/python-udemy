from tkinter import *

# INICIALIZAR
root = Tk()

# UI
root.title("Pies a metros")

frame = Frame(root, padx=12, pady=3)
frame.grid(column=0, row=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
metros_label = Label(frame, textvariable=metros)
metros_label.grid(column=1, row=1)


def calcular(*args):
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 + 0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set("ERROR")


button = Button(frame, text="Calcular", command=calcular)
button.grid(column=2, row=2)

pies_unit_label = Label(frame, text="pies")
pies_unit_label.grid(column=0, row=0)

resultado_label = Label(frame, text="es igual a:")
resultado_label.grid(column=0, row=1)

metros_unit_label = Label(frame, text="metros")
metros_unit_label.grid(column=2, row=1)

pies_input.focus()

root.bind("<Return>", calcular)

# EJECUCION
root.mainloop()
