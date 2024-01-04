""" ARQUIVO DE COM O SCRIPT CENTRAL PARA EXECUÇÃO DOS CÓDIGOS """

import datetime
from dateutil.relativedelta import relativedelta
from indice_bovespa import script_bovespa


def main():
    """ função principal para execução do código """
    print("------- Analise mensal do bovespa -------")
    analise_dados_bovespa(1)
    print("------- Analise trimestral do bovespa -------")
    analise_dados_bovespa(3)
    print("------- Analise semestral do bovespa -------")
    analise_dados_bovespa(6)
    print("------- Analise anual do bovespa -------")
    analise_dados_bovespa(12)


def obter_dados_bovespa(intervalo_de_tempo):
    """ Método para obter dataframe com as informações do indice Bovespa
    a partir de um intervalo de tempo informado em meses."""
    dia_atual = datetime.date.today()
    um_mes_antes = dia_atual - relativedelta(months=intervalo_de_tempo)
    df_bovespa = script_bovespa.historico_bovespa(um_mes_antes, dia_atual, "1d")
    return df_bovespa


def analise_dados_bovespa(intervalo_de_tempo):
    """Método de analise de dados do indice bovespa a partir de informacoes
    entre um intervalo de tempo dado em meses."""
    df_bovespa = obter_dados_bovespa(intervalo_de_tempo)
    fechamentos = script_bovespa.obter_fechamento_bovespa(df_bovespa)
    dados_estatisticos = script_bovespa.obter_valores_estatisticos(fechamentos)
    fechamento_atual = script_bovespa.obter_ultimo_fechamento_indice_bovespa()

    print("Mínimo: ", dados_estatisticos[0])
    print("Quartil 1: ", dados_estatisticos[1])
    print("Mediana: ", dados_estatisticos[2])
    print("Quartil 3: ", dados_estatisticos[3])
    print("Máximo: ", dados_estatisticos[4])
    print("Último fechamento: ", fechamento_atual)

    # fechamento de mercado com nova mínima.
    if fechamento_atual < dados_estatisticos[0]:
        print("fechamento de mercado com nova mínima")
    # fechamento de mercado entre a mínima e o primeiro quartil
    elif dados_estatisticos[0] < fechamento_atual and fechamento_atual < dados_estatisticos[1]:
        print("fechamento de mercado entre a mínima e o primeiro quartil")
    # fechamento de mercado entre o primeiro quartil e a mediana
    elif dados_estatisticos[1] < fechamento_atual and fechamento_atual < dados_estatisticos[2]:
        print("fechamento de mercado entre o primeiro quartil e a mediana")
    # fechamento de mercado entre a mediana e o terceiro quartil
    elif dados_estatisticos[2] < fechamento_atual and fechamento_atual < dados_estatisticos[3]:
        print("fechamento de mercado entre a mediana e o terceiro quartil")
    # fechamento de mercado entre o terceiro quartil e o máximo
    elif dados_estatisticos[3] < fechamento_atual and fechamento_atual < dados_estatisticos[4]:
        print("fechamento de mercado entre o terceiro quartil e o máximo")
    # fechamento de mercado com novas máximas
    elif dados_estatisticos[4] < fechamento_atual:
        print("fechamento de mercado com novas máximas")


if __name__ == "__main__":
    main()
