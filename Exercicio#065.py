numeros = 0
soma = 0
media = 0
opcao = ''
maior_numero = float('-inf')
menor_numero = float('inf')
while opcao != 'N':
    opcao = str(input('Quer adicionar um número? [S/N]: \n')).upper()
    if opcao == 'S':
        numeros = int(input('Insira um número inteiro:\n'))
        soma += numeros
        media += 1
        if numeros > maior_numero:
            maior_numero = numeros
        if numeros < menor_numero:
            menor_numero = numeros
        

print(f'O maior numero digitado foi {maior_numero}')
print(f'O menor numero digitado foi {menor_numero}')
print(f'A média entre todos os valores é de {soma/media:.2f}')