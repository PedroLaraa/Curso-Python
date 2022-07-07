class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        return self._codigo == outro._codigo

    def __str__(self):
        return '[>>Código {} | Saldo R$ {}<<]'.format(self._codigo, self._saldo)

class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(777)

print(conta1)

conta2 = ContaSalario(777)

print(conta2)

print(conta1 == conta2) # Verifica o local na memória por padrão, valores podem ser iguais, mas não a referência na memória, retorna FALSE
