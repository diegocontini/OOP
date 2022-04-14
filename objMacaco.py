class Monke():
    def __init__(self,nome):
        self.nome = nome
        self.bucho = []

    def comer(self,comida):
        self.bucho.append(comida)

    def verbucho(self):
        for i in self.bucho:
            print(i)

m1 = Monke('m1')
m2 = Monke('m2')
m1.comer('Banana')
m2.comer(m1.bucho)
m2.verbucho()