import tkinter as tk

def agregar_dato():
    """Agrega el dato del campo de texto a la lista."""
    dato = entrada_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)  # Limpia el campo de texto

def limpiar_lista():
    """Limpia todos los elementos de la lista."""
    lista_datos.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")

# Componentes de la interfaz
etiqueta_entrada = tk.Label(ventana, text="Ingrese un dato:")
etiqueta_entrada.pack()

entrada_dato = tk.Entry(ventana)
entrada_dato.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack()

lista_datos = tk.Listbox(ventana)
lista_datos.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()