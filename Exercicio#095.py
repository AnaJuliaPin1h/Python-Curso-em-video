dados_jogador = {}
dados_jogadores = []
gols_partida = []
while True:
    dados_jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados_jogador['Nome']} jogou? '))
    for i in range(partidas):
        gols_partida.append(int(input(f'Quantos gols na partida {i+1}: ')))
    dados_jogador['Gols'] = gols_partida[:]
    dados_jogador['Total'] = sum(gols_partida)
    dados_jogadores.append(dados_jogador.copy())
    gols_partida.clear()

    continuar = str(input('Quer continuar [S/N]: '))
    if continuar in 'Nn':
        break
    while continuar not in 'SsNn':
        print('Digite apenas S ou N.')
        continuar = str(input('Quer continuar [S/N]: '))
    if continuar in 'Ss':
        print('><' * 15)
    if continuar in 'Nn':
        break

print('><' * 15)
print('Cod    Nome      Gols          Total')
for indice, dados in enumerate(dados_jogadores):
    print(f'{indice}  {dados['Nome']:<10} {str(dados['Gols']):<20} {dados['Total']}')

while True:
    print('<>' * 15)
    escolher_dados = int(input('Mostrar dados de qual jogador: '))
    if escolher_dados < (len(dados_jogadores)):
        for indice, valor in enumerate(dados_jogadores):
            if escolher_dados == indice:
                print(f'-- Levantamento do jogador {valor['Nome']}:')
                for ind, golss in enumerate(valor['Gols']):
                    print(f'No jogo {ind+1} fez {golss} gols.')
    elif escolher_dados == 999:
        break
    else:
        print(f'Erro! Não existe jogador com código {escolher_dados}! Tente novamente.')
print('<< Volte Sempre >>')