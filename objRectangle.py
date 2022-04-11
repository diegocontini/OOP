class rectangle():
    def __init__(self,base,altura,proprietario,lote, quantidade): 
        self.base = base
        self.altura = altura
        self.proprietario = proprietario
        self.lote = lote
        self.quantidade = quantidade

    #Metodo para mudar o valor dos lados
    def alterarBaseAltura(self,):
        print(f'O valor atual da base é: {self.base}\nO valor atual da altura é: {self.altura} ')
        nBase = int(input('Digite um novo valor inteiro para a base: '))
        nAltura = int(input('Digite um novo valor inteiro para a altura: '))
        self.base = nBase
        self.altura = nAltura 

    #Metodo para retornar o valor dos lados
    def verBaseAltura(self):
        print(f'O valor atual da base é: {self.base}\nO valor atual da altura é: {self.altura}')
    
    #Metodo para calcular a área
    def areaRectangle(self):
        rectangleArea = self.base * self.altura
        #print(f'A área do retângulo é: {rectangleArea}.')

    #Metodo para calcular o perímetro
    def perimetroRectangle(self):
        rectanglePerimetro = 2 * (self.base + self.altura)
        #print(f'O perímetro do retângulo é: {rectanglePerimetro}')

    #Metodo para trocar o proprietário
    def alterarProprietario(self):
        newProprietario = str(input('Digite a razão social do novo proprietário do retângulo: '))
        self.proprietario =  newProprietario
        print(f'A posse do retângulo passou para {self.proprietario}')

    #Metodo para atualizar o estoque do produto
    def contagemEstoque(self):
        saldoEstoque = int(input('Você iniciou a contagem de estoque do produto, digite o novo valor em estoque do item:\n'))
        self.quantidade = saldoEstoque
        print(f'O estoque atual do produto é: {self.quantidade}')


rectangle1 = rectangle(10,20,'Diego','2022/0001',25)
rectangle1.areaRectangle()
rectangle1.alterarBaseAltura()
rectangle1.perimetroRectangle()
rectangle1.alterarProprietario()
rectangle1.contagemEstoque()



        
