class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        """
        Constructor de la clase Libro.
        Inicializa los atributos del libro y simula la apertura de un archivo de registro.
        """
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

        # Simulamos que se crea un registro del libro en un archivo.
        self.archivo_registro = open("registro_libros.txt", "a")
        self.archivo_registro.write(
            f"Libro añadido: {self.titulo} de {self.autor}, publicado en {self.año_publicacion}\n")
        print(f"Se ha añadido el libro: {self.titulo} por {self.autor}, publicado en {self.año_publicacion}.")

    def mostrar_info(self):
        """
        Muestra la información del libro.
        """
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")

    def __del__(self):
        """
        Destructor de la clase Libro.
        Cierra el archivo de registro cuando el objeto es destruido.
        """
        if hasattr(self, 'archivo_registro') and self.archivo_registro:
            self.archivo_registro.close()
            print(f"Se ha cerrado el registro del libro: {self.titulo}.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear objetos de la clase Libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("1984", "George Orwell", 1949)

    # Mostrar la información de los libros
    libro1.mostrar_info()
    libro2.mostrar_info()

    # El destructor (__del__) se activará cuando los objetos sean eliminados o al finalizar el programa
    del libro1
    del libro2
