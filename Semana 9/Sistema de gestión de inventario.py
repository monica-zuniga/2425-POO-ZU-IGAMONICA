# Clase Producto
# arroz,azucar,frejol,leche,pan
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id_producto

    def set_id(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Asegurarse de que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado al inventario.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            for p in self.productos:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("El inventario está vacío.")


# Interfaz de usuario en la consola
def mostrar_menu():
    print("\nMenu de Gestión de Inventarios - Canasta Básica")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")


def menu():
    inventario = Inventario()

    # Ejemplos de productos de la canasta básica
    arroz = Producto("001", "Arroz", 100, 1.20)  # ID, nombre, cantidad, precio por kg
    frijoles = Producto("002", "Frijoles", 50, 0.90)
    azucar = Producto("003", "Azúcar", 80, 1.10)
    leche = Producto("004", "Leche", 200, 0.80)
    pan = Producto("005", "Pan", 150, 0.50)

    # Agregar productos iniciales
    inventario.agregar_producto(arroz)
    inventario.agregar_producto(frijoles)
    inventario.agregar_producto(azucar)
    inventario.agregar_producto(leche)
    inventario.agregar_producto(pan)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()