
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def fomatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))

d = Data(10, 10, 2020)

d.fomatada()