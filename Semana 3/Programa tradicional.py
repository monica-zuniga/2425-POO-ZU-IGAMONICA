# Programación Tradicional
# Ejemplo: De la temperaturas diarias
# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


# Programa principal
def main():
    print("Programa para calcular el promedio semanal del clima (Programación Tradicional).")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = [23.5, 24.8, 22.1, 25.3, 24.0, 23.7, 22.9]  # Valores reales
    promedio = calcular_promedio(temperaturas)

    # Mostrar las temperaturas por día
    for dia, temp in zip(dias, temperaturas):
        print(f"{dia}: {temp}°C")

    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


# Ejecutar el programa
if __name__ == "__main__":
    main()
