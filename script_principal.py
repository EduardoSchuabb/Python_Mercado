""" ARQUIVO DE COM O SCRIPT CENTRAL PARA EXECUÇÃO DOS CÓDIGOS """

import datetime
from dateutil.relativedelta import relativedelta
from indice_bovespa import script_bovespa


def main():
    """ função principal para execução do código """
    #obter_dados_bovespa_1ano()

def obter_dados_bovespa_3meses():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 3 meses"""

    dia_atual = datetime.date.today()
    um_ano_antes = dia_atual - relativedelta(months=3)
    print("Dia Atual: ", dia_atual)
    print("Um ano atras: ", um_ano_antes)
    script_bovespa.historico_bovespa(um_ano_antes, dia_atual, "1d")


def obter_dados_bovespa_6meses():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 6 meses"""

    dia_atual = datetime.date.today()
    um_ano_antes = dia_atual - relativedelta(months=6)
    print("Dia Atual: ", dia_atual)
    print("Um ano atras: ", um_ano_antes)
    script_bovespa.historico_bovespa(um_ano_antes, dia_atual, "1d")

def obter_dados_bovespa_1ano():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 1 ano"""

    dia_atual = datetime.date.today()
    um_ano_antes = dia_atual - relativedelta(years=1)
    print("Dia Atual: ", dia_atual)
    print("Um ano atras: ", um_ano_antes)
    script_bovespa.historico_bovespa(um_ano_antes, dia_atual, "1d")





if __name__ == "__main__":
    main()
