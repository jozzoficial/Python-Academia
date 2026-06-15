class Pato:
    def falar(self):
        print("Quack!")


class Cachorro:
    def falar(self):
        print("Au Au!")


class Pessoa:
    def falar(self):
        print("Olá!")


def fazer_falar(animal):
    animal.falar()


print("\n--- Polimorfismo ---")

fazer_falar(Pato())
fazer_falar(Cachorro())
fazer_falar(Pessoa())


# Polimorfismo com herança e sobrescrita de métodos

class Forma:
    def area(self):
        raise NotImplementedError(
            "Subclasses devem implementar este método"
        )


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * (self.raio ** 2)


formas = [
    Retangulo(10, 5),
    Circulo(7)
]

for forma in formas:
    print(f"Área da forma: {forma.area():.2f}")