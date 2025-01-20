class Animal:
    """Clase base que representa a un animal"""

    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación: atributo privado

    def comer(self):
        print(f"{self.__nombre} está comiendo.")

    def dormir(self):
        print(f"{self.__nombre} está durmiendo.")

    def hacer_ruido(self):
        print("¡Sonido genérico de animal!")

class Mamifero(Animal):
    """Clase derivada que representa a un mamífero"""

    def __init__(self, nombre, pelo):
        super().__init__(nombre)
        self.pelo = pelo

    # Sobreescritura del método hacer_ruido
    def hacer_ruido(self):
        print("¡Sonido de mamífero!")

if __name__ == "__main__":
    # Creación de instancias
    leon = Mamifero("Leo", "Dorado")
    perro = Mamifero("Firulais", "Blanco")

    # Uso de métodos
    leon.comer()
    perro.dormir()
    leon.hacer_ruido()  # Polimorfismo: Se llama a la versión sobrescrita
    perro.hacer_ruido()