class cco():
    def __init__(self,nConta,titular,saldo):
        self.conta = nConta
        self.titular = titular
        self.saldo = saldo
    
    def alterarTitular(self):
        self.titular = input('Insira o nome do novo titular: ')

    def deposito(self):
        self.saldo += float(input('Digite o valor depositado: '))
    def saque(self):
        self.saldo -= float(input('Digte o valor sacado: '))
       
cco1 = cco(1,'Diego',0)
cco1.alterarTitular()
cco1.deposito()
cco1.saque()


       