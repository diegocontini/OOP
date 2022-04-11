#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class humano():
    def __init__(self,nome,idade,peso,altura,corOlhos,corPele):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.corOlhos = corOlhos
        self.corPele = corPele

    def humanoEnvelhecer(self):
        newAge = int(input('Digite quantos anos está pessoa envelhecerá: '))

human1 = humano('Diego',19,80,172,'Azul','Branco')
human1.humanoEnvelhecer()    