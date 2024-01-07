""" Arquivo para obter os dados das acoes usando o yfinance """

import yfinance as yf
from manipulacao_dataframes import manipulacao_dataframes

"""acoes_indice_bovespa = ["VALE3.SA", "PETR4.SA", "ITUB4.SA", "PETR3.SA","BBDC4.SA",
                        "ELET3.SA", "B3SA3.SA","BBAS3.SA", "ABEV3.SA", "ITSA4.SA",
                        "RENT3.SA", "WEGE3.SA", "BPAC11.SA", "EQTL3.SA", "SUZB3.SA",
                        "RADL3.SA", "PRIO3.SA", "RDOR3.SA", "UGPA3.SA", "JBSS3.SA",
                        "RAIL3.SA", "GGBR4.SA", "SBSP3.SA", "VBBR3.SA", "BRFS3.SA",
                        "VIVT3.SA", "BBDC3.SA", "CSAN3.SA", "BBSE3.SA", "ENEV3.SA",
                        "HAPV3.SA", "ASAI3.SA", "CPLE6.SA", "TOTS3.SA", "LREN3.SA",
                        "EMBR3.SA", "CMIG4.SA", "KLBN11.SA", "ENGI11.SA", "HYPE3.SA",
                        "TIMS3.SA", "CCRO3.SA", "ALOS3.SA", "NTCO3.SA", "ELET6.SA",
                        "CSNA3.SA", "EGIE3.SA", "SANB11.SA", "CMIN3.SA", "TAEE11.SA",
                        "MULT3.SA", "CPFE3.SA", "GOAU4.SA", "CRFB3.SA", "CYRE3.SA",
                        "YDUQ3.SA", "FLRY3.SA", "BRAP4.SA", "COGN3.SA", "RRRP3.SA",
                        "MGLU3.SA", "RECV3.SA", "BRKM5.SA", "AZUL4.SA", "IGTI11.SA",
                        "CIEL3.SA", "RAIZ4.SA", "USIM5.SA", "SMTO3.SA", "ARZZ3.SA",
                        "VAMO3.SA", "MRVE3.SA", "SLCE3.SA", "IRBR3.SA", "SOMA3.SA",
                        "MRFG3.SA", "LWSA3.SA", "DXCO3.SA", "ALPA4.SA", "BEEF3.SA",
                        "GOLL4.SA", "CVCB3.SA", "EZTC3.SA", "PETZ3.SA", "BHIA3.SA",
                        "PCAR3.SA"]"""

acoes_indice_bovespa = ["VALE3.SA", "PETR4.SA"]


def obter_dados_acoes(data_inicial, data_final):
    """Funcao para obter os dados das acoes que compoem o indice bovespa"""

    dados_acoes = {}
    for acao in acoes_indice_bovespa:
        dados_acao = yf.download(acao, start=data_inicial, end=data_final)
        dados_acoes[acao] = dados_acao

    return dados_acoes

def analise_quartil_acoes(dados_acao):
    """Funcao para analisar os dados de uma acao em relacao aos
    valores de max, min, media e os quartis"""

    fechamento_dados_acao = manipulacao_dataframes.obter_fechamentos(dados_acao[1])

    indice_maximo = fechamento_dados_acao.idxmax()
    indice_minimo = fechamento_dados_acao.idxmin()
    percentil_1 = fechamento_dados_acao.quantile(0.25)
    mediana = fechamento_dados_acao.quantile(0.5)
    percentil_3 = fechamento_dados_acao.quantile(0.75)
    media = fechamento_dados_acao.median()

    return (fechamento_dados_acao[indice_minimo], percentil_1,
            mediana, percentil_3, fechamento_dados_acao[indice_maximo], media)

def obter_ultimo_fechamento_acao(dados_acao):
    """Retorna o ultimo fechamento da acao"""
    
    return dados_acao[1].iloc[-1]["Close"]