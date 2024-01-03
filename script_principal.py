""" ARQUIVO DE COM O SCRIPT CENTRAL PARA EXECUÇÃO DOS CÓDIGOS """

import datetime
from dateutil.relativedelta import relativedelta
from indice_bovespa import script_bovespa


def main():
    """ função principal para execução do código """
    analise_dados_bovespa_1mes()

def analise_dados_bovespa_1mes():
    """ANALISAR COM DADOS ESTATISTICOS O INDICE BOVESPA A COM JANELA DE 1 MES"""
    df_bovespa = obter_dados_bovespa_1mes()
    fechamentos = script_bovespa.obter_fechamento_bovespa(df_bovespa)
    dados_estatisticos = script_bovespa.obter_valores_estatisticos(fechamentos)
    fechamento_atual = script_bovespa.obter_ultimo_fechamento_indice_bovespa()

    print("Mínimo: ", dados_estatisticos[0])
    print("Quartil 1: ", dados_estatisticos[1])
    print("Mediana: ", dados_estatisticos[2])
    print("Quartil: 3", dados_estatisticos[3])
    print("Máximo: ", dados_estatisticos[4])
    print("Último fechamento: ", fechamento_atual)
    
    # Fazer as analises condicionais para verificar a posicao
    # do ultimo fechamento em relacao os valores max, min, e
    # percentis dos referentes à 1 mes.



def obter_dados_bovespa_1mes():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 3 meses"""
    dia_atual = datetime.date.today()
    um_mes_antes = dia_atual - relativedelta(months=1)
    df_bovespa = script_bovespa.historico_bovespa(um_mes_antes, dia_atual, "1d")
    return df_bovespa

def obter_dados_bovespa_3meses():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 3 meses"""
    dia_atual = datetime.date.today()
    tres_meses_antes = dia_atual - relativedelta(months=3)
    df_bovespa = script_bovespa.historico_bovespa(tres_meses_antes, dia_atual, "1d")
    return df_bovespa

def obter_dados_bovespa_6meses():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 6 meses"""
    dia_atual = datetime.date.today()
    seis_meses_antes = dia_atual - relativedelta(months=6)
    df_bovespa = script_bovespa.historico_bovespa(seis_meses_antes, dia_atual, "1d")
    return df_bovespa

def obter_dados_bovespa_1ano():
    """ Método para obter dataframe com as informações do indice Bovespa no intervalo de 1 ano"""
    dia_atual = datetime.date.today()
    um_ano_antes = dia_atual - relativedelta(years=1)
    df_bovespa = script_bovespa.historico_bovespa(um_ano_antes, dia_atual, "1d")
    return df_bovespa



if __name__ == "__main__":
    main()
