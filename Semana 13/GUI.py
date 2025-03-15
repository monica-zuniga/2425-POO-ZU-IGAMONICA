import tkinter as tk

# Función para agregar una tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)  # Agregar tarea a la lista
        entry_tarea.delete(0, tk.END)  # Limpiar el campo de entrada

# Función para eliminar una tarea seleccionada
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        lista_tareas.delete(tarea_seleccionada)  # Eliminar la tarea seleccionada
    except:
        pass  # Si no hay tarea seleccionada, no hacer nada

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# Etiqueta de instrucción
label_instruccion = tk.Label(ventana, text="Ingresa una tarea:")
label_instruccion.pack(pady=10)

# Campo de entrada para agregar tarea
entry_tarea = tk.Entry(ventana, width=40)
entry_tarea.pack(pady=10)

# Botón para agregar tarea
boton_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
