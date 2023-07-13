"""Importacion de modulos"""
from tkinter import Tk, Label, Entry, Button, LabelFrame, Checkbutton
import sqlite3

# INICIALIZACION
root = Tk()
root.title("Hola mundo: Todo List")
root.geometry("500x500")

# BASE DE DATOS
# Conexión a la base de datos
db_connection = sqlite3.connect("todo.db")
# Cursor para consultas
db_cursor = db_connection.cursor()

# Consulta inicial: Crear tabla
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    ); 
    """)
# Ejecutar la creación de la tabla
db_connection.commit()


# FUNCIONES
def complete(id):
    """Función para marcar tarea completada segun id
    Currying: retrazar la función para que cree con al parametro command del
    boton
    """
    def _complete():
        todo = db_cursor.execute("""
            SELECT * 
            FROM todo 
            WHERE id = ?
        """, (id, )).fetchone()
        db_cursor.execute("""
            UPDATE todo 
            SET completed = ?
            WHERE id = ?
        """, (not todo[3], id))
        db_connection.commit()
        render_todo()
    return _complete


def del_todo(id):
    """Eliminar tarea
    Currying: retrazar la función para que cree con al parametro command del
    boton
    """
    def _del_todo():
        db_cursor.execute("""
            DELETE FROM todo WHERE id = ?
        """, (id, ))
        db_connection.commit()
        render_todo()
    return _del_todo


def render_todo():
    """Renderizar tarea ingresada"""
    rows = db_cursor.execute("""
        SELECT * 
        FROM todo
    """).fetchall()

    # Eliminar Checkbutton eliminados
    for widget in frame.winfo_children():
        widget.destroy()

    # Añadir Checkbutton y marcar el box
    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = "#555555" if completed else "#FFF"
        cbtn = Checkbutton(frame, text=description, fg=color,
                           width=42, anchor="w", command=complete(id))
        cbtn.grid(row=i, column=0, sticky="w")
        dbtn = Button(frame, text="Eliminar", command=del_todo(id))
        dbtn.grid(row=i, column=1)
        if completed:
            cbtn.select()
        else:
            cbtn.deselect()


def add_todo():
    """Función para agregar tarea"""
    todo = e.get()
    if todo:
        db_cursor.execute("""
            INSERT INTO todo (description, completed)
            VALUES (?, ?) 
            """, (todo, False))
        db_connection.commit()
        e.delete(0, "end")
        render_todo()
    else:
        pass


# UI
l = Label(root, text="Tarea")
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text="Agregar", command=add_todo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text="Mis tareas", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky="nswe", padx=5)

# Foco en campo
e.focus()
# Presionar "Enter" para ejecutar
root.bind("<Return>", lambda x: add_todo())
# Renderizar en consola
render_todo()

# EJECUCION
root.mainloop()
