class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"

    def __repr__(self):
        return f"Ponto(x={self.x}, y={self.y})"

    def __add__(self, outro):
        if isinstance(outro, Ponto):
            return Ponto(self.x + outro.x, self.y + outro.y)

        raise TypeError("Só pode somar Ponto com outro Ponto")

    def __len__(self):
        # Distância da origem (simplificado)
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __call__(self, escala):
        return Ponto(self.x * escala, self.y * escala)


# Exemplo de uso
p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

print(f"Representação str: {p1}")
# Saída: Ponto(1, 2)

print(f"Representação repr: {repr(p1)}")
# Saída: Ponto(x=1, y=2)

p3 = p1 + p2
print(f"Soma de pontos: {p3}")
# Saída: Ponto(4, 6)

print(f"Comprimento do ponto p1: {len(p1)}")
# Saída: 2 (sqrt(1² + 2²) = sqrt(5) ≈ 2)

p4 = p1(10)  # Chama a instância como função
print(f"Ponto p1 escalado por 10: {p4}")
# Saída: Ponto(10, 20)