'''
    7)	Classe Retangulo: Crie uma classe que modele um retangulo: 
    a.	Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher) 
    b.	Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro; 
    c.	Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
         Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. 
'''
class Retangulo:
    def __init__ (self,ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mudarLados(self,ladoA, ladoB):
        if ladoA > 0:
            self.ladoA = ladoA
        if ladoB > 0:
            self.ladoB = ladoB
    def retornarLados (self):
        return (self.ladoA,self.ladoB)
    def calcularArea (self):
        return self.ladoA*self.ladoB
    def calcularPerimetro (self):
        return (self.ladoA*2)+(self.ladoB*2)
lado1 = int(input("informe o lado A:"))
lado2 = int(input("informe o lado B:"))
R1 = Retangulo(lado1,lado2)
area = R1.calcularArea()
print "A qtde de azuleijos e: " + str(area/2)