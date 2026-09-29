# ESSAS FUNÇÕES ONDE DEVE SER ESPERADO A RESPOSTA DO USUARIO E ONDE 
# ELAS SE REPENTE CASO O USUARIO NAO USA A LETRA OU NUMERO  INDICADO

def ler_sim_nao(pergunta):
    
    resposta = input(f"{pergunta} (s/n): ").strip().lower()

    while resposta not in ["s", "n"]:
        print("OPção inválida digite apenas s ou n.")
        resposta = input(f"{pergunta} (s/n): ").strip().lower()

    return resposta == "s"

def ler_quartos():
    quartos = int(input("Você deseja quantos quartos? (1 ou 2): "))

    while quartos not in [1, 2]:
        print("Opção inválida! Escolha 1 ou 2.")
        quartos = int(input("Você deseja quantos quartos? (1 ou 2): "))

    return quartos

def ler_parcelas():
    quantidade = int(
        input("Em quantas parcelas deseja pagar a taxa contratual? (1 a 5): ")
    )

    while quantidade not in [1, 2, 3, 4, 5]:
        print("Quantidade inválida! Escolha de 1 a 5.")

        quantidade = int(
            input("Em quantas parcelas deseja pagar a taxa contratual? (1 a 5): ")
        )

    return quantidade