#  Progressão Aritmética

primeiro_termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(10):
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
    
print('FIM')