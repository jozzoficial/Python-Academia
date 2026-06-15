class Matematica:
    PI = 3.14159  # Atributo de classe

    def __init__(self, valor):
        self.valor = valor  # Atributo de instância

    def dobrar(self):
        # Método de instância
        return self.valor * 2

    @classmethod
    def area_circulo(cls, raio):
        # Método de classe
        return cls.PI * (raio ** 2)

    @staticmethod
    def somar(a, b):
        # Método estático
        return a + b


# Uso de métodos de instância
calc = Matematica(10)
print(f"Dobro de 10: {calc.dobrar()}")  # Saída: 20

# Uso de métodos de classe
print(
    f"Área do círculo com raio 5: {Matematica.area_circulo(5):.2f}"
)  # Saída: 78.54

# Uso de métodos estáticos
print(f"Soma de 7 e 3: {Matematica.somar(7, 3)}")  # Saída: 10