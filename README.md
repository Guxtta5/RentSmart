# 🏠 RentSmart

## Sistema de Orçamento e Locação de Imóveis

O **RentSmart** é uma aplicação desenvolvida em Python para auxiliar a
R.M. Imóveis na elaboração de orçamentos de locação.

O sistema permite selecionar o tipo de imóvel, informar suas características,
calcular o valor mensal do aluguel, aplicar adicionais e descontos, calcular
a taxa contratual e gerar uma projeção financeira.

---

## 📋 Sobre o projeto

O projeto foi desenvolvido utilizando conceitos de:

- Programação Orientada a Objetos (POO);
- Classes e objetos;
- Herança;
- Atributos e métodos;
- Estruturas condicionais;
- Estruturas de repetição;
- Validação de dados;
- Manipulação de arquivos CSV.

O objetivo é transformar as regras de negócio da imobiliária em uma aplicação
organizada e automatizada.

---

## 🏠 Tipos de imóveis

O sistema trabalha com três tipos de imóveis:

### Apartamento

Valor base:

**R$ 700,00**

Regras:

- 1 quarto: valor base;
- 2 quartos: acréscimo de R$ 200,00;
- garagem: acréscimo de R$ 300,00;
- clientes sem crianças recebem 5% de desconto sobre o valor após
  os adicionais.

### Casa

Valor base:

**R$ 900,00**

Regras:

- 1 quarto: valor base;
- 2 quartos: acréscimo de R$ 250,00;
- garagem: acréscimo de R$ 300,00.

### Estúdio

Valor base:

**R$ 1.200,00**

Regras:

- as 2 primeiras vagas custam R$ 250,00;
- cada vaga adicional custa R$ 60,00.

---

## 💰 Taxa contratual

A taxa contratual possui o valor de:

**R$ 2.000,00**

O cliente pode escolher pagar a taxa em até 5 parcelas.

Exemplo:

```text
Taxa contratual: R$ 2.000,00

5 parcelas:
R$ 400,00 por parcela
