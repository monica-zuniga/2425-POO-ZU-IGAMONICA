# Ejemplo de programacion Orientada a Objetos (POO)
# Caracteristicas(herencia, encapsulacion,polimorfismo)
#Autor:Zuñiga Monica
# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        # Atributos encapsulados
        self.__nombre = nombre  # Encapsulación del nombre
        self.__edad = edad      # Encapsulación de la edad

    # Métodos públicos para acceder a los atributos encapsulados
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def presentarse(self):
        return f"Hola, me llamo {self.__nombre} y tengo {self.__edad} años."


# Clase derivada: Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.grado = grado

    # Sobrescritura de método (Polimorfismo)
    def presentarse(self):
        return f"Hola, me llamo {self.obtener_nombre()}, tengo {self.obtener_edad()} años y soy estudiante de {self.grado}."


# Clase derivada: Profesor
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.materia = materia

    # Sobrescritura de método (Polimorfismo)
    def presentarse(self):
        return f"Hola, soy el profesor {self.obtener_nombre()} y enseño {self.materia}."


# Instancias de las clases
persona = Persona("Carlos", 40)
estudiante = Estudiante("Ana", 20, "Ingeniería")
profesor = Profesor("Luis", 50, "Matemáticas")

# Demostración de funcionalidades
print(persona.presentarse())         # Uso del método de la clase base
print(estudiante.presentarse())      # Sobrescritura en la clase derivada
print(profesor.presentarse())        # Sobrescritura en la clase derivada
