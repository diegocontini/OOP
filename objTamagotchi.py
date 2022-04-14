def validaHp(self):
    if self.saude > 100:
        self.saude = 100


class Bixo():
    def __init__(self,nome,idade):
        self.nome = nome
        self.fome = 10
        self.saude = 20
        self.idade = idade
    
    def changeName(self):
        self.nome = str(input('Digite o novo nome do seu Tamagotchi: '))

    def changeHunger(self):
        print('Cada alimento possuirá um valor nutricional único.\nAlimentos disponíveis:\n1- Morango(5pts)\n2- Chocolate(10pts)\n3- Ração(15pts)\n4- Água Sanitária(-25pts)')
        idFood = int(input('Digite o código do alimento que deseja fornecer para seu pet:\n'))
        if idFood == 1:
            self.fome += 5
            if self.saude < 20:
                self.saude += 2
        elif idFood == 2:
            self.fome += 10
            if self.saude < 100:
                self.saude += 5
        elif idFood == 3:
            self.fome += 15
            if self.saude < 100:
                self.saude += 8
        elif idFood == 4:
            self.fome -= 25
            self.saude -= 11
        else:
            raise Exception('Alimento não encontrado.')
        validaHp(self)

    def changeHp(self):
        if self.idade > 70:
            self.saude -=20
        if self.fome < 0:
            self.saude = 0
        if self.fome > 50:
            self.saude += 25
        if self.saude == 0:
            print('Seu pet morreu.')
    
    def cMood(self):
        nMood = 0
        if self.saude <= 10 and self.fome <= 10:
            c = 'Triste'
        elif self.saude >= 10 and self.saude <= 60 and self.fome >= 10 and self.fome <= 20:
            c = 'Neutro'
        else:
            c = 'Feliz'
        return (c)
        
pet1 = Bixo('Sushi',1)
pet1.changeHunger()
print(pet1.cMood())
