listagem = ('Leite', 32.25, 'Pão', 2, 'Macarrão', 24, 'Café', 35.25, 'Sorvete', 14.5)
print('='*45)
print(' LISTAGEM DE PREÇOS '.center(44, ' '))
print('-'*45)
for l in range(0, len(listagem), 2):
    print(f'{listagem[l]:.<32} R${listagem[l + 1]:>10.2f}')
print('-'*45)
print('FIM DA LISTAGEM'.center(44, ' '))
print('='*45)