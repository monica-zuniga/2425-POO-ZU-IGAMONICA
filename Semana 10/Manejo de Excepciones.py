import os

# Clase Producto
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

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo"""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as file:
                    for line in file:
                        id_producto, nombre, cantidad, precio = line.strip().split(',')
                        self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
                print("Inventario cargado exitosamente desde el archivo.")
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
        else:
            print("No se encontró el archivo de inventario. Se creará uno nuevo.")
            self.crear_archivo()

    def guardar_inventario(self):
        """Guarda los cambios del inventario en un archivo"""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos suficientes para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Añade un producto al inventario y lo guarda en el archivo"""
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado al inventario.")
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID y guarda los cambios en el archivo"""
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado.")
                self.guardar_inventario()
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto por ID y guarda los cambios"""
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado.")
                self.guardar_inventario()
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre"""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario"""
        if self.productos:
            for p in self.productos:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("El inventario está vacío.")

    def crear_archivo(self):
        """Crea un archivo vacío de inventario si no existe"""
        try:
            with open(self.archivo, "w") as file:
                print("Archivo de inventario creado.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

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
    inventario = Inventario("inventario.txt")

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
