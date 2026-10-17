import random
cont = 0
print('-' * 35)
print('Vamos jogar PAR ou ÍMPAR')
print('-' * 35)
while True: 
    n = int(input('Digite um valor: '))
    jogador = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper() [0]
    while jogador not in 'PI':
        jogador = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper() [0]
    print('=' * 35)
    computador = random.randint(0,10)
    resultado = n + computador
    par = resultado % 2   
    if par == 0 and jogador == 'P':
        print(f'Voce jogou {n} e computador {computador}. Totalizando {resultado} deu PAR!')
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 35)
        cont += 1

    if par == 1 and jogador == 'I':
        print(f'Voce jogou {n} e computador {computador}. Totalizando {resultado} deu IMPAR')
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 35)
        cont += 1

    if par == 1 and jogador == 'P':
        print(f'Voce jogou {n} e o computador {computador}. Totalizando {resultado} deu ÍMPAR!')
        print('Voce PERDEU!')
        print('-' * 35)
        break
    
    if par == 0 and jogador == 'I':
        print(f'Voce jogou {n} e o computador {computador}. Totalizando {resultado} deu PAR!')
        print('Voce PERDEU!')
        print('-' * 35)
        break
    
print(f'GAME OVER! Voce venceu {cont} vezes.')