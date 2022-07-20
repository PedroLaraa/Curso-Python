
from validate_docbr import CPF

from validate_docbr import CNPJ

# Validação de PCF

from cpf_cnpj import ValidaDocumento

cpf_valido = '15551053601'

objeto_cpf = ValidaDocumento.cria_documento(cpf_valido)

print(objeto_cpf)

# Validação de CNPJ

cnpj = CNPJ()

cnpj_um = '05263767000127'

objeto_cnpj = ValidaDocumento.cria_documento(cnpj_um)

print(objeto_cnpj)
