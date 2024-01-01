""" ARQUIVO PARA OBTER OS DADOS DO INDICE BOVESPA UTILIZANDO YFINANCE """

import yfinance as yf
from manipulacao_dataframes import manipulacao_dataframes


def historico_bovespa(data_inicial, data_final, periodo):
    """FUNCAO PARA OBTER O HISTORICO DO INDICE BOVESPA
    argumentos:
        data_inicial = YYYY-MM-DD ou datetime
        data_final = YYYY-MM-DD ou datetime
        periodo = string
        (“1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”)"""
    bovespa = yf.Ticker("^BVSP")
    bovespa_hist_bruto = bovespa.history(start=data_inicial, end=data_final, interval= periodo)
    bovespa_hist = bovespa_hist_bruto[["Open", "High", "Low", "Close", "Volume"]]
    #print(bovespa_hist.head)
    return bovespa_hist


def obter_fechamento_bovespa(data_frame):
    """FUNCAO PARA OBTER FECHAMENTOS DO INDICE DE UM DATAFRAME"""
    fechamentos = manipulacao_dataframes.obter_fechamentos(data_frame)
    print(fechamentos)
    #print(fechamentos.head(1))
