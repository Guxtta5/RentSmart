#NOSSA CLASSE TAXA ONDE FAZ O CALCULO DA TAXA CONTRATUAL E PELO NOMEROS DE PARCELAS ESCOLIDAS 
class TaxaContratual:
    def __init__(self, valor = 2000):
        self.valor = valor

    def parcelas(self, quantidade_parcelas):
        return self.valor / quantidade_parcelas