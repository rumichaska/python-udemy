"""Proyecto de gestor de clientes"""
from tkinter import Tk, Button, Label, Entry, Toplevel, ttk, messagebox
import sqlite3

# INICIALIZACION
root = Tk()
root.title("Hola mundo: CRM")

# BASE DE DATOS
# Conexión a la base de datos
db_connection = sqlite3.connect("crm.db")
# Cursor para consultas
db_cursor = db_connection.cursor()

# Consulta inicial: Crear tabla
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        empresa TEXT NOT NULL
    ); 
    """)
# Ejecutar la creación de la tabla
db_connection.commit()


# FUNCIONES
def render_clientes():
    """Función para renderizar información de clientes agregados"""
    rows = db_cursor.execute("""
        SELECT * FROM cliente
    """).fetchall()

    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", "end", row[0], values=(row[1], row[2], row[3]))


def insertar(cliente):
    """Función para insertar cliente"""
    db_cursor.execute("""
        INSERT INTO cliente (nombre, telefono, empresa)
        VALUES (?, ?, ?)
    """, (cliente["nombre"], cliente["telefono"], cliente["empresa"]))
    db_connection.commit()
    render_clientes()


def nuevo_cliente():
    """Función para agregar nuevo cliente"""
    def guardar():
        if not e_nombre.get():
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        if not e_telefono.get():
            messagebox.showerror("Error", "El teléfono es obligatorio")
            return
        if not e_empresa.get():
            messagebox.showerror("Error", "El campo de empresa es obligatorio")
            return

        cliente = {
            "nombre": e_nombre.get(),
            "telefono": e_telefono.get(),
            "empresa": e_empresa.get()
        }
        insertar(cliente)
        w_crear.destroy()

    w_crear = Toplevel()
    w_crear.title("Nuevo cliente")

    l_nombre = Label(w_crear, text="Nombre")
    e_nombre = Entry(w_crear, width=40)
    l_nombre.grid(row=0, column=0)
    e_nombre.grid(row=0, column=1)

    l_telefono = Label(w_crear, text="Teléfono")
    e_telefono = Entry(w_crear, width=40)
    l_telefono.grid(row=1, column=0)
    e_telefono.grid(row=1, column=1)

    l_empresa = Label(w_crear, text="Empresa")
    e_empresa = Entry(w_crear, width=40)
    l_empresa.grid(row=2, column=0)
    e_empresa.grid(row=2, column=1)

    b_guardar = Button(w_crear, text="Guardar", command=guardar)
    b_guardar.grid(row=3, column=1)

    w_crear.mainloop()


def eliminar_cliente():
    """Función para eliminar nuevo cliente"""
    id_cliente = tree.selection()[0]

    cliente = db_cursor.execute("""
        SELECT * FROM cliente WHERE id = ?
    """, (id_cliente, )).fetchone()

    repuesta = messagebox.askokcancel(
        "Seguro?", "Estás seguro de querer eliminar el cliente " + cliente[1] + "?")
    if repuesta:
        db_cursor.execute("""
            DELETE FROM cliente WHERE id = ?
        """, (id_cliente, ))
        db_connection.commit()
        render_clientes()
    else:
        pass


# UI
# Botón para crear cliente
btn_crear = Button(root, text="Nuevo cliente", command=nuevo_cliente)
btn_crear.grid(row=0, column=0)
# Botón para eliminar cliente
btn_eliminar = Button(root, text="Eliminar cliente", command=eliminar_cliente)
btn_eliminar.grid(row=0, column=1)

# Definición de las columnas
tree = ttk.Treeview(root)
tree["columns"] = ("Nombre", "Teléfono", "Empresa")
# Definición de los índices
tree.column("#0", width=0, stretch=False)
tree.column("Nombre")
tree.column("Teléfono")
tree.column("Empresa")
# Definición de los encabezados
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Empresa", text="Empresa")

tree.grid(row=1, column=0, columnspan=2)

# Actualizar lista de clientes
render_clientes()

# EJECUCION
root.mainloop()
