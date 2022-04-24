#callMethods
from obj_animal import *
from obj_funcionario_gerente import * 
a1 = Gato('Bits',4,'Preto','Macho',4)
a2 = Coelho('Bytes',2,'Branco','Checkered Giant Rabbit','Cenoura')
a3 = Cachorro('MegaBit',5,'Laranja','Azul','4')
a1.Comer()
a2.Comer()
a3.Comer()

f1 = Funcionario('Diego','104.334.729.10',1000,'Desenvolvimento')
f1.Bonificar()
print(f1.salario)

g1 = Gerente('Andre','000.000.001.91',1000,'Testador','1234','22')
g1.autenticarSenha()
g1.BonificarGerente()
print(f'O salário de {g1.nome}, incluindo a bonificação é de R${g1.salario}')
