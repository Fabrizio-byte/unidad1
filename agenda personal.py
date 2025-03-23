import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la visualización de eventos
        self.eventos_frame = ttk.Frame(root, padding="10")
        self.eventos_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.eventos_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para la entrada de datos
        self.entrada_frame = ttk.Frame(root, padding="10")
        self.entrada_frame.pack(fill=tk.X)

        ttk.Label(self.entrada_frame, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W)
        self.fecha_entry = ttk.Entry(self.entrada_frame)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.entrada_frame, text="Hora (HH:MM):").grid(row=1, column=0, sticky=tk.W)
        self.hora_entry = ttk.Entry(self.entrada_frame)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.entrada_frame, text="Descripción:").grid(row=2, column=0, sticky=tk.W)
        self.descripcion_entry = ttk.Entry(self.entrada_frame)
        self.descripcion_entry.grid(row=2, column=1)

        # Frame para los botones
        self.botones_frame = ttk.Frame(root, padding="10")
        self.botones_frame.pack(fill=tk.X)

        ttk.Button(self.botones_frame, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0)
        ttk.Button(self.botones_frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1)
        ttk.Button(self.botones_frame, text="Salir", command=root.quit).grid(row=0, column=2)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            datetime.datetime.strptime(hora, "%H:%M")
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Selecciona un evento para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            self.tree.delete(seleccion)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()