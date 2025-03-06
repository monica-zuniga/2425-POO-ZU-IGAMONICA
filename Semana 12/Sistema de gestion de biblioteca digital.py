# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = tuple(autor)  # Usamos tupla para autor, ya que no cambia
        self.categoria = categoria
        self.isbn = isbn

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista de libros prestados

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros (ISBN -> libro)
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.usuarios:
            self.usuarios.add(usuario.usuario_id)
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")
            return True
        print(f"El usuario con ID '{usuario.usuario_id}' ya está registrado.")
        return False

    def dar_baja_usuario(self, usuario):
        if usuario.usuario_id in self.usuarios:
            self.usuarios.remove(usuario.usuario_id)
            print(f"Usuario '{usuario.nombre}' eliminado de la biblioteca.")
            return True
        print(f"El usuario con ID '{usuario.usuario_id}' no existe.")
        return False

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros and usuario.usuario_id in self.usuarios:
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            return True
        print("No se puede prestar el libro, asegúrate de que el libro exista y el usuario esté registrado.")
        return False

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.añadir_libro(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return True
        print(f"El libro con ISBN '{isbn}' no está en los libros prestados de {usuario.nombre}.")
        return False

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo.lower() in libro.titulo.lower()) or \
               (autor and any(a.lower() in autor.lower() for a in libro.autor)) or \
               (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados


# Ejemplo de uso:

# Crear libros
libro1 = Libro("Cien Años de Soledad", ["Gabriel García Márquez"], "Ficción", "978-3-16-148410-0")
libro2 = Libro("El Principito", ["Antoine de Saint-Exupéry"], "Infantil", "978-3-16-148411-7")
libro3 = Libro("1984", ["George Orwell"], "Distopía", "978-3-16-148412-4")

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "usuario_123")
usuario2 = Usuario("Ana Gómez", "usuario_456")

# Crear la biblioteca
biblioteca = Biblioteca()

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Prestar un libro
biblioteca.prestar_libro(usuario1, "978-3-16-148410-0")

# Buscar libros
libros_encontrados = biblioteca.buscar_libro(titulo="1984")
print("\nLibros encontrados con '1984':")
for libro in libros_encontrados:
    print(f"Titulo: {libro.titulo}, Autor: {', '.join(libro.autor)}, Categoría: {libro.categoria}")

# Listar libros prestados por un usuario
print("\nLibros prestados a Juan Pérez:")
for libro in biblioteca.listar_libros_prestados(usuario1):
    print(f"Titulo: {libro.titulo}, Autor: {', '.join(libro.autor)}")

# Devolver un libro
biblioteca.devolver_libro(usuario1, "978-3-16-148410-0")

# Eliminar un libro
biblioteca.quitar_libro("978-3-16-148411-7")

# Dar baja un usuario
biblioteca.dar_baja_usuario(usuario2)
