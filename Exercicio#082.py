lista = []
par = []
impar =  []

while True:
    try:
        n = int(input('Digite um valor: '))
        lista.append(n)
    except ValueError:
        print('Valor invalido')
        continue
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opc not in 'SN':
        print('Insira apenas S ou N')
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opc == 'N':
        break

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')