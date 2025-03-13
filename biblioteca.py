class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN: Libro
        self.usuarios = set()  # IDs de usuarios únicos
        self.usuarios_data = {} # id_usuario: Usuario

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_data[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}.")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_data[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios_data[id_usuario]
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print("El libro ya está prestado a este usuario.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios_data[id_usuario]
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print("El libro no está prestado a este usuario.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios_data[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []


# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9780061120084")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "9780451524935")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Novela", "9780156012195")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

usuario1 = Usuario("Alice", "U001")
usuario2 = Usuario("Bob", "U002")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("U001", "9780061120084")
biblioteca.prestar_libro("U002", "9780451524935")

print("\nLibros prestados a Alice:")
for libro in biblioteca.listar_libros_prestados("U001"):
    print(libro)

print("\nLibros prestados a Bob:")
for libro in biblioteca.listar_libros_prestados("U002"):
    print(libro)

biblioteca.devolver_libro("U001", "9780061120084")

print("\nLibros prestados a Alice después de la devolución:")
for libro in biblioteca.listar_libros_prestados("U001"):
    print(libro)

print("\nBúsqueda de libros por autor (George Orwell):")
for libro in biblioteca.buscar_libros("autor", "George Orwell"):
    print(libro)