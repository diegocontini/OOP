'''
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
'''
class rectangle():
    def __init__(self,base,altura,proprietario,serialNumber,lote):
        self.base = base
        self.altura = altura
        self.proprietario = proprietario
        self.serialNumber = serialNumber
        self.lote = lote
    def alterarBaseAltura(self,):
        print(f'O valor atual da base é {self.base}\nO valor atual da altura é: {self.altura} ')
        nBase = int(input('Digite um novo valor inteiro para a base: '))
        nAltura = int(input('Digite um novo valor inteiro para a altura: '))
        self.base = nBase
        self.altura = nAltura 
        print(self.base,self.altura)

rectangle1 = rectangle(10,20,'Diego','2022/0001','2022/04/09',)
rectangle1.alterarBaseAltura()       
        
