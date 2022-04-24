class aluno():
    def __init__(self,nome,sobrenome,cpf,):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.__primeiroSemestreNota = 0
        self.__segundoSemestreNota = 0
        self.__finalMedia = 0

    #Encapsulamento notas do primeiro semestre 
    @property
    def primeiroSemestreNota(self):
        return self.__primeiroSemestreNota
    @primeiroSemestreNota.setter
    def primeiroSemestreNota(self,novaNota):
        raise ValueError('Utilize o método primeiroSemestreNotaEntrada') 
    
    #Encapsulamento notas do segundo semestre
    @property 
    def segundoSemestreNota(self):
        return self.__segundoSemestreNota
    @segundoSemestreNota.setter
    def segundoSemestreNota(self,novaNota):
        raise ValueError('Utilize o método segundoSemestreNotaEntrada')
    
    #Encapsulamento media final
    @property
    def finalMedia(self):
        return self.__finalMedia
    @finalMedia.setter
    def finalMedia(self,novaMedia):
        raise ValueError('Utilize o método calcularMedia')

    #Input da nota do primeiro semestre
    def primeiroSemestreNotaEntrada(self):
        self.__primeiroSemestreNota = float(input('Digite a nota do primeiro semestre:\n'))

    #Input da nota do segundo semestre
    def segundoSemestreNotaEntrada(self):
        self.__segundoSemestreNota = float(input('Digite a nota do segundo semestre:\n'))
    
    #Calculo da media final
    def calcularMedia(self):
        self.__finalMedia =  (self.primeiroSemestreNota + self.segundoSemestreNota) / 2 
        print(f'A media final do aluno {self.nome} é {self.finalMedia}')
    


  
            
        


        

