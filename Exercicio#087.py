matriz = []
numeros = []
soma_valores_pares = 0
maior_valor_seg_linha = float('-inf')
for n in range(0,3):
    for m in range(0,3):
        numero = int(input('Digite um número:'))
        if numero % 2 == 0:
            soma_valores_pares += numero
        numeros.append(numero)
    matriz.append(numeros[:])
    numeros.clear()
    
for num in matriz[1]:
    if num > maior_valor_seg_linha:
        maior_valor_seg_linha = num

for ma in matriz:
    for q in range(0,3):
        print(f"[{ma[q]}]", end=' ')
    print()
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma de todos os valores pares digitados foi {soma_valores_pares}')
print(f'O maior valor da segunda linha é o {maior_valor_seg_linha}')
print(f'A soma da terceira coluna é {soma_terceira_coluna}')