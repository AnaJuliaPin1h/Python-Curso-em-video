aluno = {}

aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
else:
    aluno['Situação'] = 'Reprovado(a)'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')