""" ARQUIVO DE COM O SCRIPT CENTRAL PARA EXECUÇÃO DOS CÓDIGOS """

import datetime
from dateutil.relativedelta import relativedelta
from indice_bovespa import script_bovespa
from manipulacao_acoes import script_acoes


def main():
    """ função principal para execução do código """
    """print("------- Analise mensal do bovespa -------")
    analise_dados_bovespa(1)
    print("------- Analise trimestral do bovespa -------")
    analise_dados_bovespa(3)
    print("------- Analise semestral do bovespa -------")
    analise_dados_bovespa(6)
    print("------- Analise anual do bovespa -------")
    analise_dados_bovespa(12)"""

    print("------------------------------------------")
    analise_dados_acoes(3)


def obter_dados_acoes(intervalo_de_tempo):
    """Método para obter as informações das ações que
    compõem o indice Bovespa
    intervalo_de_tempo em meses"""
    dia_atual = datetime.date.today()
    data_anterior = dia_atual - relativedelta(months=intervalo_de_tempo)
    dados_acoes = script_acoes.obter_dados_acoes(data_anterior, dia_atual)
    return dados_acoes

def analise_dados_acoes(intervalo_de_tempo):
    """Método para analisar a informações das ações que
    compõem o indice Bosvespa
    intervalo_de_tempo em meses"""
    dados_acoes = obter_dados_acoes(intervalo_de_tempo)
    for acao in dados_acoes.items():
        dados_estatistico_acao = script_acoes.analise_quartil_acoes(acao)
        ultimo_fechamento = script_acoes.obter_ultimo_fechamento_acao(acao)
        print("Ação: ", acao[0])
        mostrar_dados_estatisticos(dados_estatistico_acao, ultimo_fechamento)
        print("-----------------------------")

def mostrar_dados_estatisticos(dados_estatistico_acao, ultimo_fechamento, detalhe = False):
    """Funcao para mostrar os dados estatisticos da acao"""
    if(detalhe):
        print("O valor foi mínimo de: ", dados_estatistico_acao[0])
        print("Percentil 1: ", dados_estatistico_acao[1])
        print("Mediana: ", dados_estatistico_acao[2])
        print("Percentil 3: ", dados_estatistico_acao[3])
        print("O valor foi máximo de: ", dados_estatistico_acao[4])
        print("Media: ", dados_estatistico_acao[5])
        print("Ultimo fechamento: ", ultimo_fechamento)

     # fechamento de mercado com nova mínima.
    if ultimo_fechamento < dados_estatistico_acao[0]:
        print("Acao com nova mínima")
    # fechamento de mercado entre a mínima e o primeiro quartil
    elif dados_estatistico_acao[0] < ultimo_fechamento and ultimo_fechamento < dados_estatistico_acao[1]:
        print("Acao entre a mínima e o primeiro quartil")
    # fechamento de mercado entre o primeiro quartil e a mediana
    elif dados_estatistico_acao[1] < ultimo_fechamento and ultimo_fechamento < dados_estatistico_acao[2]:
        print("Acao entre o primeiro quartil e a mediana")
    # fechamento de mercado entre a mediana e o terceiro quartil
    elif dados_estatistico_acao[2] < ultimo_fechamento and ultimo_fechamento < dados_estatistico_acao[3]:
        print("Acao entre a mediana e o terceiro quartil")
    # fechamento de mercado entre o terceiro quartil e o máximo
    elif dados_estatistico_acao[3] < ultimo_fechamento and ultimo_fechamento < dados_estatistico_acao[4]:
        print("Acao entre o terceiro quartil e o máximo")
    # fechamento de mercado com novas máximas
    elif dados_estatistico_acao[4] < ultimo_fechamento:
        print("Acao com novas máximas")


def obter_dados_bovespa(intervalo_de_tempo):
    """ Método para obter dataframe com as informações do indice Bovespa
    a partir de um intervalo de tempo informado em meses."""
    dia_atual = datetime.date.today()
    data_anterior = dia_atual - relativedelta(months=intervalo_de_tempo)
    df_bovespa = script_bovespa.historico_bovespa(data_anterior, dia_atual, "1d")
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
