lista = list()

for i in range(0, 5):
    lista.append(int(input(f'Digita um valor para a posição {i}º: ')))
print(lista)

print(f'O maior valor digitado foi {max(lista)} e suas posições é', end=' ')
for i in range(0, 10):
    if i <= 4:
        if lista[i] == max(lista):
            print(f'{i}', end='º ')
    else:
        print(f'\nO menor valor digitado foi {min(lista)} e sua posição é', end=' ')  if i == 5 else ''
        if lista[i-5] == min(lista):
            print(f'{i-5}', end='º ')

print('\nprograma finalizado')