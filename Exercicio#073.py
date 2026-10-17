times = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 
    'Cruzeiro', 'Atlético-MG', 'Coritiba', 'Botafogo', 'Red Bull Bragantino',
    'Santos', 'São Paulo', 'Vitória', 'Corinthians', 'Mirassol', 'Grêmio',
    'Internacional', 'Vasco', 'Remo', 'Chapecoense')

print('| LISTA DOS TIMES NO BRASILEIRÃO |'.center(45, '='))

for p in range(len(times)):
    if p < 4:
        color = '\033[36m'
    elif p > 15:
        color = '\033[35m'
    else:
        color = ''
    print(f'{color}{p + 1:>2}º | {times[p]}\033[m')

print('='*45)
print(f'Os 5 primeiros: \033[36m{times[:5]}\033[m')
print('='*45)
print(f'Os 4 últimos: \033[35m{times[-4:]}\033[m')
print('='*45)
print(f'Por ordem alfabética: {sorted(times)}')
print('='*45)
pos = times.index('Chapecoense')
print(f'O time {times[pos].upper()} está na {pos + 1}ª posição')