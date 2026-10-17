n = (int(input('Digite um numero!: ')), 
int(input('Digite outro numero!: ')),
int(input('Digite mais um numero!: ')),
int(input('Digite o ultimo numero!: ')))#tupla e inputs
print(f'Valores guardados: {n}')#mostrando a tuplas
print(f'O 9 apareceu: {n.count(9)}')#contando quantos numeros 9 tem
print(f'O 3 esta na posição: {n.index(3)+1}')#achando a posição do numero 3 na tupla
print('Os valores parés são: ', end='')
for c in n:# verificando se os valores são pares
    if c % 2 == 0:
        print(c, end=' ')