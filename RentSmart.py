from Imovel import *
from Taxa import *
from Funcoes import *
from Csv import *
from Orcamento import * 

print("======================================")
print("======== Bem-Vindo a RentSmart =======")
print("======================================\n")
print("======================================")
print("=========== 1 - Apartamento ==========")
print("=========== 2 - Casa =================")
print("=========== 3 - Estúdio ==============")
print("======================================")
print()
escolha = int(input("Escolha um imóvel: "))

match escolha:
    #APARTAMENTO
    case 1:
        print("Você escolheu Apartamento")

        quartos = ler_quartos()

        garagem = ler_sim_nao("Deseja vaga em garagem?")
        
        criancas = ler_sim_nao("Possui Crianças?")

        apartamento = Apartamento(
            quartos,
            garagem,
            criancas
        )

        valor = apartamento.calcular_aluguel()

        taxa = TaxaContratual()

        quantidade_parcelas = ler_parcelas()

        parcela_taxa = taxa.parcelas(quantidade_parcelas)

        exibir_orcamento(
            apartamento,
            taxa,
            quantidade_parcelas,
            parcela_taxa
        )
        
        gerar_csv(
            valor,
            parcela_taxa,
            quantidade_parcelas
        )

    #CASA
    case 2:
        print("Você escolheu Casa")

        quartos = ler_quartos()
        garagem = ler_sim_nao("Deseja vaga em garagem?")

        casa = Casa (
            quartos,
            garagem
        )

        valor = casa.calcular_aluguel()

        taxa = TaxaContratual()
        
        quantidade_parcelas = ler_parcelas()

        parcela_taxa = taxa.parcelas(quantidade_parcelas)

        exibir_orcamento(
            casa,
            taxa,
            quantidade_parcelas,
            parcela_taxa
        )
                
        gerar_csv(
            valor,
            parcela_taxa,
            quantidade_parcelas
        )

    #ESTÚDIO
    case 3:
        print("Você escolheu Estúdio")

        garagem = int(input("quantas vagas de estacionamento você deseja? "))

        while garagem < 2:
            print("O estúdio presisa pelomenos ter 2 vagas de garagem.")
            garagem = int(input("quantas vaga de estacionamento você deseja? "))

        estudio = Estudio(garagem)

        valor = estudio.calcular_aluguel()

        taxa = TaxaContratual()
        
        quantidade_parcelas = ler_parcelas()
        
        parcela_taxa = taxa.parcelas(quantidade_parcelas)

        exibir_orcamento(
            estudio,
            taxa,
            quantidade_parcelas,
            parcela_taxa
        )
                
        gerar_csv(
            valor,
            parcela_taxa,
            quantidade_parcelas
        )

    case _:
        print("opção inválida!")


    