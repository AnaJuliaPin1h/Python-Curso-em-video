Cont = 0
Soma = 0
print('----Digite 999 para parar----')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    Cont += 1
    Soma += num
print(f'''Você digitou {Cont} números

Já a soma deles deu {Soma}''')