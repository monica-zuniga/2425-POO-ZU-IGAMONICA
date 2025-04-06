import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Entrada de nueva tarea
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.focus()

        # Botones
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar Completada", command=self.mark_completed).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), selectbackground="#a0a0ff", activestyle="none")
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.mark_completed())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.task_listbox.get(index)
            if not task.startswith("[✓] "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"[✓] {task}")
        else:
            messagebox.showinfo("Selección", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showinfo("Selección", "Selecciona una tarea para eliminarla.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
