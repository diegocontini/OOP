#ObjFuncionarioGerente
#Classe 
class Funcionario():
    def __init__(self,nome,CPF,salario,departamento) -> None:
        self.nome = nome
        self.CPF = CPF
        self.salario = salario
        self.departamento = departamento

    #Metodo de bonificação do funcionário
    def Bonificar(self):
        self.salario += self.salario * 0.1


 #Sub Classe Gerente   
class Gerente(Funcionario):
    def __init__(self,nome,CPF,salario,departamento,senha,subordinados):
        Funcionario.__init__(self,nome,CPF,salario,departamento)
        self.senha = senha
        self.subordinados = subordinados
    
    #Verificar Senha
    def autenticarSenha(self):
        senhaInput = str(input('Para liberar o crédito, digite a senha de gerente:\n'))
        if self.senha == senhaInput:
            print('Crédito liberado')
        else:
            print('Liberação não realizada, retorne ao balcão.')
    
    #Bonificar o salário do gerente
    def BonificarGerente(self):
        self.salario += self.salario * 0.15
        






