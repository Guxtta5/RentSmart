# função para criar o CSV em excel
from Imovel import *
import csv

def gerar_csv(aluguel, parcela_taxa, quantidade_parcelas):

    with open("locação.csv","w", newline="",encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow([
            "Mês",
            "Aluguel",
            "Parcela Texa Cantratual",
            "Total do Mês"
        ])

        for mes in range (1, 13):
            parcela = parcela_taxa
        else:
            parcela = 0
        total =  aluguel + parcela

        escritor.writerow([
            mes,
            f"{aluguel:.2f}",
            f"{parcela:.2f}",
            f"{total:.2f}"
        ])