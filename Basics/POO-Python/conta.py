
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo  
        self.__limite = limite
        print('Contruindo objeto...{}'.format(self))
    
    @property
    def extrato(self):  
        print("{} - Saldo: {}".format(self.__titular, self.__saldo))

    def set_depositar(self, valor):
        self.__saldo += valor
        self.extrato
    
    def set_sacar(self, valor):
        self.__saldo -= valor
        self.extrato

    def set_transferir(self, valor, destino):
        self.set_sacar(valor)
        destino.set_depositar(valor)
        print('{} transferiu para {} R${}'.format(self.__titular, destino.__titular, valor))

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
        print('Novo limite: {}'.format(self.__limite))

contaPedro = Conta(321, 'Pedro', 0, 1600)

contaMaria = Conta(123, 'Maria', 0, 1000)

contaPedro.set_depositar(200)

contaPedro.set_transferir(150, contaMaria)

contaPedro.limite = 2000