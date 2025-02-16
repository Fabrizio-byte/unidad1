#main.py
from inventario import Inventario
#from producto import Producto

def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            elif opcion == '2':
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            elif opcion == '3':
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (o Enter para omitir): ")
                precio = input("Nuevo precio (o Enter para omitir): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            elif opcion == '4':
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_producto_por_nombre(nombre)
                if resultados:
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre.")
            elif opcion == '5':
                inventario.mostrar_todos_los_productos()
            elif opcion == '6':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("¡Error! Debe ingresar un número entero para ID y cantidad, y un número decimal para el precio.")

if __name__ == "__main__":
    main()