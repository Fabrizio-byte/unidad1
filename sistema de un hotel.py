class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print("Habitación reservada.")
        else:
            print("Habitación ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print("Habitación liberada.")
        else:
            print("Habitación ya está libre.")

class Hotel:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def buscar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None

# Crear algunas habitaciones
habitacion1 = Habitacion(101, "Sencilla", 50)
habitacion2 = Habitacion(202, "Doble", 80)

# Crear un hotel y agregar las habitaciones
hotel = Hotel()
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Reservar una habitación
habitacion_buscada = hotel.buscar_habitacion(101)
habitacion_buscada.reservar()