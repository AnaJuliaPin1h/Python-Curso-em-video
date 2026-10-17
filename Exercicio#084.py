dados = []
max_peso = min_peso = 0
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))

    if not dados:
        max_peso = min_peso = peso
    elif peso > max_peso:
        max_peso = peso
    elif peso < min_peso:
        min_peso = peso

    dados.append([nome, peso])

    res = ' '
    while res not in 'SN':
        res = input('Continuar: [S/N] ').strip().upper()[0]
    if res == 'N':
        break

print(f'{len(dados)} Pessoas foram cadastradas.')
print(f'O maior peso foi de {max_peso}Kg. Peso de ', end='')
for pessoa in dados:
    if pessoa[1] == max_peso:
        print(f'{pessoa[0].upper()}, ', end='')
print(f'\nO menor peso foi de {min_peso}Kg. Peso de ', end='')
for pessoa in dados:
    if pessoa[1] == min_peso:
        print(f'{pessoa[0].upper()}, ', end='')