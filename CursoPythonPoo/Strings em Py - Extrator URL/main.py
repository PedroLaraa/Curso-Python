url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# url = '                 '

# Sanitização da URL

url = url.replace(' ', '')

if url == '':
    raise ValueError('A URL está vazia!!!')
else:
    indice_interrogacao = url.find('?')

    #Separa a base do URL
    url_base = url[:indice_interrogacao]
    # print(url_base)

    #Separa os params do URL
    url_params = url[indice_interrogacao + 1:]
    print(f'url_params: {url_params}')

    #Busca o valor de um param
    parametro_busca = 'moedaDestino'
    indice_parametro = url_params.find(parametro_busca)

    indice_valor = indice_parametro + len(parametro_busca) + 1

    indice_e_comercial = url_params.find('&', indice_valor)

    if indice_e_comercial == -1 :
        valor = url_params[indice_valor:]
    else:
        valor = url_params[indice_valor:indice_e_comercial]

    print(f'valor: {valor}')
