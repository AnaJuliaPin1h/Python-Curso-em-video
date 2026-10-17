jogador = {'nome' : input('Nome do jogador: ').strip().title(),
           'gols' : [], 'total' : 0}
part = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
for p in range(part):
    gols = (int(input(f'Quantos gols na {p + 1}ª partida: ')))
    jogador['gols'].append(gols)
    jogador['total'] += gols
print('-'*35)
print(jogador)
print('-'*35)
for k, v in jogador.items():
    print(f'{k.capitalize()}: {v}')
print('-'*35)
print(f'O jogador {jogador["nome"]} jogou {part} partidas:')
for p, g in enumerate(jogador['gols']):
    print(f' * {p + 1}ª Partida, {jogador["nome"]} fez {g} gols')
print(f'{jogador["nome"]} fez {jogador["total"]} em sua carreira.')