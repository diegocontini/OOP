from obj_aluno import *
from obj_combustivel import *

#Objeto e métodos relacionados ao aluno
a1 = aluno('Diego','Contini','104.334.729.10')
a1.primeiroSemestreNotaEntrada()
a1.segundoSemestreNotaEntrada()
a1.calcularMedia()  

#Objetos e métodos relacionados a bomba de combustível
bomba_padrao = bomba_combustivel (1,2000)
bomba_padrao.abastecer_por_valor()
bomba_padrao.abastecer_por_litro()

bomba_gasolina = combustivel_gasolina (2, 2500)
bomba_gasolina.abastecer_por_valor()
bomba_gasolina.abastecer_por_litro()

bomba_etanol = combustivel_etanol(3,300)
bomba_etanol.abastecer_por_valor()
bomba_etanol.abastecer_por_litro()


