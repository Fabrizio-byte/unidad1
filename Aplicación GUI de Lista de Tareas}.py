import tkinter as tk
from tkinter import ttk, messagebox

class GestorDeTareas:
    def __init__(self, master):
        """
        Inicializa la aplicación del gestor de tareas.

        Args:
            master: El widget maestro (ventana principal).
        """
        self.master = master
        self.master.title("Gestor de Tareas")

        self.tareas = []

        # Componentes de la interfaz
        self.etiqueta_nueva_tarea = ttk.Label(master, text="Nueva Tarea:")
        self.etiqueta_nueva_tarea.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entrada_tarea = ttk.Entry(master)
        self.entrada_tarea.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.entrada_tarea.bind("<Return>", self.agregar_tarea_enter) # Enlazar Enter a la adición

        self.boton_agregar = ttk.Button(master, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=2, padx=5, pady=5)

        self.lista_tareas = tk.Listbox(master, selectmode=tk.SINGLE)
        self.lista_tareas.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.lista_tareas.bind("<Double-Button-1>", self.marcar_completada_doble_click) # Opcional: doble clic para completar

        self.boton_completar = ttk.Button(master, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.boton_eliminar = ttk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # Configurar pesos de las filas y columnas para que la lista se expanda
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(1, weight=1)

        self.actualizar_lista()

    def agregar_tarea(self):
        """
        Añade una nueva tarea a la lista.
        """
        nueva_tarea = self.entrada_tarea.get().strip()
        if nueva_tarea:
            self.tareas.append({"texto": nueva_tarea, "completada": False})
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def agregar_tarea_enter(self, event):
        """
        Añade una nueva tarea cuando se presiona la tecla Enter en el campo de entrada.

        Args:
            event: El evento de teclado.
        """
        self.agregar_tarea()

    def marcar_completada(self):
        """
        Marca la tarea seleccionada como completada.
        """
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            self.tareas[indice_seleccionado]["completada"] = not self.tareas[indice_seleccionado]["completada"]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def marcar_completada_doble_click(self, event):
        """
        Opcional: Marca la tarea con doble clic como completada.

        Args:
            event: El evento del doble clic del ratón.
        """
        self.marcar_completada()

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista.
        """
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            tarea_a_eliminar = self.tareas[indice_seleccionado]["texto"]
            if messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar la tarea: '{tarea_a_eliminar}'?"):
                del self.tareas[indice_seleccionado]
                self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        """
        Actualiza el contenido del Listbox con las tareas actuales.
        Las tareas completadas se muestran con un prefijo "[Completada]".
        """
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[Completada] " if tarea["completada"] else ""
            self.lista_tareas.insert(tk.END, estado + tarea["texto"])
            if tarea["completada"]:
                self.lista_tareas.itemconfig(tk.END, fg="gray", selectbackground="lightgray")
            else:
                self.lista_tareas.itemconfig(tk.END, fg="black", selectbackground="lightblue")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorDeTareas(root)
    root.mainloop()