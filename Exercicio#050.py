
# Soma dos pares
soma = 0
for c in range (1, 7):
    num = int(input(f'Digite o {c} valor: '))
    pares = (num % 2) == 0
    soma += pares

print(f'Voce informou {soma} PARES e a soma foi {soma * num}')