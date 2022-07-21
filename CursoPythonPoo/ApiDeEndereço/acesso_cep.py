import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido')
    
    def __str__(self):
        return f'CEP: {self.format_cep()} | Dados: {self.acessa_via_cep()}'

    def cep_e_valido(self, cep):
        if len(cep) != 8:
            return False
        else:
            return True

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        r = requests.get('https://viacep.com.br/ws/{}/json/'.format(self.cep))
        dados = r.json()
        return (
            dados['localidade'],
            dados['uf']
        )
