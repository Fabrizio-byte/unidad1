class MiClase:
    def __init__(self, nombre, valor):
        print(f"Constructor llamado para {nombre}")
        self.nombre = nombre
        self.valor = valor

    def __del__(self):
        print(f"Destructor llamado para {self.nombre}")
        # Aquí podrías realizar tareas de limpieza, como cerrar archivos o liberar recursos

# Ejemplo de uso
objeto1 = MiClase("Objeto 1", 10)
objeto2 = MiClase("Objeto 2", 20)

print(f"{objeto1.nombre}: {objeto1.valor}")
print(f"{objeto2.nombre}: {objeto2.valor}")

del objeto1  # Fuerza la llamada al destructor para objeto1