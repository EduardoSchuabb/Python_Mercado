""" ARQUIVO DE COM O SCRIPT CENTRAL PARA EXECUÇÃO DOS CÓDIGOS """

from indice_bovespa import script_bovespa
import datetime

def main():
    """ função principal para execução do código """

    dia_atual = datetime.date.today()
    script_bovespa.historico_bovespa("2023-01-01", dia_atual, "1d")




if __name__ == "__main__":
    main()

