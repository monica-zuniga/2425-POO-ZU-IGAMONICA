# Programa para calcular el área de un círculo
# Autor: [MONICA ZUÑIGA]
# Este programa solicita al usuario el radio de un círculo, valida la entrada
# y calcula el área del círculo utilizando la fórmula matemática correspondiente.

import math  # Importa la biblioteca matemática


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: float. El radio del círculo ingresado por el usuario.
    :return: float. El área calculada del círculo.
    """
    if radio <= 0:
        return "Error: El radio debe ser un número positivo."

    area = math.pi * radio ** 2  # Fórmula del área
    return area


# Solicitar entrada al usuario
radio_circulo = float(input("Ingrese el radio del círculo: "))

# Validar y calcular
es_valido = radio_circulo > 0  # Booleano para verificar validez

