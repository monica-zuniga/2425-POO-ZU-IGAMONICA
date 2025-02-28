#productos de inventario
import json
class Producto:
    """
    Representa un producto en el inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    """
    Administra el inventario de productos utilizando un diccionario.
    """
    def __init__(self):
        self.productos = {}  # Diccionario {id_producto: Producto}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("\n⚠️ Error: El ID ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
            print("\n✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("\n✅ Producto eliminado correctamente.")
        else:
            print("\n⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("\n✅ Producto actualizado correctamente.")
        else:
            print("\n⚠️ Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados if encontrados else None

    def mostrar_productos(self):
        if not self.productos:
            print("\n📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario de productos:")
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, f, indent=4)
        print("\n💾 Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {int(id): Producto(**prod) for id, prod in data.items()}
            print("\n📂 Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("\n⚠️ Archivo no encontrado. Se inicia un inventario vacío.")


def menu():
    """
    Menú interactivo para gestionar el inventario.
    """
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n📦 Gestión de Inventario")
        print("1️⃣ Añadir producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Buscar producto")
        print("5️⃣ Mostrar inventario")
        print("6️⃣ Guardar y salir")

        opcion = input("🔹 Selecciona una opción: ")

        if opcion == "1":
            try:
                id_prod = int(input("🔸 ID: "))
                nombre = input("🔸 Nombre: ")
                cantidad = int(input("🔸 Cantidad: "))
                precio = float(input("🔸 Precio: "))
                inventario.agregar_producto(Producto(id_prod, nombre, cantidad, precio))
            except ValueError:
                print("\n⚠️ Error: Ingresa valores válidos.")

        elif opcion == "2":
            try:
                id_prod = int(input("🔸 ID del producto a eliminar: "))
                inventario.eliminar_producto(id_prod)
            except ValueError:
                print("\n⚠️ Error: Ingresa un ID válido.")

        elif opcion == "3":
            try:
                id_prod = int(input("🔸 ID del producto a actualizar: "))
                cantidad = input("🔹 Nueva cantidad (dejar vacío para no cambiar): ")
                precio = input("🔹 Nuevo precio (dejar vacío para no cambiar): ")
                inventario.actualizar_producto(
                    id_prod,
                    int(cantidad) if cantidad else None,
                    float(precio) if precio else None
                )
            except ValueError:
                print("\n⚠️ Error: Ingresa valores válidos.")

        elif opcion == "4":
            nombre = input("🔸 Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("\n🔍 Productos encontrados:")
                for res in resultados:
                    print(res)
            else:
                print("\n⚠️ Producto no encontrado.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("\n👋 ¡Hasta luego!")
            break

        else:
            print("\n⚠️ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
