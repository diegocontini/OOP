#Exemplo 1
class animal():
    def __init__(self,nome):
        self.nome = nome

    def locomover():
        pass

class humano(animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def locomover(self):
        print('O ser humano anda')

class passaro(animal):
    def __init__(self, nome):
        super().__init__(nome)

    def locomover(self):
        print('O pássaro voa')

class penguin(passaro):
    def __init__(self, nome):
        super().__init__(nome)
    
    def locomover(self):
        print('O penguin nada e voa')

p1 = penguin('pingu')
p1.locomover()

#Exemplo 2
class veiculo():
    def __init__(self,modelo):
        self.modelo = modelo

    def locomocao(self):
        pass

class aviao(veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)
    
    def locomocao(self):
        print('O avião possui asas')

class carro(veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)
    def locomocao(self):
        print('O carro possui rodas')

c1 = carro('Nissian Skyline')
c1.locomocao()

#Exemplo 3

class poema():
    def __init__(self,tipo_poema) -> None:
        self.tipo_poema = tipo_poema

    def caracteristicas_poema(self):
        print('o poema é um arranjo de palavras que contêm significado. Por meio dele são expressos os pensamentos e sentimentos do autor.')

class soneto(poema):
    def __init__(self, tipo_poema) -> None:
        super().__init__(tipo_poema)

    def caracteristicas_poema(self):
        print('É um tipo de poema que possui uma estrutura fixa. Ele contém quatro estrofes com 14 versos,sendo que dois deles são quartetos, estrofes com quatro versos cada, e dois são tercetos, estrofes com três versos. Geralmente, os versos são decassílabos, ou seja, possuem dez sílabas poéticas.')

class poema_epico(poema):
    def __init__(self, tipo_poema) -> None:
        super().__init__(tipo_poema)
    
    def caracteristicas_poema(self):
        print('Está centrado em figuras míticas ou heroicas, por exemplo, as fábulas')
    
p1 = poema_epico('teste')   
p1.caracteristicas_poema() 

#Exemplo 4

class astros():
    def __init__(self,nome):
        self.nome = nome
    
    def luz_propia(self):
        pass

class planeta(astros):
    def __init__(self, nome):
        super().__init__(nome)
    
    def luz_propia(self):
        print(f'O planeta {self.nome} não possui luz própria')
    
class estrela(astros):
    def __init__(self, nome):
        super().__init__(nome)

    def luz_propia(self):
        print(f'A estrela {self.nome} possui luz própria')

a1 = planeta('terra')
a1.luz_propia()
a2 = estrela('sol')
a2.luz_propia()

#Exemplo 5
class pessoa():
    def __init__(self,nome):
        self.nome = nome
    
    def vender(self):
        pass

class cliente(pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    
    def vender(self):
        valor_venda = float(input('Digite o total da venda: '))
        print(f'O total da venda é:{valor_venda}')

class cliente_bonificado(pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    
    def vender(self):
        valor_venda = float(input('Digite o total da venda:\n'))
        valor_desconto = float(input('Digite a ''%'' de desconto que deseja aplicar:\n'))
        total_desconto = valor_venda * (valor_desconto/100)
        total_venda = valor_venda - total_desconto
        print(f'O valor da venda foi {valor_venda}\nO total de desconto foi {total_desconto}\nO total da venda com desconto foi de {total_venda}')
    
p1 = cliente_bonificado('Diego')
p1.vender()
    


    
    





