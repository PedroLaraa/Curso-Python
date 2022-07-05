url = 'https://bytebank.com/cambio?moedaOrigem'

indice_interrogacao = url.find('?')

url_base = url[0 :indice_interrogacao]

print(url_base)

url_params = url[indice_interrogacao + 1: len(url) + 1]

print(url_params)
