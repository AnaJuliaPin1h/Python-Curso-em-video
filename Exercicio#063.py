termos = int(input('Quantos termos da sequencia você deseja: '))
print('~'*30)
penultimo = 0
ultimo = 1
count = 3
print(f'{penultimo}-{ultimo}', end="-")
while count <= termos:
    novo = penultimo + ultimo
    print(f'{novo}-',end="")
    penultimo = ultimo
    ultimo = novo
    count += 1
print('FIM')
print('~'*30)