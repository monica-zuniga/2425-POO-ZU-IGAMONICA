#tarea semana 15
import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Crear un campo de entrada (Entry) para escribir nueva tarea
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Crear un Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Crear botones para añadir, eliminar y marcar como completada la tarea
        self.add_button = tk.Button(self.root, text="Añadir tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.root, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(self.root, text="Marcar como completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Vincular el evento de presionar Enter para añadir tarea
        self.root.bind("<Return>", self.add_task_event)

        # Manejo de evento doble clic en tarea para marcarla como completada
        self.task_listbox.bind("<Double-1>", self.complete_task_double_click)

    def add_task(self, event=None):
        task = self.entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea antes de añadirla.")

    def add_task_event(self, event):
        self.add_task()  # Llamar a la función add_task cuando presionamos Enter

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Obtener la tarea seleccionada
            self.task_listbox.delete(selected_task_index)  # Eliminar tarea seleccionada
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Obtener la tarea seleccionada
            task = self.task_listbox.get(selected_task_index)  # Obtener el nombre de la tarea
            # Marcar la tarea como completada (Añadir un '✔' al inicio)
            completed_task = "✔ " + task
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)  # Actualizar la tarea
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def complete_task_double_click(self, event):
        try:
            selected_task_index = self.task_listbox.nearest(event.y)  # Obtener la tarea seleccionada por doble clic
            task = self.task_listbox.get(selected_task_index)  # Obtener el nombre de la tarea
            completed_task = "✔ " + task
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)  # Actualizar la tarea
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")


# Crear la ventana principal
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
