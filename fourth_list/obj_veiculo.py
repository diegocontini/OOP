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