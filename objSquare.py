class square():
    def __init__(self,lado,cor,material,temperatura):
        self.lado = lado
        self.cor = cor
        self.material = material
        self.temperatura = temperatura
    #Metodo para alterar o valor do lado do quadrado.
    def valorLado(self,dataInput):
        self.lado = dataInput
    #Metodo para visualizar o valor do lado do quadrado
    def verLado (self):
        print(self.lado)
    #Metodo para calcular a area do quadrado.
    def calcArea(self):
        area = self.lado * self.lado
        #print(area)
    #Metodo para trocar o material do quadrado
    def trocarMaterial(self,newMaterial):
        self.material = newMaterial
        #print(self.material)
    #Metodo para verificar o estado do quadrado
    def quenteFrio(self):
        if self.temperatura >= 25:
            print('O quadrado está quente.')
        elif self.temperatura < 25 and self.temperatura >= 12:
            print('O quadrado está ameno.')
        elif self.temperatura < 12 and self.temperatura >= -13:
            print('O quadrado está frio')
        else:
            print('O quadrado está congelado.')
    #Metodo para aumentar ou diminuir a temperatura do quadrado.
    def esquentarEsfriar(self):
        print(f'A temperatura atual do quadrado é: {self.temperatura}\nDigite ''+'' para aumentar, ou ''-'' para diminuir, a temperatura em 5 pontos.')
        validador = str(input())
        if validador == '+':
            self.temperatura += 5
        elif validador == '-':
            self.temperatura -= 5
        else:      
             raise Exception('O valor inserido não é um valor válido.')

square1 = square(10,'Amarelo','Estanho',-14)
square1.valorLado(23)
square1.verLado()
square1.calcArea()
square1.trocarMaterial('Pedra')
square1.esquentarEsfriar()
square1.quenteFrio()


        