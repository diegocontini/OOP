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
    


    
    


