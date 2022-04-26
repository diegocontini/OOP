class poema():
    def __init__(self,tipo_poema) -> None:
        self.tipo_poema = tipo_poema

    def caracteristicas_poema(self):
        print('o poema é um arranjo de palavras que contêm significado. Por meio dele são expressos os pensamentos e sentimentos do autor.')

class soneto(poema):
    def __init__(self, tipo_poema) -> None:
        super().__init__(tipo_poema)

    def caracteristicas_poema(self):
        print('É um tipo de poema que possui uma estrutura fixa. Ele contém quatro estrofes com 14 versos,sendo que dois deles são quartetos, estrofes com quatro versos cada, e dois são tercetos, estrofes com três versos. Geralmente, os versos são decassílabos, ou seja, possuem dez sílabas poéticas.')

class poema_epico(poema):
    def __init__(self, tipo_poema) -> None:
        super().__init__(tipo_poema)
    
    def caracteristicas_poema(self):
        print('Está centrado em figuras míticas ou heroicas, por exemplo, as fábulas')
    
p1 = poema_epico('teste')   
p1.caracteristicas_poema() 