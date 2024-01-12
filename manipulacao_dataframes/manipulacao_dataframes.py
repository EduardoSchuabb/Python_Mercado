""" ARQUIVO DE MANIPULAÇAO DOS DATAFRAMES """


#import pandas as pd

def obter_fechamentos(data_frame):
    """Metodo responsavel por obter a coluna fechamento
    (Close) de um Dataframe do yfinance"""
    fechamentos = data_frame['Close']
    return fechamentos

def obter_volume(data_frame):
    """Metodo responsavel por obter a coluna fechamento
    (Volume) de um Dataframe do yfinance"""
    volumes = data_frame['Volume']
    return volumes
