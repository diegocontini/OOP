#ObjAnimal
class Animal():
    def init(self,nome,peso,cor) -> None:
        self.nome = nome
        self.peso = peso
        self.cor = cor

    def Comer(self):
        alimento = str(input(f'Insira o alimento que o {self.__class__.__name__} comerá:\n'))
        print(f'{self.nome} está comendo {alimento}, e sua subclasse é {self.__class__.__name__}')

class Gato(Animal):
    def __init__(self,nome,peso,cor,sexo,patas):
        super().init(nome,peso,cor)
        self.sexo = sexo
        self.patas = patas

class Coelho(Animal):
    def __init__(self,nome,peso,cor,raca,comidaFavorita) -> None:
        super().init(nome,peso,cor)
        self.raca = raca
        self.comidaFavorita = comidaFavorita

class Cachorro(Animal):
    def __init__(self,nome,peso,cor,corOlhos,idade) -> None:
        super().init(nome,peso,cor)
        self.corOlhos = corOlhos
        self.idade = idade







