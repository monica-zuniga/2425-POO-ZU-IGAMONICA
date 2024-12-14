#Ejemplo del Mundo Real

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad disponible: {self.cantidad}")

    def actualizar_cantidad(self, cantidad_vendida):
        self.cantidad -= cantidad_vendida
        print(f"Cantidad restante de {self.nombre}: {self.cantidad}")


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        print(f"Inventario de la tienda {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad:
                    producto.actualizar_cantidad(cantidad)
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print(f"No hay suficiente stock de {nombre_producto}.")
                return
        print(f"Producto {nombre_producto} no encontrado en el inventario.")

# Crear objetos y simular interacciones
producto1 = Producto("Camiseta", 15, 100)
producto2 = Producto("Pantalón", 25, 50)

tienda = Tienda("Tienda de Ropa")
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_inventario()

# Vender productos
tienda.vender_producto("Camiseta", 20)
tienda.vender_producto("Pantalón", 60)

tienda.mostrar_inventario()
