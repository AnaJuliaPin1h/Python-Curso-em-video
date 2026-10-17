numero = int(input('digite o seu numero: '))
cont = numero
fac = 1
print(f'calculando {numero}!')
for  cont in range(numero, 0, -1):
    print(f'{cont}',end= ' ')
    print(f'x' if cont > 1 else '=',end= ' ')
    fac *= cont
    cont -= 1
print(f'{fac}')