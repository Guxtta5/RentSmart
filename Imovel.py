# CLASSE IMOVEL É A CLASSE BASE DO PROJETO
class Imovel:
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

# ESSA E NOSSA CLASSE APARTAMENTO ONDE ELA HERDA ALGUMAS COISAS DA NOSSA CLASSE BASE
class Apartamento (Imovel):
    def __init__(self, quarto, garagem, crianca):
        super().__init__("Apartamento", 700)

        self.quarto = quarto
        self.garagem = garagem
        self.crianca = crianca

        self.adicional_quarto = 0
        self.adicional_garagem = 0
        self.desconto = 0

    def calcular_aluguel(self):
        valor = self.valor_base

        if self.quarto == 2:
            self.adicional_quarto = 200
            valor += self.adicional_quarto

        if self.garagem:
            self.adicional_garagem = 300
            valor += self.adicional_garagem

        if not self.crianca:
            self.desconto = valor * 0.05
            valor -= self.desconto
        return valor

# ESSA E NOSSA CLASSE CASA ONDE ELA HERDA ALGUMAS COISAS DA NOSSA CLASSE BASE
class Casa(Imovel):
    def __init__(self, quarto, garagem):
        super().__init__("Casa", 900)

        self.quarto = quarto
        self.garagem = garagem

        self.adicional_quarto = 0
        self.adicional_garagem = 0

    def calcular_aluguel(self):
        valor = self.valor_base

        if self.quarto == 2:
            self.adicional_quarto = 250
            valor += self.adicional_quarto

        if self.garagem:
            self.adicional_garagem = 300
            valor += self.adicional_garagem

        return valor

# ESSA E NOSSA CLASSE Estúdio ONDE ELA HERDA ALGUMAS COISAS DA NOSSA CLASSE BASE
class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__("Estúdio", 1200)

        self.vagas = vagas
        self.adicional_vaga = 0
        self.adicional_estacionamento = 0
    
    def calcular_aluguel(self):
        valor = self.valor_base

        if self.vagas >= 2:
            self.adicional_vaga = 250

            vagas_adicional = self.vagas - 2
            self.adicional_estacionamento += vagas_adicional * 60
            valor += self.adicional_vaga
            valor += self.adicional_estacionamento
        return valor
