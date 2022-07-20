
from validate_docbr import CPF

from validate_docbr import CNPJ

class ValidaDocumento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return CpfValidate(documento)
        elif len(documento) == 14:
            return CnpjValidate(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class CnpjValidate:
    
    def __init__(self, documento):
        if self.cpf_e_valido(documento):
            self.cnpj = documento
        else:
            raise Exception('CNPJ inválido')

    def __str__(self):
        return self.format()
    
    def cpf_e_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format(self):
        mascara = CNPJ()
        return 'Documento válido: ' + mascara.mask(self.cnpj)

class CpfValidate:
    
    def __init__(self, documento):
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise Exception('CPF inválido')

    def __str__(self):
        return self.format()
    
    def cpf_e_valido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format(self):
        mascara = CPF()
        return 'Documento válido: ' + mascara.mask(self.cpf)
