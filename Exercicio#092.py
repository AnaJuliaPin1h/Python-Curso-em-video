from datetime import date
hoje = date.today()
ano_atual = hoje.year

lista_user = {}

nome = str(input('Nome: '))
nascimento =  int(input('Ano nascimento: '))
ctps = int(input('Carteira de Trabalho (0 se não tiver): '))
lista_user['nome'] = nome
lista_user['nascimento'] = nascimento
lista_user['ctps'] = ctps
if ctps != 0:
    ano_contrato = int(input('Ano contratação: '))
    lista_user['contratação'] = ano_contrato
    salario = float(input('Salario: '))
    lista_user['salario'] = salario

    temp_falta = 35 - (ano_atual-ano_contrato)
    aposentadoria = (ano_atual-nascimento) + temp_falta
    lista_user['aposentadoria'] = aposentadoria

for k, j in lista_user.items():
    print(f'O {k} tem o valor {j}')