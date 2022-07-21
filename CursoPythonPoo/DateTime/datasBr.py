
from datetime import datetime


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return f'Data de cadastro: {self.format_data()}'

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y')
        return data_formatada

    def tempo_cadastro(self):
            tempo_cadastro = datetime.today() - self.momento_cadastro
            return tempo_cadastro

    # def mes_cadastro(self):
    #     meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    #     mes_cadastro = self.momento_cadastro.month
    #     return meses_do_ano[mes_cadastro - 1]

    # def dia_semana(self):
    #     dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    #     dia_semana = self.momento_cadastro.weekday()
    #     return dias_semana[dia_semana]
