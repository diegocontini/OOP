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
