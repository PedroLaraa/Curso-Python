import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_a_url(url)
        self.valida_url()
    
    # Sanitiza a URL para validação
    def sanitiza_a_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    # Validação da URL
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia!!!')
        else:
            self.url_base

    # Separa a base da URL
    @property
    def url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        padrao_url =re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        if padrao_url.match(url_base):
            return url_base
        else:
            raise ValueError('A URL não é válida!!!')
    
    # Pega os params da URL
    @property
    def url_params(self):
        indice_interrogacao = self.url.find('?')
        url_params = self.url[indice_interrogacao + 1:]
        return url_params

    # Pega o valor de um param de acordo com o que foi requisitado
    def get_valor_params(self, parametro_busca):
        indice_parametro = self.url_params.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.url_params.find('&', indice_valor)
        if indice_e_comercial == -1 :
            valor = self.url_params[indice_valor:]
        else:
            valor = self.url_params[indice_valor:indice_e_comercial]
        return valor

    @property
    def converte_moeda(self):
        moeda_destino = self.get_valor_params('moedaDestino')
        valorDoParamDolar = self.get_valor_params('valor')
        if moeda_destino == 'real':
            return f'Dólar para real: R${int(valorDoParamDolar) * 5}'
        else:
            return f'Real para Dólar: ${int(valorDoParamDolar) / 5}'
    

urlBruta = ExtratorURL('http://bytebank.com/cambio?valor=100&moedaDestino=real&moedaOrigem=dolar')
valor_quantidade = urlBruta.converte_moeda
print(valor_quantidade)
