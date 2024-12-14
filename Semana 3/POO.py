# Programación Orientada a Objetos (POO)
# Ejemplo: De temperaturas diarias

class ClimaSemanal:
    def __init__(self, temperaturas=None):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = temperaturas if temperaturas else []

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para mostrar las temperaturas
    def mostrar_temperaturas(self):
        for dia, temp in zip(self.dias, self.temperaturas):
            print(f"{dia}: {temp}°C")

# Programa principal
def main():
    print("Programa para calcular el promedio semanal del clima (POO).")
    temperaturas = [23.5, 24.8, 22.1, 25.3, 24.0, 23.7, 22.9]  # Valores reales
    clima = ClimaSemanal(temperaturas)
    clima.mostrar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
