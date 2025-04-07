import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pendientes")

        self.tasks = []
        self.task_var = tk.StringVar(value=self.tasks)

        self.create_widgets()
        self.bind_shortcuts()

    def create_widgets(self):
        # Campo de entrada para nuevas tareas
        self.new_task_entry = ttk.Entry(self.root, width=40)
        self.new_task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.new_task_entry.focus()

        # Botón para añadir tarea
        add_button = ttk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, listvariable=self.task_var, height=15, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Botones para marcar como completada y eliminar
        self.complete_button = ttk.Button(self.root, text="Marcar como Completada", command=self.mark_complete)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.delete_button = ttk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Configurar el comportamiento de redimensionamiento de la ventana
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

    def bind_shortcuts(self):
        # Atajo para añadir tarea con Enter
        self.new_task_entry.bind("<Return>", lambda event: self.add_task())

        # Atajos para marcar como completada y eliminar
        self.root.bind("c", lambda event: self.mark_complete())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("d", lambda event: self.delete_task())

        # Atajo para cerrar la aplicación con Escape
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def add_task(self):
        new_task = self.new_task_entry.get().strip()
        if new_task:
            self.tasks.append({"text": new_task, "completed": False})
            self.update_task_list()
            self.new_task_entry.delete(0, tk.END)

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = not self.tasks[index]["completed"]
                self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar esta tarea?"):
                del self.tasks[index]
                self.update_task_list()

    def update_task_list(self):
        self.task_var.set(["[✓] " + task["text"] if task["completed"] else "[ ] " + task["text"] for task in self.tasks])
        # Actualizar la selección para que no quede una tarea previamente seleccionada
        if self.tasks:
            self.task_listbox.selection_clear(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()