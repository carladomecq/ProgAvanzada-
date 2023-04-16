import math

class FiguraGeometrica:
    def calcular_perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_perimetro(self):
        return self.lado*4
    
class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
circulo = Circulo(50)
print(circulo.calcular_perimetro()) # imprime 314.1592653589793

rectangulo = Rectangulo(8, 10)
print(rectangulo.calcular_perimetro()) # imprime 36

cuadrado = Cuadrado(6)
print(cuadrado.calcular_perimetro()) # imprime 24

triangulo = Triangulo(2, 5, 7)
print(triangulo.calcular_perimetro()) # imprime 14