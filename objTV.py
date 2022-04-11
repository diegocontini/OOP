from logging import exception
from xml.sax.handler import DTDHandler


class tv():
    def __init__(self,canal):
        self.canal = canal
        self.volume = 0
    
    def volumeTV(self):
        alterarVol = int(input('Digite o volume desejado: '))
        volIntervalo = [0,1,2,3,4,5,6,7,8,9,10]
        if alterarVol in volIntervalo:
            self.volume = alterarVol
        else:
            raise Exception('Digite um volume válido')
        print(self.volume)

    def canalTV(self):
        alterarCanal = int(input('Digite o canal desejado: '))
        canalIntervalo = [0,1,2,3,4,5,6,7,8,9,10]
        if alterarCanal in canalIntervalo:
            self.canal = alterarCanal
        else:
            raise Exception('Digite um canal válido')
        print(self.canal)
        

tv1 = tv(0)
tv1.volumeTV()
tv1.canalTV()


    