""" ARQUIVO DE TESTE DO USO DO MODULO YFINANCE"""

import warnings
import datetime
import time
from yahoo_fin import stock_info as si
import yfinance as yf
import pandas as pd

def main():
    """ funcao main"""
    #dia_atual = datetime.date.today()
    #historico_bovespa("2023-01-01", dia_atual, "1d")
    #print("-------------------------------------------")
    #historico_acoes("2023-01-01", dia_atual, "1d")
    warnings.filterwarnings("ignore", category=FutureWarning)
    obter_dados_intra_day()

# Criando um decorator para analise de tempo de execucao.
def tempo_execucao(funcao):
    """ funcao para usar como decorator - calcular tempo de execucao"""
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f'tempo de execicao foi de {tempo_final - tempo_inicial} s')
    return wrapper


#@tempo_execucao
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
    print(bovespa_hist.head)

def historico_acoes(data_inicial, data_final, periodo):
    """FUNCAO PARA OBTER O HISTORICO DAS ACOES
    argumentos:
        data_inicial = YYYY-MM-DD ou datetime
        data_final = YYYY-MM-DD ou datetime
        periodo = string
        (“1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”)"""
    # a ideia é pegar de um arquivo as informacoes das
    # acoes junto com o seu peso da composicao do BOVESPA
    empresas = ['PETR4.SA','PETR3.SA', 'BBAS3.SA',
                 'BBDC4.SA', 'ITUB4.SA', 'VALE3.SA',
                 'BRKM5.SA', 'CSAN3.SA', 'ELET3.SA',
                 'EMBR3.SA', 'GOLL4.SA', 'USIM5.SA',
                 'CSNA3.SA', 'GGBR4.SA', 'JBSS3.SA',
                 'BRFS3.SA', 'ABEV3.SA', 'MRVE3.SA',
                 'NTCO3.SA', 'SANB11.SA', 'BBSE3.SA']
    empresas_dados = yf.Tickers(empresas)
    empresas_hist_bruto = empresas_dados.history(start=data_inicial,
                                                 end=data_final,
                                                 interval= periodo)
    empresas_hist = empresas_hist_bruto[["Open", "High", "Low", "Close", "Volume"]]
    print(empresas_hist.head)

#   TESTAR DURANTE OS DIAS DE MERCADO ABERTO
# Para obter informacoes em tempo real, utilizar o seguinte codigo:
# from yahoo_fin import stock_info as si
# round(si.get_live_price('PETR4.SA'), 2)

def obter_dados_intra_day():
    """ FUNCAO PARA BUSCAR VALORES INTRA-DAY """
    count = 0
    intra_day_frame = pd.DataFrame(columns = ['Hora','Preço'])

    minutos = 3
    tempo_estimado = time.time() + minutos*60
    while time.time() < tempo_estimado:
        # buscando valor do etherium somente para teste.
        preco = round(si.get_live_price('ETH-USD'), 2)
        tempo_real = datetime.datetime.fromtimestamp(time.time())
        tempo_real = tempo_real.strftime("%d-%b-%Y %H:%M:%S")
        modelo = {'Hora': tempo_real, 'Preço': preco}
        print(modelo) 
        linha = pd.DataFrame(data = modelo, index = [count])
        count += 1
        intra_day_frame = pd.concat([intra_day_frame, linha], ignore_index= True)
        time.sleep(60)

if __name__ == "__main__":
    main()
