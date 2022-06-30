
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def cliente(self):
        print('Nome: {}'.format(self.__nome.title()))

    @cliente.setter
    def cliente(self, nome):
        self.__nome = nome
        print('Nome: {}'.format(self.__nome.title()))
    
clientePedro = Cliente('pedro')

clientePedro.cliente

clientePedro.cliente = 'maria'