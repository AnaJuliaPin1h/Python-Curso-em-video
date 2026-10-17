def jogador(nome='desconhecido',gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if str(gols).isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s).')

nome = input('Digite o nome do jogador: ')
gols = input('Digite a quantidade de gols: ')

jogador(nome,gols)