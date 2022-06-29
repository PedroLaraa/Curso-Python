
# conta = {"numero": 123, "titular": "João", "saldo": 0, "limite": 1000}

# print(conta["titular"])

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar_conta(conta, valor):
    conta["saldo"] += valor
    return conta

def sacar_conta(conta, valor):
    conta["saldo"] -= valor
    return conta

def extrato_conta(conta):
    print("Saldo: R$ %.2f" % conta["saldo"])
    return conta

conta = criar_conta(123, "João", 0, 1000)

depositar_conta(conta, 100)

extrato_conta(conta)