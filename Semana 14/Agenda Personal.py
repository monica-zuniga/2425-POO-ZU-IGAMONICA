#agenda personal
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Crear el frame superior para la lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10)

        # Crear el TreeView para mostrar los eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Crear el frame para la entrada de datos
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10)

        # Campos de entrada
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear el frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botones de acción
        tk.Button(frame_botones, text="Agendar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Salir", command=self.root.quit).grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        """ Agrega un evento a la lista """
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def eliminar_evento(self):
        """ Elimina el evento seleccionado """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
