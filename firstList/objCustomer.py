class humano():
    def __init__(self,nome,idade,peso,altura,corOlhos,corPele):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.corOlhos = corOlhos
        self.corPele = corPele

    def humanoEnvelhecer(self):
        newAge = self.idade + int(input('Digite quantos anos está pessoa envelhecerá: '))
        if self.idade < 21:
            while self.idade < 21 and self.idade < newAge:
                self.idade += 1
                self.altura += 5
        else:
            self.idade = newAge
    
    def humanoEngodar(self):
        self.peso += float(input('Digite quanto de peso essa pessoa ganhou: '))
    
    def humanoEmagrecer(self):
        self.peso -= float(input('Digite quantos KGs essa essa pessoa perdeu: '))

    def humanoCrescer(self):
        self.altura += int(input('Digite quantos centímetros essa pessoa cresceu: '))
        

human1 = humano('Diego',19,80,170,'Azul','Branco')
human1.humanoEnvelhecer()
human1.humanoEngodar()
human1.humanoEmagrecer()
human1.humanoCrescer()    