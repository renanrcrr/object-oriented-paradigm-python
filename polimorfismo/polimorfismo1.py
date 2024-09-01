import math

class Forma:
    def __init__(self):
        print('Construtor da forma')
    
    def area(self):
        print('Area da forma')
    
    def perimetro(self):
        print('Perimetro da forma')

    def descricao(self):
        print('DescriçÃo da forma')

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio
    
q = Quadrado(2) 
print(q.area())
print(q.perimetro())

c = Circulo(10)
print(c.area())
print(c.perimetro())