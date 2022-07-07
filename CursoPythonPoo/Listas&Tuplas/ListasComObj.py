from abc import ABCMeta, abstractmethod
class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    @abstractmethod
    def passa_o_mes(self):
        pass

    def deposita(self, valor): 
        self._saldo += valor

    def __str__(self):
        return '[>>Codigo {} | Saldo {}<<]'.format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo += 0.1

conta_do_pedro = ContaCorrente(123)

conta_do_pedro.deposita(777)

# print(conta_do_pedro)

conta_da_maria = ContaPoupanca(456)

conta_da_maria.deposita(444)

# print(conta_da_maria)

contas = [conta_da_maria, conta_do_pedro]

for conta in contas:
    conta.passa_o_mes()
    print(conta)


