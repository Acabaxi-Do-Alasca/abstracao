class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

retangulo = Retangulo(10, 3)
print(f"A área é: {retangulo.calcular_area()}")