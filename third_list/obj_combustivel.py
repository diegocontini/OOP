class bomba_combustivel():
    def __init__(self,valor_litro,quantidade_disponivel):
        self.__valor_litro = valor_litro
        self.__quantidade_disponivel = quantidade_disponivel

    #Encapsulamento do valor litro
    @property
    def valor_litro(self):
        return self.__valor_litro
    @valor_litro.setter
    def valor_litro(self,novo_valor):
        raise ValueError('Utilize o método abastecer_por_valor, ou abastecer_por_litro')
    
    #Encapsulamento da quantidade disponível
    @property
    def quantidade_disponivel(self):
        return self.__quantidade_disponivel
    @quantidade_disponivel.setter
    def quantidade_disponivel(self,nova_quantidade):
        raise ValueError('Utilize o método ...')

    #Métodos de abastecimento
    def abastecer_por_valor(self):
        valor_abastecido = int(input('Digite o valor que deseja abastecer, em R$:\n'))
        quantidade_abastecida = valor_abastecido / self.valor_litro
        if quantidade_abastecida <= self.quantidade_disponivel:
            print(f'Seu veículo foi abastecido em {quantidade_abastecida} litros')
            self.__quantidade_disponivel -= quantidade_abastecida
            print(f'Saldo atualizado na bomba: {self.quantidade_disponivel} litros')
        else:
            print('A quantidade de combustível disponível na bomba não é suficiente.')
    def abastecer_por_litro(self):
        quantidade_abastecida = int(input('Digite o valor que deseja abastecer, em litors:\n'))
        if quantidade_abastecida <= self.quantidade_disponivel:
            print(f'Seu veículo foi abastecido em {quantidade_abastecida} litros')
            self.__quantidade_disponivel -= quantidade_abastecida
            print(f'Saldo atualizado na bomba: {self.quantidade_disponivel} litros')
        else:
            print('A quantidade de combustível disponível na bomba não é suficiente.')

class combustivel_gasolina(bomba_combustivel):
    def __init__(self, valor_litro, quantidade_disponivel,):
        super().__init__(valor_litro, quantidade_disponivel)
        self.tipo_combustivel = 'Gasolina'
class combustivel_etanol(bomba_combustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
        self.tipo_combustivel = 'Etanol'

  








    
        