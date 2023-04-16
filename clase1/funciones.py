############################################################
# Calculamos el area de las diferentes figuras geometricas #
############################################################
def area_cuadrado(lado1):
    return lado1*lado1

def area_rectangulo(lado1, lado2):
    return lado1 * lado2

def area_triangulo(base, altura):
    return (base*altura)/2

import math #importamos math module para usar la constante pi
def area_circulo(radio):
    return math.pi * radio * radio

############################################################
#Calculamos perimetro de las diferentes figuras geometricas# (
############################################################


def perimetro_cuadrado(lado1):
    return lado1*4

def perimetro_rectangulos(Lado1, lado2):
    return 2*(Lado1 + lado2)

def perimetro_triangulo(Lado1, lado2, lado3):
    return (Lado1 + lado2 + lado3)

import math #importamos math module para usar la constante pi
def perimetro_circulo(radio):
    return 2* math.pi * radio 

