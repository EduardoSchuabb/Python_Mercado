""" ARQUIVO PARA OBTER OS DADOS DO INDICE BOVESPA UTILIZANDO YFINANCE """

import yfinance as yf
from manipulacao_dataframes import manipulacao_dataframes


def obter_ultimo_fechamento_indice_bovespa():
    """"""
    dados = yf.download("^BVSP", period="1d")
    # Obter o valor de fechamento mais recente
    valor_atual = dados['Close'].iloc[-1]
    return valor_atual

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
    return fechamentos

def obter_valores_estatisticos(serie):
    """METODO PARA OBTER OS DADOS ESTATISTICOS DA SERIE.
    OS DADOS SAO: MAX, MIN E QUARTIS"""

    indice_maximo = serie.idxmax()
    indice_minimo = serie.idxmin()
    percentil_1 = serie.quantile(0.25)
    mediana = serie.quantile(0.5)
    percentil_3 = serie.quantile(0.75)

    #print("Na data: ", indice_maximo, " o valor foi máximo de: ", serie[indice_maximo])
    #print("Na data: ", indice_minimo, " o valor foi mínimo de: ", serie[indice_minimo])
    #print("Percentil 1:", percentil_1)
    #print("Mediana :", mediana)
    #print("Percentil 3:", percentil_3)
    return serie[indice_minimo], percentil_1, mediana, percentil_3, serie[indice_maximo]

